from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Group(db.Model, IDto):
    __tablename__ = "group"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    kindergarten_id = db.Column(db.Integer, db.ForeignKey('kindergarten.id'), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name, "kindergarten_id": self.kindergarten_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Group:
        return Group(**dto_dict)