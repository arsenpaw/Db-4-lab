from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class EmployeeGroups(db.Model, IDto):
    __tablename__ = "employee_groups"
    current_group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    current_employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), primary_key=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "current_group_id": self.current_group_id,
            "current_employee_id": self.current_employee_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EmployeeGroups:
        return EmployeeGroups(**dto_dict)