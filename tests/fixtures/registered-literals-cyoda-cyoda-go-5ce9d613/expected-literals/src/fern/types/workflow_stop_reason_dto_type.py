

import typing

WorkflowStopReasonDtoType = typing.Union[
    typing.Literal[
        "COMPLETED_NO_AUTO_TRANSITIONS",
        "COMPLETED_ALL_CRITERIA_REJECTED",
        "PAUSED_FOR_PROCESSING",
        "CANCELED",
        "NO_WORKFLOW_FOUND",
        "WORKFLOW_SKIPPED",
        "FORCE_SUCCESS",
        "INCOMPLETE_TRANSACTION",
        "UNKNOWN",
    ],
    typing.Any,
]
