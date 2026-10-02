

import typing

PatchHookIdTrigger = typing.Union[
    typing.Literal[
        "ActionRun has Completed",
        "Document is Created",
        "Email is Received",
        "Prediction is Created",
        "ValidationTask has Completed",
        "ValidationTask is Created",
    ],
    typing.Any,
]
