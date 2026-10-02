

import typing

FieldCardinality = typing.Union[
    typing.Literal["CARDINALITY_UNKNOWN", "CARDINALITY_OPTIONAL", "CARDINALITY_REQUIRED", "CARDINALITY_REPEATED"],
    typing.Any,
]
