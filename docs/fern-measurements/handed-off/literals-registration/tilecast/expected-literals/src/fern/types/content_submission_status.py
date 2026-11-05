

import typing

ContentSubmissionStatus = typing.Union[
    typing.Literal[
        "in_review", "changes_requested", "approved", "scheduled", "published", "superseded", "publication_failed"
    ],
    typing.Any,
]
