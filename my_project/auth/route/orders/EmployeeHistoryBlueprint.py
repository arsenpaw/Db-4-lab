from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import employee_history_controller
from my_project.auth.domain.orders.EmployeeHistory import EmployeeHistory

employee_history_bp = Blueprint('employeeHistory', __name__, url_prefix='/employee-history')

@employee_history_bp.get('')
def get_all_employee_histories() -> Response:
    histories = employee_history_controller.find_all()
    histories_dto = [history.put_into_dto() for history in histories]
    return make_response(jsonify(histories_dto), HTTPStatus.OK)

@employee_history_bp.post('')
def create_employee_history() -> Response:
    content = request.get_json()
    history = EmployeeHistory.create_from_dto(content)
    employee_history_controller.create(history)
    return make_response(jsonify(history.put_into_dto()), HTTPStatus.CREATED)

@employee_history_bp.get('/<int:history_id>')
def get_employee_history(history_id: int) -> Response:
    history = employee_history_controller.find_by_id(history_id)
    if history:
        return make_response(jsonify(history.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Employee history not found"}), HTTPStatus.NOT_FOUND)

@employee_history_bp.get('/employee/<int:employee_id>')
def get_employee_history_by_employee_id(employee_id: int) -> Response:
    histories = employee_history_controller.find_by_employee_id(employee_id)
    histories_dto = [history.put_into_dto() for history in histories]
    return make_response(jsonify(histories_dto), HTTPStatus.OK)

@employee_history_bp.delete('/<int:history_id>')
def delete_employee_history(history_id: int) -> Response:
    employee_history_controller.delete(history_id)
    return make_response("Employee history deleted", HTTPStatus.NO_CONTENT)
