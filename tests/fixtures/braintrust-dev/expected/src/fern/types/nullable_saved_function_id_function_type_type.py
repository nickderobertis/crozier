

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NullableSavedFunctionIdFunctionTypeType(enum.StrEnum):
    GLOBAL = "global"

    def visit(self, global_: typing.Callable[[], T_Result]) -> T_Result:
        if self is NullableSavedFunctionIdFunctionTypeType.GLOBAL:
            return global_()
