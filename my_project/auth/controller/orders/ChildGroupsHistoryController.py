# ChildGroupsHistoryController.py
from typing import List
from my_project.auth.dao.orders.ChildGroupsHistoryDao import ChildGroupsHistoryDAO
from my_project.auth.domain.orders.ChildGroupsHistory import ChildGroupsHistory

class ChildGroupsHistoryController:
    _dao = ChildGroupsHistoryDAO()

    def find_all(self) -> List[ChildGroupsHistory]:
        return self._dao.find_all()

    def create(self, history: ChildGroupsHistory) -> None:
        self._dao.create(history)

    def find_by_child_id(self, child_id: int) -> List[ChildGroupsHistory]:
        return self._dao.find_by_child_id(child_id)

    def delete(self, child_id: int, group_id: int) -> None:
        self._dao.delete(child_id, group_id)
