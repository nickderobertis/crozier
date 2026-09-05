

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EcmpLoadBalancingEcmpLoadBalancingEnabled(enum.StrEnum):
    ENABLE = "enable"
    DISABLE = "disable"

    def visit(self, enable: typing.Callable[[], T_Result], disable: typing.Callable[[], T_Result]) -> T_Result:
        if self is EcmpLoadBalancingEcmpLoadBalancingEnabled.ENABLE:
            return enable()
        if self is EcmpLoadBalancingEcmpLoadBalancingEnabled.DISABLE:
            return disable()
