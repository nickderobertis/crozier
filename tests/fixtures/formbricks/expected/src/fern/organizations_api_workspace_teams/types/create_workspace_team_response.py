

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_workspace_team_response_permission import CreateWorkspaceTeamResponsePermission


class CreateWorkspaceTeamResponse(UniversalBaseModel):
    created_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The date and time the Workspace team was created"),
    ] = None
    """
    The date and time the Workspace team was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The date and time the Workspace team was last updated"),
    ] = None
    """
    The date and time the Workspace team was last updated
    """

    workspace_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="The ID of the Workspace"),
    ] = None
    """
    The ID of the Workspace
    """

    project_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="projectId"),
        pydantic.Field(alias="projectId", description="Deprecated alias for workspaceId."),
    ] = None
    """
    Deprecated alias for workspaceId.
    """

    team_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="teamId"),
        pydantic.Field(alias="teamId", description="The ID of the team"),
    ] = None
    """
    The ID of the team
    """

    permission: typing.Optional[CreateWorkspaceTeamResponsePermission] = pydantic.Field(default=None)
    """
    Level of access granted to the Workspace
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
