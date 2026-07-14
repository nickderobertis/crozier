

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.connection_id import ConnectionId
from ..types.connection_state import ConnectionState
from .raw_client import AsyncRawStateClient, RawStateClient


OMIT = typing.cast(typing.Any, ...)


class StateClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStateClient
        """
        return self._raw_client

    def create_or_update_state(
        self,
        *,
        connection_id: ConnectionId,
        connection_state: ConnectionState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionState:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        connection_state : ConnectionState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionState
            Successful operation

        Examples
        --------
        from fern import ConnectionState, ConnectionStateType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.state.create_or_update_state(
            connection_id="connectionId",
            connection_state=ConnectionState(
                connection_id="connectionId",
                state_type=ConnectionStateType.GLOBAL,
            ),
        )
        """
        _response = self._raw_client.create_or_update_state(
            connection_id=connection_id, connection_state=connection_state, request_options=request_options
        )
        return _response.data

    def get_state(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionState:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionState
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.state.get_state(
            connection_id="connectionId",
        )
        """
        _response = self._raw_client.get_state(connection_id=connection_id, request_options=request_options)
        return _response.data


class AsyncStateClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStateClient
        """
        return self._raw_client

    async def create_or_update_state(
        self,
        *,
        connection_id: ConnectionId,
        connection_state: ConnectionState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionState:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        connection_state : ConnectionState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionState
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ConnectionState, ConnectionStateType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.state.create_or_update_state(
                connection_id="connectionId",
                connection_state=ConnectionState(
                    connection_id="connectionId",
                    state_type=ConnectionStateType.GLOBAL,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_update_state(
            connection_id=connection_id, connection_state=connection_state, request_options=request_options
        )
        return _response.data

    async def get_state(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionState:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionState
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.state.get_state(
                connection_id="connectionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_state(connection_id=connection_id, request_options=request_options)
        return _response.data
