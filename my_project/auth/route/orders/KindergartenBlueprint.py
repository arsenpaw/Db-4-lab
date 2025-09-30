from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import kindergarten_controller
from my_project.auth.domain.orders.Kindergarten import Kindergarten

kindergarten_bp = Blueprint('kindergarten', __name__, url_prefix='/kindergarten')

@kindergarten_bp.get('')
def get_all_kindergartens() -> Response:
    """
    Get all kindergartens
    ---
    tags:
      - Kindergarten
    summary: Retrieve all kindergartens
    description: Get a list of all available kindergartens
    responses:
      200:
        description: List of kindergartens
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
                    example: "Sunshine Kindergarten"
                  address:
                    type: string
                    example: "123 Main St"
                  phone:
                    type: string
                    example: "+1234567890"
    """
    kindergartens = kindergarten_controller.find_all()
    kindergartens_dto = [kindergarten.put_into_dto() for kindergarten in kindergartens]
    return make_response(jsonify(kindergartens_dto), HTTPStatus.OK)

@kindergarten_bp.post('')
def create_kindergarten() -> Response:
    """
    Create a new kindergarten
    ---
    tags:
      - Kindergarten
    summary: Create a new kindergarten
    description: Create a new kindergarten record
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
                example: "Rainbow Kindergarten"
                description: Name of the kindergarten
              address:
                type: string
                example: "456 Oak Ave"
                description: Address of the kindergarten
              phone:
                type: string
                example: "+1234567891"
                description: Phone number of the kindergarten
    responses:
      201:
        description: Kindergarten created successfully
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
                  example: "Rainbow Kindergarten"
                address:
                  type: string
                  example: "456 Oak Ave"
                phone:
                  type: string
                  example: "+1234567891"
      400:
        description: Invalid input data
    """
    content = request.get_json()
    kindergarten = Kindergarten.create_from_dto(content)
    kindergarten_controller.create(kindergarten)
    return make_response(jsonify(kindergarten.put_into_dto()), HTTPStatus.CREATED)

@kindergarten_bp.get('/<int:kindergarten_id>')
def get_kindergarten(kindergarten_id: int) -> Response:
    """
    Get kindergarten by ID
    ---
    tags:
      - Kindergarten
    summary: Retrieve a specific kindergarten
    description: Get a kindergarten by its ID
    parameters:
      - in: path
        name: kindergarten_id
        required: true
        schema:
          type: integer
        description: ID of the kindergarten to retrieve
        example: 1
    responses:
      200:
        description: Kindergarten found
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
                  example: "Sunshine Kindergarten"
                address:
                  type: string
                  example: "123 Main St"
                phone:
                  type: string
                  example: "+1234567890"
      404:
        description: Kindergarten not found
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Kindergarten not found"
    """
    kindergarten = kindergarten_controller.find_by_id(kindergarten_id)
    if kindergarten:
        return make_response(jsonify(kindergarten.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Kindergarten not found"}), HTTPStatus.NOT_FOUND)

@kindergarten_bp.put('/<int:kindergarten_id>')
def update_kindergarten(kindergarten_id: int) -> Response:
    """
    Update kindergarten
    ---
    tags:
      - Kindergarten
    summary: Update an existing kindergarten
    description: Update a kindergarten record by ID
    parameters:
      - in: path
        name: kindergarten_id
        required: true
        schema:
          type: integer
        description: ID of the kindergarten to update
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
                example: "Updated Kindergarten Name"
                description: Updated name of the kindergarten
              address:
                type: string
                example: "789 Updated St"
                description: Updated address of the kindergarten
              phone:
                type: string
                example: "+1234567892"
                description: Updated phone number of the kindergarten
    responses:
      200:
        description: Kindergarten updated successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Kindergarten updated"
      404:
        description: Kindergarten not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    kindergarten = Kindergarten.create_from_dto(content)
    kindergarten_controller.update(kindergarten_id, kindergarten)
    return make_response("Kindergarten updated", HTTPStatus.OK)

@kindergarten_bp.delete('/<int:kindergarten_id>')
def delete_kindergarten(kindergarten_id: int) -> Response:
    """
    Delete kindergarten
    ---
    tags:
      - Kindergarten
    summary: Delete a kindergarten
    description: Delete a kindergarten record by ID
    parameters:
      - in: path
        name: kindergarten_id
        required: true
        schema:
          type: integer
        description: ID of the kindergarten to delete
        example: 1
    responses:
      204:
        description: Kindergarten deleted successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Kindergarten deleted"
      404:
        description: Kindergarten not found
    """
    kindergarten_controller.delete(kindergarten_id)
    return make_response("Kindergarten deleted", HTTPStatus.NO_CONTENT)
