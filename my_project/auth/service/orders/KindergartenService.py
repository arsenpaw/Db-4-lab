from typing import List

from my_project.auth.dao import awardDao, kindergartenDao
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


class KindergartenService(GeneralService):
    _dao = kindergartenDao

    def create(self, kindergarten: Kindergarten) -> None:
        self._dao.create(kindergarten)

    def get_all_kindergartens(self) -> List[Kindergarten]:
        return self._dao.find_all()
