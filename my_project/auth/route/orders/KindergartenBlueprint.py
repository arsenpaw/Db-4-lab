from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import kindergarten_controller
from my_project.auth.domain.orders.Kindergarten import Kindergarten

kindergarten_bp = Blueprint('kindergarten', __name__, url_prefix='/kindergarten')

@kindergarten_bp.get('')
def get_all_kindergartens() -> Response:
    kindergartens = kindergarten_controller.find_all()
    kindergartens_dto = [kindergarten.put_into_dto() for kindergarten in kindergartens]
    return make_response(jsonify(kindergartens_dto), HTTPStatus.OK)

@kindergarten_bp.post('')
def create_kindergarten() -> Response:
    content = request.get_json()
    kindergarten = Kindergarten.create_from_dto(content)
    kindergarten_controller.create(kindergarten)
    return make_response(jsonify(kindergarten.put_into_dto()), HTTPStatus.CREATED)

@kindergarten_bp.get('/<int:kindergarten_id>')
def get_kindergarten(kindergarten_id: int) -> Response:
    kindergarten = kindergarten_controller.find_by_id(kindergarten_id)
    if kindergarten:
        return make_response(jsonify(kindergarten.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Kindergarten not found"}), HTTPStatus.NOT_FOUND)

@kindergarten_bp.put('/<int:kindergarten_id>')
def update_kindergarten(kindergarten_id: int) -> Response:
    content = request.get_json()
    kindergarten = Kindergarten.create_from_dto(content)
    kindergarten_controller.update(kindergarten_id, kindergarten)
    return make_response("Kindergarten updated", HTTPStatus.OK)

@kindergarten_bp.delete('/<int:kindergarten_id>')
def delete_kindergarten(kindergarten_id: int) -> Response:
    kindergarten_controller.delete(kindergarten_id)
    return make_response("Kindergarten deleted", HTTPStatus.NO_CONTENT)
