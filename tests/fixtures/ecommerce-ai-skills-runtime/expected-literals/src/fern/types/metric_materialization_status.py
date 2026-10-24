

import typing

MetricMaterializationStatus = typing.Union[
    typing.Literal["running", "succeeded", "partial", "quarantined", "failed"], typing.Any
]
