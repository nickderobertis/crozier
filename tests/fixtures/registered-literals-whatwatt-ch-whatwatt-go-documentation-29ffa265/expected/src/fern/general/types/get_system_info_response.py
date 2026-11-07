

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_system_info_response_device import GetSystemInfoResponseDevice
from .get_system_info_response_meter import GetSystemInfoResponseMeter
from .get_system_info_response_wifi import GetSystemInfoResponseWifi


class GetSystemInfoResponse(UniversalBaseModel):
    device: typing.Optional[GetSystemInfoResponseDevice] = None
    meter: typing.Optional[GetSystemInfoResponseMeter] = None
    wifi: typing.Optional[GetSystemInfoResponseWifi] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
