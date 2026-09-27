

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionSymmetryContractContractLinksItemKindOne(enum.StrEnum):
    DEFORMER = "deformer"

    def visit(self, deformer: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionSymmetryContractContractLinksItemKindOne.DEFORMER:
            return deformer()
