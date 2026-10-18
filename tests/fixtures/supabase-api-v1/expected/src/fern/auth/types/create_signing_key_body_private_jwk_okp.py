

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_signing_key_body_private_jwk_okp_alg import CreateSigningKeyBodyPrivateJwkOkpAlg
from .create_signing_key_body_private_jwk_okp_crv import CreateSigningKeyBodyPrivateJwkOkpCrv
from .create_signing_key_body_private_jwk_okp_key_ops_item import CreateSigningKeyBodyPrivateJwkOkpKeyOpsItem
from .create_signing_key_body_private_jwk_okp_use import CreateSigningKeyBodyPrivateJwkOkpUse


class CreateSigningKeyBodyPrivateJwkOkp(UniversalBaseModel):
    kid: typing.Optional[str] = None
    use: typing.Optional[CreateSigningKeyBodyPrivateJwkOkpUse] = None
    key_ops: typing.Optional[typing.List[CreateSigningKeyBodyPrivateJwkOkpKeyOpsItem]] = None
    ext: typing.Optional[bool] = None
    alg: typing.Optional[CreateSigningKeyBodyPrivateJwkOkpAlg] = None
    crv: CreateSigningKeyBodyPrivateJwkOkpCrv
    x: str
    d: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
