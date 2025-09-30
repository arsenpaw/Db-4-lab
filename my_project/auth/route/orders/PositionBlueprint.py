from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import position_controller
from my_project.auth.domain.orders.Position import Position

position_bp = Blueprint('position', __name__, url_prefix='/position')

@position_bp.get('')
def get_all_positions() -> Response:
    """
    Get all positions
    ---
    tags:
      - Position
    summary: Retrieve all positions
    description: Get a list of all available positions
    responses:
      200:
        description: List of positions
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
                  title:
                    type: string
                    example: "Teacher"
                  description:
                    type: string
                    example: "Kindergarten teacher position"
                  salary:
                    type: number
                    format: float
                    example: 45000.00
    """
    positions = position_controller.find_all()
    positions_dto = [position.put_into_dto() for position in positions]
    return make_response(jsonify(positions_dto), HTTPStatus.OK)

@position_bp.post('')
def create_position() -> Response:
    """
    Create a new position
    ---
    tags:
      - Position
    summary: Create a new position
    description: Create a new position record
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - title
            properties:
              title:
                type: string
                example: "Assistant Teacher"
                description: Title of the position
              description:
                type: string
                example: "Assistant to the main teacher"
                description: Description of the position
              salary:
                type: number
                format: float
                example: 35000.00
                description: Salary for this position
    responses:
      201:
        description: Position created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                title:
                  type: string
                  example: "Assistant Teacher"
                description:
                  type: string
                  example: "Assistant to the main teacher"
                salary:
                  type: number
                  format: float
                  example: 35000.00
      400:
        description: Invalid input data
    """
    content = request.get_json()
    position = Position.create_from_dto(content)
    position_controller.create(position)
    return make_response(jsonify(position.put_into_dto()), HTTPStatus.CREATED)

@position_bp.get('/<int:position_id>')
def get_position(position_id: int) -> Response:
    """
    Get position by ID
    ---
    tags:
      - Position
    summary: Retrieve a specific position
    description: Get a position by its ID
    parameters:
      - in: path
        name: position_id
        required: true
        schema:
          type: integer
        description: ID of the position to retrieve
        example: 1
    responses:
      200:
        description: Position found
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                title:
                  type: string
                  example: "Teacher"
                description:
                  type: string
                  example: "Kindergarten teacher position"
                salary:
                  type: number
                  format: float
                  example: 45000.00
      404:
        description: Position not found
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Position not found"
    """
    position = position_controller.find_by_id(position_id)
    if position:
        return make_response(jsonify(position.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Position not found"}), HTTPStatus.NOT_FOUND)

@position_bp.put('/<int:position_id>')
def update_position(position_id: int) -> Response:
    """
    Update position
    ---
    tags:
      - Position
    summary: Update an existing position
    description: Update a position record by ID
    parameters:
      - in: path
        name: position_id
        required: true
        schema:
          type: integer
        description: ID of the position to update
        example: 1
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - title
            properties:
              title:
                type: string
                example: "Senior Teacher"
                description: Updated title of the position
              description:
                type: string
                example: "Senior kindergarten teacher with experience"
                description: Updated description of the position
              salary:
                type: number
                format: float
                example: 55000.00
                description: Updated salary for this position
    responses:
      200:
        description: Position updated successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Position updated"
      404:
        description: Position not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    position = Position.create_from_dto(content)
    position_controller.update(position_id, position)
    return make_response("Position updated", HTTPStatus.OK)

@position_bp.delete('/<int:position_id>')
def delete_position(position_id: int) -> Response:
    """
    Delete position
    ---
    tags:
      - Position
    summary: Delete a position
    description: Delete a position record by ID
    parameters:
      - in: path
        name: position_id
        required: true
        schema:
          type: integer
        description: ID of the position to delete
        example: 1
    responses:
      204:
        description: Position deleted successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Position deleted"
      404:
        description: Position not found
    """
    position_controller.delete(position_id)
    return make_response("Position deleted", HTTPStatus.NO_CONTENT)
