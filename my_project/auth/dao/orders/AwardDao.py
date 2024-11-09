from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Award import Award  # Ensure this is the correct path

class AwardDAO(GeneralDAO):
    _domain_type = Award

    def create(self, award: Award) -> None:
        self._session.add(award)
        self._session.commit()

    def find_all(self) -> List[Award]:
        return self._session.query(Award).all()

    def find_by_title(self, title: str) -> Optional[Award]:
        return self._session.query(Award).filter(Award.title == title).first()
