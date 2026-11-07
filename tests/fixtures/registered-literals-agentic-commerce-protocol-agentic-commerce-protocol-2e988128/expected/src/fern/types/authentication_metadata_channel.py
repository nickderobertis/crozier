

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .authentication_metadata_channel_browser import AuthenticationMetadataChannelBrowser
from .authentication_metadata_channel_type import AuthenticationMetadataChannelType


class AuthenticationMetadataChannel(UniversalBaseModel):
    """
    Details about the channel used for this 3DS Authentication.
    """

    type: AuthenticationMetadataChannelType = pydantic.Field()
    """
    Use "browser" to indicate the transaction originated from a browser.
    """

    browser: AuthenticationMetadataChannelBrowser = pydantic.Field()
    """
    Browser details collected server- or client-side.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
