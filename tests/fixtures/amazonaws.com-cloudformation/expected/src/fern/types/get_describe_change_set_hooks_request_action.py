

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetDescribeChangeSetHooksRequestAction(enum.StrEnum):
    DESCRIBE_CHANGE_SET_HOOKS = "DescribeChangeSetHooks"

    def visit(self, describe_change_set_hooks: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDescribeChangeSetHooksRequestAction.DESCRIBE_CHANGE_SET_HOOKS:
            return describe_change_set_hooks()
