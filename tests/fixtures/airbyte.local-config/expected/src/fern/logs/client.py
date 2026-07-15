

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.log_type import LogType
from .raw_client import AsyncRawLogsClient, RawLogsClient


OMIT = typing.cast(typing.Any, ...)


class LogsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLogsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLogsClient
        """
        return self._raw_client

    def get_logs(
        self, *, log_type: LogType, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        log_type : LogType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Returns the log file

        Examples
        --------
        from fern import FernApi, LogType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.logs.get_logs(
            log_type=LogType.SERVER,
        )
        """
        with self._raw_client.get_logs(log_type=log_type, request_options=request_options) as r:
            yield from r.data


class AsyncLogsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLogsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLogsClient
        """
        return self._raw_client

    async def get_logs(
        self, *, log_type: LogType, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        log_type : LogType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Returns the log file

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LogType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.logs.get_logs(
                log_type=LogType.SERVER,
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_logs(log_type=log_type, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
