

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SuggestionsConfigItemDtoType(enum.StrEnum):
    POLICY = "Policy"
    MODULE = "Module"

    def visit(self, policy: typing.Callable[[], T_Result], module: typing.Callable[[], T_Result]) -> T_Result:
        if self is SuggestionsConfigItemDtoType.POLICY:
            return policy()
        if self is SuggestionsConfigItemDtoType.MODULE:
            return module()
