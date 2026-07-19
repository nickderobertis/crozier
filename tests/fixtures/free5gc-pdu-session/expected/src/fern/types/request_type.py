

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RequestType(enum.StrEnum):
    INITIAL_REQUEST = "INITIAL_REQUEST"
    EXISTING_PDU_SESSION = "EXISTING_PDU_SESSION"
    INITIAL_EMERGENCY_REQUEST = "INITIAL_EMERGENCY_REQUEST"
    EXISTING_EMERGENCY_PDU_SESSION = "EXISTING_EMERGENCY_PDU_SESSION"

    def visit(
        self,
        initial_request: typing.Callable[[], T_Result],
        existing_pdu_session: typing.Callable[[], T_Result],
        initial_emergency_request: typing.Callable[[], T_Result],
        existing_emergency_pdu_session: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RequestType.INITIAL_REQUEST:
            return initial_request()
        if self is RequestType.EXISTING_PDU_SESSION:
            return existing_pdu_session()
        if self is RequestType.INITIAL_EMERGENCY_REQUEST:
            return initial_emergency_request()
        if self is RequestType.EXISTING_EMERGENCY_PDU_SESSION:
            return existing_emergency_pdu_session()
