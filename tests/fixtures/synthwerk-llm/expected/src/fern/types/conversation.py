

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message import Message
from .model_alias import ModelAlias


class Conversation(UniversalBaseModel):
    id: str
    model: ModelAlias
    created_at: dt.datetime
    messages: typing.List[Message] = pydantic.Field()
    """
    Messages, oldest first.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
