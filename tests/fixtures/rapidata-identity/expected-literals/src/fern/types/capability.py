

import typing

Capability = typing.Union[
    typing.Literal[
        "SkipContentCheck",
        "PreheatBoost",
        "ManagedImageFaucet",
        "RequestFeatures",
        "RunExperiments",
        "ManagedForgeFaucet",
        "UploadLongMedia",
    ],
    typing.Any,
]
