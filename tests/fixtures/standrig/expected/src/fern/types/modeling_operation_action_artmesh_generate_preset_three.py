

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionArtmeshGeneratePresetThree(enum.StrEnum):
    EYE = "eye"

    def visit(self, eye: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionArtmeshGeneratePresetThree.EYE:
            return eye()
