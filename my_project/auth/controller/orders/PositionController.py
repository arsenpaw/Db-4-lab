# PositionController.py
from typing import List
from my_project.auth.dao.orders.PositionDao import PositionDAO
from my_project.auth.domain.orders.Position import Position

class PositionController:
    _dao = PositionDAO()

    def find_all(self) -> List[Position]:
        return self._dao.find_all()

    def create(self, position: Position) -> None:
        self._dao.create(position)

    def find_by_id(self, position_id: int) -> Position:
        return self._dao.find_by_id(position_id)

    def update(self, position_id: int, position: Position) -> None:
        self._dao.update(position_id, position)

    def delete(self, position_id: int) -> None:
        self._dao.delete(position_id)
