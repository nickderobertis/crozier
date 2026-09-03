

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_certs_response_keys_item_kty import GetCertsResponseKeysItemKty
from .get_certs_response_keys_item_use import GetCertsResponseKeysItemUse


class GetCertsResponseKeysItem(UniversalBaseModel):
    kid: str = pydantic.Field()
    """
    The certificate's Key ID
    """

    use: GetCertsResponseKeysItemUse = pydantic.Field()
    """
    How the Key is used. Valid value: sig
    """

    kty: GetCertsResponseKeysItemKty = pydantic.Field()
    """
    Cryptographic algorithm family for the certificate's Key pair. Valid value: RSA
    """

    e: str = pydantic.Field()
    """
    RSA Key value (exponent) for Key blinding
    """

    n: str = pydantic.Field()
    """
    RSA modulus value
    """

    x5t_s256: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="x5t#S256"),
        pydantic.Field(alias="x5t#S256", description="SHA-256 thumbprint of the certificate."),
    ]
    """
    SHA-256 thumbprint of the certificate.
    """

    x5c: typing.List[str] = pydantic.Field()
    """
    Certificate to validate the Oauth server trust.
    """

    exp: dt.datetime = pydantic.Field()
    """
    Expire datetime of the key. Given in ISO format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
