

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.feature_announcement_read import FeatureAnnouncementRead
from .raw_client import AsyncRawFeatureAnnouncementClient, RawFeatureAnnouncementClient


class FeatureAnnouncementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFeatureAnnouncementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFeatureAnnouncementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFeatureAnnouncementClient
        """
        return self._raw_client

    def read_feature_announcement_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeatureAnnouncementRead:
        """
        view for updating the feature display.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeatureAnnouncementRead
            view for updating the feature display.

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
        client.feature_announcement.read_feature_announcement_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_feature_announcement_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncFeatureAnnouncementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFeatureAnnouncementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFeatureAnnouncementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFeatureAnnouncementClient
        """
        return self._raw_client

    async def read_feature_announcement_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FeatureAnnouncementRead:
        """
        view for updating the feature display.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeatureAnnouncementRead
            view for updating the feature display.

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
            await client.feature_announcement.read_feature_announcement_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_feature_announcement_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
