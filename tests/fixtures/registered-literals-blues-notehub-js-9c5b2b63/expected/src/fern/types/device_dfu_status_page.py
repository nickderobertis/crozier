

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_dfu_status import DeviceDfuStatus


class DeviceDfuStatusPage(UniversalBaseModel):
    devices: typing.Optional[typing.List[DeviceDfuStatus]] = None
    has_more: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
