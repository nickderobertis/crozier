

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tracker_student import TrackerStudent


class TrackerSpace(UniversalBaseModel):
    """
    Tracker Space.
    """

    slot: int
    is_first_available: bool
    is_on_room_capacity: bool
    student: typing.Optional[TrackerStudent] = None
    space_status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
