

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObjectChangeActionLabel(enum.StrEnum):
    CREATED = "Created"
    UPDATED = "Updated"
    DELETED = "Deleted"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        updated: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObjectChangeActionLabel.CREATED:
            return created()
        if self is ObjectChangeActionLabel.UPDATED:
            return updated()
        if self is ObjectChangeActionLabel.DELETED:
            return deleted()
