

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AtlasClassificationEntityStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    PURGED = "PURGED"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        purged: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AtlasClassificationEntityStatus.ACTIVE:
            return active()
        if self is AtlasClassificationEntityStatus.DELETED:
            return deleted()
        if self is AtlasClassificationEntityStatus.PURGED:
            return purged()
