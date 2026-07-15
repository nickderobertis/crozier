

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.airbyte_catalog import AirbyteCatalog
from ..types.connection_id import ConnectionId
from ..types.connection_read import ConnectionRead
from ..types.connection_read_list import ConnectionReadList
from ..types.connection_schedule import ConnectionSchedule
from ..types.connection_schedule_data import ConnectionScheduleData
from ..types.connection_schedule_type import ConnectionScheduleType
from ..types.connection_status import ConnectionStatus
from ..types.destination_id import DestinationId
from ..types.destination_search import DestinationSearch
from ..types.geography import Geography
from ..types.job_info_read import JobInfoRead
from ..types.namespace_definition_type import NamespaceDefinitionType
from ..types.non_breaking_changes_preference import NonBreakingChangesPreference
from ..types.operation_id import OperationId
from ..types.resource_requirements import ResourceRequirements
from ..types.source_id import SourceId
from ..types.source_search import SourceSearch
from ..types.workspace_id import WorkspaceId
from .raw_client import AsyncRawConnectionClient, RawConnectionClient


OMIT = typing.cast(typing.Any, ...)


class ConnectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConnectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConnectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConnectionClient
        """
        return self._raw_client

    def create_connection(
        self,
        *,
        destination_id: DestinationId,
        source_id: SourceId,
        status: ConnectionStatus,
        geography: typing.Optional[Geography] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        non_breaking_changes_preference: typing.Optional[NonBreakingChangesPreference] = OMIT,
        notify_schema_changes: typing.Optional[bool] = OMIT,
        operation_ids: typing.Optional[typing.Sequence[OperationId]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionRead:
        """
        Parameters
        ----------
        destination_id : DestinationId

        source_id : SourceId

        status : ConnectionStatus

        geography : typing.Optional[Geography]

        name : typing.Optional[str]
            Optional name of the connection

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        non_breaking_changes_preference : typing.Optional[NonBreakingChangesPreference]

        notify_schema_changes : typing.Optional[bool]

        operation_ids : typing.Optional[typing.Sequence[OperationId]]

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        resource_requirements : typing.Optional[ResourceRequirements]

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        source_catalog_id : typing.Optional[str]

        sync_catalog : typing.Optional[AirbyteCatalog]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionRead
            Successful operation

        Examples
        --------
        from fern import ConnectionStatus, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connection.create_connection(
            destination_id="destinationId",
            source_id="sourceId",
            status=ConnectionStatus.ACTIVE,
        )
        """
        _response = self._raw_client.create_connection(
            destination_id=destination_id,
            source_id=source_id,
            status=status,
            geography=geography,
            name=name,
            namespace_definition=namespace_definition,
            namespace_format=namespace_format,
            non_breaking_changes_preference=non_breaking_changes_preference,
            notify_schema_changes=notify_schema_changes,
            operation_ids=operation_ids,
            prefix=prefix,
            resource_requirements=resource_requirements,
            schedule=schedule,
            schedule_data=schedule_data,
            schedule_type=schedule_type,
            source_catalog_id=source_catalog_id,
            sync_catalog=sync_catalog,
            request_options=request_options,
        )
        return _response.data

    def delete_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connection.delete_connection(
            connection_id="connectionId",
        )
        """
        _response = self._raw_client.delete_connection(connection_id=connection_id, request_options=request_options)
        return _response.data

    def get_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionRead:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connection.get_connection(
            connection_id="connectionId",
        )
        """
        _response = self._raw_client.get_connection(connection_id=connection_id, request_options=request_options)
        return _response.data

    def list_connections_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionReadList:
        """
        List connections for workspace. Does not return deleted connections.

        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connection.list_connections_for_workspace(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_connections_for_workspace(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def list_all_connections_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionReadList:
        """
        List connections for workspace, including deleted connections.

        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connection.list_all_connections_for_workspace(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_all_connections_for_workspace(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def reset_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> JobInfoRead:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfoRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connection.reset_connection(
            connection_id="connectionId",
        )
        """
        _response = self._raw_client.reset_connection(connection_id=connection_id, request_options=request_options)
        return _response.data

    def search_connections(
        self,
        *,
        connection_id: typing.Optional[ConnectionId] = OMIT,
        destination: typing.Optional[DestinationSearch] = OMIT,
        destination_id: typing.Optional[DestinationId] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source: typing.Optional[SourceSearch] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionReadList:
        """
        Parameters
        ----------
        connection_id : typing.Optional[ConnectionId]

        destination : typing.Optional[DestinationSearch]

        destination_id : typing.Optional[DestinationId]

        name : typing.Optional[str]

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        source : typing.Optional[SourceSearch]

        source_id : typing.Optional[SourceId]

        status : typing.Optional[ConnectionStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connection.search_connections()
        """
        _response = self._raw_client.search_connections(
            connection_id=connection_id,
            destination=destination,
            destination_id=destination_id,
            name=name,
            namespace_definition=namespace_definition,
            namespace_format=namespace_format,
            prefix=prefix,
            schedule=schedule,
            schedule_data=schedule_data,
            schedule_type=schedule_type,
            source=source,
            source_id=source_id,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def sync_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> JobInfoRead:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfoRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connection.sync_connection(
            connection_id="connectionId",
        )
        """
        _response = self._raw_client.sync_connection(connection_id=connection_id, request_options=request_options)
        return _response.data

    def update_connection(
        self,
        *,
        connection_id: ConnectionId,
        breaking_change: typing.Optional[bool] = OMIT,
        geography: typing.Optional[Geography] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        non_breaking_changes_preference: typing.Optional[NonBreakingChangesPreference] = OMIT,
        notify_schema_changes: typing.Optional[bool] = OMIT,
        operation_ids: typing.Optional[typing.Sequence[OperationId]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionRead:
        """
        Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
        Note that if a catalog is present in the request body, the connection's entire catalog will be replaced
        with the catalog from the request. This means that to modify a single stream, the entire new catalog
        containing the updated stream needs to be sent.

        Parameters
        ----------
        connection_id : ConnectionId

        breaking_change : typing.Optional[bool]

        geography : typing.Optional[Geography]

        name : typing.Optional[str]
            Name that will be set to this connection

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        non_breaking_changes_preference : typing.Optional[NonBreakingChangesPreference]

        notify_schema_changes : typing.Optional[bool]

        operation_ids : typing.Optional[typing.Sequence[OperationId]]

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        resource_requirements : typing.Optional[ResourceRequirements]

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        source_catalog_id : typing.Optional[str]

        status : typing.Optional[ConnectionStatus]

        sync_catalog : typing.Optional[AirbyteCatalog]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connection.update_connection(
            connection_id="connectionId",
        )
        """
        _response = self._raw_client.update_connection(
            connection_id=connection_id,
            breaking_change=breaking_change,
            geography=geography,
            name=name,
            namespace_definition=namespace_definition,
            namespace_format=namespace_format,
            non_breaking_changes_preference=non_breaking_changes_preference,
            notify_schema_changes=notify_schema_changes,
            operation_ids=operation_ids,
            prefix=prefix,
            resource_requirements=resource_requirements,
            schedule=schedule,
            schedule_data=schedule_data,
            schedule_type=schedule_type,
            source_catalog_id=source_catalog_id,
            status=status,
            sync_catalog=sync_catalog,
            request_options=request_options,
        )
        return _response.data


class AsyncConnectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConnectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConnectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConnectionClient
        """
        return self._raw_client

    async def create_connection(
        self,
        *,
        destination_id: DestinationId,
        source_id: SourceId,
        status: ConnectionStatus,
        geography: typing.Optional[Geography] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        non_breaking_changes_preference: typing.Optional[NonBreakingChangesPreference] = OMIT,
        notify_schema_changes: typing.Optional[bool] = OMIT,
        operation_ids: typing.Optional[typing.Sequence[OperationId]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionRead:
        """
        Parameters
        ----------
        destination_id : DestinationId

        source_id : SourceId

        status : ConnectionStatus

        geography : typing.Optional[Geography]

        name : typing.Optional[str]
            Optional name of the connection

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        non_breaking_changes_preference : typing.Optional[NonBreakingChangesPreference]

        notify_schema_changes : typing.Optional[bool]

        operation_ids : typing.Optional[typing.Sequence[OperationId]]

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        resource_requirements : typing.Optional[ResourceRequirements]

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        source_catalog_id : typing.Optional[str]

        sync_catalog : typing.Optional[AirbyteCatalog]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ConnectionStatus

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connection.create_connection(
                destination_id="destinationId",
                source_id="sourceId",
                status=ConnectionStatus.ACTIVE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_connection(
            destination_id=destination_id,
            source_id=source_id,
            status=status,
            geography=geography,
            name=name,
            namespace_definition=namespace_definition,
            namespace_format=namespace_format,
            non_breaking_changes_preference=non_breaking_changes_preference,
            notify_schema_changes=notify_schema_changes,
            operation_ids=operation_ids,
            prefix=prefix,
            resource_requirements=resource_requirements,
            schedule=schedule,
            schedule_data=schedule_data,
            schedule_type=schedule_type,
            source_catalog_id=source_catalog_id,
            sync_catalog=sync_catalog,
            request_options=request_options,
        )
        return _response.data

    async def delete_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connection.delete_connection(
                connection_id="connectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_connection(
            connection_id=connection_id, request_options=request_options
        )
        return _response.data

    async def get_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionRead:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connection.get_connection(
                connection_id="connectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_connection(connection_id=connection_id, request_options=request_options)
        return _response.data

    async def list_connections_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionReadList:
        """
        List connections for workspace. Does not return deleted connections.

        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connection.list_connections_for_workspace(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_connections_for_workspace(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def list_all_connections_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionReadList:
        """
        List connections for workspace, including deleted connections.

        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connection.list_all_connections_for_workspace(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_connections_for_workspace(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def reset_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> JobInfoRead:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfoRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connection.reset_connection(
                connection_id="connectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_connection(
            connection_id=connection_id, request_options=request_options
        )
        return _response.data

    async def search_connections(
        self,
        *,
        connection_id: typing.Optional[ConnectionId] = OMIT,
        destination: typing.Optional[DestinationSearch] = OMIT,
        destination_id: typing.Optional[DestinationId] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source: typing.Optional[SourceSearch] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionReadList:
        """
        Parameters
        ----------
        connection_id : typing.Optional[ConnectionId]

        destination : typing.Optional[DestinationSearch]

        destination_id : typing.Optional[DestinationId]

        name : typing.Optional[str]

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        source : typing.Optional[SourceSearch]

        source_id : typing.Optional[SourceId]

        status : typing.Optional[ConnectionStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connection.search_connections()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_connections(
            connection_id=connection_id,
            destination=destination,
            destination_id=destination_id,
            name=name,
            namespace_definition=namespace_definition,
            namespace_format=namespace_format,
            prefix=prefix,
            schedule=schedule,
            schedule_data=schedule_data,
            schedule_type=schedule_type,
            source=source,
            source_id=source_id,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def sync_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> JobInfoRead:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobInfoRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connection.sync_connection(
                connection_id="connectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sync_connection(connection_id=connection_id, request_options=request_options)
        return _response.data

    async def update_connection(
        self,
        *,
        connection_id: ConnectionId,
        breaking_change: typing.Optional[bool] = OMIT,
        geography: typing.Optional[Geography] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        non_breaking_changes_preference: typing.Optional[NonBreakingChangesPreference] = OMIT,
        notify_schema_changes: typing.Optional[bool] = OMIT,
        operation_ids: typing.Optional[typing.Sequence[OperationId]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionRead:
        """
        Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
        Note that if a catalog is present in the request body, the connection's entire catalog will be replaced
        with the catalog from the request. This means that to modify a single stream, the entire new catalog
        containing the updated stream needs to be sent.

        Parameters
        ----------
        connection_id : ConnectionId

        breaking_change : typing.Optional[bool]

        geography : typing.Optional[Geography]

        name : typing.Optional[str]
            Name that will be set to this connection

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        non_breaking_changes_preference : typing.Optional[NonBreakingChangesPreference]

        notify_schema_changes : typing.Optional[bool]

        operation_ids : typing.Optional[typing.Sequence[OperationId]]

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        resource_requirements : typing.Optional[ResourceRequirements]

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        source_catalog_id : typing.Optional[str]

        status : typing.Optional[ConnectionStatus]

        sync_catalog : typing.Optional[AirbyteCatalog]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connection.update_connection(
                connection_id="connectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_connection(
            connection_id=connection_id,
            breaking_change=breaking_change,
            geography=geography,
            name=name,
            namespace_definition=namespace_definition,
            namespace_format=namespace_format,
            non_breaking_changes_preference=non_breaking_changes_preference,
            notify_schema_changes=notify_schema_changes,
            operation_ids=operation_ids,
            prefix=prefix,
            resource_requirements=resource_requirements,
            schedule=schedule,
            schedule_data=schedule_data,
            schedule_type=schedule_type,
            source_catalog_id=source_catalog_id,
            status=status,
            sync_catalog=sync_catalog,
            request_options=request_options,
        )
        return _response.data
