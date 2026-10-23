

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemColumnsType(enum.StrEnum):
    MATRIX = "matrix"

    def visit(self, matrix: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemElementsItemColumnsType.MATRIX:
            return matrix()
