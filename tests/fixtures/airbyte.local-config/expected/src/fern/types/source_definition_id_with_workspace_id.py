

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .source_definition_id import SourceDefinitionId
from .workspace_id import WorkspaceId


class SourceDefinitionIdWithWorkspaceId(UniversalBaseModel):
    source_definition_id: typing_extensions.Annotated[
        SourceDefinitionId, FieldMetadata(alias="sourceDefinitionId"), pydantic.Field(alias="sourceDefinitionId")
    ]
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
