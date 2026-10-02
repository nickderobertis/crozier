

import typing

ChangeSetSummaryStatus = typing.Union[
    typing.Literal[
        "CREATE_PENDING",
        "CREATE_IN_PROGRESS",
        "CREATE_COMPLETE",
        "DELETE_PENDING",
        "DELETE_IN_PROGRESS",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "FAILED",
    ],
    typing.Any,
]
