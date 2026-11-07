

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_device_health_log_response_health_log_item import GetDeviceHealthLogResponseHealthLogItem


class GetDeviceHealthLogResponse(UniversalBaseModel):
    health_log: typing.List[GetDeviceHealthLogResponseHealthLogItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
