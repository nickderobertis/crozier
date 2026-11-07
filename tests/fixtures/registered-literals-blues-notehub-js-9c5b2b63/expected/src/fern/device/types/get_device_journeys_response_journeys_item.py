

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetDeviceJourneysResponseJourneysItem(UniversalBaseModel):
    end_date: dt.datetime = pydantic.Field()
    """
    Latest event time within the journey.
    """

    journey_id: int = pydantic.Field()
    """
    Identifier of the journey, taken from the numeric `journey` field in the event body. This value is itself a Unix timestamp marking the start of the journey.
    """

    start_date: dt.datetime = pydantic.Field()
    """
    Earliest event time within the journey.
    """

    total_events: int = pydantic.Field()
    """
    The number of events in the journey.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
