

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .authentication_provider_provider import AuthenticationProviderProvider
from .authentication_provider_supported_authentication_methods_item import (
    AuthenticationProviderSupportedAuthenticationMethodsItem,
)


class AuthenticationProvider(UniversalBaseModel):
    provider: AuthenticationProviderProvider
    merchant_id: str
    supported_authentication_methods: typing.List[AuthenticationProviderSupportedAuthenticationMethodsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
