

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1UsersCreateUserUserLevel(enum.StrEnum):
    """
    **(Deprecated)**
                             Specifies the user level
                             Required if **role_id** is blank.
                             Must be **normal** if **role_id** is blank and **admin** is true
                             Must be **limited** if **role_id** is blank and **hide_hourly_rate** is true
                             Must be **limited** if **role_id** is blank and **hide_internal_hourly_rate** is true"
    """

    NORMAL = "normal"
    LIMITED = "limited"

    def visit(self, normal: typing.Callable[[], T_Result], limited: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1UsersCreateUserUserLevel.NORMAL:
            return normal()
        if self is V1UsersCreateUserUserLevel.LIMITED:
            return limited()
