from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.EmployeeHistory import EmployeeHistory


class EmployeeHistoryDAO(GeneralDAO):
    _domain_type = EmployeeHistory

    def create(self, history: EmployeeHistory) -> None:
        self._session.add(history)
        self._session.commit()

    def find_all(self) -> List[EmployeeHistory]:
        return self._session.query(EmployeeHistory).all()

    def find_by_employee_id(self, employee_id: int) -> List[EmployeeHistory]:
        return self._session.query(EmployeeHistory).filter(EmployeeHistory.employee_id == employee_id).all()