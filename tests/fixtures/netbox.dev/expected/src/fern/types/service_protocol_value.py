

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ServiceProtocolValue(str, enum.Enum):
    TCP = "tcp"
    UDP = "udp"
    SCTP = "sctp"

    def visit(
        self,
        tcp: typing.Callable[[], T_Result],
        udp: typing.Callable[[], T_Result],
        sctp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceProtocolValue.TCP:
            return tcp()
        if self is ServiceProtocolValue.UDP:
            return udp()
        if self is ServiceProtocolValue.SCTP:
            return sctp()
