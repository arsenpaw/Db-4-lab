from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import child_groups_history_controller
from my_project.auth.domain.orders.ChildGroupsHistory import ChildGroupsHistory

child_groups_history_bp = Blueprint('childGroupsHistory', __name__, url_prefix='/child-groups-history')


@child_groups_history_bp.get('all')
def get_all_child_groups_histories_and_all() -> Response:
    histories = child_groups_history_controller.find_all_with_related_data()
    histories_dto = [history.put_into_large_dto() for history in histories]
    return make_response(jsonify(histories_dto), HTTPStatus.OK)


@child_groups_history_bp.get('')
def get_all_child_groups_histories() -> Response:
    histories = child_groups_history_controller.find_all()
    histories_dto = [history.put_into_dto() for history in histories]
    return make_response(jsonify(histories_dto), HTTPStatus.OK)

@child_groups_history_bp.post('')
def create_child_groups_history() -> Response:
    content = request.get_json()
    history = ChildGroupsHistory.create_from_dto(content)
    child_groups_history_controller.create(history)
    return make_response(jsonify(history.put_into_dto()), HTTPStatus.CREATED)

@child_groups_history_bp.get('/<int:child_id>')
def get_child_groups_history(child_id: int) -> Response:
    histories = child_groups_history_controller.find_by_child_id(child_id)
    histories_dto = [history.put_into_dto() for history in histories]
    return make_response(jsonify(histories_dto), HTTPStatus.OK)

@child_groups_history_bp.delete('/<int:child_id>/<int:group_id>')
def delete_child_groups_history(child_id: int, group_id: int) -> Response:
    child_groups_history_controller.delete(child_id, group_id)
    return make_response("Child group history deleted", HTTPStatus.NO_CONTENT)
