

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType


class MessageAttachmentRequest(UniversalBaseModel):
    id: SnowflakeType
    filename: typing.Optional[str] = None
    description: typing.Optional[str] = None
    duration_secs: typing.Optional[float] = None
    waveform: typing.Optional[str] = None
    title: typing.Optional[str] = None
    is_remix: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
