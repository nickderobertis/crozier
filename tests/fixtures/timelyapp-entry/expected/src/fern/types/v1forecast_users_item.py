

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1forecast_users_item_avatar import V1ForecastUsersItemAvatar
from .v1forecast_users_item_estimated_duration import V1ForecastUsersItemEstimatedDuration


class V1ForecastUsersItem(UniversalBaseModel):
    id: typing.Optional[int] = None
    email: str
    name: str
    avatar: V1ForecastUsersItemAvatar
    updated_at: typing.Optional[str] = None
    estimated_minutes: typing.Optional[int] = None
    estimated_duration: typing.Optional[V1ForecastUsersItemEstimatedDuration] = None
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
