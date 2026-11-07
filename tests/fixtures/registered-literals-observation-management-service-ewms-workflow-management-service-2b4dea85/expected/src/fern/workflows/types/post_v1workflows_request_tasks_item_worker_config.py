

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v1workflows_request_tasks_item_worker_config_worker_disk import (
    PostV1WorkflowsRequestTasksItemWorkerConfigWorkerDisk,
)
from .post_v1workflows_request_tasks_item_worker_config_worker_memory import (
    PostV1WorkflowsRequestTasksItemWorkerConfigWorkerMemory,
)


class PostV1WorkflowsRequestTasksItemWorkerConfig(UniversalBaseModel):
    """
    Configuration settings for the HTCondor cluster submission.
    """

    do_transfer_worker_stdouterr: bool = pydantic.Field()
    """
    Indicates whether to transfer back the workers' stdout and stderr (accessible on the AP).
    """

    max_worker_runtime: int = pydantic.Field()
    """
    The maximum runtime for a worker. Adjust this to optimize performance (e.g., to terminate slow CPUs).
    """

    n_cores: int = pydantic.Field()
    """
    The number of cores to request per HTCondor worker.
    """

    priority: int = pydantic.Field()
    """
    The priority level for the HTCondor submission.
    """

    worker_disk: PostV1WorkflowsRequestTasksItemWorkerConfigWorkerDisk
    worker_memory: PostV1WorkflowsRequestTasksItemWorkerConfigWorkerMemory
    condor_requirements: str = pydantic.Field()
    """
    The 'requirements' string given to the HTCondor submission.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
