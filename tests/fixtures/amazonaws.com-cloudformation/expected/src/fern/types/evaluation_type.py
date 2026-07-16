

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EvaluationType(enum.StrEnum):
    STATIC = "Static"
    DYNAMIC = "Dynamic"

    def visit(self, static: typing.Callable[[], T_Result], dynamic: typing.Callable[[], T_Result]) -> T_Result:
        if self is EvaluationType.STATIC:
            return static()
        if self is EvaluationType.DYNAMIC:
            return dynamic()
