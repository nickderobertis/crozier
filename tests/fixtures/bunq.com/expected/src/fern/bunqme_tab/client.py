

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bunq_me_tab_create import BunqMeTabCreate
from ..types.bunq_me_tab_entry import BunqMeTabEntry
from ..types.bunq_me_tab_listing import BunqMeTabListing
from ..types.bunq_me_tab_read import BunqMeTabRead
from ..types.bunq_me_tab_update import BunqMeTabUpdate
from .raw_client import AsyncRawBunqmeTabClient, RawBunqmeTabClient


OMIT = typing.cast(typing.Any, ...)


class BunqmeTabClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBunqmeTabClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBunqmeTabClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBunqmeTabClient
        """
        return self._raw_client

    def list_all_bunqme_tab_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BunqMeTabListing]:
        """
        bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BunqMeTabListing]
            bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

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
        client.bunqme_tab.list_all_bunqme_tab_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_bunqme_tab_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def create_bunqme_tab_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        bunqme_tab_entry: BunqMeTabEntry,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BunqMeTabCreate:
        """
        bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_tab_entry : BunqMeTabEntry
            The bunq.me entry containing the payment information.

        status : typing.Optional[str]
            The status of the bunq.me. Ignored in POST requests but can be used for cancelling the bunq.me by setting status as CANCELLED with a PUT request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BunqMeTabCreate
            bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

        Examples
        --------
        from fern import BunqMeTabEntry, FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.bunqme_tab.create_bunqme_tab_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            bunqme_tab_entry=BunqMeTabEntry(),
        )
        """
        _response = self._raw_client.create_bunqme_tab_for_user_monetary_account(
            user_id,
            monetary_account_id,
            bunqme_tab_entry=bunqme_tab_entry,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def read_bunqme_tab_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BunqMeTabRead:
        """
        bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BunqMeTabRead
            bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

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
        client.bunqme_tab.read_bunqme_tab_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_bunqme_tab_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def update_bunqme_tab_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        bunqme_tab_entry: BunqMeTabEntry,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BunqMeTabUpdate:
        """
        bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        bunqme_tab_entry : BunqMeTabEntry
            The bunq.me entry containing the payment information.

        status : typing.Optional[str]
            The status of the bunq.me. Ignored in POST requests but can be used for cancelling the bunq.me by setting status as CANCELLED with a PUT request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BunqMeTabUpdate
            bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

        Examples
        --------
        from fern import BunqMeTabEntry, FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.bunqme_tab.update_bunqme_tab_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
            bunqme_tab_entry=BunqMeTabEntry(),
        )
        """
        _response = self._raw_client.update_bunqme_tab_for_user_monetary_account(
            user_id,
            monetary_account_id,
            item_id,
            bunqme_tab_entry=bunqme_tab_entry,
            status=status,
            request_options=request_options,
        )
        return _response.data


class AsyncBunqmeTabClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBunqmeTabClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBunqmeTabClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBunqmeTabClient
        """
        return self._raw_client

    async def list_all_bunqme_tab_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BunqMeTabListing]:
        """
        bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BunqMeTabListing]
            bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

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
            await client.bunqme_tab.list_all_bunqme_tab_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_bunqme_tab_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def create_bunqme_tab_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        bunqme_tab_entry: BunqMeTabEntry,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BunqMeTabCreate:
        """
        bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        bunqme_tab_entry : BunqMeTabEntry
            The bunq.me entry containing the payment information.

        status : typing.Optional[str]
            The status of the bunq.me. Ignored in POST requests but can be used for cancelling the bunq.me by setting status as CANCELLED with a PUT request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BunqMeTabCreate
            bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BunqMeTabEntry

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.bunqme_tab.create_bunqme_tab_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                bunqme_tab_entry=BunqMeTabEntry(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_bunqme_tab_for_user_monetary_account(
            user_id,
            monetary_account_id,
            bunqme_tab_entry=bunqme_tab_entry,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def read_bunqme_tab_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BunqMeTabRead:
        """
        bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BunqMeTabRead
            bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

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
            await client.bunqme_tab.read_bunqme_tab_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_bunqme_tab_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_bunqme_tab_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        bunqme_tab_entry: BunqMeTabEntry,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BunqMeTabUpdate:
        """
        bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        bunqme_tab_entry : BunqMeTabEntry
            The bunq.me entry containing the payment information.

        status : typing.Optional[str]
            The status of the bunq.me. Ignored in POST requests but can be used for cancelling the bunq.me by setting status as CANCELLED with a PUT request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BunqMeTabUpdate
            bunq.me tabs allows you to create a payment request and share the link through e-mail, chat, etc. Multiple persons are able to respond to the payment request and pay through bunq, iDeal or SOFORT.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BunqMeTabEntry

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.bunqme_tab.update_bunqme_tab_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
                bunqme_tab_entry=BunqMeTabEntry(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_bunqme_tab_for_user_monetary_account(
            user_id,
            monetary_account_id,
            item_id,
            bunqme_tab_entry=bunqme_tab_entry,
            status=status,
            request_options=request_options,
        )
        return _response.data
