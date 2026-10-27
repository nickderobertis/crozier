

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_message_reactions_item_user_user import ChatMessageReactionsItemUserUser


class ChatMessageReactionsItemUser(UniversalBaseModel):
    application: typing.Optional[typing.Dict[str, typing.Any]] = None
    device: typing.Optional[typing.Dict[str, typing.Any]] = None
    user: typing.Optional[ChatMessageReactionsItemUserUser] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
