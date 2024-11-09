"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes for each entity
    :param app: Flask application object
    """
    # Register error handler blueprint
    app.register_blueprint(err_handler_bp)

    # Import and register blueprints for each of your specific entities
    from .orders.GenderBlueprint import gender_bp
    from .orders.KindergartenBlueprint import kindergarten_bp
    from .orders.GroupBlueprint import group_bp
    from .orders.PositionBlueprint import position_bp
    from .orders.AwardBlueprint import award_bp
    from .orders.ChildBlueprint import child_bp
    from .orders.EmployeeBlueprint import employee_bp
    from .orders.ChildGroupsHistoryBlueprint import child_groups_history_bp
    from .orders.ChildHistoryBlueprint import child_history_bp
    from .orders.ChildKindergartensBlueprint import child_kindergartens_bp
    from .orders.EmployeeGroupsBlueprint import employee_groups_bp
    from .orders.EmployeeHistoryBlueprint import employee_history_bp

    # Register each blueprint with the app
    app.register_blueprint(gender_bp)
    app.register_blueprint(kindergarten_bp)
    app.register_blueprint(group_bp)
    app.register_blueprint(position_bp)
    app.register_blueprint(award_bp)
    app.register_blueprint(child_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(child_groups_history_bp)
    app.register_blueprint(child_history_bp)
    app.register_blueprint(child_kindergartens_bp)
    app.register_blueprint(employee_groups_bp)
    app.register_blueprint(employee_history_bp)
