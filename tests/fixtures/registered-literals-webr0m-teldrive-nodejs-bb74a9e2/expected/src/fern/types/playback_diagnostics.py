

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .playback_diagnostics_file import PlaybackDiagnosticsFile
from .playback_diagnostics_metadata import PlaybackDiagnosticsMetadata
from .playback_diagnostics_nodes_item import PlaybackDiagnosticsNodesItem


class PlaybackDiagnostics(UniversalBaseModel):
    file: PlaybackDiagnosticsFile
    metadata: typing.Optional[PlaybackDiagnosticsMetadata] = None
    unavailable_nodes: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="unavailableNodes"), pydantic.Field(alias="unavailableNodes")
    ]
    nodes: typing.List[PlaybackDiagnosticsNodesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
