

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DisputeState(str, enum.Enum):
    """
    The list of possible dispute states.
    """

    UNKNOWN_STATE = "UNKNOWN_STATE"
    INQUIRY_EVIDENCE_REQUIRED = "INQUIRY_EVIDENCE_REQUIRED"
    INQUIRY_PROCESSING = "INQUIRY_PROCESSING"
    INQUIRY_CLOSED = "INQUIRY_CLOSED"
    EVIDENCE_REQUIRED = "EVIDENCE_REQUIRED"
    PROCESSING = "PROCESSING"
    WON = "WON"
    LOST = "LOST"
    ACCEPTED = "ACCEPTED"
    WAITING_THIRD_PARTY = "WAITING_THIRD_PARTY"

    def visit(
        self,
        unknown_state: typing.Callable[[], T_Result],
        inquiry_evidence_required: typing.Callable[[], T_Result],
        inquiry_processing: typing.Callable[[], T_Result],
        inquiry_closed: typing.Callable[[], T_Result],
        evidence_required: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        won: typing.Callable[[], T_Result],
        lost: typing.Callable[[], T_Result],
        accepted: typing.Callable[[], T_Result],
        waiting_third_party: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DisputeState.UNKNOWN_STATE:
            return unknown_state()
        if self is DisputeState.INQUIRY_EVIDENCE_REQUIRED:
            return inquiry_evidence_required()
        if self is DisputeState.INQUIRY_PROCESSING:
            return inquiry_processing()
        if self is DisputeState.INQUIRY_CLOSED:
            return inquiry_closed()
        if self is DisputeState.EVIDENCE_REQUIRED:
            return evidence_required()
        if self is DisputeState.PROCESSING:
            return processing()
        if self is DisputeState.WON:
            return won()
        if self is DisputeState.LOST:
            return lost()
        if self is DisputeState.ACCEPTED:
            return accepted()
        if self is DisputeState.WAITING_THIRD_PARTY:
            return waiting_third_party()
