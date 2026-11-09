

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InclusionProofProofItemDirection(enum.StrEnum):
    LEFT = "left"
    RIGHT = "right"

    def visit(self, left: typing.Callable[[], T_Result], right: typing.Callable[[], T_Result]) -> T_Result:
        if self is InclusionProofProofItemDirection.LEFT:
            return left()
        if self is InclusionProofProofItemDirection.RIGHT:
            return right()
