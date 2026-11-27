

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .custom_fields import CustomFields
from .entry_day import EntryDay
from .entry_schema import EntrySchema
from .fields import Fields
from .user_summary import UserSummary


class StageEntry(UniversalBaseModel):
    """
    A notebook entry used for execution of one or more stage runs in a legacy workflow.
    """

    api_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiURL"),
        pydantic.Field(alias="apiURL", description="The canonical url of the Entry in the API."),
    ] = None
    """
    The canonical url of the Entry in the API.
    """

    assigned_reviewers: typing_extensions.Annotated[
        typing.Optional[typing.List[UserSummary]],
        FieldMetadata(alias="assignedReviewers"),
        pydantic.Field(
            alias="assignedReviewers", description="Array of users assigned to review the stage entry, if any."
        ),
    ] = None
    """
    Array of users assigned to review the stage entry, if any.
    """

    authors: typing.Optional[typing.List[UserSummary]] = pydantic.Field(default=None)
    """
    Array of UserSummary Resources of the authors of the stage entry. This defaults to the creator but can be manually changed.
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="DateTime the stage entry was created at"),
    ] = None
    """
    DateTime the stage entry was created at
    """

    creator: typing.Optional[UserSummary] = pydantic.Field(default=None)
    """
    UserSummary Resource of the user who created the stage entry
    """

    custom_fields: typing_extensions.Annotated[
        typing.Optional[CustomFields], FieldMetadata(alias="customFields"), pydantic.Field(alias="customFields")
    ] = None
    days: typing.Optional[typing.List[EntryDay]] = pydantic.Field(default=None)
    """
    Array of day objects. Each day object has a date field (string) and notes field (array of notes, expand further for details on note types).
    """

    display_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayId"),
        pydantic.Field(alias="displayId", description="User-friendly ID of the stage entry"),
    ] = None
    """
    User-friendly ID of the stage entry
    """

    fields: typing.Optional[Fields] = None
    folder_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="folderId"),
        pydantic.Field(alias="folderId", description="ID of the folder that contains the stage entry"),
    ] = None
    """
    ID of the folder that contains the stage entry
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the stage entry
    """

    modified_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="modifiedAt"),
        pydantic.Field(alias="modifiedAt", description="DateTime the stage entry was last modified"),
    ] = None
    """
    DateTime the stage entry was last modified
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Title of the stage entry
    """

    review_record: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="reviewRecord"),
        pydantic.Field(alias="reviewRecord", description="Review record if set"),
    ] = None
    """
    Review record if set
    """

    schema_: typing_extensions.Annotated[
        typing.Optional[EntrySchema],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema", description="Entry schema if set"),
    ] = None
    """
    Entry schema if set
    """

    web_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="webURL"),
        pydantic.Field(alias="webURL", description="URL of the stage entry"),
    ] = None
    """
    URL of the stage entry
    """

    workflow_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workflowId"),
        pydantic.Field(alias="workflowId", description="ID of the parent workflow"),
    ] = None
    """
    ID of the parent workflow
    """

    workflow_stage_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workflowStageId"),
        pydantic.Field(alias="workflowStageId", description="ID of the associated workflow stage"),
    ] = None
    """
    ID of the associated workflow stage
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
