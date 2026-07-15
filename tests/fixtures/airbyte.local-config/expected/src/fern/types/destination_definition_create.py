

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .actor_definition_resource_requirements import ActorDefinitionResourceRequirements


class DestinationDefinitionCreate(UniversalBaseModel):
    docker_image_tag: typing_extensions.Annotated[str, FieldMetadata(alias="dockerImageTag")]
    docker_repository: typing_extensions.Annotated[str, FieldMetadata(alias="dockerRepository")]
    documentation_url: typing_extensions.Annotated[str, FieldMetadata(alias="documentationUrl")]
    icon: typing.Optional[str] = None
    name: str
    resource_requirements: typing_extensions.Annotated[
        typing.Optional[ActorDefinitionResourceRequirements], FieldMetadata(alias="resourceRequirements")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
