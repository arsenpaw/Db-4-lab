# ChildHistoryController.py
from typing import List
from my_project.auth.dao.orders.ChildHistoryDao import ChildHistoryDAO
from my_project.auth.domain.orders.ChildHistory import ChildHistory

class ChildHistoryController:
    _dao = ChildHistoryDAO()

    def find_all(self) -> List[ChildHistory]:
        return self._dao.find_all()

    def create(self, history: ChildHistory) -> None:
        self._dao.create(history)

    def find_by_id(self, history_id: int) -> ChildHistory:
        return self._dao.find_by_id(history_id)

    def delete(self, history_id: int) -> None:
        self._dao.delete(history_id)
