

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_row_component_response import ActionRowComponentResponse
from .message_attachment_response import MessageAttachmentResponse
from .message_embed_response import MessageEmbedResponse
from .message_sticker_item_response import MessageStickerItemResponse
from .message_type import MessageType
from .minimal_content_message_response_stickers_item import MinimalContentMessageResponseStickersItem
from .resolved_objects_response import ResolvedObjectsResponse
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class MinimalContentMessageResponse(UniversalBaseModel):
    type: MessageType
    content: str
    mentions: typing.List[UserResponse]
    mention_roles: typing.List[SnowflakeType]
    attachments: typing.List[MessageAttachmentResponse]
    embeds: typing.List[MessageEmbedResponse]
    timestamp: dt.datetime
    edited_timestamp: typing.Optional[dt.datetime] = None
    flags: int
    components: typing.List[ActionRowComponentResponse]
    resolved: typing.Optional[ResolvedObjectsResponse] = None
    stickers: typing.Optional[typing.List[MinimalContentMessageResponseStickersItem]] = None
    sticker_items: typing.Optional[typing.List[MessageStickerItemResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
