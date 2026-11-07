

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WorkflowScheduleUpsertRequest(UniversalBaseModel):
    cron_expression: typing.Optional[str] = None
    interval_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Fixed elapsed interval between runs, in seconds. Mutually exclusive with cron_expression.
    """

    first_fire_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    First run of an interval schedule; later runs follow every interval_seconds from it. Must be in the future when changed. Defaults to one interval after creation.
    """

    timezone: str
    enabled: typing.Optional[bool] = None
    parameters: typing.Optional[typing.Dict[str, typing.Any]] = None
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
