# EmployeeGroupsController.py
from typing import List
from my_project.auth.dao.orders.EmployeeGroupsDao import EmployeeGroupsDAO
from my_project.auth.domain.orders.EmployeeGroups import EmployeeGroups

class EmployeeGroupsController:
    _dao = EmployeeGroupsDAO()

    def find_all(self) -> List[EmployeeGroups]:
        """
        Retrieves all employee-group associations.
        :return: List of EmployeeGroups records
        """
        return self._dao.find_all()

    def create(self, association: EmployeeGroups) -> None:
        """
        Creates a new association between an employee and a group.
        :param association: EmployeeGroups record to create
        """
        self._dao.create(association)

    def find_by_group_id(self, group_id: int) -> List[EmployeeGroups]:
        """
        Retrieves all employees associated with a specific group.
        :param group_id: ID of the group
        :return: List of EmployeeGroups records
        """
        return self._dao.find_by_group_id(group_id)

    def find_by_employee_id(self, employee_id: int) -> List[EmployeeGroups]:
        """
        Retrieves all groups that a specific employee is associated with.
        :param employee_id: ID of the employee
        :return: List of EmployeeGroups records
        """
        return self._dao.find_by_employee_id(employee_id)

    def delete(self, group_id: int, employee_id: int) -> None:
        """
        Deletes a specific employee-group association.
        :param group_id: ID of the group
        :param employee_id: ID of the employee
        """
        self._dao.delete(group_id, employee_id)
