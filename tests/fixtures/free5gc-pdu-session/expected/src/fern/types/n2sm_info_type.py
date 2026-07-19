

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class N2SmInfoType(enum.StrEnum):
    PDU_RES_SETUP_REQ = "PDU_RES_SETUP_REQ"
    PDU_RES_SETUP_RSP = "PDU_RES_SETUP_RSP"
    PDU_RES_SETUP_FAIL = "PDU_RES_SETUP_FAIL"
    PDU_RES_REL_CMD = "PDU_RES_REL_CMD"
    PDU_RES_REL_RSP = "PDU_RES_REL_RSP"
    PDU_RES_MOD_REQ = "PDU_RES_MOD_REQ"
    PDU_RES_MOD_RSP = "PDU_RES_MOD_RSP"
    PDU_RES_MOD_FAIL = "PDU_RES_MOD_FAIL"
    PDU_RES_NTY = "PDU_RES_NTY"
    PDU_RES_NTY_REL = "PDU_RES_NTY_REL"
    PDU_RES_MOD_IND = "PDU_RES_MOD_IND"
    PDU_RES_MOD_CFM = "PDU_RES_MOD_CFM"
    PATH_SWITCH_REQ = "PATH_SWITCH_REQ"
    PATH_SWITCH_SETUP_FAIL = "PATH_SWITCH_SETUP_FAIL"
    PATH_SWITCH_REQ_ACK = "PATH_SWITCH_REQ_ACK"
    PATH_SWITCH_REQ_FAIL = "PATH_SWITCH_REQ_FAIL"
    HANDOVER_REQUIRED = "HANDOVER_REQUIRED"
    HANDOVER_CMD = "HANDOVER_CMD"
    HANDOVER_PREP_FAIL = "HANDOVER_PREP_FAIL"
    HANDOVER_REQ_ACK = "HANDOVER_REQ_ACK"
    HANDOVER_RES_ALLOC_FAIL = "HANDOVER_RES_ALLOC_FAIL"

    def visit(
        self,
        pdu_res_setup_req: typing.Callable[[], T_Result],
        pdu_res_setup_rsp: typing.Callable[[], T_Result],
        pdu_res_setup_fail: typing.Callable[[], T_Result],
        pdu_res_rel_cmd: typing.Callable[[], T_Result],
        pdu_res_rel_rsp: typing.Callable[[], T_Result],
        pdu_res_mod_req: typing.Callable[[], T_Result],
        pdu_res_mod_rsp: typing.Callable[[], T_Result],
        pdu_res_mod_fail: typing.Callable[[], T_Result],
        pdu_res_nty: typing.Callable[[], T_Result],
        pdu_res_nty_rel: typing.Callable[[], T_Result],
        pdu_res_mod_ind: typing.Callable[[], T_Result],
        pdu_res_mod_cfm: typing.Callable[[], T_Result],
        path_switch_req: typing.Callable[[], T_Result],
        path_switch_setup_fail: typing.Callable[[], T_Result],
        path_switch_req_ack: typing.Callable[[], T_Result],
        path_switch_req_fail: typing.Callable[[], T_Result],
        handover_required: typing.Callable[[], T_Result],
        handover_cmd: typing.Callable[[], T_Result],
        handover_prep_fail: typing.Callable[[], T_Result],
        handover_req_ack: typing.Callable[[], T_Result],
        handover_res_alloc_fail: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is N2SmInfoType.PDU_RES_SETUP_REQ:
            return pdu_res_setup_req()
        if self is N2SmInfoType.PDU_RES_SETUP_RSP:
            return pdu_res_setup_rsp()
        if self is N2SmInfoType.PDU_RES_SETUP_FAIL:
            return pdu_res_setup_fail()
        if self is N2SmInfoType.PDU_RES_REL_CMD:
            return pdu_res_rel_cmd()
        if self is N2SmInfoType.PDU_RES_REL_RSP:
            return pdu_res_rel_rsp()
        if self is N2SmInfoType.PDU_RES_MOD_REQ:
            return pdu_res_mod_req()
        if self is N2SmInfoType.PDU_RES_MOD_RSP:
            return pdu_res_mod_rsp()
        if self is N2SmInfoType.PDU_RES_MOD_FAIL:
            return pdu_res_mod_fail()
        if self is N2SmInfoType.PDU_RES_NTY:
            return pdu_res_nty()
        if self is N2SmInfoType.PDU_RES_NTY_REL:
            return pdu_res_nty_rel()
        if self is N2SmInfoType.PDU_RES_MOD_IND:
            return pdu_res_mod_ind()
        if self is N2SmInfoType.PDU_RES_MOD_CFM:
            return pdu_res_mod_cfm()
        if self is N2SmInfoType.PATH_SWITCH_REQ:
            return path_switch_req()
        if self is N2SmInfoType.PATH_SWITCH_SETUP_FAIL:
            return path_switch_setup_fail()
        if self is N2SmInfoType.PATH_SWITCH_REQ_ACK:
            return path_switch_req_ack()
        if self is N2SmInfoType.PATH_SWITCH_REQ_FAIL:
            return path_switch_req_fail()
        if self is N2SmInfoType.HANDOVER_REQUIRED:
            return handover_required()
        if self is N2SmInfoType.HANDOVER_CMD:
            return handover_cmd()
        if self is N2SmInfoType.HANDOVER_PREP_FAIL:
            return handover_prep_fail()
        if self is N2SmInfoType.HANDOVER_REQ_ACK:
            return handover_req_ack()
        if self is N2SmInfoType.HANDOVER_RES_ALLOC_FAIL:
            return handover_res_alloc_fail()
