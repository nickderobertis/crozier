

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TombstoneResourceType(enum.StrEnum):
    """
    The kind of resource that was deleted.
    """

    RO_CRATE = "RO-Crate"
    ENTITY = "entity"
    FILE = "file"

    def visit(
        self,
        ro_crate: typing.Callable[[], T_Result],
        entity: typing.Callable[[], T_Result],
        file: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TombstoneResourceType.RO_CRATE:
            return ro_crate()
        if self is TombstoneResourceType.ENTITY:
            return entity()
        if self is TombstoneResourceType.FILE:
            return file()
