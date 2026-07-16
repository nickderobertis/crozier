

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rack_weight_unit_label import RackWeightUnitLabel
from .rack_weight_unit_value import RackWeightUnitValue


class RackWeightUnit(UniversalBaseModel):
    label: RackWeightUnitLabel
    value: RackWeightUnitValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
