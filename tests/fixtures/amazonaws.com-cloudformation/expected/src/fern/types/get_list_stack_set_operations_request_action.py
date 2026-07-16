

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetListStackSetOperationsRequestAction(enum.StrEnum):
    LIST_STACK_SET_OPERATIONS = "ListStackSetOperations"

    def visit(self, list_stack_set_operations: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListStackSetOperationsRequestAction.LIST_STACK_SET_OPERATIONS:
            return list_stack_set_operations()
