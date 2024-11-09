from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import employee_controller
from my_project.auth.domain.orders.Employee import Employee

employee_bp = Blueprint('employee', __name__, url_prefix='/employee')

@employee_bp.get('')
def get_all_employees() -> Response:
    employees = employee_controller.find_all()
    employees_dto = [employee.put_into_dto() for employee in employees]
    return make_response(jsonify(employees_dto), HTTPStatus.OK)

@employee_bp.post('')
def create_employee() -> Response:
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.create(employee)
    return make_response(jsonify(employee.put_into_dto()), HTTPStatus.CREATED)

@employee_bp.get('/<int:employee_id>')
def get_employee(employee_id: int) -> Response:
    employee = employee_controller.find_by_id(employee_id)
    if employee:
        return make_response(jsonify(employee.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Employee not found"}), HTTPStatus.NOT_FOUND)

@employee_bp.put('/<int:employee_id>')
def update_employee(employee_id: int) -> Response:
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.update(employee_id, employee)
    return make_response("Employee updated", HTTPStatus.OK)

@employee_bp.delete('/<int:employee_id>')
def delete_employee(employee_id: int) -> Response:
    employee_controller.delete(employee_id)
    return make_response("Employee deleted", HTTPStatus.NO_CONTENT)
