# KindergartenController.py
from typing import List
from my_project.auth.dao.orders.KidergartenDao import KindergartenDAO
from my_project.auth.domain.orders.Kindergarten import Kindergarten

class KindergartenController:
    _dao = KindergartenDAO()

    def find_all(self) -> List[Kindergarten]:
        return self._dao.find_all()

    def create(self, kindergarten: Kindergarten) -> None:
        self._dao.create(kindergarten)

    def find_by_id(self, kindergarten_id: int) -> Kindergarten:
        return self._dao.find_by_id(kindergarten_id)

    def update(self, kindergarten_id: int, kindergarten: Kindergarten) -> None:
        self._dao.update(kindergarten_id, kindergarten)

    def delete(self, kindergarten_id: int) -> None:
        self._dao.delete(kindergarten_id)

    def find_by_name(self, name: str) -> List[Kindergarten]:
        return self._dao.find_by_name(name)
