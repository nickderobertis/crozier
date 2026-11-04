

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserMessageItemParamRole(enum.StrEnum):
    """
    The message role. Always `user`.
    """

    USER = "user"

    def visit(self, user: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserMessageItemParamRole.USER:
            return user()
