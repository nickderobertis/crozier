

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TracingType(enum.StrEnum):
    NETWORKING_DROP = "networking_drop"
    IO = "io_tracing"
    TCP_RETRANSMIT = "tcp_retransmit"

    def visit(
        self,
        networking_drop: typing.Callable[[], T_Result],
        io: typing.Callable[[], T_Result],
        tcp_retransmit: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TracingType.NETWORKING_DROP:
            return networking_drop()
        if self is TracingType.IO:
            return io()
        if self is TracingType.TCP_RETRANSMIT:
            return tcp_retransmit()
