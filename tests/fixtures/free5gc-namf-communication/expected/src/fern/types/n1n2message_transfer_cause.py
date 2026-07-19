

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class N1N2MessageTransferCause(enum.StrEnum):
    ATTEMPTING_TO_REACH_UE = "ATTEMPTING_TO_REACH_UE"
    N1N2TRANSFER_INITIATED = "N1_N2_TRANSFER_INITIATED"
    WAITING_FOR_ASYNCHRONOUS_TRANSFER = "WAITING_FOR_ASYNCHRONOUS_TRANSFER"
    UE_NOT_RESPONDING = "UE_NOT_RESPONDING"
    N1MSG_NOT_TRANSFERRED = "N1_MSG_NOT_TRANSFERRED"
    UE_NOT_REACHABLE_FOR_SESSION = "UE_NOT_REACHABLE_FOR_SESSION"

    def visit(
        self,
        attempting_to_reach_ue: typing.Callable[[], T_Result],
        n1n2transfer_initiated: typing.Callable[[], T_Result],
        waiting_for_asynchronous_transfer: typing.Callable[[], T_Result],
        ue_not_responding: typing.Callable[[], T_Result],
        n1msg_not_transferred: typing.Callable[[], T_Result],
        ue_not_reachable_for_session: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is N1N2MessageTransferCause.ATTEMPTING_TO_REACH_UE:
            return attempting_to_reach_ue()
        if self is N1N2MessageTransferCause.N1N2TRANSFER_INITIATED:
            return n1n2transfer_initiated()
        if self is N1N2MessageTransferCause.WAITING_FOR_ASYNCHRONOUS_TRANSFER:
            return waiting_for_asynchronous_transfer()
        if self is N1N2MessageTransferCause.UE_NOT_RESPONDING:
            return ue_not_responding()
        if self is N1N2MessageTransferCause.N1MSG_NOT_TRANSFERRED:
            return n1msg_not_transferred()
        if self is N1N2MessageTransferCause.UE_NOT_REACHABLE_FOR_SESSION:
            return ue_not_reachable_for_session()
