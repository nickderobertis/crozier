

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jwk_alg import JwkAlg
from .jwk_crv import JwkCrv
from .jwk_kty import JwkKty
from .jwk_use import JwkUse


class Jwk(UniversalBaseModel):
    kty: JwkKty = pydantic.Field()
    """
    Key type
    """

    use: JwkUse = pydantic.Field()
    """
    Key use
    """

    alg: JwkAlg = pydantic.Field()
    """
    Algorithm
    """

    kid: str = pydantic.Field()
    """
    Key identifier
    """

    n: typing.Optional[str] = pydantic.Field(default=None)
    """
    RSA modulus
    """

    e: typing.Optional[str] = pydantic.Field(default=None)
    """
    RSA public exponent
    """

    crv: typing.Optional[JwkCrv] = pydantic.Field(default=None)
    """
    Elliptic curve
    """

    x: typing.Optional[str] = pydantic.Field(default=None)
    """
    EC/OKP x coordinate
    """

    y: typing.Optional[str] = pydantic.Field(default=None)
    """
    EC y coordinate
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
