

import typing

AgentRunsRunsItemStatus = typing.Union[
    typing.Literal[
        "archived",
        "exported",
        "pending-export",
        "pending-predictions",
        "ready-for-review",
        "review-completed",
        "succeeded-predictions",
        "error",
        "running",
        "completed",
        "review-in-progress",
    ],
    typing.Any,
]
