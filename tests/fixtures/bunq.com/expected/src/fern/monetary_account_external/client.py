

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.monetary_account_external_listing import MonetaryAccountExternalListing
from ..types.monetary_account_external_read import MonetaryAccountExternalRead
from .raw_client import AsyncRawMonetaryAccountExternalClient, RawMonetaryAccountExternalClient


class MonetaryAccountExternalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMonetaryAccountExternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMonetaryAccountExternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMonetaryAccountExternalClient
        """
        return self._raw_client

    def list_all_monetary_account_external_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonetaryAccountExternalListing]:
        """
        Endpoint for managing monetary accounts which are connected to external services.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonetaryAccountExternalListing]
            Endpoint for managing monetary accounts which are connected to external services.

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
        client.monetary_account_external.list_all_monetary_account_external_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_monetary_account_external_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    def read_monetary_account_external_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MonetaryAccountExternalRead:
        """
        Endpoint for managing monetary accounts which are connected to external services.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountExternalRead
            Endpoint for managing monetary accounts which are connected to external services.

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
        client.monetary_account_external.read_monetary_account_external_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_monetary_account_external_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncMonetaryAccountExternalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMonetaryAccountExternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMonetaryAccountExternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMonetaryAccountExternalClient
        """
        return self._raw_client

    async def list_all_monetary_account_external_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonetaryAccountExternalListing]:
        """
        Endpoint for managing monetary accounts which are connected to external services.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonetaryAccountExternalListing]
            Endpoint for managing monetary accounts which are connected to external services.

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
            await client.monetary_account_external.list_all_monetary_account_external_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_monetary_account_external_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def read_monetary_account_external_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MonetaryAccountExternalRead:
        """
        Endpoint for managing monetary accounts which are connected to external services.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountExternalRead
            Endpoint for managing monetary accounts which are connected to external services.

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
            await client.monetary_account_external.read_monetary_account_external_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_monetary_account_external_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
