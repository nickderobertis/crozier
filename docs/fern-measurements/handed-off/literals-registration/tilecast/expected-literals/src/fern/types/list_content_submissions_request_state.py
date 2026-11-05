

import typing

ListContentSubmissionsRequestState = typing.Union[
    typing.Literal[
        "in_review", "changes_requested", "approved", "scheduled", "published", "publication_failed", "superseded"
    ],
    typing.Any,
]
