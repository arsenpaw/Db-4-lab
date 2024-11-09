from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import employee_groups_controller
from my_project.auth.domain.orders.EmployeeGroups import EmployeeGroups

employee_groups_bp = Blueprint('employeeGroups', __name__, url_prefix='/employee-groups')

@employee_groups_bp.get('')
def get_all_employee_groups() -> Response:
    associations = employee_groups_controller.find_all()
    associations_dto = [assoc.put_into_dto() for assoc in associations]
    return make_response(jsonify(associations_dto), HTTPStatus.OK)

@employee_groups_bp.post('')
def create_employee_group() -> Response:
    content = request.get_json()
    association = EmployeeGroups.create_from_dto(content)
    employee_groups_controller.create(association)
    return make_response(jsonify(association.put_into_dto()), HTTPStatus.CREATED)

@employee_groups_bp.get('/group/<int:group_id>')
def get_employee_groups_by_group_id(group_id: int) -> Response:
    associations = employee_groups_controller.find_by_group_id(group_id)
    associations_dto = [assoc.put_into_dto() for assoc in associations]
    return make_response(jsonify(associations_dto), HTTPStatus.OK)

@employee_groups_bp.get('/employee/<int:employee_id>')
def get_employee_groups_by_employee_id(employee_id: int) -> Response:
    associations = employee_groups_controller.find_by_employee_id(employee_id)
    associations_dto = [assoc.put_into_dto() for assoc in associations]
    return make_response(jsonify(associations_dto), HTTPStatus.OK)

@employee_groups_bp.delete('/<int:group_id>/<int:employee_id>')
def delete_employee_group(group_id: int, employee_id: int) -> Response:
    employee_groups_controller.delete(group_id, employee_id)
    return make_response("Employee-group association deleted", HTTPStatus.NO_CONTENT)
