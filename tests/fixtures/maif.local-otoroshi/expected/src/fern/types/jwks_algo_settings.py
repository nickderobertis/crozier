

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JwksAlgoSettings(UniversalBaseModel):
    """
    Settings for a JWK set
    """

    headers: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The headers for the http call
    """

    kty: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of key: RSA or EC
    """

    timeout: typing.Optional[int] = pydantic.Field(default=None)
    """
    The timeout of the http call
    """

    ttl: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ttl of the keyset
    """

    type: str = pydantic.Field()
    """
    String with value JWKSAlgoSettings
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The url for the http call
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
