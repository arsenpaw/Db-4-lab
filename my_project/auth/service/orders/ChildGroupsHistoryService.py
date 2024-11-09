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

class ChildGroupsHistoryService(GeneralService):
    _dao = childKindergartensDao

    def create(self, history: ChildGroupsHistory) -> None:
        self._dao.create(history)

    def get_all_histories(self) -> List[ChildGroupsHistory]:
        return self._dao.find_all()

    def get_histories_by_child_id(self, child_id: int) -> List[ChildGroupsHistory]:
        return self._dao.find_by_child_id(child_id)
