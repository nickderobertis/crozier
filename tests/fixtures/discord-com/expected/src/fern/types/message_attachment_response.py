

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_response import ApplicationResponse
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class MessageAttachmentResponse(UniversalBaseModel):
    id: SnowflakeType
    filename: str
    size: int
    url: str
    proxy_url: str
    width: typing.Optional[int] = None
    height: typing.Optional[int] = None
    duration_secs: typing.Optional[float] = None
    waveform: typing.Optional[str] = None
    description: typing.Optional[str] = None
    content_type: typing.Optional[str] = None
    ephemeral: typing.Optional[bool] = None
    title: typing.Optional[str] = None
    application: typing.Optional[ApplicationResponse] = None
    clip_created_at: typing.Optional[dt.datetime] = None
    clip_participants: typing.Optional[typing.List[UserResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
