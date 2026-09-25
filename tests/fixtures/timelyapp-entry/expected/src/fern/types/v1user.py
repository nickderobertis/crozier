

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1user_avatar import V1UserAvatar
from .v1user_role import V1UserRole


class V1User(UniversalBaseModel):
    id: int
    email: str
    name: str
    active: bool
    day_view_onboarded: bool
    memory_onboarded: bool
    created_at: int = pydantic.Field()
    """
    The time represented as a Unix timestamp (epoch) (seconds since January 1, 1970)
    """

    updated_at: int = pydantic.Field()
    """
    The time represented as a Unix timestamp (epoch) (seconds since January 1, 1970)
    """

    last_received_memories_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    ISO8601
    """

    sign_in_count: typing.Optional[int] = None
    external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Can be used to reference external resource IDs to Timely resources
    """

    time_zone: str
    memory_retention_days: typing.Optional[int] = None
    type: str
    avatar: V1UserAvatar
    work_days: typing.Optional[str] = pydantic.Field(default=None)
    """
    Coma separated working days. Example: *'SUN,MON,TUE,WED,THU,FRI,SAT'*
    """

    weekdays: typing.Optional[str] = pydantic.Field(default=None)
    """
    Coma separated working days. Example: *'SU,MO,TU,WE,TH,FR,SA'*
    """

    weekly_capacity: typing.Optional[float] = pydantic.Field(default=None)
    """
    Specifies the user's weekly hour capacity. The default is account's weekly capacity. Can only have a decimal place of .5 (e.g. 3.5 hours)
    """

    active_projects_count: typing.Optional[int] = None
    user_level: typing.Optional[str] = pydantic.Field(default=None)
    """
    Describes user access level like **admin**, **manager**, **employee** or **team_lead**
    """

    admin: typing.Optional[bool] = None
    hide_hourly_rate: typing.Optional[bool] = None
    hide_internal_hourly_rate: typing.Optional[bool] = None
    deleted: typing.Optional[bool] = None
    default_hour_rate: typing.Optional[float] = None
    internal_hour_rate: typing.Optional[float] = None
    role_id: typing.Optional[int] = None
    role: typing.Optional[V1UserRole] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
