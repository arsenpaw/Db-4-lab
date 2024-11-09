from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import child_kindergartens_controller
from my_project.auth.domain.orders.ChildKindergartens import ChildKindergartens

child_kindergartens_bp = Blueprint('childKindergartens', __name__, url_prefix='/child-kindergartens')

@child_kindergartens_bp.get('')
def get_all_child_kindergartens() -> Response:
    records = child_kindergartens_controller.find_all()
    records_dto = [record.put_into_dto() for record in records]
    return make_response(jsonify(records_dto), HTTPStatus.OK)

@child_kindergartens_bp.post('')
def create_child_kindergarten() -> Response:
    content = request.get_json()
    record = ChildKindergartens.create_from_dto(content)
    child_kindergartens_controller.create(record)
    return make_response(jsonify(record.put_into_dto()), HTTPStatus.CREATED)

@child_kindergartens_bp.get('/<int:child_id>')
def get_child_kindergartens_by_child_id(child_id: int) -> Response:
    records = child_kindergartens_controller.find_by_child_id(child_id)
    records_dto = [record.put_into_dto() for record in records]
    return make_response(jsonify(records_dto), HTTPStatus.OK)

@child_kindergartens_bp.delete('/<int:child_id>/<int:kindergarten_id>')
def delete_child_kindergarten(child_id: int, kindergarten_id: int) -> Response:
    child_kindergartens_controller.delete(child_id, kindergarten_id)
    return make_response("Child-kindergarten record deleted", HTTPStatus.NO_CONTENT)
