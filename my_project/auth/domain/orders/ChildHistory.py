from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class ChildHistory(db.Model, IDto):
    __tablename__ = "child_history"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admission_date = db.Column(db.Date, nullable=False)
    graduation_date = db.Column(db.Date, nullable=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "admission_date": str(self.admission_date),
            "graduation_date": str(self.graduation_date) if self.graduation_date else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ChildHistory:
        return ChildHistory(**dto_dict)