

import typing

StatusCode = typing.Union[
    typing.Literal[
        "Pending",
        "Active",
        "Repaid",
        "WrittenOff",
        "Failed",
        "Revoked",
        "Requested",
        "Reviewing",
        "Approved",
        "Rejected",
        "Cancelled",
    ],
    typing.Any,
]
