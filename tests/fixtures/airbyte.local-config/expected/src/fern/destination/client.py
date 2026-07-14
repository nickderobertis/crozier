

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.check_connection_read import CheckConnectionRead
from ..types.destination_clone_configuration import DestinationCloneConfiguration
from ..types.destination_configuration import DestinationConfiguration
from ..types.destination_definition_id import DestinationDefinitionId
from ..types.destination_id import DestinationId
from ..types.destination_read import DestinationRead
from ..types.destination_read_list import DestinationReadList
from ..types.workspace_id import WorkspaceId
from .raw_client import AsyncRawDestinationClient, RawDestinationClient


OMIT = typing.cast(typing.Any, ...)


class DestinationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDestinationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDestinationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDestinationClient
        """
        return self._raw_client

    def check_connection_to_destination(
        self, *, destination_id: DestinationId, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckConnectionRead:
        """
        Parameters
        ----------
        destination_id : DestinationId

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
        client.destination.check_connection_to_destination(
            destination_id="destinationId",
        )
        """
        _response = self._raw_client.check_connection_to_destination(
            destination_id=destination_id, request_options=request_options
        )
        return _response.data

    def check_connection_to_destination_for_update(
        self,
        *,
        connection_configuration: DestinationConfiguration,
        destination_id: DestinationId,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckConnectionRead:
        """
        Parameters
        ----------
        connection_configuration : DestinationConfiguration

        destination_id : DestinationId

        name : str

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
        client.destination.check_connection_to_destination_for_update(
            connection_configuration={"user": "charles"},
            destination_id="destinationId",
            name="name",
        )
        """
        _response = self._raw_client.check_connection_to_destination_for_update(
            connection_configuration=connection_configuration,
            destination_id=destination_id,
            name=name,
            request_options=request_options,
        )
        return _response.data

    def clone_destination(
        self,
        *,
        destination_clone_id: DestinationId,
        destination_configuration: typing.Optional[DestinationCloneConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationRead:
        """
        Parameters
        ----------
        destination_clone_id : DestinationId

        destination_configuration : typing.Optional[DestinationCloneConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination.clone_destination(
            destination_clone_id="destinationCloneId",
        )
        """
        _response = self._raw_client.clone_destination(
            destination_clone_id=destination_clone_id,
            destination_configuration=destination_configuration,
            request_options=request_options,
        )
        return _response.data

    def create_destination(
        self,
        *,
        connection_configuration: DestinationConfiguration,
        destination_definition_id: DestinationDefinitionId,
        name: str,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationRead:
        """
        Parameters
        ----------
        connection_configuration : DestinationConfiguration

        destination_definition_id : DestinationDefinitionId

        name : str

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination.create_destination(
            connection_configuration={"user": "charles"},
            destination_definition_id="destinationDefinitionId",
            name="name",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.create_destination(
            connection_configuration=connection_configuration,
            destination_definition_id=destination_definition_id,
            name=name,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    def delete_destination(
        self, *, destination_id: DestinationId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        destination_id : DestinationId

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
        client.destination.delete_destination(
            destination_id="destinationId",
        )
        """
        _response = self._raw_client.delete_destination(destination_id=destination_id, request_options=request_options)
        return _response.data

    def get_destination(
        self, *, destination_id: DestinationId, request_options: typing.Optional[RequestOptions] = None
    ) -> DestinationRead:
        """
        Parameters
        ----------
        destination_id : DestinationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination.get_destination(
            destination_id="destinationId",
        )
        """
        _response = self._raw_client.get_destination(destination_id=destination_id, request_options=request_options)
        return _response.data

    def list_destinations_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> DestinationReadList:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination.list_destinations_for_workspace(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_destinations_for_workspace(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def search_destinations(
        self,
        *,
        connection_configuration: typing.Optional[DestinationConfiguration] = OMIT,
        destination_definition_id: typing.Optional[DestinationDefinitionId] = OMIT,
        destination_id: typing.Optional[DestinationId] = OMIT,
        destination_name: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        workspace_id: typing.Optional[WorkspaceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationReadList:
        """
        Parameters
        ----------
        connection_configuration : typing.Optional[DestinationConfiguration]

        destination_definition_id : typing.Optional[DestinationDefinitionId]

        destination_id : typing.Optional[DestinationId]

        destination_name : typing.Optional[str]

        name : typing.Optional[str]

        workspace_id : typing.Optional[WorkspaceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination.search_destinations()
        """
        _response = self._raw_client.search_destinations(
            connection_configuration=connection_configuration,
            destination_definition_id=destination_definition_id,
            destination_id=destination_id,
            destination_name=destination_name,
            name=name,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    def update_destination(
        self,
        *,
        connection_configuration: DestinationConfiguration,
        destination_id: DestinationId,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationRead:
        """
        Parameters
        ----------
        connection_configuration : DestinationConfiguration

        destination_id : DestinationId

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination.update_destination(
            connection_configuration={"user": "charles"},
            destination_id="destinationId",
            name="name",
        )
        """
        _response = self._raw_client.update_destination(
            connection_configuration=connection_configuration,
            destination_id=destination_id,
            name=name,
            request_options=request_options,
        )
        return _response.data


class AsyncDestinationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDestinationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDestinationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDestinationClient
        """
        return self._raw_client

    async def check_connection_to_destination(
        self, *, destination_id: DestinationId, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckConnectionRead:
        """
        Parameters
        ----------
        destination_id : DestinationId

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
            await client.destination.check_connection_to_destination(
                destination_id="destinationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_connection_to_destination(
            destination_id=destination_id, request_options=request_options
        )
        return _response.data

    async def check_connection_to_destination_for_update(
        self,
        *,
        connection_configuration: DestinationConfiguration,
        destination_id: DestinationId,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckConnectionRead:
        """
        Parameters
        ----------
        connection_configuration : DestinationConfiguration

        destination_id : DestinationId

        name : str

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
            await client.destination.check_connection_to_destination_for_update(
                connection_configuration={"user": "charles"},
                destination_id="destinationId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_connection_to_destination_for_update(
            connection_configuration=connection_configuration,
            destination_id=destination_id,
            name=name,
            request_options=request_options,
        )
        return _response.data

    async def clone_destination(
        self,
        *,
        destination_clone_id: DestinationId,
        destination_configuration: typing.Optional[DestinationCloneConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationRead:
        """
        Parameters
        ----------
        destination_clone_id : DestinationId

        destination_configuration : typing.Optional[DestinationCloneConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination.clone_destination(
                destination_clone_id="destinationCloneId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clone_destination(
            destination_clone_id=destination_clone_id,
            destination_configuration=destination_configuration,
            request_options=request_options,
        )
        return _response.data

    async def create_destination(
        self,
        *,
        connection_configuration: DestinationConfiguration,
        destination_definition_id: DestinationDefinitionId,
        name: str,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationRead:
        """
        Parameters
        ----------
        connection_configuration : DestinationConfiguration

        destination_definition_id : DestinationDefinitionId

        name : str

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination.create_destination(
                connection_configuration={"user": "charles"},
                destination_definition_id="destinationDefinitionId",
                name="name",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_destination(
            connection_configuration=connection_configuration,
            destination_definition_id=destination_definition_id,
            name=name,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    async def delete_destination(
        self, *, destination_id: DestinationId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        destination_id : DestinationId

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
            await client.destination.delete_destination(
                destination_id="destinationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_destination(
            destination_id=destination_id, request_options=request_options
        )
        return _response.data

    async def get_destination(
        self, *, destination_id: DestinationId, request_options: typing.Optional[RequestOptions] = None
    ) -> DestinationRead:
        """
        Parameters
        ----------
        destination_id : DestinationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination.get_destination(
                destination_id="destinationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_destination(
            destination_id=destination_id, request_options=request_options
        )
        return _response.data

    async def list_destinations_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> DestinationReadList:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination.list_destinations_for_workspace(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_destinations_for_workspace(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def search_destinations(
        self,
        *,
        connection_configuration: typing.Optional[DestinationConfiguration] = OMIT,
        destination_definition_id: typing.Optional[DestinationDefinitionId] = OMIT,
        destination_id: typing.Optional[DestinationId] = OMIT,
        destination_name: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        workspace_id: typing.Optional[WorkspaceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationReadList:
        """
        Parameters
        ----------
        connection_configuration : typing.Optional[DestinationConfiguration]

        destination_definition_id : typing.Optional[DestinationDefinitionId]

        destination_id : typing.Optional[DestinationId]

        destination_name : typing.Optional[str]

        name : typing.Optional[str]

        workspace_id : typing.Optional[WorkspaceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination.search_destinations()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_destinations(
            connection_configuration=connection_configuration,
            destination_definition_id=destination_definition_id,
            destination_id=destination_id,
            destination_name=destination_name,
            name=name,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    async def update_destination(
        self,
        *,
        connection_configuration: DestinationConfiguration,
        destination_id: DestinationId,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationRead:
        """
        Parameters
        ----------
        connection_configuration : DestinationConfiguration

        destination_id : DestinationId

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination.update_destination(
                connection_configuration={"user": "charles"},
                destination_id="destinationId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_destination(
            connection_configuration=connection_configuration,
            destination_id=destination_id,
            name=name,
            request_options=request_options,
        )
        return _response.data
