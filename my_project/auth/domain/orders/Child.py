from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Child(db.Model, IDto):
    __tablename__ = "child"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id', name="fk_child_gender_id"), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    current_kindergarten_id = db.Column(db.Integer, db.ForeignKey('kindergarten.id', name="fk_child_kindergarten_id"))
    current_group_id = db.Column(db.Integer, db.ForeignKey('group.id', name="fk_child_group_id"))
    history_id = db.Column(db.Integer, nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender_id": self.gender_id,
            "birth_date": str(self.birth_date),
            "current_kindergarten_id": self.current_kindergarten_id,
            "current_group_id": self.current_group_id,
            "history_id": self.history_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Child:
        return Child(**dto_dict)
