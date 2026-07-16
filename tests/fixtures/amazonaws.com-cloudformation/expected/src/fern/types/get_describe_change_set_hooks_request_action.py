

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetDescribeChangeSetHooksRequestAction(str, enum.Enum):
    DESCRIBE_CHANGE_SET_HOOKS = "DescribeChangeSetHooks"

    def visit(self, describe_change_set_hooks: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDescribeChangeSetHooksRequestAction.DESCRIBE_CHANGE_SET_HOOKS:
            return describe_change_set_hooks()
