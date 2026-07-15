

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .job import Job
from .sla_miss import SlaMiss
from .task_state import TaskState
from .trigger import Trigger


class TaskInstance(UniversalBaseModel):
    dag_id: typing.Optional[str] = None
    dag_run_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DagRun ID for this task instance
    
    *New in version 2.3.0*
    """

    duration: typing.Optional[float] = None
    end_date: typing.Optional[str] = None
    execution_date: typing.Optional[str] = None
    executor_config: typing.Optional[str] = None
    hostname: typing.Optional[str] = None
    map_index: typing.Optional[int] = None
    max_tries: typing.Optional[int] = None
    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    Contains manually entered notes by the user about the TaskInstance.
    
    *New in version 2.5.0*
    """

    operator: typing.Optional[str] = pydantic.Field(default=None)
    """
    *Changed in version 2.1.1*&#58; Field becomes nullable.
    """

    pid: typing.Optional[int] = None
    pool: typing.Optional[str] = None
    pool_slots: typing.Optional[int] = None
    priority_weight: typing.Optional[int] = None
    queue: typing.Optional[str] = None
    queued_when: typing.Optional[str] = None
    rendered_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    JSON object describing rendered fields.
    
    *New in version 2.3.0*
    """

    sla_miss: typing.Optional[SlaMiss] = None
    start_date: typing.Optional[str] = None
    state: typing.Optional[TaskState] = None
    task_id: typing.Optional[str] = None
    trigger: typing.Optional[Trigger] = None
    triggerer_job: typing.Optional[Job] = None
    try_number: typing.Optional[int] = None
    unixname: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
