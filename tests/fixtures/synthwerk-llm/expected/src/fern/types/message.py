

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_role import MessageRole
from .message_status import MessageStatus


class Message(UniversalBaseModel):
    id: str
    role: MessageRole
    content: str = pydantic.Field()
    """
    Plain text. Never HTML.
    """

    status: MessageStatus
    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
