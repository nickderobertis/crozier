

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rack_outer_unit_label import RackOuterUnitLabel
from .rack_outer_unit_value import RackOuterUnitValue


class RackOuterUnit(UniversalBaseModel):
    label: RackOuterUnitLabel
    value: RackOuterUnitValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
