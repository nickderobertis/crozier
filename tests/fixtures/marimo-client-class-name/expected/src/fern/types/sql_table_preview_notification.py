

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_table import DataTable
from .request_id import RequestId
from .sql_metadata import SqlMetadata
from .sql_table_preview_notification_op import SqlTablePreviewNotificationOp


class SqlTablePreviewNotification(UniversalBaseModel):
    """
    SQL table preview.

        Attributes:
            request_id: Request ID this responds to.
            metadata: Database and schema metadata.
            table: Table data (None if error).
            error: Error message if failed.
    """

    error: typing.Optional[str] = None
    metadata: SqlMetadata
    op: SqlTablePreviewNotificationOp
    request_id: RequestId
    table: typing.Optional[DataTable] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
