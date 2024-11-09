from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import child_controller
from my_project.auth.domain.orders.Child import Child

child_bp = Blueprint('child', __name__, url_prefix='/child')

@child_bp.get('')
def get_all_children() -> Response:
    children = child_controller.find_all()
    children_dto = [child.put_into_dto() for child in children]
    return make_response(jsonify(children_dto), HTTPStatus.OK)

@child_bp.post('')
def create_child() -> Response:
    content = request.get_json()
    child = Child.create_from_dto(content)
    child_controller.create(child)
    return make_response(jsonify(child.put_into_dto()), HTTPStatus.CREATED)

@child_bp.get('/<int:child_id>')
def get_child(child_id: int) -> Response:
    child = child_controller.find_by_id(child_id)
    if child:
        return make_response(jsonify(child.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Child not found"}), HTTPStatus.NOT_FOUND)

@child_bp.put('/<int:child_id>')
def update_child(child_id: int) -> Response:
    content = request.get_json()
    child = Child.create_from_dto(content)
    child_controller.update(child_id, child)
    return make_response("Child updated", HTTPStatus.OK)

@child_bp.delete('/<int:child_id>')
def delete_child(child_id: int) -> Response:
    child_controller.delete(child_id)
    return make_response("Child deleted", HTTPStatus.NO_CONTENT)
