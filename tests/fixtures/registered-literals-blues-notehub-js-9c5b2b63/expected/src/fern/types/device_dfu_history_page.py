

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_dfu_history import DeviceDfuHistory


class DeviceDfuHistoryPage(UniversalBaseModel):
    devices: typing.Optional[typing.List[DeviceDfuHistory]] = None
    has_more: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
