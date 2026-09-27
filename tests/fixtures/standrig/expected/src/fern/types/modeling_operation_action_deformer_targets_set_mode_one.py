

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerTargetsSetModeOne(enum.StrEnum):
    MERGE = "merge"

    def visit(self, merge: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerTargetsSetModeOne.MERGE:
            return merge()
