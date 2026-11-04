

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .system_info_device import SystemInfoDevice
from .system_info_meter import SystemInfoMeter
from .system_info_wifi import SystemInfoWifi


class SystemInfo(UniversalBaseModel):
    device: typing.Optional[SystemInfoDevice] = None
    meter: typing.Optional[SystemInfoMeter] = None
    wifi: typing.Optional[SystemInfoWifi] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
