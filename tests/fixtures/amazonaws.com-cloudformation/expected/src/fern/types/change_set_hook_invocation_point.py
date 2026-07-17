

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChangeSetHookInvocationPoint(enum.StrEnum):
    """
    Specifies the points in provisioning logic where a hook is invoked.
    """

    PRE_PROVISION = "PRE_PROVISION"

    def visit(self, pre_provision: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChangeSetHookInvocationPoint.PRE_PROVISION:
            return pre_provision()
