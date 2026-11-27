

import typing

EntryReviewRecordStatus = typing.Union[
    typing.Literal[
        "ACCEPTED",
        "NEEDS_REVIEW",
        "REJECTED",
        "RETRACTED",
        "ACCEPTANCE_SNAPSHOT_IN_PROGRESS",
        "REVIEW_SNAPSHOT_IN_PROGRESS",
        "IN_PROGRESS",
        "ACTION_REQUIRED",
    ],
    typing.Any,
]
