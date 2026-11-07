

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .signed_bundle_v1signature_signer_type import SignedBundleV1SignatureSignerType


class SignedBundleV1SignatureSigner(UniversalBaseModel):
    type: typing.Optional[SignedBundleV1SignatureSignerType] = None
    id: typing.Optional[str] = None
    public_key_b64: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
