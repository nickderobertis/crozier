

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskDirectiveObject(UniversalBaseModel):
    """
    Task directive object. See https://observation-management-service.github.io/ewms-docs/services/wms.html#task-directive.
    """

    task_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier automatically generated for this task.
    """

    workflow_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the overarching workflow object (M task directives : 1 workflow).
    """

    cluster_locations: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The HTCondor pool(s) where the taskforce(s) will run.
    """

    task_image: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Docker/Singularity/Apptainer image to run for each event. Apptainer images in directory (sandbox) format will start fastest; other formats will first be converted to this format on each worker CPU.
    """

    task_args: typing.Optional[str] = pydantic.Field(default=None)
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

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    The epoch time when this task was created.
    """

    input_queues: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The message queue(s) that this task will use for event input.
    """

    output_queues: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The message queue(s) that this task will use for event output.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
