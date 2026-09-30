

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionDetailResponseStatus(enum.StrEnum):
    ACTIVE = "active"
    ARCHIVED = "archived"

    def visit(self, active: typing.Callable[[], T_Result], archived: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionDetailResponseStatus.ACTIVE:
            return active()
        if self is SessionDetailResponseStatus.ARCHIVED:
            return archived()
