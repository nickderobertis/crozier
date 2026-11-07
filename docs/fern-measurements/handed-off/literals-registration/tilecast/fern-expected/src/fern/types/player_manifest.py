

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .manifest_schedule import ManifestSchedule
from .player_manifest_canvas import PlayerManifestCanvas
from .player_manifest_mode import PlayerManifestMode
from .player_manifest_viewport import PlayerManifestViewport
from .presentation_override import PresentationOverride


class PlayerManifest(UniversalBaseModel):
    schema_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="schemaVersion"), pydantic.Field(alias="schemaVersion")
    ]
    manifest_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="manifestVersion"), pydantic.Field(alias="manifestVersion")
    ]
    screen_id: typing_extensions.Annotated[str, FieldMetadata(alias="screenId"), pydantic.Field(alias="screenId")]
    generated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="generatedAt"), pydantic.Field(alias="generatedAt")
    ]
    mode: PlayerManifestMode
    playlist: typing.Optional[typing.Dict[str, typing.Any]] = None
    layout: typing.Optional[typing.Dict[str, typing.Any]] = None
    layouts: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    assets: typing.List[typing.Dict[str, typing.Any]]
    canvas: typing.Optional[PlayerManifestCanvas] = None
    viewport: typing.Optional[PlayerManifestViewport] = None
    schedules: typing.Optional[typing.List[ManifestSchedule]] = None
    widgets: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    data_sources: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="dataSources"),
        pydantic.Field(alias="dataSources"),
    ] = None
    presentation_override: typing_extensions.Annotated[
        typing.Optional[PresentationOverride],
        FieldMetadata(alias="presentationOverride"),
        pydantic.Field(alias="presentationOverride"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
