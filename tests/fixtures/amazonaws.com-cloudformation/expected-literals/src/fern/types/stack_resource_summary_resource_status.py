

import typing

StackResourceSummaryResourceStatus = typing.Union[
    typing.Literal[
        "CREATE_IN_PROGRESS",
        "CREATE_FAILED",
        "CREATE_COMPLETE",
        "DELETE_IN_PROGRESS",
        "DELETE_FAILED",
        "DELETE_COMPLETE",
        "DELETE_SKIPPED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_FAILED",
        "UPDATE_COMPLETE",
        "IMPORT_FAILED",
        "IMPORT_COMPLETE",
        "IMPORT_IN_PROGRESS",
        "IMPORT_ROLLBACK_IN_PROGRESS",
        "IMPORT_ROLLBACK_FAILED",
        "IMPORT_ROLLBACK_COMPLETE",
        "UPDATE_ROLLBACK_IN_PROGRESS",
        "UPDATE_ROLLBACK_COMPLETE",
        "UPDATE_ROLLBACK_FAILED",
        "ROLLBACK_IN_PROGRESS",
        "ROLLBACK_COMPLETE",
        "ROLLBACK_FAILED",
    ],
    typing.Any,
]
