from typing import List

from my_project.auth.dao import awardDao, employeeDao
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


class EmployeeService(GeneralService):
    _dao = employeeDao

    def create(self, employee: Employee) -> None:
        self._dao.create(employee)

    def get_all_employees(self) -> List[Employee]:
        return self._dao.find_all()

    def get_employees_by_position_id(self, position_id: int) -> List[Employee]:
        return self._dao.find_by_position_id(position_id)