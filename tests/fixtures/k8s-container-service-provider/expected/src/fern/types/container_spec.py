

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .container_image import ContainerImage
from .container_metadata import ContainerMetadata
from .container_network import ContainerNetwork
from .container_process import ContainerProcess
from .container_resources import ContainerResources
from .container_spec_service_type import ContainerSpecServiceType


class ContainerSpec(UniversalBaseModel):
    """
    Container specification with input fields for creating a container
    """

    service_type: ContainerSpecServiceType = pydantic.Field()
    """
    Service type identifier (must be "container")
    """

    metadata: ContainerMetadata
    image: ContainerImage
    resources: ContainerResources
    process: typing.Optional[ContainerProcess] = None
    network: typing.Optional[ContainerNetwork] = None
    provider_hints: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Optional provider-specific hints from the catalog (accepted, not acted upon)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
