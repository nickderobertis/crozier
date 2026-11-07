

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TagEntityStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    PURGED = "PURGED"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        purged: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TagEntityStatus.ACTIVE:
            return active()
        if self is TagEntityStatus.DELETED:
            return deleted()
        if self is TagEntityStatus.PURGED:
            return purged()
