

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .container_state import ContainerState


class DockerContainerInspect(UniversalBaseModel):
    container_state: ContainerState = pydantic.Field()
    """
    current state of container
    """

    name: str = pydantic.Field()
    """
    docker name of the container
    """

    id: str = pydantic.Field()
    """
    docker id of the container
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
