

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pricing_unit_cost_update_cost_per_unit import PricingUnitCostUpdateCostPerUnit


class PricingUnitCostUpdate(UniversalBaseModel):
    cost_per_unit: PricingUnitCostUpdateCostPerUnit
    comment: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
