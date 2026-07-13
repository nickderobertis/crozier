

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.monetary_account_listing import MonetaryAccountListing
from ..types.monetary_account_read import MonetaryAccountRead
from .raw_client import AsyncRawMonetaryAccountClient, RawMonetaryAccountClient


class MonetaryAccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMonetaryAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMonetaryAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMonetaryAccountClient
        """
        return self._raw_client

    def list_all_monetary_account_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonetaryAccountListing]:
        """
        Get a collection of all your MonetaryAccounts.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonetaryAccountListing]
            Used to show the MonetaryAccounts that you can access. Currently the only MonetaryAccount type is MonetaryAccountBank. See also: monetary-account-bank.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/2/page/callbacks">dedicated callbacks page</a>.

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
        client.monetary_account.list_all_monetary_account_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_monetary_account_for_user(user_id, request_options=request_options)
        return _response.data

    def read_monetary_account_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MonetaryAccountRead:
        """
        Get a specific MonetaryAccount.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountRead
            Used to show the MonetaryAccounts that you can access. Currently the only MonetaryAccount type is MonetaryAccountBank. See also: monetary-account-bank.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/2/page/callbacks">dedicated callbacks page</a>.

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
        client.monetary_account.read_monetary_account_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_monetary_account_for_user(user_id, item_id, request_options=request_options)
        return _response.data


class AsyncMonetaryAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMonetaryAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMonetaryAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMonetaryAccountClient
        """
        return self._raw_client

    async def list_all_monetary_account_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonetaryAccountListing]:
        """
        Get a collection of all your MonetaryAccounts.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonetaryAccountListing]
            Used to show the MonetaryAccounts that you can access. Currently the only MonetaryAccount type is MonetaryAccountBank. See also: monetary-account-bank.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/2/page/callbacks">dedicated callbacks page</a>.

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
            await client.monetary_account.list_all_monetary_account_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_monetary_account_for_user(user_id, request_options=request_options)
        return _response.data

    async def read_monetary_account_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MonetaryAccountRead:
        """
        Get a specific MonetaryAccount.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonetaryAccountRead
            Used to show the MonetaryAccounts that you can access. Currently the only MonetaryAccount type is MonetaryAccountBank. See also: monetary-account-bank.<br/><br/>Notification filters can be set on a monetary account level to receive callbacks. For more information check the <a href="/api/2/page/callbacks">dedicated callbacks page</a>.

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
            await client.monetary_account.read_monetary_account_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_monetary_account_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
