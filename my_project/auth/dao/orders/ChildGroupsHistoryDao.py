from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders import (Gender, Kindergarten, Group, Position, Award, Child, Employee, ChildGroupsHistory, ChildHistory, ChildKindergartens, EmployeeGroups, EmployeeHistory)


class ChildGroupsHistoryDAO(GeneralDAO):
    _domain_type = ChildGroupsHistory

    def create(self, history: ChildGroupsHistory) -> None:
        self._session.add(history)
        self._session.commit()

    def find_all(self) -> List[ChildGroupsHistory]:
        return self._session.query(ChildGroupsHistory).all()

    def find_by_child_id(self, child_id: int) -> List[ChildGroupsHistory]:
        return self._session.query(ChildGroupsHistory).filter(ChildGroupsHistory.child_id == child_id).all()
