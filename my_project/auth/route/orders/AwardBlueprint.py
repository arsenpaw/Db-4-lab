from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import award_controller
from my_project.auth.domain.orders.Award import Award

award_bp = Blueprint('award', __name__, url_prefix='/award')

@award_bp.get('')
def get_all_awards() -> Response:
    awards = award_controller.find_all()
    awards_dto = [award.put_into_dto() for award in awards]
    return make_response(jsonify(awards_dto), HTTPStatus.OK)

@award_bp.post('')
def create_award() -> Response:
    content = request.get_json()
    award = Award.create_from_dto(content)
    award_controller.create(award)
    return make_response(jsonify(award.put_into_dto()), HTTPStatus.CREATED)

@award_bp.get('/<int:award_id>')
def get_award(award_id: int) -> Response:
    award = award_controller.find_by_id(award_id)
    if award:
        return make_response(jsonify(award.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Award not found"}), HTTPStatus.NOT_FOUND)

@award_bp.put('/<int:award_id>')
def update_award(award_id: int) -> Response:
    content = request.get_json()
    award = Award.create_from_dto(content)
    award_controller.update(award_id, award)
    return make_response("Award updated", HTTPStatus.OK)

@award_bp.delete('/<int:award_id>')
def delete_award(award_id: int) -> Response:
    award_controller.delete(award_id)
    return make_response("Award deleted", HTTPStatus.NO_CONTENT)
