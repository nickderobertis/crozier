

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_client_client_id_request_request_enc_public_key_crv_alg import (
    PatchClientClientIdRequestRequestEncPublicKeyCrvAlg,
)
from .patch_client_client_id_request_request_enc_public_key_crv_crv import (
    PatchClientClientIdRequestRequestEncPublicKeyCrvCrv,
)
from .patch_client_client_id_request_request_enc_public_key_crv_kty import (
    PatchClientClientIdRequestRequestEncPublicKeyCrvKty,
)
from .patch_client_client_id_request_request_enc_public_key_crv_use import (
    PatchClientClientIdRequestRequestEncPublicKeyCrvUse,
)


class PatchClientClientIdRequestRequestEncPublicKeyCrv(UniversalBaseModel):
    """
    Elliptic Curve public key for encryption
    """

    kty: PatchClientClientIdRequestRequestEncPublicKeyCrvKty = pydantic.Field()
    """
    Key type (EC)
    """

    crv: PatchClientClientIdRequestRequestEncPublicKeyCrvCrv = pydantic.Field()
    """
    Curve name
    """

    x: str = pydantic.Field()
    """
    X coordinate (Base64URL encoded)
    """

    y: str = pydantic.Field()
    """
    Y coordinate (Base64URL encoded)
    """

    use: typing.Optional[PatchClientClientIdRequestRequestEncPublicKeyCrvUse] = pydantic.Field(default=None)
    """
    Key use (enc for encryption)
    """

    alg: typing.Optional[PatchClientClientIdRequestRequestEncPublicKeyCrvAlg] = pydantic.Field(default=None)
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
