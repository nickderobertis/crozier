

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Types4(enum.StrEnum):
    TYPED_OBJECT_WITH_VALUE = "TypedObjectWithValue"

    def visit(self, typed_object_with_value: typing.Callable[[], T_Result]) -> T_Result:
        if self is Types4.TYPED_OBJECT_WITH_VALUE:
            return typed_object_with_value()
