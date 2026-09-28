

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feature_flags_patch_response_enabled import FeatureFlagsPatchResponseEnabled


class FeatureFlagsPatchResponse(UniversalBaseModel):
    key: str
    enabled: FeatureFlagsPatchResponseEnabled

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
