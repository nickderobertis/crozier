

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionPartContourShadeShadeProfile(enum.StrEnum):
    CHEEK = "cheek"

    def visit(self, cheek: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionPartContourShadeShadeProfile.CHEEK:
            return cheek()
