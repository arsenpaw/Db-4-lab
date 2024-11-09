from typing import List

from my_project.auth.dao import awardDao, employeeHistoryDao
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

class EmployeeHistoryService(GeneralService):
    _dao = employeeHistoryDao

    def create(self, history: EmployeeHistory) -> None:
        self._dao.create(history)

    def get_all_employee_histories(self) -> List[EmployeeHistory]:
        return self._dao.find_all()

    def get_employee_histories_by_employee_id(self, employee_id: int) -> List[EmployeeHistory]:
        return self._dao.find_by_employee_id(employee_id)