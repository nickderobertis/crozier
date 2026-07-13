

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.whitelist_sdd_one_off_create import WhitelistSddOneOffCreate
from ..types.whitelist_sdd_one_off_delete import WhitelistSddOneOffDelete
from ..types.whitelist_sdd_one_off_listing import WhitelistSddOneOffListing
from ..types.whitelist_sdd_one_off_read import WhitelistSddOneOffRead
from ..types.whitelist_sdd_one_off_update import WhitelistSddOneOffUpdate
from .raw_client import AsyncRawWhitelistSddOneOffClient, RawWhitelistSddOneOffClient


OMIT = typing.cast(typing.Any, ...)


class WhitelistSddOneOffClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWhitelistSddOneOffClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWhitelistSddOneOffClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWhitelistSddOneOffClient
        """
        return self._raw_client

    def list_all_whitelist_sdd_one_off_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WhitelistSddOneOffListing]:
        """
        Get a listing of all one off SDD whitelist entries for a target monetary account.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WhitelistSddOneOffListing]
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

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
        client.whitelist_sdd_one_off.list_all_whitelist_sdd_one_off_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_whitelist_sdd_one_off_for_user(user_id, request_options=request_options)
        return _response.data

    def create_whitelist_sdd_one_off_for_user(
        self,
        user_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WhitelistSddOneOffCreate:
        """
        Create a new one off SDD whitelist entry.

        Parameters
        ----------
        user_id : int


        monetary_account_paying_id : int
            ID of the monetary account of which you want to pay from.

        request_id : int
            ID of the request for which you want to whitelist the originating SDD.

        maximum_amount_per_month : typing.Optional[Amount]
            The maximum amount of money that is allowed to be deducted based on the whitelist.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhitelistSddOneOffCreate
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

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
        client.whitelist_sdd_one_off.create_whitelist_sdd_one_off_for_user(
            user_id=1,
            monetary_account_paying_id=1,
            request_id=1,
        )
        """
        _response = self._raw_client.create_whitelist_sdd_one_off_for_user(
            user_id,
            monetary_account_paying_id=monetary_account_paying_id,
            request_id=request_id,
            maximum_amount_per_month=maximum_amount_per_month,
            request_options=request_options,
        )
        return _response.data

    def read_whitelist_sdd_one_off_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhitelistSddOneOffRead:
        """
        Get a specific one off SDD whitelist entry.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhitelistSddOneOffRead
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

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
        client.whitelist_sdd_one_off.read_whitelist_sdd_one_off_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_whitelist_sdd_one_off_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    def update_whitelist_sdd_one_off_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WhitelistSddOneOffUpdate:
        """
        Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

        Parameters
        ----------
        user_id : int


        item_id : int


        monetary_account_paying_id : int
            ID of the monetary account of which you want to pay from.

        request_id : int
            ID of the request for which you want to whitelist the originating SDD.

        maximum_amount_per_month : typing.Optional[Amount]
            The maximum amount of money that is allowed to be deducted based on the whitelist.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhitelistSddOneOffUpdate
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

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
        client.whitelist_sdd_one_off.update_whitelist_sdd_one_off_for_user(
            user_id=1,
            item_id=1,
            monetary_account_paying_id=1,
            request_id=1,
        )
        """
        _response = self._raw_client.update_whitelist_sdd_one_off_for_user(
            user_id,
            item_id,
            monetary_account_paying_id=monetary_account_paying_id,
            request_id=request_id,
            maximum_amount_per_month=maximum_amount_per_month,
            request_options=request_options,
        )
        return _response.data

    def delete_whitelist_sdd_one_off_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhitelistSddOneOffDelete:
        """
        Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhitelistSddOneOffDelete
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

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
        client.whitelist_sdd_one_off.delete_whitelist_sdd_one_off_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_whitelist_sdd_one_off_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncWhitelistSddOneOffClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWhitelistSddOneOffClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWhitelistSddOneOffClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWhitelistSddOneOffClient
        """
        return self._raw_client

    async def list_all_whitelist_sdd_one_off_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WhitelistSddOneOffListing]:
        """
        Get a listing of all one off SDD whitelist entries for a target monetary account.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WhitelistSddOneOffListing]
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

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
            await client.whitelist_sdd_one_off.list_all_whitelist_sdd_one_off_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_whitelist_sdd_one_off_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def create_whitelist_sdd_one_off_for_user(
        self,
        user_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WhitelistSddOneOffCreate:
        """
        Create a new one off SDD whitelist entry.

        Parameters
        ----------
        user_id : int


        monetary_account_paying_id : int
            ID of the monetary account of which you want to pay from.

        request_id : int
            ID of the request for which you want to whitelist the originating SDD.

        maximum_amount_per_month : typing.Optional[Amount]
            The maximum amount of money that is allowed to be deducted based on the whitelist.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhitelistSddOneOffCreate
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

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
            await client.whitelist_sdd_one_off.create_whitelist_sdd_one_off_for_user(
                user_id=1,
                monetary_account_paying_id=1,
                request_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_whitelist_sdd_one_off_for_user(
            user_id,
            monetary_account_paying_id=monetary_account_paying_id,
            request_id=request_id,
            maximum_amount_per_month=maximum_amount_per_month,
            request_options=request_options,
        )
        return _response.data

    async def read_whitelist_sdd_one_off_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhitelistSddOneOffRead:
        """
        Get a specific one off SDD whitelist entry.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhitelistSddOneOffRead
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

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
            await client.whitelist_sdd_one_off.read_whitelist_sdd_one_off_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_whitelist_sdd_one_off_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_whitelist_sdd_one_off_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WhitelistSddOneOffUpdate:
        """
        Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

        Parameters
        ----------
        user_id : int


        item_id : int


        monetary_account_paying_id : int
            ID of the monetary account of which you want to pay from.

        request_id : int
            ID of the request for which you want to whitelist the originating SDD.

        maximum_amount_per_month : typing.Optional[Amount]
            The maximum amount of money that is allowed to be deducted based on the whitelist.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhitelistSddOneOffUpdate
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

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
            await client.whitelist_sdd_one_off.update_whitelist_sdd_one_off_for_user(
                user_id=1,
                item_id=1,
                monetary_account_paying_id=1,
                request_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_whitelist_sdd_one_off_for_user(
            user_id,
            item_id,
            monetary_account_paying_id=monetary_account_paying_id,
            request_id=request_id,
            maximum_amount_per_month=maximum_amount_per_month,
            request_options=request_options,
        )
        return _response.data

    async def delete_whitelist_sdd_one_off_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhitelistSddOneOffDelete:
        """
        Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhitelistSddOneOffDelete
            Whitelist an one off SDD so that when another one off SDD from the creditor comes in, it is automatically accepted.

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
            await client.whitelist_sdd_one_off.delete_whitelist_sdd_one_off_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_whitelist_sdd_one_off_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
