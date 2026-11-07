

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .capability_payment_requirement_handlers_item import CapabilityPaymentRequirementHandlersItem
from .capability_payment_requirement_mode import CapabilityPaymentRequirementMode


class CapabilityPaymentRequirement(UniversalBaseModel):
    mode: CapabilityPaymentRequirementMode
    handlers: typing.List[CapabilityPaymentRequirementHandlersItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
