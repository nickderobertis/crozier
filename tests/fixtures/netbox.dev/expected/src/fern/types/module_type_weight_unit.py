

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .module_type_weight_unit_label import ModuleTypeWeightUnitLabel
from .module_type_weight_unit_value import ModuleTypeWeightUnitValue


class ModuleTypeWeightUnit(UniversalBaseModel):
    label: ModuleTypeWeightUnitLabel
    value: ModuleTypeWeightUnitValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
