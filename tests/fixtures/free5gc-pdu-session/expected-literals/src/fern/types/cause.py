

import typing

Cause = typing.Union[
    typing.Literal[
        "REL_DUE_TO_HO",
        "EPS_FALLBACK",
        "REL_DUE_TO_UP_SEC",
        "DNN_CONGESTION",
        "S-NSSAI_CONGESTION",
        "REL_DUE_TO_REACTIVATION",
        "5G_AN_NOT_RESPONDING",
        "REL_DUE_TO_SLICE_NOT_AVAILABLE",
        "REL_DUE_TO_DUPLICATE_SESSION_ID",
        "PDU_SESSION_STATUS_MISMATCH",
        "HO_FAILURE",
    ],
    typing.Any,
]
