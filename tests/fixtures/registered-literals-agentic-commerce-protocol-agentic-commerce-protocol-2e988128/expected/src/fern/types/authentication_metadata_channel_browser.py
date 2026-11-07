

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AuthenticationMetadataChannelBrowser(UniversalBaseModel):
    """
    Browser details collected server- or client-side.
    """

    accept_header: str = pydantic.Field()
    """
    The HTTP Accept header from the cardholder’s browser.
    """

    ip_address: str = pydantic.Field()
    """
    The IP address of the browser.
    """

    javascript_enabled: bool = pydantic.Field()
    """
    Whether the cardholder browser can execute JavaScript.
    """

    language: str = pydantic.Field()
    """
    An IETF BCP 47 language tag representing the browser language.
    """

    user_agent: str = pydantic.Field()
    """
    The browser user agent string.
    """

    color_depth: typing.Optional[int] = pydantic.Field(default=None)
    """
    The screen color depth. Required if javascript_enabled is true.
    """

    java_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Browser Java support. Required if javascript_enabled is true.
    """

    screen_height: typing.Optional[int] = pydantic.Field(default=None)
    """
    Screen height in pixels. Required if javascript_enabled is true.
    """

    screen_width: typing.Optional[int] = pydantic.Field(default=None)
    """
    Screen width in pixels. Required if javascript_enabled is true.
    """

    timezone_offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time difference in minutes between UTC and the browser local time. Required if javascript_enabled is true.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
