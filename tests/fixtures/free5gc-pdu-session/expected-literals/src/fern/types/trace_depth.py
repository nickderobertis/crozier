

import typing

TraceDepth = typing.Union[
    typing.Literal[
        "MINIMUM",
        "MEDIUM",
        "MAXIMUM",
        "MINIMUM_WO_VENDOR_EXTENSION",
        "MEDIUM_WO_VENDOR_EXTENSION",
        "MAXIMUM_WO_VENDOR_EXTENSION",
    ],
    typing.Any,
]
