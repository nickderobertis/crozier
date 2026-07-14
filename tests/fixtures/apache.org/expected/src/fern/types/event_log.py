

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EventLog(UniversalBaseModel):
    """
    Log of user operations via CLI or Web UI.
    """

    dag_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DAG ID
    """

    event: typing.Optional[str] = pydantic.Field(default=None)
    """
    A key describing the type of event.
    """

    event_log_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The event log ID
    """

    execution_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the event was dispatched for an object having execution_date, the value of this field.
    """

    extra: typing.Optional[str] = pydantic.Field(default=None)
    """
    Other information that was not included in the other fields, e.g. the complete CLI command.
    """

    owner: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the user who triggered these events a.
    """

    task_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DAG ID
    """

    when: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when these events happened.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
