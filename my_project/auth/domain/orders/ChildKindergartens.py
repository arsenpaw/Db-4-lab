from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto



class ChildKindergartens(db.Model, IDto):
    __tablename__ = "child_kindergartens"
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'), primary_key=True)
    kindergarten_id = db.Column(db.Integer, db.ForeignKey('kindergarten.id'), primary_key=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "child_id": self.child_id,
            "kindergarten_id": self.kindergarten_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ChildKindergartens:
        return ChildKindergartens(**dto_dict)