

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tracker_period import TrackerPeriod


class TrackerRoom(UniversalBaseModel):
    """
    Tracker Room.
    """

    room_id: str = pydantic.Field()
    """
    Room id.
    """

    room_name: str
    room_capacity: typing.Optional[int] = None
    staff_ratio: str
    room_age_low: typing.Optional[float] = None
    room_age_high: typing.Optional[float] = None
    periods: typing.Optional[typing.List[TrackerPeriod]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
