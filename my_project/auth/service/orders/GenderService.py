from typing import List

from my_project.auth.dao import awardDao, genderDao
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


class GenderService(GeneralService):
    _dao = genderDao

    def create(self, gender: Gender) -> None:
        self._dao.create(gender)

    def get_all_genders(self) -> List[Gender]:
        return self._dao.find_all()