

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_type import MessageType
from .message_user import MessageUser


class Message(UniversalBaseModel):
    id: typing.Optional[int] = None
    user_id: typing.Optional[int] = None
    type: typing.Optional[MessageType] = None
    content: typing.Optional[str] = None
    file_path: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    user: typing.Optional[MessageUser] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
