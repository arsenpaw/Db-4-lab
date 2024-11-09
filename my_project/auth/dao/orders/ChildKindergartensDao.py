from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.ChildKindergartens import ChildKindergartens


class ChildKindergartensDAO(GeneralDAO):
    _domain_type = ChildKindergartens

    def create(self, record: ChildKindergartens) -> None:
        self._session.add(record)
        self._session.commit()

    def find_all(self) -> List[ChildKindergartens]:
        return self._session.query(ChildKindergartens).all()
