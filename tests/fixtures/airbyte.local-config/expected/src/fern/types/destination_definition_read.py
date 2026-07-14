

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .actor_definition_resource_requirements import ActorDefinitionResourceRequirements
from .destination_definition_id import DestinationDefinitionId
from .normalization_destination_definition_config import NormalizationDestinationDefinitionConfig
from .release_stage import ReleaseStage


class DestinationDefinitionRead(UniversalBaseModel):
    destination_definition_id: typing_extensions.Annotated[
        DestinationDefinitionId, FieldMetadata(alias="destinationDefinitionId")
    ]
    docker_image_tag: typing_extensions.Annotated[str, FieldMetadata(alias="dockerImageTag")]
    docker_repository: typing_extensions.Annotated[str, FieldMetadata(alias="dockerRepository")]
    documentation_url: typing_extensions.Annotated[str, FieldMetadata(alias="documentationUrl")]
    icon: typing.Optional[str] = None
    name: str
    normalization_config: typing_extensions.Annotated[
        NormalizationDestinationDefinitionConfig, FieldMetadata(alias="normalizationConfig")
    ]
    protocol_version: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="protocolVersion")] = (
        pydantic.Field(default=None)
    )
    """
    The Airbyte Protocol version supported by the connector
    """

    release_date: typing_extensions.Annotated[typing.Optional[dt.date], FieldMetadata(alias="releaseDate")] = (
        pydantic.Field(default=None)
    )
    """
    The date when this connector was first released, in yyyy-mm-dd format.
    """

    release_stage: typing_extensions.Annotated[typing.Optional[ReleaseStage], FieldMetadata(alias="releaseStage")] = (
        None
    )
    resource_requirements: typing_extensions.Annotated[
        typing.Optional[ActorDefinitionResourceRequirements], FieldMetadata(alias="resourceRequirements")
    ] = None
    supports_dbt: typing_extensions.Annotated[bool, FieldMetadata(alias="supportsDbt")] = pydantic.Field()
    """
    an optional flag indicating whether DBT is used in the normalization. If the flag value is NULL - DBT is not used.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
