

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destination_definition_id import DestinationDefinitionId
from .workspace_id import WorkspaceId


class DestinationDefinitionIdWithWorkspaceId(UniversalBaseModel):
    destination_definition_id: typing_extensions.Annotated[
        DestinationDefinitionId,
        FieldMetadata(alias="destinationDefinitionId"),
        pydantic.Field(alias="destinationDefinitionId"),
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
