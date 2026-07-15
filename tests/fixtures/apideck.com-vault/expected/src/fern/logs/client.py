

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_logs_response import GetLogsResponse
from ..types.logs_filter import LogsFilter
from .raw_client import AsyncRawLogsClient, RawLogsClient


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

    def all_(
        self,
        *,
        apideck_consumer_id: str,
        filter: typing.Optional[LogsFilter] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLogsResponse:
        """
        This endpoint includes all consumer request logs.

        Parameters
        ----------
        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        filter : typing.Optional[LogsFilter]
            Filter results

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLogsResponse
            Logs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.logs.all_(
            apideck_consumer_id="x-apideck-consumer-id",
        )
        """
        _response = self._raw_client.all_(
            apideck_consumer_id=apideck_consumer_id,
            filter=filter,
            cursor=cursor,
            limit=limit,
            request_options=request_options,
        )
        return _response.data


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

    async def all_(
        self,
        *,
        apideck_consumer_id: str,
        filter: typing.Optional[LogsFilter] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLogsResponse:
        """
        This endpoint includes all consumer request logs.

        Parameters
        ----------
        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        filter : typing.Optional[LogsFilter]
            Filter results

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLogsResponse
            Logs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.logs.all_(
                apideck_consumer_id="x-apideck-consumer-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            apideck_consumer_id=apideck_consumer_id,
            filter=filter,
            cursor=cursor,
            limit=limit,
            request_options=request_options,
        )
        return _response.data
