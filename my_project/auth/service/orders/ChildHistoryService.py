from typing import List

from my_project.auth.dao import awardDao, childHistoryDao
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


class ChildHistoryService(GeneralService):
    _dao = childHistoryDao

    def create(self, history: ChildHistory) -> None:
        self._dao.create(history)

    def get_all_child_histories(self) -> List[ChildHistory]:
        return self._dao.find_all()

    def get_child_histories_by_admission_date(self, admission_date: str) -> List[ChildHistory]:
        return self._dao.find_by_admission_date(admission_date)