

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .source_configuration import SourceConfiguration
from .source_definition_id import SourceDefinitionId
from .source_id import SourceId
from .workspace_id import WorkspaceId


class SourceSearch(UniversalBaseModel):
    connection_configuration: typing_extensions.Annotated[
        typing.Optional[SourceConfiguration], FieldMetadata(alias="connectionConfiguration")
    ] = None
    name: typing.Optional[str] = None
    source_definition_id: typing_extensions.Annotated[
        typing.Optional[SourceDefinitionId], FieldMetadata(alias="sourceDefinitionId")
    ] = None
    source_id: typing_extensions.Annotated[typing.Optional[SourceId], FieldMetadata(alias="sourceId")] = None
    source_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="sourceName")] = None
    workspace_id: typing_extensions.Annotated[typing.Optional[WorkspaceId], FieldMetadata(alias="workspaceId")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
