

import typing

NgapIeType = typing.Union[
    typing.Literal[
        "PDU_RES_SETUP_REQ",
        "PDU_RES_REL_CMD",
        "PDU_RES_MOD_REQ",
        "HANDOVER_CMD",
        "HANDOVER_REQUIRED",
        "HANDOVER_PREP_FAIL",
        "SRC_TO_TAR_CONTAINER",
        "TAR_TO_SRC_CONTAINER",
        "RAN_STATUS_TRANS_CONTAINER",
        "SON_CONFIG_TRANSFER",
        "NRPPA_PDU",
        "UE_RADIO_CAPABILITY",
    ],
    typing.Any,
]
