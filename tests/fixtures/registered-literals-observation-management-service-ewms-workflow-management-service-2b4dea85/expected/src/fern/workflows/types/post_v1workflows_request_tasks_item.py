

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v1workflows_request_tasks_item_pilot_config import PostV1WorkflowsRequestTasksItemPilotConfig
from .post_v1workflows_request_tasks_item_worker_config import PostV1WorkflowsRequestTasksItemWorkerConfig


class PostV1WorkflowsRequestTasksItem(UniversalBaseModel):
    cluster_locations: typing.List[str] = pydantic.Field()
    """
    The HTCondor pool(s) where the taskforce(s) will run.
    """

    task_image: str = pydantic.Field()
    """
    The Docker/Singularity/Apptainer image to run for each event. Apptainer images in directory (sandbox) format will start fastest; other formats will first be converted to this format on each worker CPU.
    """

    task_args: str = pydantic.Field()
    """
    The argument string to pass to the task image.
    """

    task_env: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Environment variables (and values) to set in the task instance.
    """

    init_image: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Docker/Singularity/Apptainer image for the init container. See 'task_image' for caveats/optimizations regarding the image format.
    """

    init_args: typing.Optional[str] = pydantic.Field(default=None)
    """
    The argument string to pass to the init container.
    """

    init_env: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Environment variables (and values) to set in the init container.
    """

    input_queue_aliases: typing.List[str] = pydantic.Field()
    """
    User-defined aliases for input event queues. Globally-unique IDs for the queues will be generated after submission.
    """

    output_queue_aliases: typing.List[str] = pydantic.Field()
    """
    User-defined aliases for output event queues. Globally-unique IDs for the queues will be generated after submission.
    """

    pilot_config: typing.Optional[PostV1WorkflowsRequestTasksItemPilotConfig] = pydantic.Field(default=None)
    """
    Configuration settings for the EWMS pilot.
    """

    worker_config: PostV1WorkflowsRequestTasksItemWorkerConfig = pydantic.Field()
    """
    Configuration settings for the HTCondor cluster submission.
    """

    n_workers: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of workers in this taskforce's HTCondor cluster (immutable).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
