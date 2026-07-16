

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .actor_definition_resource_requirements import ActorDefinitionResourceRequirements
from .release_stage import ReleaseStage
from .source_definition_id import SourceDefinitionId
from .source_definition_read_source_type import SourceDefinitionReadSourceType


class SourceDefinitionRead(UniversalBaseModel):
    docker_image_tag: typing_extensions.Annotated[
        str, FieldMetadata(alias="dockerImageTag"), pydantic.Field(alias="dockerImageTag")
    ]
    docker_repository: typing_extensions.Annotated[
        str, FieldMetadata(alias="dockerRepository"), pydantic.Field(alias="dockerRepository")
    ]
    documentation_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="documentationUrl"), pydantic.Field(alias="documentationUrl")
    ] = None
    icon: typing.Optional[str] = None
    name: str
    protocol_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="protocolVersion"),
        pydantic.Field(alias="protocolVersion", description="The Airbyte Protocol version supported by the connector"),
    ] = None
    """
    The Airbyte Protocol version supported by the connector
    """

    release_date: typing_extensions.Annotated[
        typing.Optional[dt.date],
        FieldMetadata(alias="releaseDate"),
        pydantic.Field(
            alias="releaseDate", description="The date when this connector was first released, in yyyy-mm-dd format."
        ),
    ] = None
    """
    The date when this connector was first released, in yyyy-mm-dd format.
    """

    release_stage: typing_extensions.Annotated[
        typing.Optional[ReleaseStage], FieldMetadata(alias="releaseStage"), pydantic.Field(alias="releaseStage")
    ] = None
    resource_requirements: typing_extensions.Annotated[
        typing.Optional[ActorDefinitionResourceRequirements],
        FieldMetadata(alias="resourceRequirements"),
        pydantic.Field(alias="resourceRequirements"),
    ] = None
    source_definition_id: typing_extensions.Annotated[
        SourceDefinitionId, FieldMetadata(alias="sourceDefinitionId"), pydantic.Field(alias="sourceDefinitionId")
    ]
    source_type: typing_extensions.Annotated[
        typing.Optional[SourceDefinitionReadSourceType],
        FieldMetadata(alias="sourceType"),
        pydantic.Field(alias="sourceType"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
