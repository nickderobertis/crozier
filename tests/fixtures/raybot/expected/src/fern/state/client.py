

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.limit_switch_state import LimitSwitchState
from .raw_client import AsyncRawStateClient, RawStateClient


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

    def get_limit_switch_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> LimitSwitchState:
        """
        Get the limit switch state

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LimitSwitchState
            The limit switch state

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.state.get_limit_switch_state()
        """
        _response = self._raw_client.get_limit_switch_state(request_options=request_options)
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

    async def get_limit_switch_state(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LimitSwitchState:
        """
        Get the limit switch state

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LimitSwitchState
            The limit switch state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.state.get_limit_switch_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_limit_switch_state(request_options=request_options)
        return _response.data
