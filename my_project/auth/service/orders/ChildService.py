from typing import List

from my_project.auth.dao import awardDao, childDao
from my_project.auth.dao.orders import (
    GenderDao, KidergartenDao, GroupDao, PositionDao,
    AwardDao, ChildDao, EmployeeDao, ChildGroupsHistoryDao,
    ChildHistoryDao, ChildKindergartensDao, EmployeeGroupsDao,
    EmployeeHistoryDAO
)
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import (
    Gender, Kindergarten, Group, Position, Award, Child, Employee,
    ChildGroupsHistory, ChildHistory, ChildKindergartens, EmployeeGroups, EmployeeHistory
)


class ChildService(GeneralService):
    _dao = childDao

    def create(self, child: Child) -> None:
        self._dao.create(child)

    def get_all_children(self) -> List[Child]:
        return self._dao.find_all()

    def get_children_by_last_name(self, last_name: str) -> List[Child]:
        return self._dao.find_by_last_name(last_name)
