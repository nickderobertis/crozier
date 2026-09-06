

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawActivityLogsClient, RawActivityLogsClient
from .types.list_activity_logs_response import ListActivityLogsResponse


class ActivityLogsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawActivityLogsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawActivityLogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawActivityLogsClient
        """
        return self._raw_client

    def list(
        self,
        site_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListActivityLogsResponse:
        """
        Retrieve Activity Logs for a specific Site.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `site_activity:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListActivityLogsResponse
            A list of site activity logs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.activity_logs.list(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.list(site_id, limit=limit, offset=offset, request_options=request_options)
        return _response.data


class AsyncActivityLogsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawActivityLogsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawActivityLogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawActivityLogsClient
        """
        return self._raw_client

    async def list(
        self,
        site_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListActivityLogsResponse:
        """
        Retrieve Activity Logs for a specific Site.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `site_activity:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListActivityLogsResponse
            A list of site activity logs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.activity_logs.list(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(site_id, limit=limit, offset=offset, request_options=request_options)
        return _response.data
