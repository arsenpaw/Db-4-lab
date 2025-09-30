from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import gender_controller
from my_project.auth.domain.orders.Gender import Gender

gender_bp = Blueprint('gender', __name__, url_prefix='/gender')

@gender_bp.get('')
def get_all_genders() -> Response:
    """
    Get all genders
    ---
    tags:
      - Gender
    summary: Retrieve all genders
    description: Get a list of all available genders
    responses:
      200:
        description: List of genders
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
                  name:
                    type: string
                    example: "Male"
    """
    genders = gender_controller.find_all()
    genders_dto = [gender.put_into_dto() for gender in genders]
    return make_response(jsonify(genders_dto), HTTPStatus.OK)

@gender_bp.post('')
def create_gender() -> Response:
    """
    Create a new gender
    ---
    tags:
      - Gender
    summary: Create a new gender
    description: Create a new gender record
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - name
            properties:
              name:
                type: string
                example: "Female"
                description: Name of the gender
    responses:
      201:
        description: Gender created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                name:
                  type: string
                  example: "Female"
      400:
        description: Invalid input data
    """
    content = request.get_json()
    gender = Gender.create_from_dto(content)
    gender_controller.create(gender)
    return make_response(jsonify(gender.put_into_dto()), HTTPStatus.CREATED)

@gender_bp.get('/<int:gender_id>')
def get_gender(gender_id: int) -> Response:
    """
    Get gender by ID
    ---
    tags:
      - Gender
    summary: Retrieve a specific gender
    description: Get a gender by its ID
    parameters:
      - in: path
        name: gender_id
        required: true
        schema:
          type: integer
        description: ID of the gender to retrieve
        example: 1
    responses:
      200:
        description: Gender found
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                name:
                  type: string
                  example: "Male"
      404:
        description: Gender not found
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Gender not found"
    """
    gender = gender_controller.find_by_id(gender_id)
    if gender:
        return make_response(jsonify(gender.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Gender not found"}), HTTPStatus.NOT_FOUND)

@gender_bp.put('/<int:gender_id>')
def update_gender(gender_id: int) -> Response:
    """
    Update gender
    ---
    tags:
      - Gender
    summary: Update an existing gender
    description: Update a gender record by ID
    parameters:
      - in: path
        name: gender_id
        required: true
        schema:
          type: integer
        description: ID of the gender to update
        example: 1
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - name
            properties:
              name:
                type: string
                example: "Non-binary"
                description: Updated name of the gender
    responses:
      200:
        description: Gender updated successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Gender updated"
      404:
        description: Gender not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    gender = Gender.create_from_dto(content)
    gender_controller.update(gender_id, gender)
    return make_response("Gender updated", HTTPStatus.OK)

@gender_bp.delete('/<int:gender_id>')
def delete_gender(gender_id: int) -> Response:
    """
    Delete gender
    ---
    tags:
      - Gender
    summary: Delete a gender
    description: Delete a gender record by ID
    parameters:
      - in: path
        name: gender_id
        required: true
        schema:
          type: integer
        description: ID of the gender to delete
        example: 1
    responses:
      204:
        description: Gender deleted successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Gender deleted"
      404:
        description: Gender not found
    """
    gender_controller.delete(gender_id)
    return make_response("Gender deleted", HTTPStatus.NO_CONTENT)
