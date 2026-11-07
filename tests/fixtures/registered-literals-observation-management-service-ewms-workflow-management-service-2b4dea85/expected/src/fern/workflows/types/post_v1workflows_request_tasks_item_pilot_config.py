

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v1workflows_request_tasks_item_pilot_config_environment_value import (
    PostV1WorkflowsRequestTasksItemPilotConfigEnvironmentValue,
)
from .post_v1workflows_request_tasks_item_pilot_config_image_source import (
    PostV1WorkflowsRequestTasksItemPilotConfigImageSource,
)


class PostV1WorkflowsRequestTasksItemPilotConfig(UniversalBaseModel):
    """
    Configuration settings for the EWMS pilot.
    """

    tag: str = pydantic.Field()
    """
    The image tag to use (e.g., '#.#.#', 'latest', or a feature branch tag). Note: tags like # or #.# are disallowed since these are mutable. This field is useful for repeatability.
    """

    image_source: PostV1WorkflowsRequestTasksItemPilotConfigImageSource = pydantic.Field()
    """
    The canonical source name for the image.
    """

    environment: typing.Dict[str, PostV1WorkflowsRequestTasksItemPilotConfigEnvironmentValue] = pydantic.Field()
    """
    Environment variables and their corresponding values.
    """

    input_files: typing.List[str] = pydantic.Field()
    """
    Paths to files to make available to the task container. These files must already be accessible on the AP.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
