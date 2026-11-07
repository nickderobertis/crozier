

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .citizenship_bundle_v1 import CitizenshipBundleV1
from .signed_bundle_v1signature import SignedBundleV1Signature


class SignedBundleV1(UniversalBaseModel):
    bundle: CitizenshipBundleV1
    signature: SignedBundleV1Signature

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
