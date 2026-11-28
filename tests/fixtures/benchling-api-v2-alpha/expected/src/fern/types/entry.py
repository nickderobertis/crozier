

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .archive_record import ArchiveRecord
from .custom_fields import CustomFields
from .entry_day import EntryDay
from .entry_review_record import EntryReviewRecord
from .entry_schema import EntrySchema
from .fields import Fields
from .user_summary import UserSummary


class Entry(UniversalBaseModel):
    """
    Entries are notes that users can take. They're organized by "days" (which are user-configurable) and modeled within each day as a list of "notes." Each note has a type - the simplest is a "text" type, but lists, tables, and external files are also supported.

    *Note:* the current Entry resource has a few limitations:
    - Formatting information is not yet supported. Header formatting, bolding, and other stylistic information is not presented.
    - Data in tables is presented as text always - numeric values will need to be parsed into floats or integers, as appropriate.

    Note: Data in Results tables are not accessible through this API call. Results table data can be called through the Results API calls.
    """

    api_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiURL"),
        pydantic.Field(alias="apiURL", description="The canonical url of the Entry in the API."),
    ] = None
    """
    The canonical url of the Entry in the API.
    """

    archive_record: typing_extensions.Annotated[
        typing.Optional[ArchiveRecord],
        FieldMetadata(alias="archiveRecord"),
        pydantic.Field(
            alias="archiveRecord",
            description="ArchiveRecord Resource if the entry is archived. This is null if the entry is not archived.",
        ),
    ] = None
    """
    ArchiveRecord Resource if the entry is archived. This is null if the entry is not archived.
    """

    assigned_reviewers: typing_extensions.Annotated[
        typing.Optional[typing.List[UserSummary]],
        FieldMetadata(alias="assignedReviewers"),
        pydantic.Field(alias="assignedReviewers", description="Array of users assigned to review the entry, if any."),
    ] = None
    """
    Array of users assigned to review the entry, if any.
    """

    authors: typing.Optional[typing.List[UserSummary]] = pydantic.Field(default=None)
    """
    Array of UserSummary Resources of the authors of the entry. This defaults to the creator but can be manually changed.
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="DateTime the entry was created at"),
    ] = None
    """
    DateTime the entry was created at
    """

    creator: typing.Optional[UserSummary] = pydantic.Field(default=None)
    """
    UserSummary Resource of the user who created the entry
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
        pydantic.Field(alias="displayId", description="User-friendly ID of the entry"),
    ] = None
    """
    User-friendly ID of the entry
    """

    entry_template_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="entryTemplateId"),
        pydantic.Field(alias="entryTemplateId", description="ID of the Entry Template this Entry was created from"),
    ] = None
    """
    ID of the Entry Template this Entry was created from
    """

    fields: typing.Optional[Fields] = None
    folder_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="folderId"),
        pydantic.Field(alias="folderId", description="ID of the folder that contains the entry"),
    ] = None
    """
    ID of the folder that contains the entry
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the entry
    """

    modified_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="modifiedAt"),
        pydantic.Field(alias="modifiedAt", description="DateTime the entry was last modified"),
    ] = None
    """
    DateTime the entry was last modified
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Title of the entry
    """

    review_record: typing_extensions.Annotated[
        typing.Optional[EntryReviewRecord],
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
        pydantic.Field(alias="webURL", description="URL of the entry"),
    ] = None
    """
    URL of the entry
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
