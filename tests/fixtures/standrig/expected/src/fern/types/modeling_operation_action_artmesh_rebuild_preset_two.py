

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionArtmeshRebuildPresetTwo(enum.StrEnum):
    EYELID = "eyelid"

    def visit(self, eyelid: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionArtmeshRebuildPresetTwo.EYELID:
            return eyelid()
