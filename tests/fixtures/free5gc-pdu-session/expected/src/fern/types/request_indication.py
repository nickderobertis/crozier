

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RequestIndication(enum.StrEnum):
    UE_REQ_PDU_SES_MOD = "UE_REQ_PDU_SES_MOD"
    UE_REQ_PDU_SES_REL = "UE_REQ_PDU_SES_REL"
    PDU_SES_MOB = "PDU_SES_MOB"
    NW_REQ_PDU_SES_AUTH = "NW_REQ_PDU_SES_AUTH"
    NW_REQ_PDU_SES_MOD = "NW_REQ_PDU_SES_MOD"
    NW_REQ_PDU_SES_REL = "NW_REQ_PDU_SES_REL"
    EBI_ASSIGNMENT_REQ = "EBI_ASSIGNMENT_REQ"

    def visit(
        self,
        ue_req_pdu_ses_mod: typing.Callable[[], T_Result],
        ue_req_pdu_ses_rel: typing.Callable[[], T_Result],
        pdu_ses_mob: typing.Callable[[], T_Result],
        nw_req_pdu_ses_auth: typing.Callable[[], T_Result],
        nw_req_pdu_ses_mod: typing.Callable[[], T_Result],
        nw_req_pdu_ses_rel: typing.Callable[[], T_Result],
        ebi_assignment_req: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RequestIndication.UE_REQ_PDU_SES_MOD:
            return ue_req_pdu_ses_mod()
        if self is RequestIndication.UE_REQ_PDU_SES_REL:
            return ue_req_pdu_ses_rel()
        if self is RequestIndication.PDU_SES_MOB:
            return pdu_ses_mob()
        if self is RequestIndication.NW_REQ_PDU_SES_AUTH:
            return nw_req_pdu_ses_auth()
        if self is RequestIndication.NW_REQ_PDU_SES_MOD:
            return nw_req_pdu_ses_mod()
        if self is RequestIndication.NW_REQ_PDU_SES_REL:
            return nw_req_pdu_ses_rel()
        if self is RequestIndication.EBI_ASSIGNMENT_REQ:
            return ebi_assignment_req()
