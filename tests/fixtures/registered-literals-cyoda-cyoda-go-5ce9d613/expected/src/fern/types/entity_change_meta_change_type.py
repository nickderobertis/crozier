

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntityChangeMetaChangeType(enum.StrEnum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"

    def visit(
        self,
        create: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntityChangeMetaChangeType.CREATE:
            return create()
        if self is EntityChangeMetaChangeType.UPDATE:
            return update()
        if self is EntityChangeMetaChangeType.DELETE:
            return delete()
