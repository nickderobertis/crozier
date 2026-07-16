

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .connection_id import ConnectionId
from .connection_schedule_data import ConnectionScheduleData
from .connection_schedule_type import ConnectionScheduleType
from .connection_status import ConnectionStatus
from .destination_snippet_read import DestinationSnippetRead
from .job_created_at import JobCreatedAt
from .job_status import JobStatus
from .schema_change import SchemaChange
from .source_snippet_read import SourceSnippetRead


class WebBackendConnectionListItem(UniversalBaseModel):
    """
    Information about a connection that shows up in the connection list view.
    """

    connection_id: typing_extensions.Annotated[
        ConnectionId, FieldMetadata(alias="connectionId"), pydantic.Field(alias="connectionId")
    ]
    destination: DestinationSnippetRead
    is_syncing: typing_extensions.Annotated[bool, FieldMetadata(alias="isSyncing"), pydantic.Field(alias="isSyncing")]
    latest_sync_job_created_at: typing_extensions.Annotated[
        typing.Optional[JobCreatedAt],
        FieldMetadata(alias="latestSyncJobCreatedAt"),
        pydantic.Field(alias="latestSyncJobCreatedAt"),
    ] = None
    latest_sync_job_status: typing_extensions.Annotated[
        typing.Optional[JobStatus],
        FieldMetadata(alias="latestSyncJobStatus"),
        pydantic.Field(alias="latestSyncJobStatus"),
    ] = None
    name: str
    schedule_data: typing_extensions.Annotated[
        typing.Optional[ConnectionScheduleData],
        FieldMetadata(alias="scheduleData"),
        pydantic.Field(alias="scheduleData"),
    ] = None
    schedule_type: typing_extensions.Annotated[
        typing.Optional[ConnectionScheduleType],
        FieldMetadata(alias="scheduleType"),
        pydantic.Field(alias="scheduleType"),
    ] = None
    schema_change: typing_extensions.Annotated[
        SchemaChange, FieldMetadata(alias="schemaChange"), pydantic.Field(alias="schemaChange")
    ]
    source: SourceSnippetRead
    status: ConnectionStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
