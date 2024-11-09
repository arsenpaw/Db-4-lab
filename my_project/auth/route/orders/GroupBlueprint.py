from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import group_controller
from my_project.auth.domain.orders.Group import Group

group_bp = Blueprint('group', __name__, url_prefix='/group')

@group_bp.get('')
def get_all_groups() -> Response:
    groups = group_controller.find_all()
    groups_dto = [group.put_into_dto() for group in groups]
    return make_response(jsonify(groups_dto), HTTPStatus.OK)

@group_bp.post('')
def create_group() -> Response:
    content = request.get_json()
    group = Group.create_from_dto(content)
    group_controller.create(group)
    return make_response(jsonify(group.put_into_dto()), HTTPStatus.CREATED)

@group_bp.get('/<int:group_id>')
def get_group(group_id: int) -> Response:
    group = group_controller.find_by_id(group_id)
    if group:
        return make_response(jsonify(group.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Group not found"}), HTTPStatus.NOT_FOUND)

@group_bp.put('/<int:group_id>')
def update_group(group_id: int) -> Response:
    content = request.get_json()
    group = Group.create_from_dto(content)
    group_controller.update(group_id, group)
    return make_response("Group updated", HTTPStatus.OK)

@group_bp.delete('/<int:group_id>')
def delete_group(group_id: int) -> Response:
    group_controller.delete(group_id)
    return make_response("Group deleted", HTTPStatus.NO_CONTENT)
