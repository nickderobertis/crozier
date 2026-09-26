

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2table_import_rejected_sample import V2TableImportRejectedSample
from .v2table_upload_import_source import V2TableUploadImportSource
from .v2upload_backed_table_import_status import V2UploadBackedTableImportStatus
from .v2upload_backed_table_import_target import V2UploadBackedTableImportTarget


class V2UploadBackedTableImport(UniversalBaseModel):
    """
    Table import whose CSV source is uploaded through signed transfer instructions.
    """

    id: str = pydantic.Field()
    """
    Unique table-import identifier.
    """

    workspace_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="Workspace that owns the import."),
    ]
    """
    Workspace that owns the import.
    """

    status: V2UploadBackedTableImportStatus = pydantic.Field()
    """
    Current import lifecycle state.
    """

    source: V2TableUploadImportSource = pydantic.Field()
    """
    Uploaded CSV source for this import.
    """

    target: V2UploadBackedTableImportTarget = pydantic.Field()
    """
    New or existing table import target.
    """

    table_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tableId"),
        pydantic.Field(alias="tableId", description="Resulting or target table identifier."),
    ] = None
    """
    Resulting or target table identifier.
    """

    rows_processed: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="rowsProcessed"),
        pydantic.Field(alias="rowsProcessed", description="Rows processed so far."),
    ]
    """
    Rows processed so far.
    """

    rows_rejected: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="rowsRejected"),
        pydantic.Field(
            alias="rowsRejected",
            description="Minimum number of source records dropped by parser failures. One failure can discard multiple records, such as an unterminated quote consuming the rest of the file. A non-zero value means partial import even with `completed` status; zero does not guarantee no loss.",
        ),
    ]
    """
    Minimum number of source records dropped by parser failures. One failure can discard multiple records, such as an unterminated quote consuming the rest of the file. A non-zero value means partial import even with `completed` status; zero does not guarantee no loss.
    """

    cells_rejected: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="cellsRejected"),
        pydantic.Field(
            alias="cellsRejected",
            description="Non-empty cell values the target column type could not represent. Their rows were imported with the cell left blank.",
        ),
    ]
    """
    Non-empty cell values the target column type could not represent. Their rows were imported with the cell left blank.
    """

    rejected_samples: typing_extensions.Annotated[
        typing.List[V2TableImportRejectedSample],
        FieldMetadata(alias="rejectedSamples"),
        pydantic.Field(
            alias="rejectedSamples",
            description="Bounded sample of the dropped records, for locating them in the source file.",
        ),
    ]
    """
    Bounded sample of the dropped records, for locating them in the source file.
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
