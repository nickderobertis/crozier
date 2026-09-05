

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PricingPlanToServiceAdminGet(UniversalBaseModel):
    pricing_plan_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="pricingPlanId"), pydantic.Field(alias="pricingPlanId")
    ]
    service_key: typing_extensions.Annotated[str, FieldMetadata(alias="serviceKey"), pydantic.Field(alias="serviceKey")]
    service_version: typing_extensions.Annotated[
        str, FieldMetadata(alias="serviceVersion"), pydantic.Field(alias="serviceVersion")
    ]
    created: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
