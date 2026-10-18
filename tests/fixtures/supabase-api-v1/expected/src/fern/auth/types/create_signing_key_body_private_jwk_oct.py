

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_signing_key_body_private_jwk_oct_alg import CreateSigningKeyBodyPrivateJwkOctAlg
from .create_signing_key_body_private_jwk_oct_key_ops_item import CreateSigningKeyBodyPrivateJwkOctKeyOpsItem
from .create_signing_key_body_private_jwk_oct_use import CreateSigningKeyBodyPrivateJwkOctUse


class CreateSigningKeyBodyPrivateJwkOct(UniversalBaseModel):
    kid: typing.Optional[str] = None
    use: typing.Optional[CreateSigningKeyBodyPrivateJwkOctUse] = None
    key_ops: typing.Optional[typing.List[CreateSigningKeyBodyPrivateJwkOctKeyOpsItem]] = None
    ext: typing.Optional[bool] = None
    alg: typing.Optional[CreateSigningKeyBodyPrivateJwkOctAlg] = None
    k: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
