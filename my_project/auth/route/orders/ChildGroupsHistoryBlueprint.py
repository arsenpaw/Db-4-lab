from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import child_groups_history_controller
from my_project.auth.domain.orders.ChildGroupsHistory import ChildGroupsHistory

child_groups_history_bp = Blueprint('childGroupsHistory', __name__, url_prefix='/child-groups-history')


@child_groups_history_bp.get('all')
def get_all_child_groups_histories_and_all() -> Response:
    """
    Get all child groups histories with related data
    ---
    tags:
      - Child Groups History
    summary: Retrieve all child groups histories with detailed information
    description: Get a list of all child groups histories including related child and group data
    responses:
      200:
        description: List of child groups histories with related data
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
                  group_id:
                    type: integer
                    example: 1
                  start_date:
                    type: string
                    format: date
                    example: "2023-09-01"
                  end_date:
                    type: string
                    format: date
                    example: "2024-06-30"
                  child:
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
                  group:
                    type: object
                    properties:
                      id:
                        type: integer
                        example: 1
                      name:
                        type: string
                        example: "Sunflower Group"
    """
    histories = child_groups_history_controller.find_all_with_related_data()
    histories_dto = [history.put_into_large_dto() for history in histories]
    return make_response(jsonify(histories_dto), HTTPStatus.OK)


@child_groups_history_bp.get('')
def get_all_child_groups_histories() -> Response:
    """
    Get all child groups histories
    ---
    tags:
      - Child Groups History
    summary: Retrieve all child groups histories
    description: Get a list of all child groups histories with basic information
    responses:
      200:
        description: List of child groups histories
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
                  group_id:
                    type: integer
                    example: 1
                  start_date:
                    type: string
                    format: date
                    example: "2023-09-01"
                  end_date:
                    type: string
                    format: date
                    example: "2024-06-30"
    """
    histories = child_groups_history_controller.find_all()
    histories_dto = [history.put_into_dto() for history in histories]
    return make_response(jsonify(histories_dto), HTTPStatus.OK)

@child_groups_history_bp.post('')
def create_child_groups_history() -> Response:
    """
    Create a new child groups history record
    ---
    tags:
      - Child Groups History
    summary: Create a new child groups history
    description: Record a child's assignment to a group with start and end dates
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - child_id
              - group_id
              - start_date
            properties:
              child_id:
                type: integer
                example: 1
                description: ID of the child
              group_id:
                type: integer
                example: 1
                description: ID of the group
              start_date:
                type: string
                format: date
                example: "2023-09-01"
                description: Start date of the child's assignment to the group
              end_date:
                type: string
                format: date
                example: "2024-06-30"
                description: End date of the child's assignment to the group (optional)
    responses:
      201:
        description: Child groups history created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                child_id:
                  type: integer
                  example: 1
                group_id:
                  type: integer
                  example: 1
                start_date:
                  type: string
                  format: date
                  example: "2023-09-01"
                end_date:
                  type: string
                  format: date
                  example: "2024-06-30"
      400:
        description: Invalid input data
    """
    content = request.get_json()
    history = ChildGroupsHistory.create_from_dto(content)
    child_groups_history_controller.create(history)
    return make_response(jsonify(history.put_into_dto()), HTTPStatus.CREATED)

@child_groups_history_bp.get('/<int:child_id>')
def get_child_groups_history(child_id: int) -> Response:
    """
    Get child groups history by child ID
    ---
    tags:
      - Child Groups History
    summary: Retrieve groups history for a specific child
    description: Get all group assignments for a specific child
    parameters:
      - in: path
        name: child_id
        required: true
        schema:
          type: integer
        description: ID of the child to retrieve groups history for
        example: 1
    responses:
      200:
        description: Child groups history found
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
                  group_id:
                    type: integer
                    example: 1
                  start_date:
                    type: string
                    format: date
                    example: "2023-09-01"
                  end_date:
                    type: string
                    format: date
                    example: "2024-06-30"
      404:
        description: No history found for this child
    """
    histories = child_groups_history_controller.find_by_child_id(child_id)
    histories_dto = [history.put_into_dto() for history in histories]
    return make_response(jsonify(histories_dto), HTTPStatus.OK)

@child_groups_history_bp.delete('/<int:child_id>/<int:group_id>')
def delete_child_groups_history(child_id: int, group_id: int) -> Response:
    """
    Delete child groups history
    ---
    tags:
      - Child Groups History
    summary: Delete a child groups history record
    description: Remove a specific child's assignment to a group
    parameters:
      - in: path
        name: child_id
        required: true
        schema:
          type: integer
        description: ID of the child
        example: 1
      - in: path
        name: group_id
        required: true
        schema:
          type: integer
        description: ID of the group
        example: 1
    responses:
      204:
        description: Child groups history deleted successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Child group history deleted"
      404:
        description: Child groups history not found
    """
    child_groups_history_controller.delete(child_id, group_id)
    return make_response("Child group history deleted", HTTPStatus.NO_CONTENT)
