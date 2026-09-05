

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .u_int32type import UInt32Type


class MessageEmbedImageResponse(UniversalBaseModel):
    url: typing.Optional[str] = None
    proxy_url: typing.Optional[str] = None
    width: typing.Optional[UInt32Type] = None
    height: typing.Optional[UInt32Type] = None
    placeholder: typing.Optional[str] = None
    placeholder_version: typing.Optional[UInt32Type] = None
    flags: typing.Optional[UInt32Type] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
