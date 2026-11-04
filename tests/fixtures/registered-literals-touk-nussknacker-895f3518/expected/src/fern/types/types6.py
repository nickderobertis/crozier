

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Types6(enum.StrEnum):
    TYPED_NULL = "TypedNull"

    def visit(self, typed_null: typing.Callable[[], T_Result]) -> T_Result:
        if self is Types6.TYPED_NULL:
            return typed_null()
