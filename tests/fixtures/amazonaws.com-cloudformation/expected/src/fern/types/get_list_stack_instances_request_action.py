

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetListStackInstancesRequestAction(enum.StrEnum):
    LIST_STACK_INSTANCES = "ListStackInstances"

    def visit(self, list_stack_instances: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListStackInstancesRequestAction.LIST_STACK_INSTANCES:
            return list_stack_instances()
