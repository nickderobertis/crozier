

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chat_message_attachment import ChatMessageAttachment
from .chat_message_body import ChatMessageBody
from .chat_message_channel_identity import ChatMessageChannelIdentity
from .chat_message_from import ChatMessageFrom
from .chat_message_hosted_contents_item import ChatMessageHostedContentsItem
from .chat_message_importance import ChatMessageImportance
from .chat_message_mentions_item import ChatMessageMentionsItem
from .chat_message_message_type import ChatMessageMessageType
from .chat_message_policy_violation import ChatMessagePolicyViolation
from .chat_message_reactions_item import ChatMessageReactionsItem


class ChatMessage(UniversalBaseModel):
    odata_context: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="@odata.context"), pydantic.Field(alias="@odata.context")
    ] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the message
    """

    reply_to_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="replyToId"),
        pydantic.Field(alias="replyToId", description="ID of the parent message"),
    ] = None
    """
    ID of the parent message
    """

    from_: typing_extensions.Annotated[
        typing.Optional[ChatMessageFrom], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    etag: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version of the message
    """

    message_type: typing_extensions.Annotated[
        typing.Optional[ChatMessageMessageType], FieldMetadata(alias="messageType"), pydantic.Field(alias="messageType")
    ] = None
    created_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdDateTime"), pydantic.Field(alias="createdDateTime")
    ] = None
    last_modified_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastModifiedDateTime"),
        pydantic.Field(alias="lastModifiedDateTime"),
    ] = None
    last_edited_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastEditedDateTime"),
        pydantic.Field(alias="lastEditedDateTime"),
    ] = None
    deleted_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="deletedDateTime"), pydantic.Field(alias="deletedDateTime")
    ] = None
    subject: typing.Optional[str] = None
    body: typing.Optional[ChatMessageBody] = None
    summary: typing.Optional[str] = None
    attachments: typing.Optional[typing.List[ChatMessageAttachment]] = None
    mentions: typing.Optional[typing.List[ChatMessageMentionsItem]] = None
    importance: typing.Optional[ChatMessageImportance] = None
    reactions: typing.Optional[typing.List[ChatMessageReactionsItem]] = None
    locale: typing.Optional[str] = None
    web_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="webUrl"), pydantic.Field(alias="webUrl")
    ] = None
    channel_identity: typing_extensions.Annotated[
        typing.Optional[ChatMessageChannelIdentity],
        FieldMetadata(alias="channelIdentity"),
        pydantic.Field(alias="channelIdentity"),
    ] = None
    policy_violation: typing_extensions.Annotated[
        typing.Optional[ChatMessagePolicyViolation],
        FieldMetadata(alias="policyViolation"),
        pydantic.Field(alias="policyViolation"),
    ] = None
    event_detail: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="eventDetail"),
        pydantic.Field(alias="eventDetail", description="Details of system event messages"),
    ] = None
    """
    Details of system event messages
    """

    chat_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="chatId"), pydantic.Field(alias="chatId")
    ] = None
    hosted_contents: typing_extensions.Annotated[
        typing.Optional[typing.List[ChatMessageHostedContentsItem]],
        FieldMetadata(alias="hostedContents"),
        pydantic.Field(alias="hostedContents"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
