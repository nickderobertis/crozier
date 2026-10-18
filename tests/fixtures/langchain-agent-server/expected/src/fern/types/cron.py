

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Cron(UniversalBaseModel):
    """
    Represents a scheduled task.
    """

    cron_id: str = pydantic.Field()
    """
    The ID of the cron.
    """

    assistant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the assistant.
    """

    thread_id: str = pydantic.Field()
    """
    The ID of the thread.
    """

    end_time: dt.datetime = pydantic.Field()
    """
    The end date to stop running the cron.
    """

    schedule: str = pydantic.Field()
    """
    The schedule to run, cron format.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The time the cron was created.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    The last time the cron was updated.
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the user.
    """

    payload: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The run payload to use for creating new run.
    """

    next_run_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The next run date of the cron.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The cron metadata.
    """

    enabled: bool = pydantic.Field()
    """
    Whether the cron job should be enabled. Disabled crons are not executed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
