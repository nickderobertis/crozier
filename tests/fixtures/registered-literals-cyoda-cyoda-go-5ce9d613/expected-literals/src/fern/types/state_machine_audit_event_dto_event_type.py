

import typing

StateMachineAuditEventDtoEventType = typing.Union[
    typing.Literal[
        "STARTED",
        "FINISHED",
        "CANCELLED",
        "FORCED_SUCCESS",
        "WORKFLOW_FOUND",
        "WORKFLOW_NOT_FOUND",
        "WORKFLOW_SKIPPED",
        "TRANSITION_MADE",
        "TRANSITION_NOT_FOUND",
        "TRANSITION_CRITERION_NOT_MATCHED",
        "PROCESS_CRITERION_NOT_MATCHED",
        "PROCESSING_PAUSED",
        "STATE_PROCESS_RESULT",
    ],
    typing.Any,
]
