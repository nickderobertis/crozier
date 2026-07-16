

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cable_length_unit_label import CableLengthUnitLabel
from .cable_length_unit_value import CableLengthUnitValue


class CableLengthUnit(UniversalBaseModel):
    label: CableLengthUnitLabel
    value: CableLengthUnitValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
