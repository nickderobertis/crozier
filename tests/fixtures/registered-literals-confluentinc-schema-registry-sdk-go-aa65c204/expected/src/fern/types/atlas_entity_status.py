

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AtlasEntityStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    PURGED = "PURGED"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        purged: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AtlasEntityStatus.ACTIVE:
            return active()
        if self is AtlasEntityStatus.DELETED:
            return deleted()
        if self is AtlasEntityStatus.PURGED:
            return purged()
