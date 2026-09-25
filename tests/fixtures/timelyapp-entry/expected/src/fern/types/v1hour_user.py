

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1hour_user_avatar import V1HourUserAvatar


class V1HourUser(UniversalBaseModel):
    """
    User who logged this time
    """

    id: int
    email: str
    name: str
    avatar: V1HourUserAvatar
    active: typing.Optional[bool] = None
    day_view_onboarded: typing.Optional[bool] = None
    memory_onboarded: typing.Optional[bool] = None
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None
    last_received_memories_date: typing.Optional[dt.datetime] = None
    sign_in_count: typing.Optional[int] = None
    external_id: typing.Optional[str] = None
    time_zone: typing.Optional[str] = None
    memory_retention_days: typing.Optional[int] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
