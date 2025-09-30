from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import child_controller
from my_project.auth.domain.orders.Child import Child

child_bp = Blueprint('child', __name__, url_prefix='/child')

@child_bp.get('')
def get_all_children() -> Response:
    """
    Get all children
    ---
    tags:
      - Child
    summary: Retrieve all children
    description: Get a list of all children enrolled in the kindergarten system
    responses:
      200:
        description: List of children
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
                    example: "Emma"
                  last_name:
                    type: string
                    example: "Johnson"
                  birth_date:
                    type: string
                    format: date
                    example: "2019-05-15"
                  gender_id:
                    type: integer
                    example: 2
                  parent_name:
                    type: string
                    example: "Sarah Johnson"
                  parent_phone:
                    type: string
                    example: "+1234567890"
    """
    children = child_controller.find_all()
    children_dto = [child.put_into_dto() for child in children]
    return make_response(jsonify(children_dto), HTTPStatus.OK)

@child_bp.post('')
def create_child() -> Response:
    """
    Create a new child
    ---
    tags:
      - Child
    summary: Create a new child record
    description: Register a new child in the kindergarten system
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - first_name
              - last_name
              - birth_date
              - gender_id
            properties:
              first_name:
                type: string
                example: "Lucas"
                description: First name of the child
              last_name:
                type: string
                example: "Miller"
                description: Last name of the child
              birth_date:
                type: string
                format: date
                example: "2020-03-10"
                description: Birth date of the child
              gender_id:
                type: integer
                example: 1
                description: ID of the child's gender
              parent_name:
                type: string
                example: "Michael Miller"
                description: Name of the parent/guardian
              parent_phone:
                type: string
                example: "+1234567891"
                description: Phone number of the parent/guardian
    responses:
      201:
        description: Child created successfully
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
                  example: "Lucas"
                last_name:
                  type: string
                  example: "Miller"
                birth_date:
                  type: string
                  format: date
                  example: "2020-03-10"
                gender_id:
                  type: integer
                  example: 1
                parent_name:
                  type: string
                  example: "Michael Miller"
                parent_phone:
                  type: string
                  example: "+1234567891"
      400:
        description: Invalid input data
    """
    content = request.get_json()
    child = Child.create_from_dto(content)
    child_controller.create(child)
    return make_response(jsonify(child.put_into_dto()), HTTPStatus.CREATED)

@child_bp.get('/<int:child_id>')
def get_child(child_id: int) -> Response:
    """
    Get child by ID
    ---
    tags:
      - Child
    summary: Retrieve a specific child
    description: Get a child's information by their ID
    parameters:
      - in: path
        name: child_id
        required: true
        schema:
          type: integer
        description: ID of the child to retrieve
        example: 1
    responses:
      200:
        description: Child found
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
                  example: "Emma"
                last_name:
                  type: string
                  example: "Johnson"
                birth_date:
                  type: string
                  format: date
                  example: "2019-05-15"
                gender_id:
                  type: integer
                  example: 2
                parent_name:
                  type: string
                  example: "Sarah Johnson"
                parent_phone:
                  type: string
                  example: "+1234567890"
      404:
        description: Child not found
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Child not found"
    """
    child = child_controller.find_by_id(child_id)
    if child:
        return make_response(jsonify(child.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Child not found"}), HTTPStatus.NOT_FOUND)

@child_bp.put('/<int:child_id>')
def update_child(child_id: int) -> Response:
    """
    Update child
    ---
    tags:
      - Child
    summary: Update an existing child
    description: Update a child's information by ID
    parameters:
      - in: path
        name: child_id
        required: true
        schema:
          type: integer
        description: ID of the child to update
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
              - birth_date
              - gender_id
            properties:
              first_name:
                type: string
                example: "Emma"
                description: Updated first name of the child
              last_name:
                type: string
                example: "Johnson-Smith"
                description: Updated last name of the child
              birth_date:
                type: string
                format: date
                example: "2019-05-15"
                description: Updated birth date of the child
              gender_id:
                type: integer
                example: 2
                description: Updated gender ID
              parent_name:
                type: string
                example: "Sarah Johnson-Smith"
                description: Updated parent/guardian name
              parent_phone:
                type: string
                example: "+1234567892"
                description: Updated parent/guardian phone number
    responses:
      200:
        description: Child updated successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Child updated"
      404:
        description: Child not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    child = Child.create_from_dto(content)
    child_controller.update(child_id, child)
    return make_response("Child updated", HTTPStatus.OK)

@child_bp.delete('/<int:child_id>')
def delete_child(child_id: int) -> Response:
    """
    Delete child
    ---
    tags:
      - Child
    summary: Delete a child
    description: Remove a child record from the system by ID
    parameters:
      - in: path
        name: child_id
        required: true
        schema:
          type: integer
        description: ID of the child to delete
        example: 1
    responses:
      204:
        description: Child deleted successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Child deleted"
      404:
        description: Child not found
    """
    child_controller.delete(child_id)
    return make_response("Child deleted", HTTPStatus.NO_CONTENT)
