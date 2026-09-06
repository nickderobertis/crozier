

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptDataToolFunctionsItemType(enum.StrEnum):
    GLOBAL = "global"

    def visit(self, global_: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptDataToolFunctionsItemType.GLOBAL:
            return global_()
