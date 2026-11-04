

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DenyResponseDataStatus(enum.StrEnum):
    DENIED = "denied"

    def visit(self, denied: typing.Callable[[], T_Result]) -> T_Result:
        if self is DenyResponseDataStatus.DENIED:
            return denied()
