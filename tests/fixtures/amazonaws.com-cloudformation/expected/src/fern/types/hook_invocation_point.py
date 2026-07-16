

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HookInvocationPoint(enum.StrEnum):
    PRE_PROVISION = "PRE_PROVISION"

    def visit(self, pre_provision: typing.Callable[[], T_Result]) -> T_Result:
        if self is HookInvocationPoint.PRE_PROVISION:
            return pre_provision()
