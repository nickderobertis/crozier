

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NgapIeType(enum.StrEnum):
    PDU_RES_SETUP_REQ = "PDU_RES_SETUP_REQ"
    PDU_RES_REL_CMD = "PDU_RES_REL_CMD"
    PDU_RES_MOD_REQ = "PDU_RES_MOD_REQ"
    HANDOVER_CMD = "HANDOVER_CMD"
    HANDOVER_REQUIRED = "HANDOVER_REQUIRED"
    HANDOVER_PREP_FAIL = "HANDOVER_PREP_FAIL"
    SRC_TO_TAR_CONTAINER = "SRC_TO_TAR_CONTAINER"
    TAR_TO_SRC_CONTAINER = "TAR_TO_SRC_CONTAINER"
    RAN_STATUS_TRANS_CONTAINER = "RAN_STATUS_TRANS_CONTAINER"
    SON_CONFIG_TRANSFER = "SON_CONFIG_TRANSFER"
    NRPPA_PDU = "NRPPA_PDU"
    UE_RADIO_CAPABILITY = "UE_RADIO_CAPABILITY"

    def visit(
        self,
        pdu_res_setup_req: typing.Callable[[], T_Result],
        pdu_res_rel_cmd: typing.Callable[[], T_Result],
        pdu_res_mod_req: typing.Callable[[], T_Result],
        handover_cmd: typing.Callable[[], T_Result],
        handover_required: typing.Callable[[], T_Result],
        handover_prep_fail: typing.Callable[[], T_Result],
        src_to_tar_container: typing.Callable[[], T_Result],
        tar_to_src_container: typing.Callable[[], T_Result],
        ran_status_trans_container: typing.Callable[[], T_Result],
        son_config_transfer: typing.Callable[[], T_Result],
        nrppa_pdu: typing.Callable[[], T_Result],
        ue_radio_capability: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NgapIeType.PDU_RES_SETUP_REQ:
            return pdu_res_setup_req()
        if self is NgapIeType.PDU_RES_REL_CMD:
            return pdu_res_rel_cmd()
        if self is NgapIeType.PDU_RES_MOD_REQ:
            return pdu_res_mod_req()
        if self is NgapIeType.HANDOVER_CMD:
            return handover_cmd()
        if self is NgapIeType.HANDOVER_REQUIRED:
            return handover_required()
        if self is NgapIeType.HANDOVER_PREP_FAIL:
            return handover_prep_fail()
        if self is NgapIeType.SRC_TO_TAR_CONTAINER:
            return src_to_tar_container()
        if self is NgapIeType.TAR_TO_SRC_CONTAINER:
            return tar_to_src_container()
        if self is NgapIeType.RAN_STATUS_TRANS_CONTAINER:
            return ran_status_trans_container()
        if self is NgapIeType.SON_CONFIG_TRANSFER:
            return son_config_transfer()
        if self is NgapIeType.NRPPA_PDU:
            return nrppa_pdu()
        if self is NgapIeType.UE_RADIO_CAPABILITY:
            return ue_radio_capability()
