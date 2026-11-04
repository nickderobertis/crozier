

import typing

WorkflowsUpdateApprovalStatus400ResponseMessage = typing.Union[
    typing.Literal[
        "This role does not exist in this workflow",
        "invalid user for user attribute",
        "This approval either was not requested or this user was not assigned to this approval",
    ],
    typing.Any,
]
