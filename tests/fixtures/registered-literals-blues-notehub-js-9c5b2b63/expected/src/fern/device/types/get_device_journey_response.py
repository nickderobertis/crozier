

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_device_journey_response_journey import GetDeviceJourneyResponseJourney


class GetDeviceJourneyResponse(UniversalBaseModel):
    end_date: dt.datetime = pydantic.Field()
    """
    Latest event time within the journey.
    """

    journey: GetDeviceJourneyResponseJourney = pydantic.Field()
    """
    Paginated events for the journey.
    """

    journey_id: int = pydantic.Field()
    """
    Identifier of the journey.
    """

    start_date: dt.datetime = pydantic.Field()
    """
    Earliest event time within the journey.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
