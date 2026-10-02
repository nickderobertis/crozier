

import typing

DisputeState = typing.Union[
    typing.Literal[
        "UNKNOWN_STATE",
        "INQUIRY_EVIDENCE_REQUIRED",
        "INQUIRY_PROCESSING",
        "INQUIRY_CLOSED",
        "EVIDENCE_REQUIRED",
        "PROCESSING",
        "WON",
        "LOST",
        "ACCEPTED",
        "WAITING_THIRD_PARTY",
    ],
    typing.Any,
]
