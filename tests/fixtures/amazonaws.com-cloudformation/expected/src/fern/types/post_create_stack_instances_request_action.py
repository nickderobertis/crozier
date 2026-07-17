

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostCreateStackInstancesRequestAction(enum.StrEnum):
    CREATE_STACK_INSTANCES = "CreateStackInstances"

    def visit(self, create_stack_instances: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostCreateStackInstancesRequestAction.CREATE_STACK_INSTANCES:
            return create_stack_instances()
