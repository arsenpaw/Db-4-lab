from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.EmployeeGroups import EmployeeGroups

class EmployeeGroupsDAO(GeneralDAO):
    _domain_type = EmployeeGroups

    def create(self, record: EmployeeGroups) -> None:
        self._session.add(record)
        self._session.commit()

    def find_all(self) -> List[EmployeeGroups]:
        return self._session.query(EmployeeGroups).all()

    def find_by_group_id(self, group_id: int) -> List[EmployeeGroups]:
        return self._session.query(EmployeeGroups).filter(EmployeeGroups.current_group_id == group_id).all()
