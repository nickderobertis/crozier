

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tracker_room import TrackerRoom


class EnrollmentTracker(UniversalBaseModel):
    """
    Enrollment Tracker.
    """

    school_id: str = pydantic.Field()
    """
    School id.
    """

    school_name: str
    rooms: typing.Optional[typing.List[TrackerRoom]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
