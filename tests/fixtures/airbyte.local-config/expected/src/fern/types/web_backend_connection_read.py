

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .airbyte_catalog import AirbyteCatalog
from .catalog_diff import CatalogDiff
from .connection_id import ConnectionId
from .connection_schedule import ConnectionSchedule
from .connection_schedule_data import ConnectionScheduleData
from .connection_schedule_type import ConnectionScheduleType
from .connection_status import ConnectionStatus
from .destination_id import DestinationId
from .destination_read import DestinationRead
from .geography import Geography
from .job_created_at import JobCreatedAt
from .job_status import JobStatus
from .namespace_definition_type import NamespaceDefinitionType
from .non_breaking_changes_preference import NonBreakingChangesPreference
from .operation_id import OperationId
from .operation_read import OperationRead
from .resource_requirements import ResourceRequirements
from .schema_change import SchemaChange
from .source_id import SourceId
from .source_read import SourceRead


class WebBackendConnectionRead(UniversalBaseModel):
    catalog_diff: typing_extensions.Annotated[typing.Optional[CatalogDiff], FieldMetadata(alias="catalogDiff")] = None
    catalog_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="catalogId")] = None
    connection_id: typing_extensions.Annotated[ConnectionId, FieldMetadata(alias="connectionId")]
    destination: DestinationRead
    destination_id: typing_extensions.Annotated[DestinationId, FieldMetadata(alias="destinationId")]
    geography: typing.Optional[Geography] = None
    is_syncing: typing_extensions.Annotated[bool, FieldMetadata(alias="isSyncing")]
    latest_sync_job_created_at: typing_extensions.Annotated[
        typing.Optional[JobCreatedAt], FieldMetadata(alias="latestSyncJobCreatedAt")
    ] = None
    latest_sync_job_status: typing_extensions.Annotated[
        typing.Optional[JobStatus], FieldMetadata(alias="latestSyncJobStatus")
    ] = None
    name: str
    namespace_definition: typing_extensions.Annotated[
        typing.Optional[NamespaceDefinitionType], FieldMetadata(alias="namespaceDefinition")
    ] = None
    namespace_format: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="namespaceFormat")] = (
        pydantic.Field(default=None)
    )
    """
    Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.
    """

    non_breaking_changes_preference: typing_extensions.Annotated[
        NonBreakingChangesPreference, FieldMetadata(alias="nonBreakingChangesPreference")
    ]
    notify_schema_changes: typing_extensions.Annotated[bool, FieldMetadata(alias="notifySchemaChanges")]
    operation_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[OperationId]], FieldMetadata(alias="operationIds")
    ] = None
    operations: typing.Optional[typing.List[OperationRead]] = None
    prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    Prefix that will be prepended to the name of each stream when it is written to the destination.
    """

    resource_requirements: typing_extensions.Annotated[
        typing.Optional[ResourceRequirements], FieldMetadata(alias="resourceRequirements")
    ] = None
    schedule: typing.Optional[ConnectionSchedule] = None
    schedule_data: typing_extensions.Annotated[
        typing.Optional[ConnectionScheduleData], FieldMetadata(alias="scheduleData")
    ] = None
    schedule_type: typing_extensions.Annotated[
        typing.Optional[ConnectionScheduleType], FieldMetadata(alias="scheduleType")
    ] = None
    schema_change: typing_extensions.Annotated[SchemaChange, FieldMetadata(alias="schemaChange")]
    source: SourceRead
    source_id: typing_extensions.Annotated[SourceId, FieldMetadata(alias="sourceId")]
    status: ConnectionStatus
    sync_catalog: typing_extensions.Annotated[AirbyteCatalog, FieldMetadata(alias="syncCatalog")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
