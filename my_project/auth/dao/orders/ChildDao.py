from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Child import (Child)


class ChildDAO(GeneralDAO):
    _domain_type = Child

    def create(self, child: Child) -> None:
        self._session.add(child)
        self._session.commit()

    def find_all(self) -> List[Child]:
        return self._session.query(Child).all()

    def find_by_last_name(self, last_name: str) -> List[Child]:
        return self._session.query(Child).filter(Child.last_name == last_name).all()
