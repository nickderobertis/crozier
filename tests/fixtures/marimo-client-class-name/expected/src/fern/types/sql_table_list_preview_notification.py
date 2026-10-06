

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_table import DataTable
from .request_id import RequestId
from .sql_metadata import SqlMetadata
from .sql_table_list_preview_notification_op import SqlTableListPreviewNotificationOp


class SqlTableListPreviewNotification(UniversalBaseModel):
    """
    List of SQL tables in a schema.

        Attributes:
            request_id: Request ID this responds to.
            metadata: Database and schema metadata.
            tables: Tables in schema.
            error: Error message if failed.
    """

    error: typing.Optional[str] = None
    metadata: SqlMetadata
    op: SqlTableListPreviewNotificationOp
    request_id: RequestId
    tables: typing.Optional[typing.List[DataTable]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
