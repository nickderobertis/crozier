

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.conversation_id import ConversationId
from ...types.display_name import DisplayName
from ...types.href import Href
from ...types.image_url import ImageUrl
from ...types.member_id import MemberId
from ...types.member_state import MemberState
from ...types.name_conversation import NameConversation
from .getuser_conversations_response_item_timestamp import GetuserConversationsResponseItemTimestamp


class GetuserConversationsResponseItem(UniversalBaseModel):
    display_name: typing.Optional[DisplayName] = None
    href: typing.Optional[Href] = None
    id: typing.Optional[ConversationId] = None
    image_url: typing.Optional[ImageUrl] = None
    member_id: typing.Optional[MemberId] = None
    name: typing.Optional[NameConversation] = None
    sequence_number: typing.Optional[int] = pydantic.Field(default=None)
    """
    the id of the last event of the conversation (event's id is an incremental number
    """

    state: typing.Optional[MemberState] = None
    timestamp: typing.Optional[GetuserConversationsResponseItemTimestamp] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
