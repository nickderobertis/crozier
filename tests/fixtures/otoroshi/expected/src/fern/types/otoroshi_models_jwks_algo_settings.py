

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_jwks_algo_settings_proxy import OtoroshiModelsJwksAlgoSettingsProxy
from .otoroshi_models_jwks_algo_settings_type import OtoroshiModelsJwksAlgoSettingsType


class OtoroshiModelsJwksAlgoSettings(UniversalBaseModel):
    """
    Settings to use keypair from JWKS for verification
    """

    type: typing.Optional[OtoroshiModelsJwksAlgoSettingsType] = pydantic.Field(default=None)
    """
    the kind of algosettings
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    JWKS url
    """

    tls_config: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="tlsConfig"), pydantic.Field(alias="tlsConfig")
    ] = None
    kty: typing.Optional[str] = pydantic.Field(default=None)
    """
    Key type
    """

    proxy: typing.Optional[OtoroshiModelsJwksAlgoSettingsProxy] = pydantic.Field(default=None)
    """
    Web proxy for http client
    """

    headers: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Http header when fetching JWKS
    """

    ttl: typing.Optional[float] = pydantic.Field(default=None)
    """
    Cache ttl
    """

    timeout: typing.Optional[float] = pydantic.Field(default=None)
    """
    Timeout when fetching JWKS
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
