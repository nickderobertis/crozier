

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_signing_key_body_private_jwk_ec_alg import CreateSigningKeyBodyPrivateJwkEcAlg
from .create_signing_key_body_private_jwk_ec_crv import CreateSigningKeyBodyPrivateJwkEcCrv
from .create_signing_key_body_private_jwk_ec_key_ops_item import CreateSigningKeyBodyPrivateJwkEcKeyOpsItem
from .create_signing_key_body_private_jwk_ec_use import CreateSigningKeyBodyPrivateJwkEcUse


class CreateSigningKeyBodyPrivateJwkEc(UniversalBaseModel):
    kid: typing.Optional[str] = None
    use: typing.Optional[CreateSigningKeyBodyPrivateJwkEcUse] = None
    key_ops: typing.Optional[typing.List[CreateSigningKeyBodyPrivateJwkEcKeyOpsItem]] = None
    ext: typing.Optional[bool] = None
    alg: typing.Optional[CreateSigningKeyBodyPrivateJwkEcAlg] = None
    crv: CreateSigningKeyBodyPrivateJwkEcCrv
    x: str
    y: str
    d: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
