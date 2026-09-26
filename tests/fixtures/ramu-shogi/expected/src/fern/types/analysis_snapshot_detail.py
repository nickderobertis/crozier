

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ..core.serialization import FieldMetadata
from .analysis_snapshot_entry import AnalysisSnapshotEntry
from .analysis_snapshot_summary import AnalysisSnapshotSummary


class AnalysisSnapshotDetail(AnalysisSnapshotSummary):
    line_moves: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="lineMoves"), pydantic.Field(alias="lineMoves")
    ]
    analysis_settings: typing_extensions.Annotated[
        typing.Optional["JsonValue"], FieldMetadata(alias="analysisSettings"), pydantic.Field(alias="analysisSettings")
    ] = None
    metadata: typing.Optional["JsonValue"] = None
    entries: typing.List[AnalysisSnapshotEntry]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .json_value import JsonValue

update_forward_refs(AnalysisSnapshotDetail, JsonValue=JsonValue)
