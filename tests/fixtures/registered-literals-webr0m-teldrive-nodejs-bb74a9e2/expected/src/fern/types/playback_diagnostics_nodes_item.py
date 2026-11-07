

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .playback_diagnostics_nodes_item_role import PlaybackDiagnosticsNodesItemRole
from .playback_diagnostics_nodes_item_sources_item import PlaybackDiagnosticsNodesItemSourcesItem
from .playback_diagnostics_nodes_item_streams_item import PlaybackDiagnosticsNodesItemStreamsItem


class PlaybackDiagnosticsNodesItem(UniversalBaseModel):
    role: PlaybackDiagnosticsNodesItemRole
    captured_at: typing_extensions.Annotated[
        float, FieldMetadata(alias="capturedAt"), pydantic.Field(alias="capturedAt")
    ]
    started_at: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ] = None
    enabled: bool
    active_requests: typing_extensions.Annotated[
        int, FieldMetadata(alias="activeRequests"), pydantic.Field(alias="activeRequests")
    ]
    requests: int
    output_bytes: typing_extensions.Annotated[
        float, FieldMetadata(alias="outputBytes"), pydantic.Field(alias="outputBytes")
    ]
    input_bytes: typing_extensions.Annotated[
        float, FieldMetadata(alias="inputBytes"), pydantic.Field(alias="inputBytes")
    ]
    errors: int
    streams: typing.List[PlaybackDiagnosticsNodesItemStreamsItem]
    sources: typing.List[PlaybackDiagnosticsNodesItemSourcesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
