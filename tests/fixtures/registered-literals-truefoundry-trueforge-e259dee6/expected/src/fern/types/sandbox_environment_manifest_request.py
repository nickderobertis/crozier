

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resource_name import ResourceName
from .sandbox_environment_image import SandboxEnvironmentImage
from .sandbox_environment_networking import SandboxEnvironmentNetworking
from .sandbox_environment_resources import SandboxEnvironmentResources


class SandboxEnvironmentManifestRequest(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional human-readable description.
    """

    environment_variables: typing.Optional[typing.Dict[str, str]] = None
    image: typing.Optional[SandboxEnvironmentImage] = None
    name: ResourceName
    networking: typing.Optional[SandboxEnvironmentNetworking] = None
    resources: typing.Optional[SandboxEnvironmentResources] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
