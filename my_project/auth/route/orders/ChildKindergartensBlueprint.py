from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import child_kindergartens_controller
from my_project.auth.domain.orders.ChildKindergartens import ChildKindergartens

child_kindergartens_bp = Blueprint('childKindergartens', __name__, url_prefix='/child-kindergartens')

@child_kindergartens_bp.get('')
def get_all_child_kindergartens() -> Response:
    """
    Get all child-kindergarten associations
    ---
    tags:
      - Child Kindergartens
    summary: Retrieve all child-kindergarten associations
    description: Get a list of all associations between children and kindergartens
    responses:
      200:
        description: List of child-kindergarten associations
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  child_id:
                    type: integer
                    example: 1
                  kindergarten_id:
                    type: integer
                    example: 1
                  enrollment_date:
                    type: string
                    format: date
                    example: "2023-09-01"
                  graduation_date:
                    type: string
                    format: date
                    example: "2024-06-30"
    """
    records = child_kindergartens_controller.find_all()
    records_dto = [record.put_into_dto() for record in records]
    return make_response(jsonify(records_dto), HTTPStatus.OK)

@child_kindergartens_bp.post('')
def create_child_kindergarten() -> Response:
    """
    Create a new child-kindergarten association
    ---
    tags:
      - Child Kindergartens
    summary: Create a new child-kindergarten association
    description: Enroll a child in a kindergarten
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - child_id
              - kindergarten_id
              - enrollment_date
            properties:
              child_id:
                type: integer
                example: 1
                description: ID of the child
              kindergarten_id:
                type: integer
                example: 1
                description: ID of the kindergarten
              enrollment_date:
                type: string
                format: date
                example: "2023-09-01"
                description: Date when the child enrolled in the kindergarten
              graduation_date:
                type: string
                format: date
                example: "2024-06-30"
                description: Date when the child graduated from the kindergarten (optional)
    responses:
      201:
        description: Child-kindergarten association created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                child_id:
                  type: integer
                  example: 1
                kindergarten_id:
                  type: integer
                  example: 1
                enrollment_date:
                  type: string
                  format: date
                  example: "2023-09-01"
                graduation_date:
                  type: string
                  format: date
                  example: "2024-06-30"
      400:
        description: Invalid input data
    """
    content = request.get_json()
    record = ChildKindergartens.create_from_dto(content)
    child_kindergartens_controller.create(record)
    return make_response(jsonify(record.put_into_dto()), HTTPStatus.CREATED)

@child_kindergartens_bp.get('/<int:child_id>')
def get_child_kindergartens_by_child_id(child_id: int) -> Response:
    """
    Get child-kindergarten associations by child ID
    ---
    tags:
      - Child Kindergartens
    summary: Retrieve kindergarten history for a specific child
    description: Get all kindergarten enrollments for a specific child
    parameters:
      - in: path
        name: child_id
        required: true
        schema:
          type: integer
        description: ID of the child to retrieve kindergarten history for
        example: 1
    responses:
      200:
        description: Child-kindergarten associations found for the child
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  child_id:
                    type: integer
                    example: 1
                  kindergarten_id:
                    type: integer
                    example: 1
                  enrollment_date:
                    type: string
                    format: date
                    example: "2023-09-01"
                  graduation_date:
                    type: string
                    format: date
                    example: "2024-06-30"
      404:
        description: No kindergarten history found for this child
    """
    records = child_kindergartens_controller.find_by_child_id(child_id)
    records_dto = [record.put_into_dto() for record in records]
    return make_response(jsonify(records_dto), HTTPStatus.OK)

@child_kindergartens_bp.delete('/<int:child_id>/<int:kindergarten_id>')
def delete_child_kindergarten(child_id: int, kindergarten_id: int) -> Response:
    """
    Delete child-kindergarten association
    ---
    tags:
      - Child Kindergartens
    summary: Delete a child-kindergarten association
    description: Remove a child's enrollment from a kindergarten
    parameters:
      - in: path
        name: child_id
        required: true
        schema:
          type: integer
        description: ID of the child
        example: 1
      - in: path
        name: kindergarten_id
        required: true
        schema:
          type: integer
        description: ID of the kindergarten
        example: 1
    responses:
      204:
        description: Child-kindergarten association deleted successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Child-kindergarten record deleted"
      404:
        description: Child-kindergarten association not found
    """
    child_kindergartens_controller.delete(child_id, kindergarten_id)
    return make_response("Child-kindergarten record deleted", HTTPStatus.NO_CONTENT)
