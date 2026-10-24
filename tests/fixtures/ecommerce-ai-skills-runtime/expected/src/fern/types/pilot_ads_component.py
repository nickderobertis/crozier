

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pilot_ads_component_reason_code import PilotAdsComponentReasonCode
from .pilot_ads_component_status import PilotAdsComponentStatus


class PilotAdsComponent(UniversalBaseModel):
    required: bool
    status: PilotAdsComponentStatus
    reason_code: typing.Optional[PilotAdsComponentReasonCode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
