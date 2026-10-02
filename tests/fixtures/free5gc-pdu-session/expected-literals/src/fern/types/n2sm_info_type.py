

import typing

N2SmInfoType = typing.Union[
    typing.Literal[
        "PDU_RES_SETUP_REQ",
        "PDU_RES_SETUP_RSP",
        "PDU_RES_SETUP_FAIL",
        "PDU_RES_REL_CMD",
        "PDU_RES_REL_RSP",
        "PDU_RES_MOD_REQ",
        "PDU_RES_MOD_RSP",
        "PDU_RES_MOD_FAIL",
        "PDU_RES_NTY",
        "PDU_RES_NTY_REL",
        "PDU_RES_MOD_IND",
        "PDU_RES_MOD_CFM",
        "PATH_SWITCH_REQ",
        "PATH_SWITCH_SETUP_FAIL",
        "PATH_SWITCH_REQ_ACK",
        "PATH_SWITCH_REQ_FAIL",
        "HANDOVER_REQUIRED",
        "HANDOVER_CMD",
        "HANDOVER_PREP_FAIL",
        "HANDOVER_REQ_ACK",
        "HANDOVER_RES_ALLOC_FAIL",
    ],
    typing.Any,
]
