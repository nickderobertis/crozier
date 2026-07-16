

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_status_label import DeviceStatusLabel
from .device_status_value import DeviceStatusValue


class DeviceStatus(UniversalBaseModel):
    label: DeviceStatusLabel
    value: DeviceStatusValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
