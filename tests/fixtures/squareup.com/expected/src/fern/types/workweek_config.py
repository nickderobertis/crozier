

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WorkweekConfig(UniversalBaseModel):
    """
    Sets the day of the week and hour of the day that a business starts a
    workweek. This is used to calculate overtime pay.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A read-only timestamp in RFC 3339 format; presented in UTC.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UUID for this object.
    """

    start_of_day_local_time: str = pydantic.Field()
    """
    The local time at which a business week ends. Represented as a
    string in `HH:MM` format (`HH:MM:SS` is also accepted, but seconds are
    truncated).
    """

    start_of_week: str = pydantic.Field()
    """
    The day of the week on which a business week ends for
    compensation purposes.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A read-only timestamp in RFC 3339 format; presented in UTC.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Used for resolving concurrency issues. The request fails if the version
    provided does not match the server version at the time of the request. If not provided,
    Square executes a blind write; potentially overwriting data from another
    write.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
