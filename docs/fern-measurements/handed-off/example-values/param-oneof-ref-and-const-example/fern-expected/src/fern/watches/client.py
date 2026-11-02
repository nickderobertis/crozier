

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWatchesClient, RawWatchesClient
from .types.end_watch_request_watch_id import EndWatchRequestWatchId
from .types.list_watches_request_scope import ListWatchesRequestScope


class WatchesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWatchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWatchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWatchesClient
        """
        return self._raw_client

    def end_watch(
        self, watch_id: EndWatchRequestWatchId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        watch_id : EndWatchRequestWatchId
            The watch to end, or `every` for all watches.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.watches.end_watch(
            watch_id="7c1e2a90-55b1-4d0a-9e57-3f0c2b6d8a11",
        )
        """
        _response = self._raw_client.end_watch(watch_id, request_options=request_options)
        return _response.data

    def list_watches(
        self, *, scope: ListWatchesRequestScope, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        scope : ListWatchesRequestScope

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Watches

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.watches.list_watches(
            scope="7c1e2a90-55b1-4d0a-9e57-3f0c2b6d8a11",
        )
        """
        _response = self._raw_client.list_watches(scope=scope, request_options=request_options)
        return _response.data


class AsyncWatchesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWatchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWatchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWatchesClient
        """
        return self._raw_client

    async def end_watch(
        self, watch_id: EndWatchRequestWatchId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        watch_id : EndWatchRequestWatchId
            The watch to end, or `every` for all watches.

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.watches.end_watch(
                watch_id="7c1e2a90-55b1-4d0a-9e57-3f0c2b6d8a11",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.end_watch(watch_id, request_options=request_options)
        return _response.data

    async def list_watches(
        self, *, scope: ListWatchesRequestScope, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        scope : ListWatchesRequestScope

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Watches

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.watches.list_watches(
                scope="7c1e2a90-55b1-4d0a-9e57-3f0c2b6d8a11",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_watches(scope=scope, request_options=request_options)
        return _response.data
