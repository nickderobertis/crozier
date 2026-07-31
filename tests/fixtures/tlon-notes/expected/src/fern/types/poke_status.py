

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PokeStatus(enum.StrEnum):
    """
    Where the cross-ship poke stood when the timeout fired.
    `sending` = no poke-ack yet, `acked` = host accepted but no
    response-update yet, `nacked` = host crashed (a terminal
    `error` body would normally have followed; if you see this,
    the timeout beat the nack delivery).
    """

    SENDING = "sending"
    ACKED = "acked"
    NACKED = "nacked"

    def visit(
        self,
        sending: typing.Callable[[], T_Result],
        acked: typing.Callable[[], T_Result],
        nacked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PokeStatus.SENDING:
            return sending()
        if self is PokeStatus.ACKED:
            return acked()
        if self is PokeStatus.NACKED:
            return nacked()
