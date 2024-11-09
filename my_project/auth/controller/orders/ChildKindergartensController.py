# ChildKindergartensController.py
from typing import List
from my_project.auth.dao.orders.ChildKindergartensDao import ChildKindergartensDAO
from my_project.auth.domain.orders.ChildKindergartens import ChildKindergartens

class ChildKindergartensController:
    _dao = ChildKindergartensDAO()

    def find_all(self) -> List[ChildKindergartens]:
        return self._dao.find_all()

    def create(self, record: ChildKindergartens) -> None:
        self._dao.create(record)

    def find_by_child_id(self, child_id: int) -> List[ChildKindergartens]:
        return self._dao.find_by_child_id(child_id)

    def delete(self, child_id: int, kindergarten_id: int) -> None:
        self._dao.delete(child_id, kindergarten_id)
