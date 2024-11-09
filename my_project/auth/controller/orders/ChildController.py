# ChildController.py
from typing import List
from my_project.auth.dao.orders.ChildDao import ChildDAO
from my_project.auth.domain.orders.Child import Child

class ChildController:
    _dao = ChildDAO()

    def find_all(self) -> List[Child]:
        return self._dao.find_all()

    def create(self, child: Child) -> None:
        self._dao.create(child)

    def find_by_id(self, child_id: int) -> Child:
        return self._dao.find_by_id(child_id)

    def update(self, child_id: int, child: Child) -> None:
        self._dao.update(child_id, child)

    def delete(self, child_id: int) -> None:
        self._dao.delete(child_id)

    def find_by_last_name(self, last_name: str) -> List[Child]:
        return self._dao.find_by_last_name(last_name)
