

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_with_config_context_status_label import DeviceWithConfigContextStatusLabel
from .device_with_config_context_status_value import DeviceWithConfigContextStatusValue


class DeviceWithConfigContextStatus(UniversalBaseModel):
    label: DeviceWithConfigContextStatusLabel
    value: DeviceWithConfigContextStatusValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
