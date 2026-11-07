

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Types7(enum.StrEnum):
    TYPED_UNION = "TypedUnion"

    def visit(self, typed_union: typing.Callable[[], T_Result]) -> T_Result:
        if self is Types7.TYPED_UNION:
            return typed_union()
