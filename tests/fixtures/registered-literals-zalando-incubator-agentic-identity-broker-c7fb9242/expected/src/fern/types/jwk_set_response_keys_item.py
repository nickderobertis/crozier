

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jwk_set_response_keys_item_use import JwkSetResponseKeysItemUse


class JwkSetResponseKeysItem(UniversalBaseModel):
    kty: str = pydantic.Field()
    """
    Key type (e.g., EC, RSA)
    """

    crv: typing.Optional[str] = pydantic.Field(default=None)
    """
    Curve name (for EC keys)
    """

    kid: str = pydantic.Field()
    """
    Key identifier
    """

    use: JwkSetResponseKeysItemUse = pydantic.Field()
    """
    Key usage (always "sig" for signing)
    """

    alg: str = pydantic.Field()
    """
    Algorithm (e.g., ES256, RS256)
    """

    x: typing.Optional[str] = pydantic.Field(default=None)
    """
    X coordinate (for EC keys, base64url-encoded)
    """

    y: typing.Optional[str] = pydantic.Field(default=None)
    """
    Y coordinate (for EC keys, base64url-encoded)
    """

    n: typing.Optional[str] = pydantic.Field(default=None)
    """
    Modulus (for RSA keys, base64url-encoded)
    """

    e: typing.Optional[str] = pydantic.Field(default=None)
    """
    Exponent (for RSA keys, base64url-encoded)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
