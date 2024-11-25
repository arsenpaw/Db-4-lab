DROP PROCEDURE IF EXISTS CreateTablesWithRandomColumns;
CREATE PROCEDURE CreateTablesWithRandomColumns()
BEGIN
    DECLARE table_name VARCHAR(128);
    DECLARE done INT DEFAULT 0;

    DECLARE table_cursor CURSOR FOR SELECT DISTINCT id FROM award;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN table_cursor;

    read_loop: LOOP
        FETCH table_cursor INTO table_name;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SET @dynamic_table_name = CONCAT(table_name, '_', DATE_FORMAT(NOW(), '%Y%m%d%H%i%s'));

        SET @num_columns = FLOOR(1 + RAND() * 9);

        SET @create_table_sql = CONCAT('CREATE TABLE ', @dynamic_table_name, ' (');

        SET @col_index = 1;
        WHILE @col_index <= @num_columns DO
            SET @col_name = CONCAT('Column_', @col_index);
            SET @col_type = CASE FLOOR(RAND() * 4)
                WHEN 0 THEN 'INT'
                WHEN 1 THEN 'VARCHAR(50)'
                WHEN 2 THEN 'FLOAT'
                WHEN 3 THEN 'DATETIME'
            END;

            SET @create_table_sql = CONCAT(@create_table_sql, @col_name, ' ', @col_type);

            IF @col_index < @num_columns THEN
                SET @create_table_sql = CONCAT(@create_table_sql, ', ');
            END IF;

            SET @col_index = @col_index + 1;
        END WHILE;

        SET @create_table_sql = CONCAT(@create_table_sql, ');');

        PREPARE stmt FROM @create_table_sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;

    CLOSE table_cursor;
END;
