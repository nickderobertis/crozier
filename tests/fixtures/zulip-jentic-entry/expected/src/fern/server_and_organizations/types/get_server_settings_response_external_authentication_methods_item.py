

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetServerSettingsResponseExternalAuthenticationMethodsItem(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique, table, machine-readable name for the authentication method,
    intended to be used by clients with special behavior for specific
    authentication methods to correctly identify the method.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display name of the authentication method, to be used in all buttons
    for the authentication method.
    """

    display_icon: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL for an image to be displayed as an icon in all buttons for
    the external authentication method. This URL should be resolved
    relative to the server's base URL.
    
    When `null`, no icon should be displayed.
    """

    login_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to be used to initiate authentication using this method.
    """

    signup_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to be used to initiate account registration using this method.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
