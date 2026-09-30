

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SessionPatchRequestStatus(enum.StrEnum):
    ACTIVE = "active"
    ARCHIVED = "archived"

    def visit(self, active: typing.Callable[[], T_Result], archived: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionPatchRequestStatus.ACTIVE:
            return active()
        if self is SessionPatchRequestStatus.ARCHIVED:
            return archived()
