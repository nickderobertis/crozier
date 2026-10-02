

import typing

CleEventType = typing.Union[
    typing.Literal[
        "released",
        "endOfDevelopment",
        "endOfSupport",
        "endOfLife",
        "endOfDistribution",
        "endOfMarketing",
        "supersededBy",
        "componentRenamed",
        "withdrawn",
    ],
    typing.Any,
]
