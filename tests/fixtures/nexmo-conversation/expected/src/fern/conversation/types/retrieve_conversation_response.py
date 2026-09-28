

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.conversation_id import ConversationId
from ...types.display_name import DisplayName
from ...types.links_conversation import LinksConversation
from ...types.name_conversation import NameConversation
from ...types.timestamp_res_conversation import TimestampResConversation
from .retrieve_conversation_response_members_item import RetrieveConversationResponseMembersItem
from .retrieve_conversation_response_numbers import RetrieveConversationResponseNumbers
from .retrieve_conversation_response_properties import RetrieveConversationResponseProperties


class RetrieveConversationResponse(UniversalBaseModel):
    """
    Conversation Object
    """

    links: typing_extensions.Annotated[
        typing.Optional[LinksConversation], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")
    ] = None
    api_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The API key for your account
    """

    display_name: typing.Optional[DisplayName] = None
    members: typing.Optional[typing.List[RetrieveConversationResponseMembersItem]] = pydantic.Field(default=None)
    """
    Users associated to this conversation as members
    """

    name: typing.Optional[NameConversation] = None
    numbers: typing.Optional[RetrieveConversationResponseNumbers] = None
    properties: typing.Optional[RetrieveConversationResponseProperties] = None
    sequence_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last Event ID in this conversation. This ID can be used to [retrieve a specific event](#getEvent)
    """

    timestamp: typing.Optional[TimestampResConversation] = None
    uuid_: typing_extensions.Annotated[ConversationId, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
