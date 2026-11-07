

import typing

InferenceResult = typing.Union[
    typing.Literal["symbol-detection", "text-detection", "graph-construction", "line-detection", "graph-persistence"],
    typing.Any,
]
