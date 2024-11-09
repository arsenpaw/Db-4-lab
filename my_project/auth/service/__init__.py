"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import services using HelloWorld naming convention
from .orders.GenderService import GenderService
from .orders.KindergartenService import KindergartenService
from .orders.GroupService import GroupService
from .orders.PositionService import PositionService
from .orders.AwardService import AwardService
from .orders.ChildService import ChildService
from .orders.EmployeeService import EmployeeService
from .orders.ChildGroupsHistoryService import ChildGroupsHistoryService
from .orders.ChildHistoryService import ChildHistoryService
from .orders.ChildKindergartensService import ChildKindergartensService
from .orders.EmployeeGroupsService import EmployeeGroupsService
from .orders.EmployeeHistoryService import EmployeeHistoryService

# Initialize service instances with HelloWorld naming style
genderService = GenderService()
kindergartenService = KindergartenService()
groupService = GroupService()
positionService = PositionService()
awardService = AwardService()
childService = ChildService()
employeeService = EmployeeService()
childGroupsHistoryService = ChildGroupsHistoryService()
childHistoryService = ChildHistoryService()
childKindergartensService = ChildKindergartensService()
employeeGroupsService = EmployeeGroupsService()
employeeHistoryService = EmployeeHistoryService()
