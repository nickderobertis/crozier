

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QuadratsKind(enum.StrEnum):
    QUADRATS = "Quadrats"

    def visit(self, quadrats: typing.Callable[[], T_Result]) -> T_Result:
        if self is QuadratsKind.QUADRATS:
            return quadrats()
