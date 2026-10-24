

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pilot_amazon_spapi_component_status import PilotAmazonSpapiComponentStatus


class PilotAmazonSpapiComponent(UniversalBaseModel):
    required: bool
    status: PilotAmazonSpapiComponentStatus
    account_count: int
    healthy_count: int
    fresh_healthy_count: int
    credential_ready_count: int
    health_max_age_seconds: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
