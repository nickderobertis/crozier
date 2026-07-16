

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableServiceTemplateProtocol(enum.StrEnum):
    TCP = "tcp"
    UDP = "udp"
    SCTP = "sctp"

    def visit(
        self,
        tcp: typing.Callable[[], T_Result],
        udp: typing.Callable[[], T_Result],
        sctp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableServiceTemplateProtocol.TCP:
            return tcp()
        if self is WritableServiceTemplateProtocol.UDP:
            return udp()
        if self is WritableServiceTemplateProtocol.SCTP:
            return sctp()
