

import typing

CampaignReleaseStatus = typing.Union[
    typing.Literal[
        "in_review",
        "changes_requested",
        "approved",
        "scheduled",
        "published",
        "superseded",
        "cancelled",
        "publication_failed",
    ],
    typing.Any,
]
