

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class LogoutRequestLoginIdOne(enum.StrEnum):
    """
    Log out of all logins
    """

    ALL = "all"

    def visit(self, all_: typing.Callable[[], T_Result]) -> T_Result:
        if self is LogoutRequestLoginIdOne.ALL:
            return all_()
