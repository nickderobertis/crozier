

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AuthenticationMetadataChannelBrowser(UniversalBaseModel):
    accept_header: str
    ip_address: str
    javascript_enabled: bool
    language: str
    user_agent: str
    color_depth: typing.Optional[int] = None
    java_enabled: typing.Optional[bool] = None
    screen_height: typing.Optional[int] = None
    screen_width: typing.Optional[int] = None
    timezone_offset: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
