

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .session_source_schedule_type import SessionSourceScheduleType


class SessionSourceSchedule(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Schedule id.
    """

    run_id: str = pydantic.Field()
    """
    Schedule run id.
    """

    type: SessionSourceScheduleType = pydantic.Field()
    """
    Session was created by a schedule run.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
