from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import employee_controller
from my_project.auth.domain.orders.Employee import Employee

employee_bp = Blueprint('employee', __name__, url_prefix='/employee')

@employee_bp.get('all')
def get_all_employees_with() -> Response:
    """
    Get all employees with gender details
    ---
    tags:
      - Employee
    summary: Retrieve all employees with their gender information
    description: Get a list of all employees including their gender details
    responses:
      200:
        description: List of employees with gender details
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
                  first_name:
                    type: string
                    example: "John"
                  last_name:
                    type: string
                    example: "Doe"
                  gender:
                    type: object
                    properties:
                      id:
                        type: integer
                        example: 1
                      name:
                        type: string
                        example: "Male"
                  kindergarten_id:
                    type: integer
                    example: 1
                  position_id:
                    type: integer
                    example: 1
    """
    employees = employee_controller.find_with_gender()
    employees_dto = [employee.put_into_large_dto() for employee in employees]
    return make_response(jsonify(employees_dto), HTTPStatus.OK)

@employee_bp.get('')
def get_all_employees() -> Response:
    """
    Get all employees
    ---
    tags:
      - Employee
    summary: Retrieve all employees
    description: Get a list of all employees with basic information
    responses:
      200:
        description: List of employees
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
                  first_name:
                    type: string
                    example: "John"
                  last_name:
                    type: string
                    example: "Doe"
                  gender_id:
                    type: integer
                    example: 1
                  kindergarten_id:
                    type: integer
                    example: 1
                  position_id:
                    type: integer
                    example: 1
    """
    employees = employee_controller.find_all()
    employees_dto = [employee.put_into_dto() for employee in employees]
    return make_response(jsonify(employees_dto), HTTPStatus.OK)

@employee_bp.post('')
def create_employee() -> Response:
    """
    Create a new employee
    ---
    tags:
      - Employee
    summary: Create a new employee
    description: Create a new employee record
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - first_name
              - last_name
              - gender_id
              - kindergarten_id
              - position_id
            properties:
              first_name:
                type: string
                example: "Jane"
                description: First name of the employee
              last_name:
                type: string
                example: "Smith"
                description: Last name of the employee
              gender_id:
                type: integer
                example: 2
                description: ID of the gender
              kindergarten_id:
                type: integer
                example: 1
                description: ID of the kindergarten
              position_id:
                type: integer
                example: 1
                description: ID of the position
    responses:
      201:
        description: Employee created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                first_name:
                  type: string
                  example: "Jane"
                last_name:
                  type: string
                  example: "Smith"
                gender_id:
                  type: integer
                  example: 2
                kindergarten_id:
                  type: integer
                  example: 1
                position_id:
                  type: integer
                  example: 1
      400:
        description: Invalid input data
    """
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.create(employee)
    return make_response(jsonify(employee.put_into_dto()), HTTPStatus.CREATED)

@employee_bp.get('/<int:employee_id>')
def get_employee(employee_id: int) -> Response:
    """
    Get employee by ID
    ---
    tags:
      - Employee
    summary: Retrieve a specific employee
    description: Get an employee by their ID
    parameters:
      - in: path
        name: employee_id
        required: true
        schema:
          type: integer
        description: ID of the employee to retrieve
        example: 1
    responses:
      200:
        description: Employee found
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                first_name:
                  type: string
                  example: "John"
                last_name:
                  type: string
                  example: "Doe"
                gender_id:
                  type: integer
                  example: 1
                kindergarten_id:
                  type: integer
                  example: 1
                position_id:
                  type: integer
                  example: 1
      404:
        description: Employee not found
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Employee not found"
    """
    employee = employee_controller.find_by_id(employee_id)
    if employee:
        return make_response(jsonify(employee.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Employee not found"}), HTTPStatus.NOT_FOUND)

@employee_bp.put('/<int:employee_id>')
def update_employee(employee_id: int) -> Response:
    """
    Update employee
    ---
    tags:
      - Employee
    summary: Update an existing employee
    description: Update an employee record by ID
    parameters:
      - in: path
        name: employee_id
        required: true
        schema:
          type: integer
        description: ID of the employee to update
        example: 1
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - first_name
              - last_name
              - gender_id
              - kindergarten_id
              - position_id
            properties:
              first_name:
                type: string
                example: "John"
                description: Updated first name of the employee
              last_name:
                type: string
                example: "Doe"
                description: Updated last name of the employee
              gender_id:
                type: integer
                example: 1
                description: Updated gender ID
              kindergarten_id:
                type: integer
                example: 1
                description: Updated kindergarten ID
              position_id:
                type: integer
                example: 1
                description: Updated position ID
    responses:
      200:
        description: Employee updated successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Employee updated"
      404:
        description: Employee not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.update(employee_id, employee)
    return make_response("Employee updated", HTTPStatus.OK)

@employee_bp.delete('/<int:employee_id>')
def delete_employee(employee_id: int) -> Response:
    """
    Delete employee
    ---
    tags:
      - Employee
    summary: Delete an employee
    description: Delete an employee record by ID
    parameters:
      - in: path
        name: employee_id
        required: true
        schema:
          type: integer
        description: ID of the employee to delete
        example: 1
    responses:
      204:
        description: Employee deleted successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Employee deleted"
      404:
        description: Employee not found
    """
    employee_controller.delete(employee_id)
    return make_response("Employee deleted", HTTPStatus.NO_CONTENT)
