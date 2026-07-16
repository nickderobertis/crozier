

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetCreateStackInstancesRequestAction(str, enum.Enum):
    CREATE_STACK_INSTANCES = "CreateStackInstances"

    def visit(self, create_stack_instances: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCreateStackInstancesRequestAction.CREATE_STACK_INSTANCES:
            return create_stack_instances()
