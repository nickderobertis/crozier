

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionSymmetryContractContractAxis(enum.StrEnum):
    VERTICAL = "vertical"

    def visit(self, vertical: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionSymmetryContractContractAxis.VERTICAL:
            return vertical()
