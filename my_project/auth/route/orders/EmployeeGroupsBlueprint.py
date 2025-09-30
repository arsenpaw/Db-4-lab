from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import employee_groups_controller
from my_project.auth.domain.orders.EmployeeGroups import EmployeeGroups

employee_groups_bp = Blueprint('employeeGroups', __name__, url_prefix='/employee-groups')

@employee_groups_bp.get('')
def get_all_employee_groups() -> Response:
    """
    Get all employee-group associations
    ---
    tags:
      - Employee Groups
    summary: Retrieve all employee-group associations
    description: Get a list of all associations between employees and groups
    responses:
      200:
        description: List of employee-group associations
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  current_group_id:
                    type: integer
                    example: 1
                  current_employee_id:
                    type: integer
                    example: 1
                  assignment_date:
                    type: string
                    format: date
                    example: "2023-09-01"
    """
    associations = employee_groups_controller.find_all()
    associations_dto = [assoc.put_into_dto() for assoc in associations]
    return make_response(jsonify(associations_dto), HTTPStatus.OK)

@employee_groups_bp.post('')
def create_employee_group() -> Response:
    """
    Create a new employee-group association
    ---
    tags:
      - Employee Groups
    summary: Create a new employee-group association
    description: Assign an employee to a group
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - current_group_id
              - current_employee_id
            properties:
              current_group_id:
                type: integer
                example: 1
                description: ID of the group
              current_employee_id:
                type: integer
                example: 1
                description: ID of the employee
              assignment_date:
                type: string
                format: date
                example: "2023-09-01"
                description: Date when the employee was assigned to the group
    responses:
      201:
        description: Employee-group association created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                current_group_id:
                  type: integer
                  example: 1
                current_employee_id:
                  type: integer
                  example: 1
                assignment_date:
                  type: string
                  format: date
                  example: "2023-09-01"
      400:
        description: Invalid input data
    """
    content = request.get_json()
    association = EmployeeGroups.create_from_dto(content)
    employee_groups_controller.create(association)
    return make_response(jsonify(association.put_into_dto()), HTTPStatus.CREATED)

@employee_groups_bp.get('/group/<int:group_id>')
def get_employee_groups_by_group_id(group_id: int) -> Response:
    """
    Get employee-group associations by group ID
    ---
    tags:
      - Employee Groups
    summary: Retrieve all employees assigned to a specific group
    description: Get all employee assignments for a specific group
    parameters:
      - in: path
        name: group_id
        required: true
        schema:
          type: integer
        description: ID of the group to retrieve employee assignments for
        example: 1
    responses:
      200:
        description: Employee-group associations found for the group
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  current_group_id:
                    type: integer
                    example: 1
                  current_employee_id:
                    type: integer
                    example: 1
                  assignment_date:
                    type: string
                    format: date
                    example: "2023-09-01"
      404:
        description: No associations found for this group
    """
    associations = employee_groups_controller.find_by_group_id(group_id)
    associations_dto = [assoc.put_into_dto() for assoc in associations]
    return make_response(jsonify(associations_dto), HTTPStatus.OK)

@employee_groups_bp.get('/employee/<int:employee_id>')
def get_employee_groups_by_employee_id(employee_id: int) -> Response:
    """
    Get employee-group associations by employee ID
    ---
    tags:
      - Employee Groups
    summary: Retrieve all groups assigned to a specific employee
    description: Get all group assignments for a specific employee
    parameters:
      - in: path
        name: employee_id
        required: true
        schema:
          type: integer
        description: ID of the employee to retrieve group assignments for
        example: 1
    responses:
      200:
        description: Employee-group associations found for the employee
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  current_group_id:
                    type: integer
                    example: 1
                  current_employee_id:
                    type: integer
                    example: 1
                  assignment_date:
                    type: string
                    format: date
                    example: "2023-09-01"
      404:
        description: No associations found for this employee
    """
    associations = employee_groups_controller.find_by_employee_id(employee_id)
    associations_dto = [assoc.put_into_dto() for assoc in associations]
    return make_response(jsonify(associations_dto), HTTPStatus.OK)

@employee_groups_bp.delete('/<int:group_id>/<int:employee_id>')
def delete_employee_group(group_id: int, employee_id: int) -> Response:
    """
    Delete employee-group association
    ---
    tags:
      - Employee Groups
    summary: Delete an employee-group association
    description: Remove an employee's assignment to a group
    parameters:
      - in: path
        name: group_id
        required: true
        schema:
          type: integer
        description: ID of the group
        example: 1
      - in: path
        name: employee_id
        required: true
        schema:
          type: integer
        description: ID of the employee
        example: 1
    responses:
      204:
        description: Employee-group association deleted successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Employee-group association deleted"
      404:
        description: Employee-group association not found
    """
    employee_groups_controller.delete(group_id, employee_id)
    return make_response("Employee-group association deleted", HTTPStatus.NO_CONTENT)
