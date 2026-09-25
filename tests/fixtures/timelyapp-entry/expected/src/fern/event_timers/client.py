

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1hour import V1Hour
from .raw_client import AsyncRawEventTimersClient, RawEventTimersClient


class EventTimersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventTimersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventTimersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventTimersClient
        """
        return self._raw_client

    def start_timer(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Hour:
        """
        Start the timer for a specific time entry.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Time entry ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Hour
            Timer started

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event_timers.start_timer(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.start_timer(account_id, id, request_options=request_options)
        return _response.data

    def stop_timer(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Hour:
        """
        Stop the timer for a specific time entry.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Time entry ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Hour
            Timer stopped

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event_timers.stop_timer(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.stop_timer(account_id, id, request_options=request_options)
        return _response.data


class AsyncEventTimersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventTimersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventTimersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventTimersClient
        """
        return self._raw_client

    async def start_timer(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Hour:
        """
        Start the timer for a specific time entry.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Time entry ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Hour
            Timer started

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event_timers.start_timer(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_timer(account_id, id, request_options=request_options)
        return _response.data

    async def stop_timer(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Hour:
        """
        Stop the timer for a specific time entry.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Time entry ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Hour
            Timer stopped

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event_timers.stop_timer(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_timer(account_id, id, request_options=request_options)
        return _response.data
