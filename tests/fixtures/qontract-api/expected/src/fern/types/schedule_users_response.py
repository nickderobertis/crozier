

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pager_duty_user import PagerDutyUser


class ScheduleUsersResponse(UniversalBaseModel):
    """
    Response model for schedule users endpoint.

    Immutable response containing list of users currently on-call in a schedule.

    Attributes:
        users: List of users currently on-call
    """

    users: typing.Optional[typing.List[PagerDutyUser]] = pydantic.Field(default=None)
    """
    List of users currently on-call in the schedule
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
