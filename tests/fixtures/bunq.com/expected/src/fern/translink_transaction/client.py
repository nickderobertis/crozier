

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.payment import Payment
from ..types.translink_transaction_create import TranslinkTransactionCreate
from ..types.translink_transaction_listing import TranslinkTransactionListing
from ..types.translink_transaction_read import TranslinkTransactionRead
from .raw_client import AsyncRawTranslinkTransactionClient, RawTranslinkTransactionClient


OMIT = typing.cast(typing.Any, ...)


class TranslinkTransactionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTranslinkTransactionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTranslinkTransactionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTranslinkTransactionClient
        """
        return self._raw_client

    def list_all_translink_transaction_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TranslinkTransactionListing]:
        """
        Used to create translink transactions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TranslinkTransactionListing]
            Used to create translink transactions.

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
        client.translink_transaction.list_all_translink_transaction_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_translink_transaction_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def create_translink_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        description: str,
        payments: typing.Sequence[Payment],
        reference: str,
        type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TranslinkTransactionCreate:
        """
        Used to create translink transactions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        description : str
            Description of the payment request.

        payments : typing.Sequence[Payment]
            The list of payments we want to send in a single transaction.

        reference : str
            The request reference.

        type : str
            Type of transaction, can be TRIP, REFUND, WITHDRAWAL or TOP_UP.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranslinkTransactionCreate
            Used to create translink transactions.

        Examples
        --------
        from fern import FernApi, Payment

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.translink_transaction.create_translink_transaction_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            description="description",
            payments=[Payment()],
            reference="reference",
            type="type",
        )
        """
        _response = self._raw_client.create_translink_transaction_for_user_monetary_account(
            user_id,
            monetary_account_id,
            description=description,
            payments=payments,
            reference=reference,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def read_translink_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TranslinkTransactionRead:
        """
        Used to create translink transactions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranslinkTransactionRead
            Used to create translink transactions.

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
        client.translink_transaction.read_translink_transaction_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_translink_transaction_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncTranslinkTransactionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTranslinkTransactionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTranslinkTransactionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTranslinkTransactionClient
        """
        return self._raw_client

    async def list_all_translink_transaction_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TranslinkTransactionListing]:
        """
        Used to create translink transactions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TranslinkTransactionListing]
            Used to create translink transactions.

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
            await client.translink_transaction.list_all_translink_transaction_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_translink_transaction_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def create_translink_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        description: str,
        payments: typing.Sequence[Payment],
        reference: str,
        type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TranslinkTransactionCreate:
        """
        Used to create translink transactions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        description : str
            Description of the payment request.

        payments : typing.Sequence[Payment]
            The list of payments we want to send in a single transaction.

        reference : str
            The request reference.

        type : str
            Type of transaction, can be TRIP, REFUND, WITHDRAWAL or TOP_UP.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranslinkTransactionCreate
            Used to create translink transactions.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Payment

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.translink_transaction.create_translink_transaction_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                description="description",
                payments=[Payment()],
                reference="reference",
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_translink_transaction_for_user_monetary_account(
            user_id,
            monetary_account_id,
            description=description,
            payments=payments,
            reference=reference,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def read_translink_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TranslinkTransactionRead:
        """
        Used to create translink transactions.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TranslinkTransactionRead
            Used to create translink transactions.

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
            await client.translink_transaction.read_translink_transaction_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_translink_transaction_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data
