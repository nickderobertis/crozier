

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .playback_diagnostics_nodes_item_sources_item_kind import PlaybackDiagnosticsNodesItemSourcesItemKind


class PlaybackDiagnosticsNodesItemSourcesItem(UniversalBaseModel):
    id: str
    kind: PlaybackDiagnosticsNodesItemSourcesItemKind
    bot_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="botId"), pydantic.Field(alias="botId")
    ] = None
    name: typing.Optional[str] = None
    username: typing.Optional[str] = None
    active: int
    attempts: int
    failures: int
    input_bytes: typing_extensions.Annotated[
        float, FieldMetadata(alias="inputBytes"), pydantic.Field(alias="inputBytes")
    ]
    forwarded_bytes: typing_extensions.Annotated[
        float, FieldMetadata(alias="forwardedBytes"), pydantic.Field(alias="forwardedBytes")
    ]
    bytes_per_second: typing_extensions.Annotated[
        float, FieldMetadata(alias="bytesPerSecond"), pydantic.Field(alias="bytesPerSecond")
    ]
    last_byte_at: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lastByteAt"), pydantic.Field(alias="lastByteAt")
    ] = None
    active_reads: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="activeReads"), pydantic.Field(alias="activeReads")
    ] = None
    peak_reads: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="peakReads"), pydantic.Field(alias="peakReads")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
