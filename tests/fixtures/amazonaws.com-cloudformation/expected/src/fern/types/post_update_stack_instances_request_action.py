

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostUpdateStackInstancesRequestAction(str, enum.Enum):
    UPDATE_STACK_INSTANCES = "UpdateStackInstances"

    def visit(self, update_stack_instances: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostUpdateStackInstancesRequestAction.UPDATE_STACK_INSTANCES:
            return update_stack_instances()
