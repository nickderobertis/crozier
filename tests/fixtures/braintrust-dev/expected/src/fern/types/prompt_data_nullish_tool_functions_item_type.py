

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptDataNullishToolFunctionsItemType(enum.StrEnum):
    GLOBAL = "global"

    def visit(self, global_: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptDataNullishToolFunctionsItemType.GLOBAL:
            return global_()
