

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceProtocolLabel(enum.StrEnum):
    TCP = "TCP"
    UDP = "UDP"
    SCTP = "SCTP"

    def visit(
        self,
        tcp: typing.Callable[[], T_Result],
        udp: typing.Callable[[], T_Result],
        sctp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceProtocolLabel.TCP:
            return tcp()
        if self is ServiceProtocolLabel.UDP:
            return udp()
        if self is ServiceProtocolLabel.SCTP:
            return sctp()
