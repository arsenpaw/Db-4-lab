from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto



class EmployeeHistory(db.Model, IDto):
    __tablename__ = "employee_history"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    termination_date = db.Column(db.Date, nullable=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "hire_date": str(self.hire_date),
            "termination_date": str(self.termination_date) if self.termination_date else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EmployeeHistory:
        return EmployeeHistory(**dto_dict)