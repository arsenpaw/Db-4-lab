# EmployeeController.py
from typing import List
from my_project.auth.dao.orders.EmployeeDao import EmployeeDAO
from my_project.auth.domain.orders.Employee import Employee

class EmployeeController:
    _dao = EmployeeDAO()

    def find_all(self) -> List[Employee]:
        return self._dao.find_all()

    def create(self, employee: Employee) -> None:
        self._dao.create(employee)

    def find_by_id(self, employee_id: int) -> Employee:
        return self._dao.find_by_id(employee_id)

    def update(self, employee_id: int, employee: Employee) -> None:
        self._dao.update(employee_id, employee)

    def delete(self, employee_id: int) -> None:
        self._dao.delete(employee_id)

    def find_by_position_id(self, position_id: int) -> List[Employee]:
        return self._dao.find_by_position_id(position_id)
