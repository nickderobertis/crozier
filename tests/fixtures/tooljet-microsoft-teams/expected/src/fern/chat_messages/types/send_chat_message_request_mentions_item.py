

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .send_chat_message_request_mentions_item_mentioned import SendChatMessageRequestMentionsItemMentioned


class SendChatMessageRequestMentionsItem(UniversalBaseModel):
    id: typing.Optional[int] = None
    mention_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mentionText"), pydantic.Field(alias="mentionText")
    ] = None
    mentioned: typing.Optional[SendChatMessageRequestMentionsItemMentioned] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
