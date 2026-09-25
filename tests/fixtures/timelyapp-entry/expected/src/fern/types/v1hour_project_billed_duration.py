

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1HourProjectBilledDuration(UniversalBaseModel):
    hours: typing.Optional[int] = None
    minutes: typing.Optional[int] = None
    seconds: typing.Optional[int] = None
    formatted: typing.Optional[str] = None
    total_hours: typing.Optional[float] = None
    total_seconds: typing.Optional[int] = None
    total_minutes: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
