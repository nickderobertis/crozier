

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObjectChangeActionValue(enum.StrEnum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"

    def visit(
        self,
        create: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObjectChangeActionValue.CREATE:
            return create()
        if self is ObjectChangeActionValue.UPDATE:
            return update()
        if self is ObjectChangeActionValue.DELETE:
            return delete()
