

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .presentation_override_content_type import PresentationOverrideContentType


class PresentationOverride(UniversalBaseModel):
    id: str
    content_type: typing_extensions.Annotated[
        PresentationOverrideContentType, FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType")
    ]
    content_id: typing_extensions.Annotated[str, FieldMetadata(alias="contentId"), pydantic.Field(alias="contentId")]
    content_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="contentName"), pydantic.Field(alias="contentName")
    ]
    started_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ]
    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ] = None
    playlist_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="playlistId"), pydantic.Field(alias="playlistId")
    ] = None
    layout_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="layoutId"), pydantic.Field(alias="layoutId")
    ] = None
    wake_display: typing_extensions.Annotated[
        bool, FieldMetadata(alias="wakeDisplay"), pydantic.Field(alias="wakeDisplay")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
