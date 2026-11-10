

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScoreZeroDataType(enum.StrEnum):
    NUMERIC = "NUMERIC"

    def visit(self, numeric: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScoreZeroDataType.NUMERIC:
            return numeric()
