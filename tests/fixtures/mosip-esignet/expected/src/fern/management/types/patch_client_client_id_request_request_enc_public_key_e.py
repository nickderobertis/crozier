

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_client_client_id_request_request_enc_public_key_e_alg import (
    PatchClientClientIdRequestRequestEncPublicKeyEAlg,
)
from .patch_client_client_id_request_request_enc_public_key_e_kty import (
    PatchClientClientIdRequestRequestEncPublicKeyEKty,
)
from .patch_client_client_id_request_request_enc_public_key_e_use import (
    PatchClientClientIdRequestRequestEncPublicKeyEUse,
)
from .patch_client_client_id_request_request_enc_public_key_ee import PatchClientClientIdRequestRequestEncPublicKeyEe


class PatchClientClientIdRequestRequestEncPublicKeyE(UniversalBaseModel):
    """
    RSA public key for encryption
    """

    kty: PatchClientClientIdRequestRequestEncPublicKeyEKty = pydantic.Field()
    """
    Key type (RSA)
    """

    n: str = pydantic.Field()
    """
    RSA modulus (Base64URL encoded)
    """

    e: PatchClientClientIdRequestRequestEncPublicKeyEe = pydantic.Field()
    """
    RSA exponent
    """

    use: typing.Optional[PatchClientClientIdRequestRequestEncPublicKeyEUse] = pydantic.Field(default=None)
    """
    Key use (enc for encryption)
    """

    alg: typing.Optional[PatchClientClientIdRequestRequestEncPublicKeyEAlg] = pydantic.Field(default=None)
    """
    Algorithm for key management
    """

    kid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Key ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
