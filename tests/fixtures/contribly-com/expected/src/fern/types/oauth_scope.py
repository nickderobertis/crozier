

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    FULL = "full"
    """
    Full access
    """

    def visit(self, full: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.FULL:
            return full()
