# EmployeeHistoryController.py
from typing import List
from my_project.auth.dao.orders.EmployeeHistoryDAO import EmployeeHistoryDAO
from my_project.auth.domain.orders.EmployeeHistory import EmployeeHistory

class EmployeeHistoryController:
    _dao = EmployeeHistoryDAO()

    def find_all(self) -> List[EmployeeHistory]:
        return self._dao.find_all()

    def create(self, history: EmployeeHistory) -> None:
        self._dao.create(history)

    def find_by_id(self, history_id: int) -> EmployeeHistory:
        return self._dao.find_by_id(history_id)

    def find_by_employee_id(self, employee_id: int) -> List[EmployeeHistory]:
        return self._dao.find_by_employee_id(employee_id)

    def delete(self, history_id: int) -> None:
        self._dao.delete(history_id)
