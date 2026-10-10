

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CuttingMethod(enum.StrEnum):
    CUTTING = "cutting"

    def visit(self, cutting: typing.Callable[[], T_Result]) -> T_Result:
        if self is CuttingMethod.CUTTING:
            return cutting()
