

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2table_export_format import V2TableExportFormat
from .v2table_export_status import V2TableExportStatus


class V2TableExport(UniversalBaseModel):
    """
    Durable asynchronous table-export lifecycle resource.
    """

    id: str = pydantic.Field()
    """
    Unique table-export identifier.
    """

    table_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="tableId"), pydantic.Field(alias="tableId", description="Exported table identifier.")
    ]
    """
    Exported table identifier.
    """

    workspace_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="Workspace that owns the export."),
    ]
    """
    Workspace that owns the export.
    """

    format: V2TableExportFormat = pydantic.Field()
    """
    Export file format.
    """

    status: V2TableExportStatus = pydantic.Field()
    """
    Current export lifecycle state.
    """

    rows_processed: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="rowsProcessed"),
        pydantic.Field(alias="rowsProcessed", description="Rows exported so far."),
    ]
    """
    Rows exported so far.
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Terminal failure reason, or null.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="ISO 8601 creation timestamp."),
    ]
    """
    ISO 8601 creation timestamp.
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="ISO 8601 last-update timestamp."),
    ]
    """
    ISO 8601 last-update timestamp.
    """

    completed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="completedAt"),
        pydantic.Field(alias="completedAt", description="ISO 8601 completion timestamp, or null."),
    ] = None
    """
    ISO 8601 completion timestamp, or null.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
