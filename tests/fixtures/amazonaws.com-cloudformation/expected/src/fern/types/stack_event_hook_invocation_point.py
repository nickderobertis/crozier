

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackEventHookInvocationPoint(enum.StrEnum):
    """
    Invocation points are points in provisioning logic where hooks are initiated.
    """

    PRE_PROVISION = "PRE_PROVISION"

    def visit(self, pre_provision: typing.Callable[[], T_Result]) -> T_Result:
        if self is StackEventHookInvocationPoint.PRE_PROVISION:
            return pre_provision()
