

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .request_id import RequestId
from .sql_database_metadata import SqlDatabaseMetadata
from .sql_schema_list_preview_notification_op import SqlSchemaListPreviewNotificationOp


class SqlSchemaListPreviewNotification(UniversalBaseModel):
    """
    List of SQL schemas in a database.

        Attributes:
            request_id: Request ID this responds to.
            metadata: Database and schema metadata.
            schemas: Schemas in database.
            error: Error message if failed.
    """

    error: typing.Optional[str] = None
    metadata: SqlDatabaseMetadata
    op: SqlSchemaListPreviewNotificationOp
    request_id: RequestId
    schemas: typing.Optional[typing.List["Schema"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .schema import Schema

update_forward_refs(SqlSchemaListPreviewNotification, Schema=Schema)
