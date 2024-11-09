"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Orders DB imports for DAOs corresponding to each entity, using HelloWorld naming
from .orders.GenderDao import GenderDAO
from .orders.KidergartenDao import KindergartenDAO
from .orders.GroupDao import GroupDAO
from .orders.PositionDao import PositionDAO
from .orders.AwardDao import AwardDAO
from .orders.ChildDao import ChildDAO
from .orders.EmployeeDao import EmployeeDAO
from .orders.ChildGroupsHistoryDao import ChildGroupsHistoryDAO
from .orders.ChildHistoryDao import ChildHistoryDAO
from .orders.ChildKindergartensDao import ChildKindergartensDAO
from .orders.EmployeeGroupsDao import EmployeeGroupsDAO
from .orders.EmployeeHistoryDAO import EmployeeHistoryDAO

# Initialize DAOs for each entity with HelloWorld naming style
genderDao = GenderDAO()
kindergartenDao = KindergartenDAO()
groupDao = GroupDAO()
positionDao = PositionDAO()
awardDao = AwardDAO()
childDao = ChildDAO()
employeeDao = EmployeeDAO()
childGroupsHistoryDao = ChildGroupsHistoryDAO()
childHistoryDao = ChildHistoryDAO()
childKindergartensDao = ChildKindergartensDAO()
employeeGroupsDao = EmployeeGroupsDAO()
employeeHistoryDao = EmployeeHistoryDAO()
