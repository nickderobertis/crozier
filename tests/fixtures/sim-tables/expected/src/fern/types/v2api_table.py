

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2api_table_locks import V2ApiTableLocks
from .v2api_table_schema import V2ApiTableSchema
from .v2table_job_state import V2TableJobState


class V2ApiTable(UniversalBaseModel):
    """
    A user-defined table with typed columns and governance state.
    """

    id: str = pydantic.Field()
    """
    Unique table identifier.
    """

    web_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="webUrl"),
        pydantic.Field(
            alias="webUrl", description="Canonical absolute URL for opening this resource in the Sim web application."
        ),
    ]
    """
    Canonical absolute URL for opening this resource in the Sim web application.
    """

    name: str = pydantic.Field()
    """
    Table name.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Table description, or null when none is set.
    """

    owner_email: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ownerEmail"),
        pydantic.Field(alias="ownerEmail", description="Current email address of the table owner."),
    ]
    """
    Current email address of the table owner.
    """

    schema_: typing_extensions.Annotated[
        V2ApiTableSchema,
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema", description="Typed table schema."),
    ]
    """
    Typed table schema.
    """

    row_count: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="rowCount"),
        pydantic.Field(alias="rowCount", description="Current number of rows in the table."),
    ]
    """
    Current number of rows in the table.
    """

    max_rows: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="maxRows"),
        pydantic.Field(alias="maxRows", description="Maximum rows allowed by the workspace plan."),
    ]
    """
    Maximum rows allowed by the workspace plan.
    """

    folder_path: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="folderPath"),
        pydantic.Field(
            alias="folderPath",
            description='Canonical slash-prefixed folder path. `/` is the workspace root. Segments are percent-encoded, so a folder shown as "New folder" is `/New%20folder`: everything outside `A-Z a-z 0-9 - _ . ~` is escaped as uppercase hex, and only that exact encoding is accepted. A trailing slash, an empty segment, and a literal `.` or `..` segment are rejected. At most 64 segments and 4096 encoded bytes.',
        ),
    ]
    """
    Canonical slash-prefixed folder path. `/` is the workspace root. Segments are percent-encoded, so a folder shown as "New folder" is `/New%20folder`: everything outside `A-Z a-z 0-9 - _ . ~` is escaped as uppercase hex, and only that exact encoding is accepted. A trailing slash, an empty segment, and a literal `.` or `..` segment are rejected. At most 64 segments and 4096 encoded bytes.
    """

    locks: V2ApiTableLocks = pydantic.Field()
    """
    Read-only table governance locks.
    """

    job: typing.Optional[V2TableJobState] = pydantic.Field(default=None)
    """
    Current background job, or null when idle.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="ISO 8601 timestamp when the table was created."),
    ]
    """
    ISO 8601 timestamp when the table was created.
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="ISO 8601 timestamp when the table was last modified."),
    ]
    """
    ISO 8601 timestamp when the table was last modified.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
