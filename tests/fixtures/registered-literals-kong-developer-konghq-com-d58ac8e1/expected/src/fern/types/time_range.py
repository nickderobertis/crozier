

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metrics_relative_time_range_dto_v2time_range import MetricsRelativeTimeRangeDtoV2TimeRange


class TimeRange_Relative(UniversalBaseModel):
    """
    The time range to query.
    """

    type: typing.Literal["relative"] = "relative"
    tz: typing.Optional[str] = None
    time_range: MetricsRelativeTimeRangeDtoV2TimeRange

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TimeRange_Absolute(UniversalBaseModel):
    """
    The time range to query.
    """

    type: typing.Literal["absolute"] = "absolute"
    tz: typing.Optional[str] = None
    start: typing.Optional[dt.datetime] = None
    end: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TimeRange = typing_extensions.Annotated[
    typing.Union[TimeRange_Relative, TimeRange_Absolute], pydantic.Field(discriminator="type")
]
