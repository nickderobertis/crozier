

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .record_model_properties_hourly_rate_value import RecordModelPropertiesHourlyRateValue


class RecordModelPropertiesHourlyRate(UniversalBaseModel):
    type: typing.Optional[str] = None
    value: typing.Optional[RecordModelPropertiesHourlyRateValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
