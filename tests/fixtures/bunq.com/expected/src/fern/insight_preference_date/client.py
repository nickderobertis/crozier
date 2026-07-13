

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.insight_preference_date_listing import InsightPreferenceDateListing
from .raw_client import AsyncRawInsightPreferenceDateClient, RawInsightPreferenceDateClient


class InsightPreferenceDateClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInsightPreferenceDateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInsightPreferenceDateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInsightPreferenceDateClient
        """
        return self._raw_client

    def list_all_insight_preference_date_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InsightPreferenceDateListing]:
        """
        Used to allow users to set insight/budget preferences.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InsightPreferenceDateListing]
            Used to allow users to set insight/budget preferences.

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
        client.insight_preference_date.list_all_insight_preference_date_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_insight_preference_date_for_user(user_id, request_options=request_options)
        return _response.data


class AsyncInsightPreferenceDateClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInsightPreferenceDateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInsightPreferenceDateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInsightPreferenceDateClient
        """
        return self._raw_client

    async def list_all_insight_preference_date_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InsightPreferenceDateListing]:
        """
        Used to allow users to set insight/budget preferences.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InsightPreferenceDateListing]
            Used to allow users to set insight/budget preferences.

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
            await client.insight_preference_date.list_all_insight_preference_date_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_insight_preference_date_for_user(
            user_id, request_options=request_options
        )
        return _response.data
