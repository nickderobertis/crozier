

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chat_chat_type import ChatChatType
from .chat_installed_apps_item import ChatInstalledAppsItem
from .chat_last_message_preview import ChatLastMessagePreview
from .chat_online_meeting_info import ChatOnlineMeetingInfo
from .chat_viewpoint import ChatViewpoint
from .conversation_member import ConversationMember


class Chat(UniversalBaseModel):
    odata_context: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="@odata.context"), pydantic.Field(alias="@odata.context")
    ] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the chat
    """

    topic: typing.Optional[str] = pydantic.Field(default=None)
    """
    Subject or topic for the chat (optional)
    """

    created_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdDateTime"),
        pydantic.Field(alias="createdDateTime", description="Date and time when the chat was created"),
    ] = None
    """
    Date and time when the chat was created
    """

    last_updated_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUpdatedDateTime"),
        pydantic.Field(alias="lastUpdatedDateTime", description="Date and time when the chat was last updated"),
    ] = None
    """
    Date and time when the chat was last updated
    """

    chat_type: typing_extensions.Annotated[
        typing.Optional[ChatChatType],
        FieldMetadata(alias="chatType"),
        pydantic.Field(alias="chatType", description="Type of chat"),
    ] = None
    """
    Type of chat
    """

    web_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="webUrl"),
        pydantic.Field(alias="webUrl", description="A hyperlink to the chat in Microsoft Teams"),
    ] = None
    """
    A hyperlink to the chat in Microsoft Teams
    """

    tenant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tenantId"),
        pydantic.Field(alias="tenantId", description="The identifier of the tenant"),
    ] = None
    """
    The identifier of the tenant
    """

    online_meeting_info: typing_extensions.Annotated[
        typing.Optional[ChatOnlineMeetingInfo],
        FieldMetadata(alias="onlineMeetingInfo"),
        pydantic.Field(alias="onlineMeetingInfo"),
    ] = None
    viewpoint: typing.Optional[ChatViewpoint] = None
    members: typing.Optional[typing.List[ConversationMember]] = None
    installed_apps: typing_extensions.Annotated[
        typing.Optional[typing.List[ChatInstalledAppsItem]],
        FieldMetadata(alias="installedApps"),
        pydantic.Field(alias="installedApps"),
    ] = None
    last_message_preview: typing_extensions.Annotated[
        typing.Optional[ChatLastMessagePreview],
        FieldMetadata(alias="lastMessagePreview"),
        pydantic.Field(alias="lastMessagePreview"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
