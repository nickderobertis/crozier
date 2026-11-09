

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransportType(enum.StrEnum):
    """
    Transport type specifies the underlying communication protocol to the exposed port.
    """

    TCP = "tcp"
    UDP = "udp"
    TLS = "tls"

    def visit(
        self, tcp: typing.Callable[[], T_Result], udp: typing.Callable[[], T_Result], tls: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TransportType.TCP:
            return tcp()
        if self is TransportType.UDP:
            return udp()
        if self is TransportType.TLS:
            return tls()
