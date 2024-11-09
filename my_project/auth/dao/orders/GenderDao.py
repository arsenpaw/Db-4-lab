from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders import (Gender, Kindergarten, Group, Position, Award, Child, Employee, ChildGroupsHistory, ChildHistory, ChildKindergartens, EmployeeGroups, EmployeeHistory)


class GenderDAO(GeneralDAO):
    _domain_type = Gender

    def create(self, gender: Gender) -> None:
        self._session.add(gender)
        self._session.commit()

    def find_all(self) -> List[Gender]:
        return self._session.query(Gender).all()
