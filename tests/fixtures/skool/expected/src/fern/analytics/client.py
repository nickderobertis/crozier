

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAnalyticsClient, RawAnalyticsClient
from .types.get_group_analytics_response import GetGroupAnalyticsResponse


class AnalyticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAnalyticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAnalyticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAnalyticsClient
        """
        return self._raw_client

    def get_group_analytics(
        self,
        group_slug: str,
        *,
        session_id: str,
        start_date: typing.Optional[dt.date] = None,
        end_date: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetGroupAnalyticsResponse:
        """
        Retrieve analytics data for a Skool group.

        Parameters
        ----------
        group_slug : str

        session_id : str

        start_date : typing.Optional[dt.date]

        end_date : typing.Optional[dt.date]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGroupAnalyticsResponse
            Analytics data

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.analytics.get_group_analytics(
            group_slug="group_slug",
            session_id="session_id",
        )
        """
        _response = self._raw_client.get_group_analytics(
            group_slug, session_id=session_id, start_date=start_date, end_date=end_date, request_options=request_options
        )
        return _response.data


class AsyncAnalyticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAnalyticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAnalyticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAnalyticsClient
        """
        return self._raw_client

    async def get_group_analytics(
        self,
        group_slug: str,
        *,
        session_id: str,
        start_date: typing.Optional[dt.date] = None,
        end_date: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetGroupAnalyticsResponse:
        """
        Retrieve analytics data for a Skool group.

        Parameters
        ----------
        group_slug : str

        session_id : str

        start_date : typing.Optional[dt.date]

        end_date : typing.Optional[dt.date]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGroupAnalyticsResponse
            Analytics data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.analytics.get_group_analytics(
                group_slug="group_slug",
                session_id="session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_group_analytics(
            group_slug, session_id=session_id, start_date=start_date, end_date=end_date, request_options=request_options
        )
        return _response.data
