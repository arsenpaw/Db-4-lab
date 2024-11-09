# AwardController.py
from typing import List
from my_project.auth.dao.orders.AwardDao import AwardDAO
from my_project.auth.domain.orders.Award import Award

class AwardController:
    _dao = AwardDAO()

    def find_all(self) -> List[Award]:
        return self._dao.find_all()

    def create(self, award: Award) -> None:
        self._dao.create(award)

    def find_by_id(self, award_id: int) -> Award:
        return self._dao.find_by_id(award_id)

    def update(self, award_id: int, award: Award) -> None:
        self._dao.update(award_id, award)

    def delete(self, award_id: int) -> None:
        self._dao.delete(award_id)

    def find_by_title(self, title: str) -> List[Award]:
        return self._dao.find_by_title(title)
