

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .playback_diagnostics_nodes_item_streams_item_conversion_value import (
    PlaybackDiagnosticsNodesItemStreamsItemConversionValue,
)
from .playback_diagnostics_nodes_item_streams_item_reader import PlaybackDiagnosticsNodesItemStreamsItemReader


class PlaybackDiagnosticsNodesItemStreamsItem(UniversalBaseModel):
    id: str
    mode: str
    purpose: str
    state: str
    started_at: typing_extensions.Annotated[float, FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")]
    finished_at: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="finishedAt"), pydantic.Field(alias="finishedAt")
    ] = None
    first_byte_ms: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="firstByteMs"), pydantic.Field(alias="firstByteMs")
    ] = None
    range_start: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="rangeStart"), pydantic.Field(alias="rangeStart")
    ] = None
    range_end: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="rangeEnd"), pydantic.Field(alias="rangeEnd")
    ] = None
    output_bytes: typing_extensions.Annotated[
        float, FieldMetadata(alias="outputBytes"), pydantic.Field(alias="outputBytes")
    ]
    bytes_per_second: typing_extensions.Annotated[
        float, FieldMetadata(alias="bytesPerSecond"), pydantic.Field(alias="bytesPerSecond")
    ]
    source_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="sourceIds"), pydantic.Field(alias="sourceIds")
    ]
    active_reads: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="activeReads"), pydantic.Field(alias="activeReads")
    ] = None
    peak_reads: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="peakReads"), pydantic.Field(alias="peakReads")
    ] = None
    reader: typing.Optional[PlaybackDiagnosticsNodesItemStreamsItemReader] = None
    conversion: typing.Optional[typing.Dict[str, PlaybackDiagnosticsNodesItemStreamsItemConversionValue]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
