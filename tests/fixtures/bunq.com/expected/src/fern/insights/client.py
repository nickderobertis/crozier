

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.insight_listing import InsightListing
from .raw_client import AsyncRawInsightsClient, RawInsightsClient


class InsightsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInsightsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInsightsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInsightsClient
        """
        return self._raw_client

    def list_all_insights_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InsightListing]:
        """
        Used to get insights about transactions between given time range.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InsightListing]
            Used to get insights about transactions between given time range.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.insights.list_all_insights_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_insights_for_user(user_id, request_options=request_options)
        return _response.data


class AsyncInsightsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInsightsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInsightsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInsightsClient
        """
        return self._raw_client

    async def list_all_insights_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InsightListing]:
        """
        Used to get insights about transactions between given time range.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InsightListing]
            Used to get insights about transactions between given time range.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.insights.list_all_insights_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_insights_for_user(user_id, request_options=request_options)
        return _response.data
