from typing import List

from my_project.auth.dao import awardDao, positionDao
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


class PositionService(GeneralService):
    _dao = positionDao

    def create(self, position: Position) -> None:
        self._dao.create(position)

    def get_all_positions(self) -> List[Position]:
        return self._dao.find_all()