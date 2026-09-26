

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1forecast_user_avatar import V1ForecastUserAvatar
from .v1forecast_user_estimated_duration import V1ForecastUserEstimatedDuration


class V1ForecastUser(UniversalBaseModel):
    """
    Primary user assigned to the task
    """

    id: typing.Optional[int] = None
    email: str
    name: str
    avatar: V1ForecastUserAvatar
    updated_at: typing.Optional[str] = None
    estimated_minutes: typing.Optional[int] = None
    estimated_duration: typing.Optional[V1ForecastUserEstimatedDuration] = None
    weekly_capacity: typing.Optional[float] = None
    work_days: typing.Optional[str] = None
    weekdays: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
