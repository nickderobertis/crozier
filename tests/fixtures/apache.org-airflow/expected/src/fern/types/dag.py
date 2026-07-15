

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .schedule_interval import ScheduleInterval
from .tag import Tag


class Dag(UniversalBaseModel):
    """
    DAG
    """

    dag_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the DAG.
    """

    default_view: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default view of the DAG inside the webserver
    
    *New in version 2.3.0*
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    User-provided DAG description, which can consist of several sentences or paragraphs that describe DAG contents.
    """

    file_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change.
    """

    fileloc: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute path to the file.
    """

    has_import_errors: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the DAG has import errors
    
    *New in version 2.3.0*
    """

    has_task_concurrency_limits: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the DAG has task concurrency limits
    
    *New in version 2.3.0*
    """

    is_active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the DAG is currently seen by the scheduler(s).
    
    *New in version 2.1.1*
    
    *Changed in version 2.2.0*&#58; Field is read-only.
    """

    is_paused: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the DAG is paused.
    """

    is_subdag: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the DAG is SubDAG.
    """

    last_expired: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Time when the DAG last received a refresh signal
    (e.g. the DAG's "refresh" button was clicked in the web UI)
    
    *New in version 2.3.0*
    """

    last_parsed_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last time the DAG was parsed.
    
    *New in version 2.3.0*
    """

    last_pickled: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last time the DAG was pickled.
    
    *New in version 2.3.0*
    """

    max_active_runs: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of active DAG runs for the DAG
    
    *New in version 2.3.0*
    """

    max_active_tasks: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of active tasks that can be run on the DAG
    
    *New in version 2.3.0*
    """

    next_dagrun: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The logical date of the next dag run.
    
    *New in version 2.3.0*
    """

    next_dagrun_create_after: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Earliest time at which this ``next_dagrun`` can be created.
    
    *New in version 2.3.0*
    """

    next_dagrun_data_interval_end: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The end of the interval of the next dag run.
    
    *New in version 2.3.0*
    """

    next_dagrun_data_interval_start: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The start of the interval of the next dag run.
    
    *New in version 2.3.0*
    """

    owners: typing.Optional[typing.List[str]] = None
    pickle_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Foreign key to the latest pickle_id
    
    *New in version 2.3.0*
    """

    root_dag_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    If the DAG is SubDAG then it is the top level DAG identifier. Otherwise, null.
    """

    schedule_interval: typing.Optional[ScheduleInterval] = None
    scheduler_lock: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether (one of) the scheduler is scheduling this DAG at the moment
    
    *New in version 2.3.0*
    """

    tags: typing.Optional[typing.List[Tag]] = pydantic.Field(default=None)
    """
    List of tags.
    """

    timetable_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timetable/Schedule Interval description.
    
    *New in version 2.3.0*
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
