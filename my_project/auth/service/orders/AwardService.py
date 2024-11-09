from typing import List

from my_project.auth.dao import awardDao
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

class AwardService(GeneralService):
    _dao = awardDao

    def create(self, award: Award) -> None:
        self._dao.create(award)

    def get_all_awards(self) -> List[Award]:
        return self._dao.find_all()

    def get_award_by_title(self, title: str) -> Award:
        return self._dao.find_by_title(title)
