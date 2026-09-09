

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FourHundredThreeDetailsItemIssue(enum.StrEnum):
    PERMISSION_DENIED = "PERMISSION_DENIED"

    def visit(self, permission_denied: typing.Callable[[], T_Result]) -> T_Result:
        if self is FourHundredThreeDetailsItemIssue.PERMISSION_DENIED:
            return permission_denied()
