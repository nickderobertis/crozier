

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChatMessage(UniversalBaseModel):
    id: typing.Optional[str] = None
    content: typing.Optional[str] = None
    sender: typing.Optional[typing.Dict[str, typing.Any]] = None
    channel: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
