

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TagResponseEntityStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    PURGED = "PURGED"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        purged: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TagResponseEntityStatus.ACTIVE:
            return active()
        if self is TagResponseEntityStatus.DELETED:
            return deleted()
        if self is TagResponseEntityStatus.PURGED:
            return purged()
