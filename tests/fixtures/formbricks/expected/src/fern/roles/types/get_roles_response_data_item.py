

import typing

from .get_roles_response_data_item_one import GetRolesResponseDataItemOne
from .get_roles_response_data_item_three import GetRolesResponseDataItemThree
from .get_roles_response_data_item_two import GetRolesResponseDataItemTwo
from .get_roles_response_data_item_zero import GetRolesResponseDataItemZero

GetRolesResponseDataItem = typing.Union[
    GetRolesResponseDataItemZero,
    GetRolesResponseDataItemOne,
    GetRolesResponseDataItemTwo,
    GetRolesResponseDataItemThree,
]
