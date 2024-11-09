from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto



class EmployeeAwards(db.Model, IDto):
    __tablename__ = "employee_awards"
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), primary_key=True)
    award_id = db.Column(db.Integer, db.ForeignKey('award.id'), primary_key=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"employee_id": self.employee_id, "award_id": self.award_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EmployeeAwards:
        return EmployeeAwards(**dto_dict)