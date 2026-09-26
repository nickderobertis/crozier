

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoDataframeSearchInputDefSchema0Operator(enum.StrEnum):
    AND = "and"
    OR = "or"

    def visit(self, and_: typing.Callable[[], T_Result], or_: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoDataframeSearchInputDefSchema0Operator.AND:
            return and_()
        if self is MarimoDataframeSearchInputDefSchema0Operator.OR:
            return or_()
