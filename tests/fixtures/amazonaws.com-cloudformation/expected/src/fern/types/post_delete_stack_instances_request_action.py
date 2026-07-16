

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDeleteStackInstancesRequestAction(enum.StrEnum):
    DELETE_STACK_INSTANCES = "DeleteStackInstances"

    def visit(self, delete_stack_instances: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDeleteStackInstancesRequestAction.DELETE_STACK_INSTANCES:
            return delete_stack_instances()
