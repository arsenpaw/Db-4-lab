from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Award(db.Model, IDto):
    __tablename__ = "award"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "title": self.title, "description": self.description}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Award:
        return Award(**dto_dict)