

import typing

ProposalStatus = typing.Union[
    typing.Literal[
        "draft",
        "submitted",
        "approved",
        "rejected",
        "revision_required",
        "executing",
        "executed",
        "failed",
        "expired",
        "blocked",
    ],
    typing.Any,
]
