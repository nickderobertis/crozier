

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionArtmeshRebuildPresetZero(enum.StrEnum):
    FACE_FEATURE = "face-feature"

    def visit(self, face_feature: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionArtmeshRebuildPresetZero.FACE_FEATURE:
            return face_feature()
