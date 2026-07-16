

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetDeleteStackInstancesRequestAction(str, enum.Enum):
    DELETE_STACK_INSTANCES = "DeleteStackInstances"

    def visit(self, delete_stack_instances: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDeleteStackInstancesRequestAction.DELETE_STACK_INSTANCES:
            return delete_stack_instances()
