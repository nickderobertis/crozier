

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ServiceTemplateProtocolValue(str, enum.Enum):
    TCP = "tcp"
    UDP = "udp"
    SCTP = "sctp"

    def visit(
        self,
        tcp: typing.Callable[[], T_Result],
        udp: typing.Callable[[], T_Result],
        sctp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceTemplateProtocolValue.TCP:
            return tcp()
        if self is ServiceTemplateProtocolValue.UDP:
            return udp()
        if self is ServiceTemplateProtocolValue.SCTP:
            return sctp()
