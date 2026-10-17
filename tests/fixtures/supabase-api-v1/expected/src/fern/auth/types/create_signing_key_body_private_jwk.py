

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_signing_key_body_private_jwk_ec_alg import CreateSigningKeyBodyPrivateJwkEcAlg
from .create_signing_key_body_private_jwk_ec_crv import CreateSigningKeyBodyPrivateJwkEcCrv
from .create_signing_key_body_private_jwk_ec_key_ops_item import CreateSigningKeyBodyPrivateJwkEcKeyOpsItem
from .create_signing_key_body_private_jwk_ec_use import CreateSigningKeyBodyPrivateJwkEcUse
from .create_signing_key_body_private_jwk_oct_alg import CreateSigningKeyBodyPrivateJwkOctAlg
from .create_signing_key_body_private_jwk_oct_key_ops_item import CreateSigningKeyBodyPrivateJwkOctKeyOpsItem
from .create_signing_key_body_private_jwk_oct_use import CreateSigningKeyBodyPrivateJwkOctUse
from .create_signing_key_body_private_jwk_okp_alg import CreateSigningKeyBodyPrivateJwkOkpAlg
from .create_signing_key_body_private_jwk_okp_crv import CreateSigningKeyBodyPrivateJwkOkpCrv
from .create_signing_key_body_private_jwk_okp_key_ops_item import CreateSigningKeyBodyPrivateJwkOkpKeyOpsItem
from .create_signing_key_body_private_jwk_okp_use import CreateSigningKeyBodyPrivateJwkOkpUse
from .create_signing_key_body_private_jwk_rsa_alg import CreateSigningKeyBodyPrivateJwkRsaAlg
from .create_signing_key_body_private_jwk_rsa_e import CreateSigningKeyBodyPrivateJwkRsaE
from .create_signing_key_body_private_jwk_rsa_key_ops_item import CreateSigningKeyBodyPrivateJwkRsaKeyOpsItem
from .create_signing_key_body_private_jwk_rsa_use import CreateSigningKeyBodyPrivateJwkRsaUse


class CreateSigningKeyBodyPrivateJwk_Rsa(UniversalBaseModel):
    kty: typing.Literal["RSA"] = "RSA"
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


class CreateSigningKeyBodyPrivateJwk_Ec(UniversalBaseModel):
    kty: typing.Literal["EC"] = "EC"
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


class CreateSigningKeyBodyPrivateJwk_Okp(UniversalBaseModel):
    kty: typing.Literal["OKP"] = "OKP"
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


class CreateSigningKeyBodyPrivateJwk_Oct(UniversalBaseModel):
    kty: typing.Literal["oct"] = "oct"
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


CreateSigningKeyBodyPrivateJwk = typing_extensions.Annotated[
    typing.Union[
        CreateSigningKeyBodyPrivateJwk_Rsa,
        CreateSigningKeyBodyPrivateJwk_Ec,
        CreateSigningKeyBodyPrivateJwk_Okp,
        CreateSigningKeyBodyPrivateJwk_Oct,
    ],
    pydantic.Field(discriminator="kty"),
]
