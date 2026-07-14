

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.airbyte_catalog import AirbyteCatalog
from ..types.connection_id import ConnectionId
from ..types.connection_schedule import ConnectionSchedule
from ..types.connection_schedule_data import ConnectionScheduleData
from ..types.connection_schedule_type import ConnectionScheduleType
from ..types.connection_state_type import ConnectionStateType
from ..types.connection_status import ConnectionStatus
from ..types.destination_id import DestinationId
from ..types.geography import Geography
from ..types.namespace_definition_type import NamespaceDefinitionType
from ..types.non_breaking_changes_preference import NonBreakingChangesPreference
from ..types.operation_create import OperationCreate
from ..types.operation_id import OperationId
from ..types.resource_requirements import ResourceRequirements
from ..types.source_id import SourceId
from ..types.web_backend_check_updates_read import WebBackendCheckUpdatesRead
from ..types.web_backend_connection_read import WebBackendConnectionRead
from ..types.web_backend_connection_read_list import WebBackendConnectionReadList
from ..types.web_backend_geographies_list_result import WebBackendGeographiesListResult
from ..types.web_backend_operation_create_or_update import WebBackendOperationCreateOrUpdate
from ..types.web_backend_workspace_state_result import WebBackendWorkspaceStateResult
from ..types.workspace_id import WorkspaceId
from .raw_client import AsyncRawWebBackendClient, RawWebBackendClient


OMIT = typing.cast(typing.Any, ...)


class WebBackendClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebBackendClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebBackendClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebBackendClient
        """
        return self._raw_client

    def check_updates(self, *, request_options: typing.Optional[RequestOptions] = None) -> WebBackendCheckUpdatesRead:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebBackendCheckUpdatesRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_backend.check_updates()
        """
        _response = self._raw_client.check_updates(request_options=request_options)
        return _response.data

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
        operation_ids: typing.Optional[typing.Sequence[OperationId]] = OMIT,
        operations: typing.Optional[typing.Sequence[OperationCreate]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebBackendConnectionRead:
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

        operation_ids : typing.Optional[typing.Sequence[OperationId]]

        operations : typing.Optional[typing.Sequence[OperationCreate]]

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
        WebBackendConnectionRead
            Successful operation

        Examples
        --------
        from fern import ConnectionStatus, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_backend.create_connection(
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
            operation_ids=operation_ids,
            operations=operations,
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

    def get_connection(
        self,
        *,
        connection_id: ConnectionId,
        with_refreshed_catalog: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebBackendConnectionRead:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        with_refreshed_catalog : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebBackendConnectionRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_backend.get_connection(
            connection_id="connectionId",
        )
        """
        _response = self._raw_client.get_connection(
            connection_id=connection_id, with_refreshed_catalog=with_refreshed_catalog, request_options=request_options
        )
        return _response.data

    def list_connections_for_workspace(
        self,
        *,
        workspace_id: WorkspaceId,
        destination_id: typing.Optional[typing.Sequence[DestinationId]] = OMIT,
        source_id: typing.Optional[typing.Sequence[SourceId]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebBackendConnectionReadList:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        destination_id : typing.Optional[typing.Sequence[DestinationId]]

        source_id : typing.Optional[typing.Sequence[SourceId]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebBackendConnectionReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_backend.list_connections_for_workspace(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_connections_for_workspace(
            workspace_id=workspace_id,
            destination_id=destination_id,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data

    def update_connection(
        self,
        *,
        connection_id: ConnectionId,
        geography: typing.Optional[Geography] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        non_breaking_changes_preference: typing.Optional[NonBreakingChangesPreference] = OMIT,
        notify_schema_changes: typing.Optional[bool] = OMIT,
        operations: typing.Optional[typing.Sequence[WebBackendOperationCreateOrUpdate]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        skip_reset: typing.Optional[bool] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebBackendConnectionRead:
        """
        Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
        Any operations that lack an ID will be created. Then, the newly created operationId will be applied to the
        connection along with the rest of the operationIds in the request body.
        Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
        Note that if a catalog is present in the request body, the connection's entire catalog will be replaced
        with the catalog from the request. This means that to modify a single stream, the entire new catalog
        containing the updated stream needs to be sent.

        Parameters
        ----------
        connection_id : ConnectionId

        geography : typing.Optional[Geography]

        name : typing.Optional[str]
            Name that will be set to the connection

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        non_breaking_changes_preference : typing.Optional[NonBreakingChangesPreference]

        notify_schema_changes : typing.Optional[bool]

        operations : typing.Optional[typing.Sequence[WebBackendOperationCreateOrUpdate]]

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        resource_requirements : typing.Optional[ResourceRequirements]

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        skip_reset : typing.Optional[bool]

        source_catalog_id : typing.Optional[str]

        status : typing.Optional[ConnectionStatus]

        sync_catalog : typing.Optional[AirbyteCatalog]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebBackendConnectionRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_backend.update_connection(
            connection_id="connectionId",
        )
        """
        _response = self._raw_client.update_connection(
            connection_id=connection_id,
            geography=geography,
            name=name,
            namespace_definition=namespace_definition,
            namespace_format=namespace_format,
            non_breaking_changes_preference=non_breaking_changes_preference,
            notify_schema_changes=notify_schema_changes,
            operations=operations,
            prefix=prefix,
            resource_requirements=resource_requirements,
            schedule=schedule,
            schedule_data=schedule_data,
            schedule_type=schedule_type,
            skip_reset=skip_reset,
            source_catalog_id=source_catalog_id,
            status=status,
            sync_catalog=sync_catalog,
            request_options=request_options,
        )
        return _response.data

    def list_geographies(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebBackendGeographiesListResult:
        """
        Returns all available geographies in which a data sync can run.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebBackendGeographiesListResult
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_backend.list_geographies()
        """
        _response = self._raw_client.list_geographies(request_options=request_options)
        return _response.data

    def get_state_type(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionStateType:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionStateType
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_backend.get_state_type(
            connection_id="connectionId",
        )
        """
        _response = self._raw_client.get_state_type(connection_id=connection_id, request_options=request_options)
        return _response.data

    def get_workspace_state(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> WebBackendWorkspaceStateResult:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebBackendWorkspaceStateResult
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.web_backend.get_workspace_state(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_workspace_state(workspace_id=workspace_id, request_options=request_options)
        return _response.data


class AsyncWebBackendClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebBackendClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebBackendClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebBackendClient
        """
        return self._raw_client

    async def check_updates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebBackendCheckUpdatesRead:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebBackendCheckUpdatesRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_backend.check_updates()


        asyncio.run(main())
        """
        _response = await self._raw_client.check_updates(request_options=request_options)
        return _response.data

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
        operation_ids: typing.Optional[typing.Sequence[OperationId]] = OMIT,
        operations: typing.Optional[typing.Sequence[OperationCreate]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebBackendConnectionRead:
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

        operation_ids : typing.Optional[typing.Sequence[OperationId]]

        operations : typing.Optional[typing.Sequence[OperationCreate]]

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
        WebBackendConnectionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ConnectionStatus

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_backend.create_connection(
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
            operation_ids=operation_ids,
            operations=operations,
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

    async def get_connection(
        self,
        *,
        connection_id: ConnectionId,
        with_refreshed_catalog: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebBackendConnectionRead:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        with_refreshed_catalog : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebBackendConnectionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_backend.get_connection(
                connection_id="connectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_connection(
            connection_id=connection_id, with_refreshed_catalog=with_refreshed_catalog, request_options=request_options
        )
        return _response.data

    async def list_connections_for_workspace(
        self,
        *,
        workspace_id: WorkspaceId,
        destination_id: typing.Optional[typing.Sequence[DestinationId]] = OMIT,
        source_id: typing.Optional[typing.Sequence[SourceId]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebBackendConnectionReadList:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        destination_id : typing.Optional[typing.Sequence[DestinationId]]

        source_id : typing.Optional[typing.Sequence[SourceId]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebBackendConnectionReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_backend.list_connections_for_workspace(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_connections_for_workspace(
            workspace_id=workspace_id,
            destination_id=destination_id,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data

    async def update_connection(
        self,
        *,
        connection_id: ConnectionId,
        geography: typing.Optional[Geography] = OMIT,
        name: typing.Optional[str] = OMIT,
        namespace_definition: typing.Optional[NamespaceDefinitionType] = OMIT,
        namespace_format: typing.Optional[str] = OMIT,
        non_breaking_changes_preference: typing.Optional[NonBreakingChangesPreference] = OMIT,
        notify_schema_changes: typing.Optional[bool] = OMIT,
        operations: typing.Optional[typing.Sequence[WebBackendOperationCreateOrUpdate]] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ResourceRequirements] = OMIT,
        schedule: typing.Optional[ConnectionSchedule] = OMIT,
        schedule_data: typing.Optional[ConnectionScheduleData] = OMIT,
        schedule_type: typing.Optional[ConnectionScheduleType] = OMIT,
        skip_reset: typing.Optional[bool] = OMIT,
        source_catalog_id: typing.Optional[str] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        sync_catalog: typing.Optional[AirbyteCatalog] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebBackendConnectionRead:
        """
        Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
        Any operations that lack an ID will be created. Then, the newly created operationId will be applied to the
        connection along with the rest of the operationIds in the request body.
        Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
        Note that if a catalog is present in the request body, the connection's entire catalog will be replaced
        with the catalog from the request. This means that to modify a single stream, the entire new catalog
        containing the updated stream needs to be sent.

        Parameters
        ----------
        connection_id : ConnectionId

        geography : typing.Optional[Geography]

        name : typing.Optional[str]
            Name that will be set to the connection

        namespace_definition : typing.Optional[NamespaceDefinitionType]

        namespace_format : typing.Optional[str]
            Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.

        non_breaking_changes_preference : typing.Optional[NonBreakingChangesPreference]

        notify_schema_changes : typing.Optional[bool]

        operations : typing.Optional[typing.Sequence[WebBackendOperationCreateOrUpdate]]

        prefix : typing.Optional[str]
            Prefix that will be prepended to the name of each stream when it is written to the destination.

        resource_requirements : typing.Optional[ResourceRequirements]

        schedule : typing.Optional[ConnectionSchedule]

        schedule_data : typing.Optional[ConnectionScheduleData]

        schedule_type : typing.Optional[ConnectionScheduleType]

        skip_reset : typing.Optional[bool]

        source_catalog_id : typing.Optional[str]

        status : typing.Optional[ConnectionStatus]

        sync_catalog : typing.Optional[AirbyteCatalog]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebBackendConnectionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_backend.update_connection(
                connection_id="connectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_connection(
            connection_id=connection_id,
            geography=geography,
            name=name,
            namespace_definition=namespace_definition,
            namespace_format=namespace_format,
            non_breaking_changes_preference=non_breaking_changes_preference,
            notify_schema_changes=notify_schema_changes,
            operations=operations,
            prefix=prefix,
            resource_requirements=resource_requirements,
            schedule=schedule,
            schedule_data=schedule_data,
            schedule_type=schedule_type,
            skip_reset=skip_reset,
            source_catalog_id=source_catalog_id,
            status=status,
            sync_catalog=sync_catalog,
            request_options=request_options,
        )
        return _response.data

    async def list_geographies(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebBackendGeographiesListResult:
        """
        Returns all available geographies in which a data sync can run.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebBackendGeographiesListResult
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_backend.list_geographies()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_geographies(request_options=request_options)
        return _response.data

    async def get_state_type(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionStateType:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionStateType
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_backend.get_state_type(
                connection_id="connectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_state_type(connection_id=connection_id, request_options=request_options)
        return _response.data

    async def get_workspace_state(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> WebBackendWorkspaceStateResult:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebBackendWorkspaceStateResult
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.web_backend.get_workspace_state(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workspace_state(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data
