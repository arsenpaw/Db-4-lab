from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import child_history_controller
from my_project.auth.domain.orders.ChildHistory import ChildHistory

child_history_bp = Blueprint('childHistory', __name__, url_prefix='/child-history')

@child_history_bp.get('')
def get_all_child_histories() -> Response:
    histories = child_history_controller.find_all()
    histories_dto = [history.put_into_dto() for history in histories]
    return make_response(jsonify(histories_dto), HTTPStatus.OK)

@child_history_bp.post('')
def create_child_history() -> Response:
    content = request.get_json()
    history = ChildHistory.create_from_dto(content)
    child_history_controller.create(history)
    return make_response(jsonify(history.put_into_dto()), HTTPStatus.CREATED)

@child_history_bp.get('/<int:history_id>')
def get_child_history(history_id: int) -> Response:
    history = child_history_controller.find_by_id(history_id)
    if history:
        return make_response(jsonify(history.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Child history not found"}), HTTPStatus.NOT_FOUND)

@child_history_bp.put('/<int:history_id>')
def update_child_history(history_id: int) -> Response:
    content = request.get_json()
    history = ChildHistory.create_from_dto(content)
    child_history_controller.update(history_id, history)
    return make_response("Child history updated", HTTPStatus.OK)

@child_history_bp.delete('/<int:history_id>')
def delete_child_history(history_id: int) -> Response:
    child_history_controller.delete(history_id)
    return make_response("Child history deleted", HTTPStatus.NO_CONTENT)
