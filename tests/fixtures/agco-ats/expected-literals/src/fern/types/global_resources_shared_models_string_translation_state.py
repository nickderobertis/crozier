

import typing

GlobalResourcesSharedModelsStringTranslationState = typing.Union[
    typing.Literal[
        "Original",
        "Requested",
        "Processing",
        "Processed",
        "Validated",
        "Invalidated",
        "RequestPending",
        "CreatePending",
    ],
    typing.Any,
]
