from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import group_controller
from my_project.auth.domain.orders.Group import Group

group_bp = Blueprint('group', __name__, url_prefix='/group')

@group_bp.get('')
def get_all_groups() -> Response:
    """
    Get all groups
    ---
    tags:
      - Group
    summary: Retrieve all groups
    description: Get a list of all available groups
    responses:
      200:
        description: List of groups
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
                    example: "Sunflower Group"
                  kindergarten_id:
                    type: integer
                    example: 1
                  max_children:
                    type: integer
                    example: 20
    """
    groups = group_controller.find_all()
    groups_dto = [group.put_into_dto() for group in groups]
    return make_response(jsonify(groups_dto), HTTPStatus.OK)

@group_bp.post('')
def create_group() -> Response:
    """
    Create a new group
    ---
    tags:
      - Group
    summary: Create a new group
    description: Create a new group record
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - name
              - kindergarten_id
            properties:
              name:
                type: string
                example: "Rose Group"
                description: Name of the group
              kindergarten_id:
                type: integer
                example: 1
                description: ID of the kindergarten this group belongs to
              max_children:
                type: integer
                example: 15
                description: Maximum number of children in this group
    responses:
      201:
        description: Group created successfully
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
                  example: "Rose Group"
                kindergarten_id:
                  type: integer
                  example: 1
                max_children:
                  type: integer
                  example: 15
      400:
        description: Invalid input data
    """
    content = request.get_json()
    group = Group.create_from_dto(content)
    group_controller.create(group)
    return make_response(jsonify(group.put_into_dto()), HTTPStatus.CREATED)

@group_bp.get('/<int:group_id>')
def get_group(group_id: int) -> Response:
    """
    Get group by ID
    ---
    tags:
      - Group
    summary: Retrieve a specific group
    description: Get a group by its ID
    parameters:
      - in: path
        name: group_id
        required: true
        schema:
          type: integer
        description: ID of the group to retrieve
        example: 1
    responses:
      200:
        description: Group found
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
                  example: "Sunflower Group"
                kindergarten_id:
                  type: integer
                  example: 1
                max_children:
                  type: integer
                  example: 20
      404:
        description: Group not found
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "Group not found"
    """
    group = group_controller.find_by_id(group_id)
    if group:
        return make_response(jsonify(group.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Group not found"}), HTTPStatus.NOT_FOUND)

@group_bp.put('/<int:group_id>')
def update_group(group_id: int) -> Response:
    """
    Update group
    ---
    tags:
      - Group
    summary: Update an existing group
    description: Update a group record by ID
    parameters:
      - in: path
        name: group_id
        required: true
        schema:
          type: integer
        description: ID of the group to update
        example: 1
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - name
              - kindergarten_id
            properties:
              name:
                type: string
                example: "Updated Group Name"
                description: Updated name of the group
              kindergarten_id:
                type: integer
                example: 1
                description: Updated kindergarten ID
              max_children:
                type: integer
                example: 25
                description: Updated maximum number of children
    responses:
      200:
        description: Group updated successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Group updated"
      404:
        description: Group not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    group = Group.create_from_dto(content)
    group_controller.update(group_id, group)
    return make_response("Group updated", HTTPStatus.OK)

@group_bp.delete('/<int:group_id>')
def delete_group(group_id: int) -> Response:
    """
    Delete group
    ---
    tags:
      - Group
    summary: Delete a group
    description: Delete a group record by ID
    parameters:
      - in: path
        name: group_id
        required: true
        schema:
          type: integer
        description: ID of the group to delete
        example: 1
    responses:
      204:
        description: Group deleted successfully
        content:
          text/plain:
            schema:
              type: string
              example: "Group deleted"
      404:
        description: Group not found
    """
    group_controller.delete(group_id)
    return make_response("Group deleted", HTTPStatus.NO_CONTENT)
