

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pricing_plan_to_service_admin_get import PricingPlanToServiceAdminGet


class EnvelopePricingPlanToServiceAdminGet(UniversalBaseModel):
    data: typing.Optional[PricingPlanToServiceAdminGet] = None
    error: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
