

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableServiceProtocol(enum.StrEnum):
    TCP = "tcp"
    UDP = "udp"
    SCTP = "sctp"

    def visit(
        self,
        tcp: typing.Callable[[], T_Result],
        udp: typing.Callable[[], T_Result],
        sctp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableServiceProtocol.TCP:
            return tcp()
        if self is WritableServiceProtocol.UDP:
            return udp()
        if self is WritableServiceProtocol.SCTP:
            return sctp()
