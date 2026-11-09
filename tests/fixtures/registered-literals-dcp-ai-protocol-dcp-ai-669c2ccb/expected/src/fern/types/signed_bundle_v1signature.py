

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .signed_bundle_v1signature_alg import SignedBundleV1SignatureAlg
from .signed_bundle_v1signature_signer import SignedBundleV1SignatureSigner


class SignedBundleV1Signature(UniversalBaseModel):
    alg: SignedBundleV1SignatureAlg
    created_at: dt.datetime
    signer: SignedBundleV1SignatureSigner
    bundle_hash: str
    merkle_root: typing.Optional[str] = None
    sig_b64: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
