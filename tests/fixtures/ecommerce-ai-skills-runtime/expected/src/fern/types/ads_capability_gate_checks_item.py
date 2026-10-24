

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ads_capability_gate_checks_item_name import AdsCapabilityGateChecksItemName
from .ads_capability_gate_checks_item_status import AdsCapabilityGateChecksItemStatus


class AdsCapabilityGateChecksItem(UniversalBaseModel):
    name: AdsCapabilityGateChecksItemName
    status: AdsCapabilityGateChecksItemStatus
    detail: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
