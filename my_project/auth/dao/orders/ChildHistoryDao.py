from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.ChildHistory import  ChildHistory


class ChildHistoryDAO(GeneralDAO):
    _domain_type = ChildHistory

    def create(self, history: ChildHistory) -> None:
        self._session.add(history)
        self._session.commit()

    def find_all(self) -> List[ChildHistory]:
        return self._session.query(ChildHistory).all()

    def find_by_admission_date(self, admission_date: str) -> List[ChildHistory]:
        return self._session.query(ChildHistory).filter(ChildHistory.admission_date == admission_date).all()
