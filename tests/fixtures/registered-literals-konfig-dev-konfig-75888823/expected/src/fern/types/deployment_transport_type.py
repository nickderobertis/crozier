

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeploymentTransportType(enum.StrEnum):
    TCP = "tcp"
    UDP = "udp"
    TLS = "tls"

    def visit(
        self, tcp: typing.Callable[[], T_Result], udp: typing.Callable[[], T_Result], tls: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is DeploymentTransportType.TCP:
            return tcp()
        if self is DeploymentTransportType.UDP:
            return udp()
        if self is DeploymentTransportType.TLS:
            return tls()
