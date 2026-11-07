

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .auth_configuration_google import AuthConfigurationGoogle
from .record_string_never import RecordStringNever


class AuthConfiguration(UniversalBaseModel):
    """
    Configure [player authentication](https://hathora.dev/docs/lobbies-and-matchmaking/auth-service) for your application. Use Hathora's built-in auth providers or use your own [custom authentication](https://hathora.dev/docs/lobbies-and-matchmaking/auth-service#custom-auth-provider).
    """

    google: typing.Optional[AuthConfigurationGoogle] = pydantic.Field(default=None)
    """
    Enable google auth for your application.
    """

    nickname: typing.Optional[RecordStringNever] = pydantic.Field(default=None)
    """
    Enable nickname auth for your application.
    """

    anonymous: typing.Optional[RecordStringNever] = pydantic.Field(default=None)
    """
    Enable anonymous auth for your application.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
