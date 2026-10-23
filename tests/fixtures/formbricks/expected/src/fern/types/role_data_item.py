

import typing

from .role_data_item_one import RoleDataItemOne
from .role_data_item_three import RoleDataItemThree
from .role_data_item_two import RoleDataItemTwo
from .role_data_item_zero import RoleDataItemZero

RoleDataItem = typing.Union[RoleDataItemZero, RoleDataItemOne, RoleDataItemTwo, RoleDataItemThree]
