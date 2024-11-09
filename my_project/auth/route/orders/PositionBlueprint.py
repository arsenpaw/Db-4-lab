from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import position_controller
from my_project.auth.domain.orders.Position import Position

position_bp = Blueprint('position', __name__, url_prefix='/position')

@position_bp.get('')
def get_all_positions() -> Response:
    positions = position_controller.find_all()
    positions_dto = [position.put_into_dto() for position in positions]
    return make_response(jsonify(positions_dto), HTTPStatus.OK)

@position_bp.post('')
def create_position() -> Response:
    content = request.get_json()
    position = Position.create_from_dto(content)
    position_controller.create(position)
    return make_response(jsonify(position.put_into_dto()), HTTPStatus.CREATED)

@position_bp.get('/<int:position_id>')
def get_position(position_id: int) -> Response:
    position = position_controller.find_by_id(position_id)
    if position:
        return make_response(jsonify(position.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Position not found"}), HTTPStatus.NOT_FOUND)

@position_bp.put('/<int:position_id>')
def update_position(position_id: int) -> Response:
    content = request.get_json()
    position = Position.create_from_dto(content)
    position_controller.update(position_id, position)
    return make_response("Position updated", HTTPStatus.OK)

@position_bp.delete('/<int:position_id>')
def delete_position(position_id: int) -> Response:
    position_controller.delete(position_id)
    return make_response("Position deleted", HTTPStatus.NO_CONTENT)
