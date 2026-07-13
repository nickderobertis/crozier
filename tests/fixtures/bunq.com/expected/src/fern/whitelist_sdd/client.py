

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.whitelist_sdd_listing import WhitelistSddListing
from ..types.whitelist_sdd_monetary_account_paying_listing import WhitelistSddMonetaryAccountPayingListing
from ..types.whitelist_sdd_monetary_account_paying_read import WhitelistSddMonetaryAccountPayingRead
from ..types.whitelist_sdd_read import WhitelistSddRead
from .raw_client import AsyncRawWhitelistSddClient, RawWhitelistSddClient


class WhitelistSddClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWhitelistSddClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWhitelistSddClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWhitelistSddClient
        """
        return self._raw_client

    def list_all_whitelist_sdd_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WhitelistSddMonetaryAccountPayingListing]:
        """
        Get a listing of all SDD whitelist entries for a target monetary account.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WhitelistSddMonetaryAccountPayingListing]
            Whitelist an SDD so that when one comes in, it is automatically accepted.

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
        client.whitelist_sdd.list_all_whitelist_sdd_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_whitelist_sdd_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def read_whitelist_sdd_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WhitelistSddMonetaryAccountPayingRead:
        """
        Get a specific SDD whitelist entry.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhitelistSddMonetaryAccountPayingRead
            Whitelist an SDD so that when one comes in, it is automatically accepted.

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
        client.whitelist_sdd.read_whitelist_sdd_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_whitelist_sdd_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def list_all_whitelist_sdd_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WhitelistSddListing]:
        """
        Get a listing of all recurring SDD whitelist entries for a target monetary account.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WhitelistSddListing]
            Depreciated route, replaced with whitelist-sdd-recurring

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
        client.whitelist_sdd.list_all_whitelist_sdd_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_whitelist_sdd_for_user(user_id, request_options=request_options)
        return _response.data

    def read_whitelist_sdd_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhitelistSddRead:
        """
        Get a specific recurring SDD whitelist entry.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhitelistSddRead
            Depreciated route, replaced with whitelist-sdd-recurring

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
        client.whitelist_sdd.read_whitelist_sdd_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_whitelist_sdd_for_user(user_id, item_id, request_options=request_options)
        return _response.data


class AsyncWhitelistSddClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWhitelistSddClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWhitelistSddClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWhitelistSddClient
        """
        return self._raw_client

    async def list_all_whitelist_sdd_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WhitelistSddMonetaryAccountPayingListing]:
        """
        Get a listing of all SDD whitelist entries for a target monetary account.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WhitelistSddMonetaryAccountPayingListing]
            Whitelist an SDD so that when one comes in, it is automatically accepted.

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
            await client.whitelist_sdd.list_all_whitelist_sdd_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_whitelist_sdd_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def read_whitelist_sdd_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WhitelistSddMonetaryAccountPayingRead:
        """
        Get a specific SDD whitelist entry.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhitelistSddMonetaryAccountPayingRead
            Whitelist an SDD so that when one comes in, it is automatically accepted.

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
            await client.whitelist_sdd.read_whitelist_sdd_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_whitelist_sdd_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def list_all_whitelist_sdd_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WhitelistSddListing]:
        """
        Get a listing of all recurring SDD whitelist entries for a target monetary account.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WhitelistSddListing]
            Depreciated route, replaced with whitelist-sdd-recurring

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
            await client.whitelist_sdd.list_all_whitelist_sdd_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_whitelist_sdd_for_user(user_id, request_options=request_options)
        return _response.data

    async def read_whitelist_sdd_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhitelistSddRead:
        """
        Get a specific recurring SDD whitelist entry.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhitelistSddRead
            Depreciated route, replaced with whitelist-sdd-recurring

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
            await client.whitelist_sdd.read_whitelist_sdd_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_whitelist_sdd_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
