

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ads_capability_gate import AdsCapabilityGate


class GetV1AdsCapabilityGatesResponse(UniversalBaseModel):
    ads_capability_gates: typing.List[AdsCapabilityGate]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
