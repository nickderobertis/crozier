

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .taskforce_object_phase import TaskforceObjectPhase
from .taskforce_object_phase_change_log_item import TaskforceObjectPhaseChangeLogItem
from .taskforce_object_pilot_config import TaskforceObjectPilotConfig
from .taskforce_object_submit_dict_value import TaskforceObjectSubmitDictValue
from .taskforce_object_worker_config import TaskforceObjectWorkerConfig


class TaskforceObject(UniversalBaseModel):
    """
    Taskforce object. See https://observation-management-service.github.io/ewms-docs/services/wms.html#taskforce.
    """

    taskforce_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier automatically generated for this taskforce.
    """

    task_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the associated task directive object (N taskforces : 1 task directive).
    """

    workflow_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the overarching workflow object (N*M taskforces : M task directives : 1 workflow).
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    The epoch time when this taskforce was created.
    """

    priority: typing.Optional[int] = pydantic.Field(default=None)
    """
    The priority level relative to other taskforces (usually, this value is inherited from the parent workflow object).
    """

    collector: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated. Address of the HTCondor collector; no longer used.
    """

    schedd: typing.Optional[str] = pydantic.Field(default=None)
    """
    The address of the HTCondor schedd.
    """

    n_workers: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of workers in this taskforce's HTCondor cluster (immutable).
    """

    pilot_config: typing.Optional[TaskforceObjectPilotConfig] = pydantic.Field(default=None)
    """
    Configuration settings for the EWMS pilot.
    """

    worker_config: typing.Optional[TaskforceObjectWorkerConfig] = pydantic.Field(default=None)
    """
    Configuration settings for the HTCondor cluster submission.
    """

    cluster_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The identifier for the associated HTCondor cluster.
    """

    submit_dict: typing.Optional[typing.Dict[str, TaskforceObjectSubmitDictValue]] = pydantic.Field(default=None)
    """
    The actual HTCondor submit class ad.
    """

    job_event_log_fpath: typing.Optional[str] = pydantic.Field(default=None)
    """
    The file path on the HTCondor AP containing job event logs.
    """

    phase: typing.Optional[TaskforceObjectPhase] = pydantic.Field(default=None)
    """
    The current phase of the taskforce within the workflow's lifetime. Not all taskforces will enter every phase.
    """

    phase_change_log: typing.Optional[typing.List[TaskforceObjectPhaseChangeLogItem]] = pydantic.Field(default=None)
    """
    A record of all attempted phase changes, including both successful and unsuccessful ones.
    """

    compound_statuses: typing.Optional[typing.Dict[str, typing.Dict[str, int]]] = pydantic.Field(default=None)
    """
    Aggregated status of the workers, represented as a nested dictionary mapping HTCondor states to EWMS pilot states and their counts.
    """

    top_task_errors: typing.Optional[typing.Dict[str, int]] = pydantic.Field(default=None)
    """
    The most common errors encountered by workers, paired with their occurrence counts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
