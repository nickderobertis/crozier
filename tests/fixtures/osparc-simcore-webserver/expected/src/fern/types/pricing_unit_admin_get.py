

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hardware_info import HardwareInfo
from .pricing_unit_admin_get_unit_extra_info import PricingUnitAdminGetUnitExtraInfo


class PricingUnitAdminGet(UniversalBaseModel):
    pricing_unit_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="pricingUnitId"), pydantic.Field(alias="pricingUnitId")
    ]
    unit_name: typing_extensions.Annotated[str, FieldMetadata(alias="unitName"), pydantic.Field(alias="unitName")]
    unit_extra_info: typing_extensions.Annotated[
        PricingUnitAdminGetUnitExtraInfo, FieldMetadata(alias="unitExtraInfo"), pydantic.Field(alias="unitExtraInfo")
    ]
    current_cost_per_unit: typing_extensions.Annotated[
        str, FieldMetadata(alias="currentCostPerUnit"), pydantic.Field(alias="currentCostPerUnit")
    ]
    default: bool
    specific_info: typing_extensions.Annotated[
        HardwareInfo, FieldMetadata(alias="specificInfo"), pydantic.Field(alias="specificInfo")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
