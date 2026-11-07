

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .schedule_type import ScheduleType


class Schedule(UniversalBaseModel):
    days: typing.List[int] = pydantic.Field()
    """
    [] -> if schedule type is daily <br>
    1-7 -> if schedule type is weekly <br>
    1-31 -> if schedule type is monthly
    """

    object: str = pydantic.Field()
    """
    Name of the object.
    """

    type: ScheduleType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
