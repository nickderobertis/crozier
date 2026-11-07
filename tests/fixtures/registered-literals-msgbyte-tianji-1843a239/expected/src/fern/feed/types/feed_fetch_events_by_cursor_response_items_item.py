

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class FeedFetchEventsByCursorResponseItemsItem(UniversalBaseModel):
    id: str
    channel_id: typing_extensions.Annotated[str, FieldMetadata(alias="channelId"), pydantic.Field(alias="channelId")]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    event_name: typing_extensions.Annotated[str, FieldMetadata(alias="eventName"), pydantic.Field(alias="eventName")]
    event_content: typing_extensions.Annotated[
        str, FieldMetadata(alias="eventContent"), pydantic.Field(alias="eventContent")
    ]
    tags: typing.List[str]
    source: str
    sender_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="senderId"), pydantic.Field(alias="senderId")
    ] = None
    sender_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="senderName"), pydantic.Field(alias="senderName")
    ] = None
    url: typing.Optional[str] = None
    important: bool
    archived: bool
    payload: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
