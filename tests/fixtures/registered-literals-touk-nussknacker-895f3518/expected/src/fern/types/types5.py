

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Types5(enum.StrEnum):
    TYPED_TAGGED_VALUE = "TypedTaggedValue"

    def visit(self, typed_tagged_value: typing.Callable[[], T_Result]) -> T_Result:
        if self is Types5.TYPED_TAGGED_VALUE:
            return typed_tagged_value()
