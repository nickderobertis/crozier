

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V2LogStatsTimeBounds(UniversalBaseModel):
    """
    Actual bucket window. Supplied bounds are exact. Without `startDate`, the left edge is the oldest match, or 24 hours before the right edge when no run matches. Without `endDate`, the right edge is at least now. `startDate` alone spans through now.
    """

    start: dt.datetime = pydantic.Field()
    """
    ISO 8601 start of the window.
    """

    end: dt.datetime = pydantic.Field()
    """
    ISO 8601 end of the window.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
