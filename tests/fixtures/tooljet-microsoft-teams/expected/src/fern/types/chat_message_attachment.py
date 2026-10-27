

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChatMessageAttachment(UniversalBaseModel):
    id: typing.Optional[str] = None
    content_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType")
    ] = None
    content_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentUrl"), pydantic.Field(alias="contentUrl")
    ] = None
    content: typing.Optional[str] = None
    name: typing.Optional[str] = None
    thumbnail_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="thumbnailUrl"), pydantic.Field(alias="thumbnailUrl")
    ] = None
    teams_app_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="teamsAppId"), pydantic.Field(alias="teamsAppId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
