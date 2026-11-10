

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JwkPublicKey(UniversalBaseModel):
    """
    A JSON Web Key (JWK) that can be used in conjunction with [JWT libraries](https://jwt.io/#libraries-io) to verify Plaid webhooks
    """

    alg: str = pydantic.Field()
    """
    The alg member identifies the cryptographic algorithm family used with the key.
    """

    created_at: int = pydantic.Field()
    """
    The timestamp when the key was created, in Unix time.
    """

    crv: str = pydantic.Field()
    """
    The crv member identifies the cryptographic curve used with the key.
    """

    expired_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The timestamp when the key expired, in Unix time.
    """

    kid: str = pydantic.Field()
    """
    The kid (Key ID) member can be used to match a specific key. This can be used, for instance, to choose among a set of keys within the JWK during key rollover.
    """

    kty: str = pydantic.Field()
    """
    The kty (key type) parameter identifies the cryptographic algorithm family used with the key, such as RSA or EC.
    """

    use: str = pydantic.Field()
    """
    The use (public key use) parameter identifies the intended use of the public key.
    """

    x: str = pydantic.Field()
    """
    The x member contains the x coordinate for the elliptic curve point, provided as a base64url-encoded string of the coordinate's big endian representation.
    """

    y: str = pydantic.Field()
    """
    The y member contains the y coordinate for the elliptic curve point, provided as a base64url-encoded string of the coordinate's big endian representation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
