

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destination_configuration import DestinationConfiguration
from .destination_definition_id import DestinationDefinitionId
from .destination_id import DestinationId
from .workspace_id import WorkspaceId


class DestinationSearch(UniversalBaseModel):
    connection_configuration: typing_extensions.Annotated[
        typing.Optional[DestinationConfiguration], FieldMetadata(alias="connectionConfiguration")
    ] = None
    destination_definition_id: typing_extensions.Annotated[
        typing.Optional[DestinationDefinitionId], FieldMetadata(alias="destinationDefinitionId")
    ] = None
    destination_id: typing_extensions.Annotated[
        typing.Optional[DestinationId], FieldMetadata(alias="destinationId")
    ] = None
    destination_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="destinationName")] = None
    name: typing.Optional[str] = None
    workspace_id: typing_extensions.Annotated[typing.Optional[WorkspaceId], FieldMetadata(alias="workspaceId")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
