from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import award_controller
from my_project.auth.domain.orders.Award import Award

award_bp = Blueprint('award', __name__, url_prefix='/award')

@award_bp.get('')
def get_all_awards() -> Response:
    """
    Get all awards
    ---
    tags:
      - Award
    summary: Retrieve all awards
    description: Get a list of all available awards
    responses:
      200:
        description: List of awards
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
                    example: "Employee of the Month"
                  description:
                    type: string
                    example: "Recognition for outstanding performance"
                  prize_amount:
                    type: number
                    format: float
                    example: 500.00
    """
    awards = award_controller.find_all()
    awards_dto = [award.put_into_dto() for award in awards]
    return make_response(jsonify(awards_dto), HTTPStatus.OK)

@award_bp.post('')
def create_award() -> Response:
    """
    Create a new award
    ---
    tags:
      - Award
    summary: Create a new award
    description: Create a new award record
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
                example: "Teacher of the Year"
                description: Title of the award
              description:
                type: string
                example: "Annual recognition for exceptional teaching"
                description: Description of the award
              prize_amount:
                type: number
                format: float
                example: 1000.00
                description: Prize amount for this award
    responses:
      201:
        description: Award created successfully
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
                  example: "Teacher of the Year"
                description:
                  type: string
                  example: "Annual recognition for exceptional teaching"
                prize_amount:
                  type: number
                  format: float
                  example: 1000.00
      400:
        description: Invalid input data
    """
    content = request.get_json()
    award = Award.create_from_dto(content)
    award_controller.create(award)
    return make_response(jsonify(award.put_into_dto()), HTTPStatus.CREATED)

@award_bp.get('/<int:award_id>')
def get_award(award_id: int) -> Response:
    """
    Get award by ID
    ---
    tags:
      - Award
    summary: Retrieve a specific award
    description: Get an award by its ID
    parameters:
      - in: path
        name: award_id
        required: true
        schema:
          type: integer
        description: ID of the award to retrieve
        example: 1
    responses:
      200:
        description: Award found
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
                  example: "Employee of the Month"
                description:
                  type: string
                  example: "Recognition for outstanding performance"
                prize_amount:
                  type: number
                  format: float
                  example: 500.00
      404:
        description: Award not found
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Award not found"
    """
    award = award_controller.find_by_id(award_id)
    if award:
        return make_response(jsonify(award.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Award not found"}), HTTPStatus.NOT_FOUND)

@award_bp.put('/<int:award_id>')
def update_award(award_id: int) -> Response:
    """
    Update award
    ---
    tags:
      - Award
    summary: Update an existing award
    description: Update an award record by ID
    parameters:
      - in: path
        name: award_id
        required: true
        schema:
          type: integer
        description: ID of the award to update
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
                example: "Outstanding Service Award"
                description: Updated title of the award
              description:
                type: string
                example: "Recognition for exceptional service to children"
                description: Updated description of the award
              prize_amount:
                type: number
                format: float
                example: 750.00
                description: Updated prize amount for this award
    responses:
      200:
        description: Award updated successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Award updated"
      404:
        description: Award not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    award = Award.create_from_dto(content)
    award_controller.update(award_id, award)
    return make_response("Award updated", HTTPStatus.OK)

@award_bp.delete('/<int:award_id>')
def delete_award(award_id: int) -> Response:
    """
    Delete award
    ---
    tags:
      - Award
    summary: Delete an award
    description: Delete an award record by ID
    parameters:
      - in: path
        name: award_id
        required: true
        schema:
          type: integer
        description: ID of the award to delete
        example: 1
    responses:
      204:
        description: Award deleted successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Award deleted"
      404:
        description: Award not found
    """
    award_controller.delete(award_id)
    return make_response("Award deleted", HTTPStatus.NO_CONTENT)
