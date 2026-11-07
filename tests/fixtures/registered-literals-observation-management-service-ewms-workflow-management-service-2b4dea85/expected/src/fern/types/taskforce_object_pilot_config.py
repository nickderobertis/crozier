

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .taskforce_object_pilot_config_environment_value import TaskforceObjectPilotConfigEnvironmentValue
from .taskforce_object_pilot_config_image_source import TaskforceObjectPilotConfigImageSource


class TaskforceObjectPilotConfig(UniversalBaseModel):
    """
    Configuration settings for the EWMS pilot.
    """

    tag: str = pydantic.Field()
    """
    The image tag to use (e.g., '#.#.#', 'latest', or a feature branch tag). Note: tags like # or #.# are disallowed since these are mutable. This field is useful for repeatability.
    """

    image_source: TaskforceObjectPilotConfigImageSource = pydantic.Field()
    """
    The canonical source name for the image.
    """

    environment: typing.Dict[str, TaskforceObjectPilotConfigEnvironmentValue] = pydantic.Field()
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
