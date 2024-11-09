from typing import List

from my_project.auth.dao import awardDao, childKindergartensDao
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


class ChildKindergartensService(GeneralService):
    _dao = childKindergartensDao

    def create(self, record: ChildKindergartens) -> None:
        self._dao.create(record)

    def get_all_child_kindergartens(self) -> List[ChildKindergartens]:
        return self._dao.find_all()
