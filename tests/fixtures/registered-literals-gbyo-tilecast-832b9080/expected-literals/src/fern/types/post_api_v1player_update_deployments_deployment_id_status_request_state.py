

import typing

PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState = typing.Union[
    typing.Literal[
        "downloading",
        "downloaded",
        "verifying",
        "ready",
        "waiting_for_permission",
        "waiting_for_user",
        "installing",
        "reconnecting",
        "failed",
        "succeeded",
    ],
    typing.Any,
]
