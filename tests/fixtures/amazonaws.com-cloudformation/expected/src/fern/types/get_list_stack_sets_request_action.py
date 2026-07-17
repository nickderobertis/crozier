

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetListStackSetsRequestAction(enum.StrEnum):
    LIST_STACK_SETS = "ListStackSets"

    def visit(self, list_stack_sets: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListStackSetsRequestAction.LIST_STACK_SETS:
            return list_stack_sets()
