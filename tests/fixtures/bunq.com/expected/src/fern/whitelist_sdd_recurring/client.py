

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.whitelist_sdd_recurring_create import WhitelistSddRecurringCreate
from ..types.whitelist_sdd_recurring_delete import WhitelistSddRecurringDelete
from ..types.whitelist_sdd_recurring_listing import WhitelistSddRecurringListing
from ..types.whitelist_sdd_recurring_read import WhitelistSddRecurringRead
from ..types.whitelist_sdd_recurring_update import WhitelistSddRecurringUpdate
from .raw_client import AsyncRawWhitelistSddRecurringClient, RawWhitelistSddRecurringClient


OMIT = typing.cast(typing.Any, ...)


class WhitelistSddRecurringClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWhitelistSddRecurringClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWhitelistSddRecurringClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWhitelistSddRecurringClient
        """
        return self._raw_client

    def list_all_whitelist_sdd_recurring_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WhitelistSddRecurringListing]:
        """
        Get a listing of all recurring SDD whitelist entries for a target monetary account.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WhitelistSddRecurringListing]
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

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
        client.whitelist_sdd_recurring.list_all_whitelist_sdd_recurring_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_whitelist_sdd_recurring_for_user(user_id, request_options=request_options)
        return _response.data

    def create_whitelist_sdd_recurring_for_user(
        self,
        user_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WhitelistSddRecurringCreate:
        """
        Create a new recurring SDD whitelist entry.

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
        WhitelistSddRecurringCreate
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

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
        client.whitelist_sdd_recurring.create_whitelist_sdd_recurring_for_user(
            user_id=1,
            monetary_account_paying_id=1,
            request_id=1,
        )
        """
        _response = self._raw_client.create_whitelist_sdd_recurring_for_user(
            user_id,
            monetary_account_paying_id=monetary_account_paying_id,
            request_id=request_id,
            maximum_amount_per_month=maximum_amount_per_month,
            request_options=request_options,
        )
        return _response.data

    def read_whitelist_sdd_recurring_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhitelistSddRecurringRead:
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
        WhitelistSddRecurringRead
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

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
        client.whitelist_sdd_recurring.read_whitelist_sdd_recurring_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_whitelist_sdd_recurring_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    def update_whitelist_sdd_recurring_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WhitelistSddRecurringUpdate:
        """
        Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

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
        WhitelistSddRecurringUpdate
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

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
        client.whitelist_sdd_recurring.update_whitelist_sdd_recurring_for_user(
            user_id=1,
            item_id=1,
            monetary_account_paying_id=1,
            request_id=1,
        )
        """
        _response = self._raw_client.update_whitelist_sdd_recurring_for_user(
            user_id,
            item_id,
            monetary_account_paying_id=monetary_account_paying_id,
            request_id=request_id,
            maximum_amount_per_month=maximum_amount_per_month,
            request_options=request_options,
        )
        return _response.data

    def delete_whitelist_sdd_recurring_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhitelistSddRecurringDelete:
        """
        Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhitelistSddRecurringDelete
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

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
        client.whitelist_sdd_recurring.delete_whitelist_sdd_recurring_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_whitelist_sdd_recurring_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncWhitelistSddRecurringClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWhitelistSddRecurringClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWhitelistSddRecurringClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWhitelistSddRecurringClient
        """
        return self._raw_client

    async def list_all_whitelist_sdd_recurring_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WhitelistSddRecurringListing]:
        """
        Get a listing of all recurring SDD whitelist entries for a target monetary account.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WhitelistSddRecurringListing]
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

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
            await client.whitelist_sdd_recurring.list_all_whitelist_sdd_recurring_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_whitelist_sdd_recurring_for_user(
            user_id, request_options=request_options
        )
        return _response.data

    async def create_whitelist_sdd_recurring_for_user(
        self,
        user_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WhitelistSddRecurringCreate:
        """
        Create a new recurring SDD whitelist entry.

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
        WhitelistSddRecurringCreate
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

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
            await client.whitelist_sdd_recurring.create_whitelist_sdd_recurring_for_user(
                user_id=1,
                monetary_account_paying_id=1,
                request_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_whitelist_sdd_recurring_for_user(
            user_id,
            monetary_account_paying_id=monetary_account_paying_id,
            request_id=request_id,
            maximum_amount_per_month=maximum_amount_per_month,
            request_options=request_options,
        )
        return _response.data

    async def read_whitelist_sdd_recurring_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhitelistSddRecurringRead:
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
        WhitelistSddRecurringRead
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

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
            await client.whitelist_sdd_recurring.read_whitelist_sdd_recurring_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_whitelist_sdd_recurring_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_whitelist_sdd_recurring_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        monetary_account_paying_id: int,
        request_id: int,
        maximum_amount_per_month: typing.Optional[Amount] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WhitelistSddRecurringUpdate:
        """
        Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

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
        WhitelistSddRecurringUpdate
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

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
            await client.whitelist_sdd_recurring.update_whitelist_sdd_recurring_for_user(
                user_id=1,
                item_id=1,
                monetary_account_paying_id=1,
                request_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_whitelist_sdd_recurring_for_user(
            user_id,
            item_id,
            monetary_account_paying_id=monetary_account_paying_id,
            request_id=request_id,
            maximum_amount_per_month=maximum_amount_per_month,
            request_options=request_options,
        )
        return _response.data

    async def delete_whitelist_sdd_recurring_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WhitelistSddRecurringDelete:
        """
        Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhitelistSddRecurringDelete
            Whitelist a recurring SDD so that when another recurrence comes in, it is automatically accepted.

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
            await client.whitelist_sdd_recurring.delete_whitelist_sdd_recurring_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_whitelist_sdd_recurring_for_user(
            user_id, item_id, request_options=request_options
        )
        return _response.data
