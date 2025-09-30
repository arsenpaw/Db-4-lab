from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import employee_history_controller
from my_project.auth.domain.orders.EmployeeHistory import EmployeeHistory

employee_history_bp = Blueprint('employeeHistory', __name__, url_prefix='/employee-history')

@employee_history_bp.get('')
def get_all_employee_histories() -> Response:
    """
    Get all employee histories
    ---
    tags:
      - Employee History
    summary: Retrieve all employee histories
    description: Get a list of all employee employment and career histories
    responses:
      200:
        description: List of employee histories
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  employee_id:
                    type: integer
                    example: 1
                  hire_date:
                    type: string
                    format: date
                    example: "2020-09-01"
                  termination_date:
                    type: string
                    format: date
                    example: "2024-06-30"
                  position_title:
                    type: string
                    example: "Senior Teacher"
                  notes:
                    type: string
                    example: "Excellent performance and leadership skills"
    """
    histories = employee_history_controller.find_all()
    histories_dto = [history.put_into_dto() for history in histories]
    return make_response(jsonify(histories_dto), HTTPStatus.OK)

@employee_history_bp.post('')
def create_employee_history() -> Response:
    """
    Create a new employee history record
    ---
    tags:
      - Employee History
    summary: Create a new employee history
    description: Record an employee's employment and career history
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - employee_id
              - hire_date
            properties:
              employee_id:
                type: integer
                example: 1
                description: ID of the employee
              hire_date:
                type: string
                format: date
                example: "2020-09-01"
                description: Date when the employee was hired
              termination_date:
                type: string
                format: date
                example: "2024-06-30"
                description: Date when the employee was terminated (optional)
              position_title:
                type: string
                example: "Assistant Teacher"
                description: Position title during this period
              notes:
                type: string
                example: "Great contribution to the team"
                description: Additional notes about the employment period
    responses:
      201:
        description: Employee history created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                employee_id:
                  type: integer
                  example: 1
                hire_date:
                  type: string
                  format: date
                  example: "2020-09-01"
                termination_date:
                  type: string
                  format: date
                  example: "2024-06-30"
                position_title:
                  type: string
                  example: "Assistant Teacher"
                notes:
                  type: string
                  example: "Great contribution to the team"
      400:
        description: Invalid input data
    """
    content = request.get_json()
    history = EmployeeHistory.create_from_dto(content)
    employee_history_controller.create(history)
    return make_response(jsonify(history.put_into_dto()), HTTPStatus.CREATED)

@employee_history_bp.get('/<int:history_id>')
def get_employee_history(history_id: int) -> Response:
    """
    Get employee history by ID
    ---
    tags:
      - Employee History
    summary: Retrieve a specific employee history
    description: Get an employee history record by its ID
    parameters:
      - in: path
        name: history_id
        required: true
        schema:
          type: integer
        description: ID of the employee history record to retrieve
        example: 1
    responses:
      200:
        description: Employee history found
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                employee_id:
                  type: integer
                  example: 1
                hire_date:
                  type: string
                  format: date
                  example: "2020-09-01"
                termination_date:
                  type: string
                  format: date
                  example: "2024-06-30"
                position_title:
                  type: string
                  example: "Senior Teacher"
                notes:
                  type: string
                  example: "Excellent performance and leadership skills"
      404:
        description: Employee history not found
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Employee history not found"
    """
    history = employee_history_controller.find_by_id(history_id)
    if history:
        return make_response(jsonify(history.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Employee history not found"}), HTTPStatus.NOT_FOUND)

@employee_history_bp.get('/employee/<int:employee_id>')
def get_employee_history_by_employee_id(employee_id: int) -> Response:
    """
    Get employee history by employee ID
    ---
    tags:
      - Employee History
    summary: Retrieve employment history for a specific employee
    description: Get all employment history records for a specific employee
    parameters:
      - in: path
        name: employee_id
        required: true
        schema:
          type: integer
        description: ID of the employee to retrieve employment history for
        example: 1
    responses:
      200:
        description: Employee history found for the employee
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  employee_id:
                    type: integer
                    example: 1
                  hire_date:
                    type: string
                    format: date
                    example: "2020-09-01"
                  termination_date:
                    type: string
                    format: date
                    example: "2024-06-30"
                  position_title:
                    type: string
                    example: "Senior Teacher"
                  notes:
                    type: string
                    example: "Excellent performance"
      404:
        description: No employment history found for this employee
    """
    histories = employee_history_controller.find_by_employee_id(employee_id)
    histories_dto = [history.put_into_dto() for history in histories]
    return make_response(jsonify(histories_dto), HTTPStatus.OK)

@employee_history_bp.delete('/<int:history_id>')
def delete_employee_history(history_id: int) -> Response:
    """
    Delete employee history
    ---
    tags:
      - Employee History
    summary: Delete an employee history
    description: Remove an employee history record by ID
    parameters:
      - in: path
        name: history_id
        required: true
        schema:
          type: integer
        description: ID of the employee history to delete
        example: 1
    responses:
      204:
        description: Employee history deleted successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Employee history deleted"
      404:
        description: Employee history not found
    """
    employee_history_controller.delete(history_id)
    return make_response("Employee history deleted", HTTPStatus.NO_CONTENT)
