

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .composite_signature import CompositeSignature
from .signed_bundle_v2signature_hash_alg import SignedBundleV2SignatureHashAlg
from .signed_bundle_v2signature_signer import SignedBundleV2SignatureSigner


class SignedBundleV2Signature(UniversalBaseModel):
    hash_alg: typing.Optional[SignedBundleV2SignatureHashAlg] = None
    created_at: typing.Optional[dt.datetime] = None
    signer: typing.Optional[SignedBundleV2SignatureSigner] = None
    manifest_hash: typing.Optional[str] = None
    composite_sig: CompositeSignature

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
