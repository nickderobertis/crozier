

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_type_weight_unit_label import DeviceTypeWeightUnitLabel
from .device_type_weight_unit_value import DeviceTypeWeightUnitValue


class DeviceTypeWeightUnit(UniversalBaseModel):
    label: DeviceTypeWeightUnitLabel
    value: DeviceTypeWeightUnitValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
