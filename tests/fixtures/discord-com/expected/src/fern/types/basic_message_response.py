

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_row_component_response import ActionRowComponentResponse
from .basic_application_response import BasicApplicationResponse
from .basic_message_response_interaction_metadata import BasicMessageResponseInteractionMetadata
from .basic_message_response_nonce import BasicMessageResponseNonce
from .basic_message_response_stickers_item import BasicMessageResponseStickersItem
from .message_activity_response import MessageActivityResponse
from .message_attachment_response import MessageAttachmentResponse
from .message_call_response import MessageCallResponse
from .message_embed_response import MessageEmbedResponse
from .message_interaction_response import MessageInteractionResponse
from .message_mention_channel_response import MessageMentionChannelResponse
from .message_reference_response import MessageReferenceResponse
from .message_role_subscription_data_response import MessageRoleSubscriptionDataResponse
from .message_snapshot_response import MessageSnapshotResponse
from .message_sticker_item_response import MessageStickerItemResponse
from .message_type import MessageType
from .poll_response import PollResponse
from .purchase_notification_response import PurchaseNotificationResponse
from .resolved_objects_response import ResolvedObjectsResponse
from .snowflake_type import SnowflakeType
from .thread_response import ThreadResponse
from .user_response import UserResponse


class BasicMessageResponse(UniversalBaseModel):
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
    stickers: typing.Optional[typing.List[BasicMessageResponseStickersItem]] = None
    sticker_items: typing.Optional[typing.List[MessageStickerItemResponse]] = None
    id: SnowflakeType
    channel_id: SnowflakeType
    author: UserResponse
    pinned: bool
    mention_everyone: bool
    tts: bool
    call: typing.Optional[MessageCallResponse] = None
    activity: typing.Optional[MessageActivityResponse] = None
    application: typing.Optional[BasicApplicationResponse] = None
    application_id: typing.Optional[SnowflakeType] = None
    interaction: typing.Optional[MessageInteractionResponse] = None
    nonce: typing.Optional[BasicMessageResponseNonce] = None
    webhook_id: typing.Optional[SnowflakeType] = None
    message_reference: typing.Optional[MessageReferenceResponse] = None
    thread: typing.Optional[ThreadResponse] = None
    mention_channels: typing.Optional[typing.List[typing.Optional[MessageMentionChannelResponse]]] = None
    role_subscription_data: typing.Optional[MessageRoleSubscriptionDataResponse] = None
    purchase_notification: typing.Optional[PurchaseNotificationResponse] = None
    position: typing.Optional[int] = None
    poll: typing.Optional[PollResponse] = None
    interaction_metadata: typing.Optional[BasicMessageResponseInteractionMetadata] = None
    message_snapshots: typing.Optional[typing.List[MessageSnapshotResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
