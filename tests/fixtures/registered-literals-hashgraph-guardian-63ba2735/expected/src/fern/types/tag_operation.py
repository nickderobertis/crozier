

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TagOperation(enum.StrEnum):
    CREATE = "Create"
    DELETE = "Delete"

    def visit(self, create: typing.Callable[[], T_Result], delete: typing.Callable[[], T_Result]) -> T_Result:
        if self is TagOperation.CREATE:
            return create()
        if self is TagOperation.DELETE:
            return delete()
