from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import backref

from my_project import db
from my_project.auth.domain.i_dto import IDto

from sqlalchemy.orm import relationship
from my_project import db

class ChildGroupsHistory(db.Model, IDto):
    __tablename__ = "child_groups_history"
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)

    group = relationship("Group", back_populates="child_groups_history", uselist=False)
    child = relationship("Child", back_populates="child_groups_history", uselist=False)

    def put_into_large_dto(self) -> Dict[str, Any]:
        return {
            "child_groups_history": {
                "child_id": self.child_id,
                "group_id": self.group_id
            },
            "child": {
                "id": self.child.id,
                "first_name": self.child.first_name,
                "last_name": self.child.last_name,
                "birth_date": str(self.child.birth_date),
                "gender_id": self.child.gender_id,
                "current_kindergarten_id": self.child.current_kindergarten_id,
                "history_id": self.child.history_id,
            } if self.child else None,
            "group": {
                "id": self.group.id,
                "name": self.group.name,
                "kindergarten_id": self.group.kindergarten_id,
            } if self.group else None
        }

    def put_into_dto(self) -> Dict[str, Any]:
        return {"child_id": self.child_id, "group_id": self.group_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ChildGroupsHistory:
        return ChildGroupsHistory(**dto_dict)
