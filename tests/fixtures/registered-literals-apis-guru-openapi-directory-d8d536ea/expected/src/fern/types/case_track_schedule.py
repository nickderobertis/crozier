

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .case_track_schedule_type import CaseTrackScheduleType


class CaseTrackSchedule(UniversalBaseModel):
    days: typing.List[int] = pydantic.Field()
    """
    [] -> if schedule type is daily <br>
    1-7 -> if schedule type is weekly <br>
    1-31 -> if schedule type is monthly
    """

    type: CaseTrackScheduleType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
