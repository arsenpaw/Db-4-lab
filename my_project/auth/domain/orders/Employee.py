from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Employee(db.Model, IDto):
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id', name="fk_employee_gender_id"), nullable=False)
    kindergarten_id = db.Column(db.Integer, db.ForeignKey('kindergarten.id', name="fk_employee_kindergarten_id"),
                                nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id', name="fk_employee_position_id"), nullable=False)

    gender = db.relationship('Gender', back_populates="employee")

    def put_into_large_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender.put_into_dto() if self.gender else None,  # Full Gender object as nested DTO
            "kindergarten_id": self.kindergarten_id,
            "position_id": self.position_id
        }

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender_id": self.gender_id,
            "kindergarten_id": self.kindergarten_id,
            "position_id": self.position_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Employee:
        return Employee(**dto_dict)
