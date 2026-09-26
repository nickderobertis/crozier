

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2LogDetailWorkflow(UniversalBaseModel):
    """
    Workflow snapshot associated with the execution.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Workflow identifier, or null when unavailable.
    """

    name: str = pydantic.Field()
    """
    Workflow name.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Workflow description, or null when unset.
    """

    folder_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="folderPath"),
        pydantic.Field(
            alias="folderPath",
            description="Canonical folder path of the workflow, in the same form `folderPaths` accepts as a filter: `/` for a workflow at the workspace root. Null only when the path cannot be resolved — the folder has been deleted, or the workflow itself no longer exists.",
        ),
    ] = None
    """
    Canonical folder path of the workflow, in the same form `folderPaths` accepts as a filter: `/` for a workflow at the workspace root. Null only when the path cannot be resolved — the folder has been deleted, or the workflow itself no longer exists.
    """

    owner_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ownerEmail"),
        pydantic.Field(
            alias="ownerEmail",
            description="Deprecated — use the run-level `executedByEmail` instead. Email of the workflow's current owner, or null when unavailable. This is a property of the workflow as it stands today, not of the run: it changes when workflow ownership is reassigned, and the owner is not the identity a background run executes as.",
        ),
    ] = None
    """
    Deprecated — use the run-level `executedByEmail` instead. Email of the workflow's current owner, or null when unavailable. This is a property of the workflow as it stands today, not of the run: it changes when workflow ownership is reassigned, and the owner is not the identity a background run executes as.
    """

    workspace_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="Owning workspace identifier, or null when unavailable."),
    ] = None
    """
    Owning workspace identifier, or null when unavailable.
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(
            alias="createdAt", description="ISO 8601 workflow creation timestamp, or null when unavailable."
        ),
    ] = None
    """
    ISO 8601 workflow creation timestamp, or null when unavailable.
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="ISO 8601 workflow update timestamp, or null when unavailable."),
    ] = None
    """
    ISO 8601 workflow update timestamp, or null when unavailable.
    """

    deleted: bool = pydantic.Field()
    """
    Whether the workflow has been deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
