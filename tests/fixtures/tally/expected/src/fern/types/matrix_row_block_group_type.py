

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MatrixRowBlockGroupType(enum.StrEnum):
    MATRIX = "MATRIX"

    def visit(self, matrix: typing.Callable[[], T_Result]) -> T_Result:
        if self is MatrixRowBlockGroupType.MATRIX:
            return matrix()
