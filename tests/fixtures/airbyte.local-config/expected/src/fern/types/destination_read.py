

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destination_configuration import DestinationConfiguration
from .destination_definition_id import DestinationDefinitionId
from .destination_id import DestinationId
from .workspace_id import WorkspaceId


class DestinationRead(UniversalBaseModel):
    connection_configuration: typing_extensions.Annotated[
        DestinationConfiguration,
        FieldMetadata(alias="connectionConfiguration"),
        pydantic.Field(alias="connectionConfiguration"),
    ]
    destination_definition_id: typing_extensions.Annotated[
        DestinationDefinitionId,
        FieldMetadata(alias="destinationDefinitionId"),
        pydantic.Field(alias="destinationDefinitionId"),
    ]
    destination_id: typing_extensions.Annotated[
        DestinationId, FieldMetadata(alias="destinationId"), pydantic.Field(alias="destinationId")
    ]
    destination_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="destinationName"), pydantic.Field(alias="destinationName")
    ]
    icon: typing.Optional[str] = None
    name: str
    workspace_id: typing_extensions.Annotated[
        WorkspaceId, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
