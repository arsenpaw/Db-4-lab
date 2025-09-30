from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import child_history_controller
from my_project.auth.domain.orders.ChildHistory import ChildHistory

child_history_bp = Blueprint('childHistory', __name__, url_prefix='/child-history')

@child_history_bp.get('')
def get_all_child_histories() -> Response:
    """
    Get all child histories
    ---
    tags:
      - Child History
    summary: Retrieve all child histories
    description: Get a list of all child admission and attendance histories
    responses:
      200:
        description: List of child histories
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
                  child_id:
                    type: integer
                    example: 1
                  admission_date:
                    type: string
                    format: date
                    example: "2023-09-01"
                  graduation_date:
                    type: string
                    format: date
                    example: "2024-06-30"
                  notes:
                    type: string
                    example: "Good progress in learning activities"
    """
    histories = child_history_controller.find_all()
    histories_dto = [history.put_into_dto() for history in histories]
    return make_response(jsonify(histories_dto), HTTPStatus.OK)

@child_history_bp.post('')
def create_child_history() -> Response:
    """
    Create a new child history record
    ---
    tags:
      - Child History
    summary: Create a new child history
    description: Record a child's admission and academic history
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - child_id
              - admission_date
            properties:
              child_id:
                type: integer
                example: 1
                description: ID of the child
              admission_date:
                type: string
                format: date
                example: "2023-09-01"
                description: Date when the child was admitted
              graduation_date:
                type: string
                format: date
                example: "2024-06-30"
                description: Date when the child graduated (optional)
              notes:
                type: string
                example: "Excellent behavior and learning progress"
                description: Additional notes about the child's history
    responses:
      201:
        description: Child history created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                child_id:
                  type: integer
                  example: 1
                admission_date:
                  type: string
                  format: date
                  example: "2023-09-01"
                graduation_date:
                  type: string
                  format: date
                  example: "2024-06-30"
                notes:
                  type: string
                  example: "Excellent behavior and learning progress"
      400:
        description: Invalid input data
    """
    content = request.get_json()
    history = ChildHistory.create_from_dto(content)
    child_history_controller.create(history)
    return make_response(jsonify(history.put_into_dto()), HTTPStatus.CREATED)

@child_history_bp.get('/<int:history_id>')
def get_child_history(history_id: int) -> Response:
    """
    Get child history by ID
    ---
    tags:
      - Child History
    summary: Retrieve a specific child history
    description: Get a child history record by its ID
    parameters:
      - in: path
        name: history_id
        required: true
        schema:
          type: integer
        description: ID of the child history record to retrieve
        example: 1
    responses:
      200:
        description: Child history found
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                child_id:
                  type: integer
                  example: 1
                admission_date:
                  type: string
                  format: date
                  example: "2023-09-01"
                graduation_date:
                  type: string
                  format: date
                  example: "2024-06-30"
                notes:
                  type: string
                  example: "Good progress in learning activities"
      404:
        description: Child history not found
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Child history not found"
    """
    history = child_history_controller.find_by_id(history_id)
    if history:
        return make_response(jsonify(history.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Child history not found"}), HTTPStatus.NOT_FOUND)

@child_history_bp.put('/<int:history_id>')
def update_child_history(history_id: int) -> Response:
    """
    Update child history
    ---
    tags:
      - Child History
    summary: Update an existing child history
    description: Update a child history record by ID
    parameters:
      - in: path
        name: history_id
        required: true
        schema:
          type: integer
        description: ID of the child history to update
        example: 1
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - child_id
              - admission_date
            properties:
              child_id:
                type: integer
                example: 1
                description: Updated child ID
              admission_date:
                type: string
                format: date
                example: "2023-09-01"
                description: Updated admission date
              graduation_date:
                type: string
                format: date
                example: "2024-06-30"
                description: Updated graduation date
              notes:
                type: string
                example: "Updated notes about progress"
                description: Updated notes
    responses:
      200:
        description: Child history updated successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Child history updated"
      404:
        description: Child history not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    history = ChildHistory.create_from_dto(content)
    child_history_controller.update(history_id, history)
    return make_response("Child history updated", HTTPStatus.OK)

@child_history_bp.delete('/<int:history_id>')
def delete_child_history(history_id: int) -> Response:
    """
    Delete child history
    ---
    tags:
      - Child History
    summary: Delete a child history
    description: Remove a child history record by ID
    parameters:
      - in: path
        name: history_id
        required: true
        schema:
          type: integer
        description: ID of the child history to delete
        example: 1
    responses:
      204:
        description: Child history deleted successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Child history deleted"
      404:
        description: Child history not found
    """
    child_history_controller.delete(history_id)
    return make_response("Child history deleted", HTTPStatus.NO_CONTENT)
