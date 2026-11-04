

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Types1(enum.StrEnum):
    TYPED_CLASS = "TypedClass"

    def visit(self, typed_class: typing.Callable[[], T_Result]) -> T_Result:
        if self is Types1.TYPED_CLASS:
            return typed_class()
