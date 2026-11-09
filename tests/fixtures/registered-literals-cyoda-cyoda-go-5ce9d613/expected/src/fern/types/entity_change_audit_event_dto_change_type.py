

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntityChangeAuditEventDtoChangeType(enum.StrEnum):
    """
    Type of change that occurred
    """

    CREATED = "CREATED"
    UPDATED = "UPDATED"
    DELETED = "DELETED"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        updated: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntityChangeAuditEventDtoChangeType.CREATED:
            return created()
        if self is EntityChangeAuditEventDtoChangeType.UPDATED:
            return updated()
        if self is EntityChangeAuditEventDtoChangeType.DELETED:
            return deleted()
