

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionArtmeshGeneratePresetFive(enum.StrEnum):
    HAIR_ROOT = "hair-root"

    def visit(self, hair_root: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionArtmeshGeneratePresetFive.HAIR_ROOT:
            return hair_root()
