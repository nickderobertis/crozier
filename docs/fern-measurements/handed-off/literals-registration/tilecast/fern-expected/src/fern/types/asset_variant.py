

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .variant_kind import VariantKind


class AssetVariant(UniversalBaseModel):
    id: str
    kind: VariantKind
    mime_type: typing_extensions.Annotated[str, FieldMetadata(alias="mimeType"), pydantic.Field(alias="mimeType")]
    file_size: typing_extensions.Annotated[int, FieldMetadata(alias="fileSize"), pydantic.Field(alias="fileSize")]
    sha256: str
    width: typing.Optional[int] = None
    height: typing.Optional[int] = None
    duration_seconds: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="durationSeconds"), pydantic.Field(alias="durationSeconds")
    ] = None
    frame_rate: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="frameRate"), pydantic.Field(alias="frameRate")
    ] = None
    video_codec: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoCodec"), pydantic.Field(alias="videoCodec")
    ] = None
    audio_codec: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="audioCodec"), pydantic.Field(alias="audioCodec")
    ] = None
    player_compatible: typing_extensions.Annotated[
        bool, FieldMetadata(alias="playerCompatible"), pydantic.Field(alias="playerCompatible")
    ]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
