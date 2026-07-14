

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.actor_catalog_with_updated_at import ActorCatalogWithUpdatedAt
from ..types.airbyte_catalog import AirbyteCatalog
from ..types.check_connection_read import CheckConnectionRead
from ..types.discover_catalog_result import DiscoverCatalogResult
from ..types.source_clone_configuration import SourceCloneConfiguration
from ..types.source_configuration import SourceConfiguration
from ..types.source_definition_id import SourceDefinitionId
from ..types.source_discover_schema_read import SourceDiscoverSchemaRead
from ..types.source_id import SourceId
from ..types.source_read import SourceRead
from ..types.source_read_list import SourceReadList
from ..types.workspace_id import WorkspaceId
from .raw_client import AsyncRawSourceClient, RawSourceClient


OMIT = typing.cast(typing.Any, ...)


class SourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSourceClient
        """
        return self._raw_client

    def check_connection_to_source(
        self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckConnectionRead:
        """
        Parameters
        ----------
        source_id : SourceId

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
        client.source.check_connection_to_source(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.check_connection_to_source(source_id=source_id, request_options=request_options)
        return _response.data

    def check_connection_to_source_for_update(
        self,
        *,
        connection_configuration: SourceConfiguration,
        name: str,
        source_id: SourceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckConnectionRead:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        name : str

        source_id : SourceId

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
        client.source.check_connection_to_source_for_update(
            connection_configuration={"user": "charles"},
            name="name",
            source_id="sourceId",
        )
        """
        _response = self._raw_client.check_connection_to_source_for_update(
            connection_configuration=connection_configuration,
            name=name,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data

    def clone_source(
        self,
        *,
        source_clone_id: SourceId,
        source_configuration: typing.Optional[SourceCloneConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceRead:
        """
        Parameters
        ----------
        source_clone_id : SourceId

        source_configuration : typing.Optional[SourceCloneConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source.clone_source(
            source_clone_id="sourceCloneId",
        )
        """
        _response = self._raw_client.clone_source(
            source_clone_id=source_clone_id, source_configuration=source_configuration, request_options=request_options
        )
        return _response.data

    def create_source(
        self,
        *,
        connection_configuration: SourceConfiguration,
        name: str,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceRead:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        name : str

        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source.create_source(
            connection_configuration={"user": "charles"},
            name="name",
            source_definition_id="sourceDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.create_source(
            connection_configuration=connection_configuration,
            name=name,
            source_definition_id=source_definition_id,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    def delete_source(self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        source_id : SourceId

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
        client.source.delete_source(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.delete_source(source_id=source_id, request_options=request_options)
        return _response.data

    def discover_schema_for_source(
        self,
        *,
        source_id: SourceId,
        connection_id: typing.Optional[str] = OMIT,
        disable_cache: typing.Optional[bool] = OMIT,
        notify_schema_change: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceDiscoverSchemaRead:
        """
        Parameters
        ----------
        source_id : SourceId

        connection_id : typing.Optional[str]

        disable_cache : typing.Optional[bool]

        notify_schema_change : typing.Optional[bool]

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
        client.source.discover_schema_for_source(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.discover_schema_for_source(
            source_id=source_id,
            connection_id=connection_id,
            disable_cache=disable_cache,
            notify_schema_change=notify_schema_change,
            request_options=request_options,
        )
        return _response.data

    def get_source(self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None) -> SourceRead:
        """
        Parameters
        ----------
        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source.get_source(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.get_source(source_id=source_id, request_options=request_options)
        return _response.data

    def list_sources_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceReadList:
        """
        List sources for workspace. Does not return deleted sources.

        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source.list_sources_for_workspace(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_sources_for_workspace(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def get_most_recent_source_actor_catalog(
        self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None
    ) -> ActorCatalogWithUpdatedAt:
        """
        Parameters
        ----------
        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActorCatalogWithUpdatedAt
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source.get_most_recent_source_actor_catalog(
            source_id="sourceId",
        )
        """
        _response = self._raw_client.get_most_recent_source_actor_catalog(
            source_id=source_id, request_options=request_options
        )
        return _response.data

    def search_sources(
        self,
        *,
        connection_configuration: typing.Optional[SourceConfiguration] = OMIT,
        name: typing.Optional[str] = OMIT,
        source_definition_id: typing.Optional[SourceDefinitionId] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        source_name: typing.Optional[str] = OMIT,
        workspace_id: typing.Optional[WorkspaceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceReadList:
        """
        Parameters
        ----------
        connection_configuration : typing.Optional[SourceConfiguration]

        name : typing.Optional[str]

        source_definition_id : typing.Optional[SourceDefinitionId]

        source_id : typing.Optional[SourceId]

        source_name : typing.Optional[str]

        workspace_id : typing.Optional[WorkspaceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source.search_sources()
        """
        _response = self._raw_client.search_sources(
            connection_configuration=connection_configuration,
            name=name,
            source_definition_id=source_definition_id,
            source_id=source_id,
            source_name=source_name,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    def update_source(
        self,
        *,
        connection_configuration: SourceConfiguration,
        name: str,
        source_id: SourceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceRead:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        name : str

        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source.update_source(
            connection_configuration={"user": "charles"},
            name="name",
            source_id="sourceId",
        )
        """
        _response = self._raw_client.update_source(
            connection_configuration=connection_configuration,
            name=name,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data

    def write_discover_catalog_result(
        self,
        *,
        catalog: AirbyteCatalog,
        configuration_hash: typing.Optional[str] = OMIT,
        connector_version: typing.Optional[str] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DiscoverCatalogResult:
        """
        Parameters
        ----------
        catalog : AirbyteCatalog

        configuration_hash : typing.Optional[str]

        connector_version : typing.Optional[str]

        source_id : typing.Optional[SourceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DiscoverCatalogResult
            Successful Operation

        Examples
        --------
        from fern import AirbyteCatalog, AirbyteStreamAndConfiguration, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source.write_discover_catalog_result(
            catalog=AirbyteCatalog(
                streams=[AirbyteStreamAndConfiguration()],
            ),
        )
        """
        _response = self._raw_client.write_discover_catalog_result(
            catalog=catalog,
            configuration_hash=configuration_hash,
            connector_version=connector_version,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data


class AsyncSourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSourceClient
        """
        return self._raw_client

    async def check_connection_to_source(
        self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckConnectionRead:
        """
        Parameters
        ----------
        source_id : SourceId

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
            await client.source.check_connection_to_source(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_connection_to_source(
            source_id=source_id, request_options=request_options
        )
        return _response.data

    async def check_connection_to_source_for_update(
        self,
        *,
        connection_configuration: SourceConfiguration,
        name: str,
        source_id: SourceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckConnectionRead:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        name : str

        source_id : SourceId

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
            await client.source.check_connection_to_source_for_update(
                connection_configuration={"user": "charles"},
                name="name",
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_connection_to_source_for_update(
            connection_configuration=connection_configuration,
            name=name,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data

    async def clone_source(
        self,
        *,
        source_clone_id: SourceId,
        source_configuration: typing.Optional[SourceCloneConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceRead:
        """
        Parameters
        ----------
        source_clone_id : SourceId

        source_configuration : typing.Optional[SourceCloneConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source.clone_source(
                source_clone_id="sourceCloneId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clone_source(
            source_clone_id=source_clone_id, source_configuration=source_configuration, request_options=request_options
        )
        return _response.data

    async def create_source(
        self,
        *,
        connection_configuration: SourceConfiguration,
        name: str,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceRead:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        name : str

        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source.create_source(
                connection_configuration={"user": "charles"},
                name="name",
                source_definition_id="sourceDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_source(
            connection_configuration=connection_configuration,
            name=name,
            source_definition_id=source_definition_id,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    async def delete_source(
        self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        source_id : SourceId

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
            await client.source.delete_source(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_source(source_id=source_id, request_options=request_options)
        return _response.data

    async def discover_schema_for_source(
        self,
        *,
        source_id: SourceId,
        connection_id: typing.Optional[str] = OMIT,
        disable_cache: typing.Optional[bool] = OMIT,
        notify_schema_change: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceDiscoverSchemaRead:
        """
        Parameters
        ----------
        source_id : SourceId

        connection_id : typing.Optional[str]

        disable_cache : typing.Optional[bool]

        notify_schema_change : typing.Optional[bool]

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
            await client.source.discover_schema_for_source(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.discover_schema_for_source(
            source_id=source_id,
            connection_id=connection_id,
            disable_cache=disable_cache,
            notify_schema_change=notify_schema_change,
            request_options=request_options,
        )
        return _response.data

    async def get_source(
        self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceRead:
        """
        Parameters
        ----------
        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source.get_source(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_source(source_id=source_id, request_options=request_options)
        return _response.data

    async def list_sources_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceReadList:
        """
        List sources for workspace. Does not return deleted sources.

        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source.list_sources_for_workspace(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sources_for_workspace(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def get_most_recent_source_actor_catalog(
        self, *, source_id: SourceId, request_options: typing.Optional[RequestOptions] = None
    ) -> ActorCatalogWithUpdatedAt:
        """
        Parameters
        ----------
        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActorCatalogWithUpdatedAt
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source.get_most_recent_source_actor_catalog(
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_most_recent_source_actor_catalog(
            source_id=source_id, request_options=request_options
        )
        return _response.data

    async def search_sources(
        self,
        *,
        connection_configuration: typing.Optional[SourceConfiguration] = OMIT,
        name: typing.Optional[str] = OMIT,
        source_definition_id: typing.Optional[SourceDefinitionId] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        source_name: typing.Optional[str] = OMIT,
        workspace_id: typing.Optional[WorkspaceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceReadList:
        """
        Parameters
        ----------
        connection_configuration : typing.Optional[SourceConfiguration]

        name : typing.Optional[str]

        source_definition_id : typing.Optional[SourceDefinitionId]

        source_id : typing.Optional[SourceId]

        source_name : typing.Optional[str]

        workspace_id : typing.Optional[WorkspaceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source.search_sources()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_sources(
            connection_configuration=connection_configuration,
            name=name,
            source_definition_id=source_definition_id,
            source_id=source_id,
            source_name=source_name,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    async def update_source(
        self,
        *,
        connection_configuration: SourceConfiguration,
        name: str,
        source_id: SourceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceRead:
        """
        Parameters
        ----------
        connection_configuration : SourceConfiguration

        name : str

        source_id : SourceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source.update_source(
                connection_configuration={"user": "charles"},
                name="name",
                source_id="sourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_source(
            connection_configuration=connection_configuration,
            name=name,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data

    async def write_discover_catalog_result(
        self,
        *,
        catalog: AirbyteCatalog,
        configuration_hash: typing.Optional[str] = OMIT,
        connector_version: typing.Optional[str] = OMIT,
        source_id: typing.Optional[SourceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DiscoverCatalogResult:
        """
        Parameters
        ----------
        catalog : AirbyteCatalog

        configuration_hash : typing.Optional[str]

        connector_version : typing.Optional[str]

        source_id : typing.Optional[SourceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DiscoverCatalogResult
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AirbyteCatalog, AirbyteStreamAndConfiguration, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source.write_discover_catalog_result(
                catalog=AirbyteCatalog(
                    streams=[AirbyteStreamAndConfiguration()],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_discover_catalog_result(
            catalog=catalog,
            configuration_hash=configuration_hash,
            connector_version=connector_version,
            source_id=source_id,
            request_options=request_options,
        )
        return _response.data
