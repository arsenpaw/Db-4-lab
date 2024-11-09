# GroupController.py
from typing import List
from my_project.auth.dao.orders.GroupDao import GroupDAO
from my_project.auth.domain.orders.Group import Group

class GroupController:
    _dao = GroupDAO()

    def find_all(self) -> List[Group]:
        return self._dao.find_all()

    def create(self, group: Group) -> None:
        self._dao.create(group)

    def find_by_id(self, group_id: int) -> Group:
        return self._dao.find_by_id(group_id)

    def update(self, group_id: int, group: Group) -> None:
        self._dao.update(group_id, group)

    def delete(self, group_id: int) -> None:
        self._dao.delete(group_id)
