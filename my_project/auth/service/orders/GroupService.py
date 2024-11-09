from typing import List

from my_project.auth.dao import awardDao, groupDao
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

class GroupService(GeneralService):
    _dao = groupDao

    def create(self, group: Group) -> None:
        self._dao.create(group)

    def get_all_groups(self) -> List[Group]:
        return self._dao.find_all()

    def get_groups_by_kindergarten_id(self, kindergarten_id: int) -> List[Group]:
        return self._dao.find_by_kindergarten_id(kindergarten_id)
