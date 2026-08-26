

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VisitingWindow(UniversalBaseModel):
    """
    The period during which the vehicle intends to use the road network. Traffic signs with a time validity that does not overlap this period are not taken into account. The period is evaluated in the Europe/Amsterdam time zone, because the time validity of a traffic sign is expressed in Dutch local time. When omitted, every traffic sign with a time validity is treated as always applicable. The period may not be longer than 24 hours and end may not be before start.
    """

    start: dt.datetime = pydantic.Field()
    """
    Start of the period, inclusive.
    """

    end: dt.datetime = pydantic.Field()
    """
    End of the period, inclusive. May be equal to start to evaluate a single moment in time.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
