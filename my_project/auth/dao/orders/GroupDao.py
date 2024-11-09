from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Group import Group


class GroupDAO(GeneralDAO):
    _domain_type = Group

    def create(self, group: Group) -> None:
        self._session.add(group)
        self._session.commit()

    def find_all(self) -> List[Group]:
        return self._session.query(Group).all()

    def find_by_kindergarten_id(self, kindergarten_id: int) -> List[Group]:
        return self._session.query(Group).filter(Group.kindergarten_id == kindergarten_id).all()

