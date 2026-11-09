

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .citizenship_bundle_v2 import CitizenshipBundleV2
from .signed_bundle_v2signature import SignedBundleV2Signature


class SignedBundleV2(UniversalBaseModel):
    bundle: CitizenshipBundleV2
    signature: SignedBundleV2Signature

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
