

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .airbyte_catalog import AirbyteCatalog
from .connection_id import ConnectionId
from .connection_schedule import ConnectionSchedule
from .connection_schedule_data import ConnectionScheduleData
from .connection_schedule_type import ConnectionScheduleType
from .connection_status import ConnectionStatus
from .destination_id import DestinationId
from .geography import Geography
from .namespace_definition_type import NamespaceDefinitionType
from .non_breaking_changes_preference import NonBreakingChangesPreference
from .operation_id import OperationId
from .resource_requirements import ResourceRequirements
from .source_id import SourceId


class ConnectionRead(UniversalBaseModel):
    breaking_change: typing_extensions.Annotated[
        bool, FieldMetadata(alias="breakingChange"), pydantic.Field(alias="breakingChange")
    ]
    connection_id: typing_extensions.Annotated[
        ConnectionId, FieldMetadata(alias="connectionId"), pydantic.Field(alias="connectionId")
    ]
    destination_id: typing_extensions.Annotated[
        DestinationId, FieldMetadata(alias="destinationId"), pydantic.Field(alias="destinationId")
    ]
    geography: typing.Optional[Geography] = None
    name: str
    namespace_definition: typing_extensions.Annotated[
        typing.Optional[NamespaceDefinitionType],
        FieldMetadata(alias="namespaceDefinition"),
        pydantic.Field(alias="namespaceDefinition"),
    ] = None
    namespace_format: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="namespaceFormat"),
        pydantic.Field(
            alias="namespaceFormat",
            description="Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If \"${SOURCE_NAMESPACE}\" then behaves like namespaceDefinition = 'source'.",
        ),
    ] = None
    """
    Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.
    """

    non_breaking_changes_preference: typing_extensions.Annotated[
        typing.Optional[NonBreakingChangesPreference],
        FieldMetadata(alias="nonBreakingChangesPreference"),
        pydantic.Field(alias="nonBreakingChangesPreference"),
    ] = None
    notify_schema_changes: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="notifySchemaChanges"), pydantic.Field(alias="notifySchemaChanges")
    ] = None
    operation_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[OperationId]],
        FieldMetadata(alias="operationIds"),
        pydantic.Field(alias="operationIds"),
    ] = None
    prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    Prefix that will be prepended to the name of each stream when it is written to the destination.
    """

    resource_requirements: typing_extensions.Annotated[
        typing.Optional[ResourceRequirements],
        FieldMetadata(alias="resourceRequirements"),
        pydantic.Field(alias="resourceRequirements"),
    ] = None
    schedule: typing.Optional[ConnectionSchedule] = None
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
    source_catalog_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sourceCatalogId"), pydantic.Field(alias="sourceCatalogId")
    ] = None
    source_id: typing_extensions.Annotated[SourceId, FieldMetadata(alias="sourceId"), pydantic.Field(alias="sourceId")]
    status: ConnectionStatus
    sync_catalog: typing_extensions.Annotated[
        AirbyteCatalog, FieldMetadata(alias="syncCatalog"), pydantic.Field(alias="syncCatalog")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
