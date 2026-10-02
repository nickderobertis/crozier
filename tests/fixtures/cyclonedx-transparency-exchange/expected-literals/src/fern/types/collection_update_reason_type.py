

import typing

CollectionUpdateReasonType = typing.Union[
    typing.Literal["INITIAL_RELEASE", "VEX_UPDATED", "ARTIFACT_UPDATED", "ARTIFACT_ADDED", "ARTIFACT_REMOVED"],
    typing.Any,
]
