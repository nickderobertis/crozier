

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionDataSchemaSchemaType(enum.StrEnum):
    OBJECT = "object"

    def visit(self, object: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionDataSchemaSchemaType.OBJECT:
            return object()
