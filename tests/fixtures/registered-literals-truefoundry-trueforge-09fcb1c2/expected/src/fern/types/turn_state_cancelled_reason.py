

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TurnStateCancelledReason(enum.StrEnum):
    """
    Reason for the cancellation.
    """

    SERVER_EXECUTION_TIMEOUT = "server-execution-timeout"
    CLIENT_CANCELLED = "client-cancelled"
    CANCELLED_FOR_NEXT_TURN = "cancelled-for-next-turn"
    ABANDONED = "abandoned"

    def visit(
        self,
        server_execution_timeout: typing.Callable[[], T_Result],
        client_cancelled: typing.Callable[[], T_Result],
        cancelled_for_next_turn: typing.Callable[[], T_Result],
        abandoned: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TurnStateCancelledReason.SERVER_EXECUTION_TIMEOUT:
            return server_execution_timeout()
        if self is TurnStateCancelledReason.CLIENT_CANCELLED:
            return client_cancelled()
        if self is TurnStateCancelledReason.CANCELLED_FOR_NEXT_TURN:
            return cancelled_for_next_turn()
        if self is TurnStateCancelledReason.ABANDONED:
            return abandoned()
