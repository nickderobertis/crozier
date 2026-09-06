

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_response import ApiResponse
from ..types.connection_status import ConnectionStatus
from .raw_client import AsyncRawConnectionsClient, RawConnectionsClient


class ConnectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConnectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConnectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConnectionsClient
        """
        return self._raw_client

    def get_connections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ConnectionStatus]:
        """
        Returns the active users and info about their current uploads/downloads

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ConnectionStatus]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.connections.get_connections()
        """
        _response = self._raw_client.get_connections(request_options=request_options)
        return _response.data

    def close_connection(
        self, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Terminates an active connection

        Parameters
        ----------
        connection_id : str
            ID of the connection to close

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.connections.close_connection(
            connection_id="connectionID",
        )
        """
        _response = self._raw_client.close_connection(connection_id, request_options=request_options)
        return _response.data


class AsyncConnectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConnectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConnectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConnectionsClient
        """
        return self._raw_client

    async def get_connections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ConnectionStatus]:
        """
        Returns the active users and info about their current uploads/downloads

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ConnectionStatus]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.connections.get_connections()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_connections(request_options=request_options)
        return _response.data

    async def close_connection(
        self, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Terminates an active connection

        Parameters
        ----------
        connection_id : str
            ID of the connection to close

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.connections.close_connection(
                connection_id="connectionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.close_connection(connection_id, request_options=request_options)
        return _response.data
