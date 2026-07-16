

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_type_subdevice_role_label import DeviceTypeSubdeviceRoleLabel
from .device_type_subdevice_role_value import DeviceTypeSubdeviceRoleValue


class DeviceTypeSubdeviceRole(UniversalBaseModel):
    label: DeviceTypeSubdeviceRoleLabel
    value: DeviceTypeSubdeviceRoleValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
