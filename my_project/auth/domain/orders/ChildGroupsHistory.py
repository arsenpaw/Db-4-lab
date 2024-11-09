from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto



class ChildGroupsHistory(db.Model, IDto):
    __tablename__ = "child_groups_history"
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"child_id": self.child_id, "group_id": self.group_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ChildGroupsHistory:
        return ChildGroupsHistory(**dto_dict)