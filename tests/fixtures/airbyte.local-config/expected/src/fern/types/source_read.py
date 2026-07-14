

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .source_configuration import SourceConfiguration
from .source_definition_id import SourceDefinitionId
from .source_id import SourceId
from .workspace_id import WorkspaceId


class SourceRead(UniversalBaseModel):
    connection_configuration: typing_extensions.Annotated[
        SourceConfiguration, FieldMetadata(alias="connectionConfiguration")
    ]
    icon: typing.Optional[str] = None
    name: str
    source_definition_id: typing_extensions.Annotated[SourceDefinitionId, FieldMetadata(alias="sourceDefinitionId")]
    source_id: typing_extensions.Annotated[SourceId, FieldMetadata(alias="sourceId")]
    source_name: typing_extensions.Annotated[str, FieldMetadata(alias="sourceName")]
    workspace_id: typing_extensions.Annotated[WorkspaceId, FieldMetadata(alias="workspaceId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
