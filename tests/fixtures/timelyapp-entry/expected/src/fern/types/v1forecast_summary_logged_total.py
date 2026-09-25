

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1ForecastSummaryLoggedTotal(UniversalBaseModel):
    """
    Total logged duration
    """

    hours: int
    minutes: int
    seconds: int
    formatted: str
    total_hours: float
    total_seconds: int
    total_minutes: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
