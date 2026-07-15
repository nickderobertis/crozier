

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.check_connection_read import CheckConnectionRead
from ..types.destination_configuration import DestinationConfiguration
from ..types.destination_definition_id import DestinationDefinitionId
from ..types.destination_id import DestinationId
from ..types.source_configuration import SourceConfiguration
from ..types.source_definition_id import SourceDefinitionId
from ..types.source_discover_schema_read import SourceDiscoverSchemaRead
from ..types.source_id import SourceId
from ..types.workspace_id import WorkspaceId
from .raw_client import AsyncRawSchedulerClient, RawSchedulerClient


OMIT = typing.cast(typing.Any, ...)


class SchedulerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSchedulerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSchedulerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSchedulerClient
        """
        return self._raw_client

    def execute_destination_check_connection(
        self,
        *,
        connection_configuration: DestinationConfiguration,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        destination_id: typing.Optional[DestinationId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckConnectionRead:
        """
        Parameters
        ----------
        connection_configuration : DestinationConfiguration

        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        destination_id : typing.Optional[DestinationId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckConnectionRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.scheduler.execute_destination_check_connection(
            connection_configuration={"user": "charles"},
            destination_definition_id="destinationDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.execute_destination_check_connection(
            connection_configuration=connection_configuration,
            destination_definition_id=destination_definition_id,
            workspace_id=workspace_id,
            destination_id=destination_id,
            request_options=request_options,
        )
        return _response.data

    def execute_source_check_connection(
        self,
        *,
        connection_configuration: SourceConfiguration,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckConnectionRead:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        source_id : typing.Optional[SourceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckConnectionRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.scheduler.execute_source_check_connection(
            connection_configuration={"user": "charles"},
            source_definition_id="sourceDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.execute_source_check_connection(
            connection_configuration=connection_configuration,
            source_definition_id=source_definition_id,
            workspace_id=workspace_id,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data

    def execute_source_discover_schema(
        self,
        *,
        connection_configuration: SourceConfiguration,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceDiscoverSchemaRead:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        source_id : typing.Optional[SourceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDiscoverSchemaRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.scheduler.execute_source_discover_schema(
            connection_configuration={"user": "charles"},
            source_definition_id="sourceDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.execute_source_discover_schema(
            connection_configuration=connection_configuration,
            source_definition_id=source_definition_id,
            workspace_id=workspace_id,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data


class AsyncSchedulerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSchedulerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSchedulerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSchedulerClient
        """
        return self._raw_client

    async def execute_destination_check_connection(
        self,
        *,
        connection_configuration: DestinationConfiguration,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        destination_id: typing.Optional[DestinationId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckConnectionRead:
        """
        Parameters
        ----------
        connection_configuration : DestinationConfiguration

        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        destination_id : typing.Optional[DestinationId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckConnectionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.scheduler.execute_destination_check_connection(
                connection_configuration={"user": "charles"},
                destination_definition_id="destinationDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_destination_check_connection(
            connection_configuration=connection_configuration,
            destination_definition_id=destination_definition_id,
            workspace_id=workspace_id,
            destination_id=destination_id,
            request_options=request_options,
        )
        return _response.data

    async def execute_source_check_connection(
        self,
        *,
        connection_configuration: SourceConfiguration,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckConnectionRead:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        source_id : typing.Optional[SourceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckConnectionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.scheduler.execute_source_check_connection(
                connection_configuration={"user": "charles"},
                source_definition_id="sourceDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_source_check_connection(
            connection_configuration=connection_configuration,
            source_definition_id=source_definition_id,
            workspace_id=workspace_id,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data

    async def execute_source_discover_schema(
        self,
        *,
        connection_configuration: SourceConfiguration,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceDiscoverSchemaRead:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        source_id : typing.Optional[SourceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDiscoverSchemaRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.scheduler.execute_source_discover_schema(
                connection_configuration={"user": "charles"},
                source_definition_id="sourceDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_source_discover_schema(
            connection_configuration=connection_configuration,
            source_definition_id=source_definition_id,
            workspace_id=workspace_id,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data
