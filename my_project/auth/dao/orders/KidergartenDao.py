from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders import (Gender, Kindergarten, Group, Position, Award, Child, Employee, ChildGroupsHistory, ChildHistory, ChildKindergartens, EmployeeGroups, EmployeeHistory)


class KindergartenDAO(GeneralDAO):
    _domain_type = Kindergarten

    def create(self, kindergarten: Kindergarten) -> None:
        self._session.add(kindergarten)
        self._session.commit()

    def find_all(self) -> List[Kindergarten]:
        return self._session.query(Kindergarten).all()
