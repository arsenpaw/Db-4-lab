"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

import os
from datetime import datetime
from http import HTTPStatus
import secrets
from typing import Dict, Any

from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy_utils import database_exists, create_database

from my_project.auth.route import register_routes

SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

# Database
db = SQLAlchemy()

todos = {}


def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    """
    Creates Flask application
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    :return: Flask application object
    """
    _process_input_config(app_config, additional_config)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}

    _init_db(app)
    register_routes(app)
    _init_swagger(app)
    _init_function(app)
    _init_procedures(app)
    _init_trigger(app)
    _init_employee_award(app,5,4)
    _init_positions(app)
    _do_cursor_task(app)
    return app


def _do_cursor_task(app:Flask):
    with open("cursor.sql", "r") as file:
        sql_script = file.read()
    with app.app_context() as connection:
        db.session.execute(text(sql_script))
        print("SQL script executed successfully.")


def _init_positions(app: Flask):
    with app.app_context():
        for i in range(20,30):
            db.session.execute(
                """
                INSERT IGNORE INTO position (id, title)
                VALUES (:p_id, :p_titled)
                """,
                {'p_id': i, 'p_titled': f'Noname{i}'}
            )
        db.session.commit()


def _init_employee_award(app: Flask, current_group_id: int,current_employee_id: int) -> None:
    with app.app_context():
        db.session.execute("CALL AddEmployeeGroup(:current_group_id, :current_employee_id)", {
            'current_group_id': current_group_id,
            'current_employee_id': current_employee_id
        })
        db.session.commit()


def _init_procedures(app: Flask) -> None:
    with app.app_context():
        db.session.execute('''
            DROP PROCEDURE IF EXISTS AddEmployeeGroup;
                CREATE PROCEDURE AddEmployeeGroup(
                IN p_current_group_id INT,
                IN p_current_employee_id INT
            )
            BEGIN
                INSERT IGNORE  INTO employee_groups (current_group_id, current_employee_id)
                VALUES (p_current_group_id, p_current_employee_id);
            END;
          ''')
        db.session.commit()

def _init_function(app: Flask) -> None:
    with app.app_context():
        db.session.execute('''
        DROP FUNCTION IF EXISTS YoungestChild;
        CREATE FUNCTION YoungestChild() 
        RETURNS DATE
        DETERMINISTIC
        BEGIN
            DECLARE youngest_date DATE;
            SELECT MIN(admission_date) INTO youngest_date 
            FROM test.child_history;
            RETURN youngest_date;
        END;
        ''')
        db.session.execute('''
           DROP PROCEDURE IF EXISTS ExecSelect;
            CREATE PROCEDURE ExecSelect()
            BEGIN
                SELECT YoungestChild() AS AdmissionDate;
            END;
        ''')

        db.session.commit()
        result = db.session.execute('CALL ExecSelect() ').scalar()
        print(f"The youngest child has {result} admision date")


def _init_trigger(app: Flask) -> None:
    with app.app_context():
        #  as fk constraint
        db.session.execute('''
        DROP TRIGGER IF EXISTS trigger_gender_id;
        CREATE TRIGGER trigger_gender_id
        BEFORE INSERT ON employee
        FOR EACH ROW
        BEGIN
            IF NEW.Id < 0 THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Primary key cannot be negative';
            END IF;
            IF NOT EXISTS (SELECT 1 FROM gender WHERE gender.Id = NEW.gender_id) THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'No such gender exist';
            END IF;
        END;
        ''')
        #update
        db.session.execute('''
               DROP TRIGGER IF EXISTS trigger_gender_id_up;
               CREATE TRIGGER trigger_gender_id_up
               BEFORE UPDATE ON employee
               FOR EACH ROW
               BEGIN
                   IF NEW.Id < 0 THEN
                       SIGNAL SQLSTATE '45000'
                       SET MESSAGE_TEXT = 'Primary key cannot be negative';
                   END IF;
                   IF NOT EXISTS (SELECT 1 FROM gender WHERE gender.Id = NEW.gender_id) THEN
                       SIGNAL SQLSTATE '45000'
                       SET MESSAGE_TEXT = 'No such gender exist';
                   END IF;
               END;
               ''')
        #  double zero limiter
        db.session.execute('''
               DROP TRIGGER IF EXISTS double_zerro_trigger;
               CREATE TRIGGER double_zerro_trigger
               BEFORE INSERT ON gender 
               FOR EACH ROW
               BEGIN
                   IF RIGHT(NEW.Id,2) = '00' THEN
                       SIGNAL SQLSTATE '45000'
                       SET MESSAGE_TEXT = 'Identifier cannot have double zero due to the rule of universe';
                   END IF;
               END;
               ''')
        # update
        db.session.execute('''
               DROP TRIGGER IF EXISTS double_zerro_trigger_upd;
               CREATE TRIGGER double_zerro_trigger_upd
               BEFORE UPDATE ON gender 
               FOR EACH ROW
               BEGIN
                   IF RIGHT(NEW.Id,2) = '00' THEN
                       SIGNAL SQLSTATE '45000'
                       SET MESSAGE_TEXT = 'Identifier cannot have double zero due to the rule of universe';
                   END IF;
               END;
               ''')

        # max 6 chars and min 3  create
        db.session.execute('''
                        DROP TRIGGER IF EXISTS award_limiter;
                        CREATE TRIGGER award_limiter
                        BEFORE INSERT ON award
                        FOR EACH ROW
                        BEGIN
                            IF CHAR_LENGTH(NEW.description) <= 3 OR CHAR_LENGTH(NEW.description) > 6 THEN 
                                SIGNAL SQLSTATE '45000'
                                SET MESSAGE_TEXT = 'Tanos said that award description must be at least 6 characters.';
                            END IF;
                        END;

                       ''')
        # update
        db.session.execute('''
                        DROP TRIGGER IF EXISTS award_limiter_upd;
                        CREATE TRIGGER award_limiter_upd
                        BEFORE UPDATE ON award
                        FOR EACH ROW
                        BEGIN
                            IF CHAR_LENGTH(NEW.description) <= 3 OR CHAR_LENGTH(NEW.description) > 6 THEN 
                                SIGNAL SQLSTATE '45000'
                                SET MESSAGE_TEXT = 'Tanos said that award description must be at least 6 characters.';
                            END IF;
                        END;

                       ''')


        # forbid delete
        db.session.execute('''
                              DROP TRIGGER IF EXISTS on_kindergarten_remove;
                              CREATE TRIGGER on_kindergarten_remove
                              BEFORE DELETE ON kindergarten 
                              FOR EACH ROW
                              BEGIN                              
                                  SIGNAL SQLSTATE '45000'
                                  SET MESSAGE_TEXT = 'Removing kindergarden is not the jedi way';
                              END;
                              ''')

        db.session.commit()


def _init_swagger(app: Flask) -> None:
    # A-lia Swagger
    restx_api = Api(app, title='Pavelchak test backend',
                    description='A simple backend')  # https://flask-restx.readthedocs.io/

    @restx_api.route('/number/<string:todo_id>')
    class TodoSimple(Resource):
        @staticmethod
        def get(todo_id):
            return todos, 202

        @staticmethod
        def put(todo_id):
            todos[todo_id] = todo_id
            return todos, HTTPStatus.CREATED

    @app.route("/hi")
    def hello_world():
        return todos, HTTPStatus.OK


def _init_db(app: Flask) -> None:
    """
    Initializes DB with SQLAlchemy
    :param app: Flask application object
    """
    db.init_app(app)

    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    import my_project.auth.domain
    with app.app_context():
        db.create_all()


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    """
    Processes input configuration
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    """
    # Get root username and password
    root_user = os.getenv(MYSQL_ROOT_USER, additional_config[MYSQL_ROOT_USER])
    root_password = os.getenv(MYSQL_ROOT_PASSWORD, additional_config[MYSQL_ROOT_PASSWORD])
    # Set root username and password in app_config
    app_config[SQLALCHEMY_DATABASE_URI] = app_config[SQLALCHEMY_DATABASE_URI].format(root_user, root_password)
    pass
