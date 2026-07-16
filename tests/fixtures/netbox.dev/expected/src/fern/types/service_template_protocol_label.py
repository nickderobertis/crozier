

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ServiceTemplateProtocolLabel(str, enum.Enum):
    TCP = "TCP"
    UDP = "UDP"
    SCTP = "SCTP"

    def visit(
        self,
        tcp: typing.Callable[[], T_Result],
        udp: typing.Callable[[], T_Result],
        sctp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceTemplateProtocolLabel.TCP:
            return tcp()
        if self is ServiceTemplateProtocolLabel.UDP:
            return udp()
        if self is ServiceTemplateProtocolLabel.SCTP:
            return sctp()
