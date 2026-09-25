

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MatrixColumnBlockGroupType(enum.StrEnum):
    MATRIX = "MATRIX"

    def visit(self, matrix: typing.Callable[[], T_Result]) -> T_Result:
        if self is MatrixColumnBlockGroupType.MATRIX:
            return matrix()
