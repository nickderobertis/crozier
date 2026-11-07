

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .authentication_metadata_channel_browser import AuthenticationMetadataChannelBrowser
from .authentication_metadata_channel_type import AuthenticationMetadataChannelType


class AuthenticationMetadataChannel(UniversalBaseModel):
    type: AuthenticationMetadataChannelType
    browser: AuthenticationMetadataChannelBrowser

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
