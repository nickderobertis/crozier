

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pricing_plan_classification import PricingPlanClassification
from .pricing_unit_get import PricingUnitGet


class PricingPlanGet(UniversalBaseModel):
    pricing_plan_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="pricingPlanId"), pydantic.Field(alias="pricingPlanId")
    ]
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    description: str
    classification: PricingPlanClassification
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    pricing_plan_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="pricingPlanKey"), pydantic.Field(alias="pricingPlanKey")
    ]
    pricing_units: typing_extensions.Annotated[
        typing.Optional[typing.List[PricingUnitGet]],
        FieldMetadata(alias="pricingUnits"),
        pydantic.Field(alias="pricingUnits"),
    ] = None
    is_active: typing_extensions.Annotated[bool, FieldMetadata(alias="isActive"), pydantic.Field(alias="isActive")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
