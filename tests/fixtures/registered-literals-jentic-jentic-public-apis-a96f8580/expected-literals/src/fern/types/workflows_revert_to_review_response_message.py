

import typing

WorkflowsRevertToReviewResponseMessage = typing.Union[
    typing.Literal[
        "invalid user for user attribute",
        "workflow was not built in workflow designer and cannot be reverted to review via the API",
        "workflow cannot be reverted to review as it is not in the sign stage",
        "various malformed user payload messages",
    ],
    typing.Any,
]
