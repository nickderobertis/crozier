

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .calibrate_sensor_response_verdict import CalibrateSensorResponseVerdict


class CalibrateSensorResponse(UniversalBaseModel):
    verdict: typing.Optional[CalibrateSensorResponseVerdict] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
