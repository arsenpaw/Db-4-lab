from typing import List, Optional

from sqlalchemy.orm import joinedload

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Employee import Employee

class EmployeeDAO(GeneralDAO):
    _domain_type = Employee

    def find_with_gender(self):
        return (
            self._session.query(Employee)
            .options(
                joinedload(Employee.gender),
            )
            .all()
        )

    def create(self, employee: Employee) -> None:
        self._session.add(employee)
        self._session.commit()

    def find_all(self) -> List[Employee]:
        return self._session.query(Employee).all()

    def find_by_position_id(self, position_id: int) -> List[Employee]:
        return self._session.query(Employee).filter(Employee.position_id == position_id).all()
