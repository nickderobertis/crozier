

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetUpdateStackInstancesRequestAction(enum.StrEnum):
    UPDATE_STACK_INSTANCES = "UpdateStackInstances"

    def visit(self, update_stack_instances: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetUpdateStackInstancesRequestAction.UPDATE_STACK_INSTANCES:
            return update_stack_instances()
