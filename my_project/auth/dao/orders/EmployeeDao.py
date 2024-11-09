from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders import (Gender, Kindergarten, Group, Position, Award, Child, Employee, ChildGroupsHistory, ChildHistory, ChildKindergartens, EmployeeGroups, EmployeeHistory)

class EmployeeDAO(GeneralDAO):
    _domain_type = Employee

    def create(self, employee: Employee) -> None:
        self._session.add(employee)
        self._session.commit()

    def find_all(self) -> List[Employee]:
        return self._session.query(Employee).all()

    def find_by_position_id(self, position_id: int) -> List[Employee]:
        return self._session.query(Employee).filter(Employee.position_id == position_id).all()
