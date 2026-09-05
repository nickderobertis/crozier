

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pricing_unit_get_unit_extra_info import PricingUnitGetUnitExtraInfo


class PricingUnitGet(UniversalBaseModel):
    pricing_unit_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="pricingUnitId"), pydantic.Field(alias="pricingUnitId")
    ]
    unit_name: typing_extensions.Annotated[str, FieldMetadata(alias="unitName"), pydantic.Field(alias="unitName")]
    unit_extra_info: typing_extensions.Annotated[
        PricingUnitGetUnitExtraInfo, FieldMetadata(alias="unitExtraInfo"), pydantic.Field(alias="unitExtraInfo")
    ]
    current_cost_per_unit: typing_extensions.Annotated[
        str, FieldMetadata(alias="currentCostPerUnit"), pydantic.Field(alias="currentCostPerUnit")
    ]
    default: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
