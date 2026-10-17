

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_signing_key_body_private_jwk_rsa_alg import CreateSigningKeyBodyPrivateJwkRsaAlg
from .create_signing_key_body_private_jwk_rsa_e import CreateSigningKeyBodyPrivateJwkRsaE
from .create_signing_key_body_private_jwk_rsa_key_ops_item import CreateSigningKeyBodyPrivateJwkRsaKeyOpsItem
from .create_signing_key_body_private_jwk_rsa_use import CreateSigningKeyBodyPrivateJwkRsaUse


class CreateSigningKeyBodyPrivateJwkRsa(UniversalBaseModel):
    kid: typing.Optional[str] = None
    use: typing.Optional[CreateSigningKeyBodyPrivateJwkRsaUse] = None
    key_ops: typing.Optional[typing.List[CreateSigningKeyBodyPrivateJwkRsaKeyOpsItem]] = None
    ext: typing.Optional[bool] = None
    alg: typing.Optional[CreateSigningKeyBodyPrivateJwkRsaAlg] = None
    n: str
    e: CreateSigningKeyBodyPrivateJwkRsaE
    d: str
    p: str
    q: str
    dp: str
    dq: str
    qi: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
