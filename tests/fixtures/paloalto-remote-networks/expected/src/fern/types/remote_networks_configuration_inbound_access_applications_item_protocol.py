

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemoteNetworksConfigurationInboundAccessApplicationsItemProtocol(enum.StrEnum):
    """
    Protocol used by this application
    """

    TCP = "TCP"
    UDP = "UDP"

    def visit(self, tcp: typing.Callable[[], T_Result], udp: typing.Callable[[], T_Result]) -> T_Result:
        if self is RemoteNetworksConfigurationInboundAccessApplicationsItemProtocol.TCP:
            return tcp()
        if self is RemoteNetworksConfigurationInboundAccessApplicationsItemProtocol.UDP:
            return udp()
