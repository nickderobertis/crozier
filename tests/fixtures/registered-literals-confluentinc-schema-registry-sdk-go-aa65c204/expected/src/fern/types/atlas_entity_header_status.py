

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AtlasEntityHeaderStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    PURGED = "PURGED"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        purged: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AtlasEntityHeaderStatus.ACTIVE:
            return active()
        if self is AtlasEntityHeaderStatus.DELETED:
            return deleted()
        if self is AtlasEntityHeaderStatus.PURGED:
            return purged()
