

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostListStackInstancesRequestAction(str, enum.Enum):
    LIST_STACK_INSTANCES = "ListStackInstances"

    def visit(self, list_stack_instances: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostListStackInstancesRequestAction.LIST_STACK_INSTANCES:
            return list_stack_instances()
