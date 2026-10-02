

import typing

RequestType = typing.Union[
    typing.Literal[
        "INITIAL_REQUEST", "EXISTING_PDU_SESSION", "INITIAL_EMERGENCY_REQUEST", "EXISTING_EMERGENCY_PDU_SESSION"
    ],
    typing.Any,
]
