

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemoteNetworksConfigurationEcmpLoadBalancing(enum.StrEnum):
    ENABLE = "enable"
    DISABLE = "disable"

    def visit(self, enable: typing.Callable[[], T_Result], disable: typing.Callable[[], T_Result]) -> T_Result:
        if self is RemoteNetworksConfigurationEcmpLoadBalancing.ENABLE:
            return enable()
        if self is RemoteNetworksConfigurationEcmpLoadBalancing.DISABLE:
            return disable()
