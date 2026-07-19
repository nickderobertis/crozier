

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Cause(enum.StrEnum):
    REL_DUE_TO_HO = "REL_DUE_TO_HO"
    EPS_FALLBACK = "EPS_FALLBACK"
    REL_DUE_TO_UP_SEC = "REL_DUE_TO_UP_SEC"
    DNN_CONGESTION = "DNN_CONGESTION"
    S_NSSAI_CONGESTION = "S-NSSAI_CONGESTION"
    REL_DUE_TO_REACTIVATION = "REL_DUE_TO_REACTIVATION"
    FIVE_G_AN_NOT_RESPONDING = "5G_AN_NOT_RESPONDING"
    REL_DUE_TO_SLICE_NOT_AVAILABLE = "REL_DUE_TO_SLICE_NOT_AVAILABLE"
    REL_DUE_TO_DUPLICATE_SESSION_ID = "REL_DUE_TO_DUPLICATE_SESSION_ID"
    PDU_SESSION_STATUS_MISMATCH = "PDU_SESSION_STATUS_MISMATCH"
    HO_FAILURE = "HO_FAILURE"

    def visit(
        self,
        rel_due_to_ho: typing.Callable[[], T_Result],
        eps_fallback: typing.Callable[[], T_Result],
        rel_due_to_up_sec: typing.Callable[[], T_Result],
        dnn_congestion: typing.Callable[[], T_Result],
        s_nssai_congestion: typing.Callable[[], T_Result],
        rel_due_to_reactivation: typing.Callable[[], T_Result],
        five_g_an_not_responding: typing.Callable[[], T_Result],
        rel_due_to_slice_not_available: typing.Callable[[], T_Result],
        rel_due_to_duplicate_session_id: typing.Callable[[], T_Result],
        pdu_session_status_mismatch: typing.Callable[[], T_Result],
        ho_failure: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Cause.REL_DUE_TO_HO:
            return rel_due_to_ho()
        if self is Cause.EPS_FALLBACK:
            return eps_fallback()
        if self is Cause.REL_DUE_TO_UP_SEC:
            return rel_due_to_up_sec()
        if self is Cause.DNN_CONGESTION:
            return dnn_congestion()
        if self is Cause.S_NSSAI_CONGESTION:
            return s_nssai_congestion()
        if self is Cause.REL_DUE_TO_REACTIVATION:
            return rel_due_to_reactivation()
        if self is Cause.FIVE_G_AN_NOT_RESPONDING:
            return five_g_an_not_responding()
        if self is Cause.REL_DUE_TO_SLICE_NOT_AVAILABLE:
            return rel_due_to_slice_not_available()
        if self is Cause.REL_DUE_TO_DUPLICATE_SESSION_ID:
            return rel_due_to_duplicate_session_id()
        if self is Cause.PDU_SESSION_STATUS_MISMATCH:
            return pdu_session_status_mismatch()
        if self is Cause.HO_FAILURE:
            return ho_failure()
