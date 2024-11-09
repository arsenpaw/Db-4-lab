from typing import List

from my_project.auth.dao import awardDao, employeeGroupsDao
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

class EmployeeGroupsService(GeneralService):
    _dao = employeeGroupsDao

    def create(self, record: EmployeeGroups) -> None:
        self._dao.create(record)

    def get_all_employee_groups(self) -> List[EmployeeGroups]:
        return self._dao.find_all()

    def get_employee_groups_by_group_id(self, group_id: int) -> List[EmployeeGroups]:
        return self._dao.find_by_group_id(group_id)