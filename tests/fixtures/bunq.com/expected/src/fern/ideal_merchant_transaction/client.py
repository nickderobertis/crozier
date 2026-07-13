

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.ideal_merchant_transaction_create import IdealMerchantTransactionCreate
from ..types.ideal_merchant_transaction_listing import IdealMerchantTransactionListing
from ..types.ideal_merchant_transaction_read import IdealMerchantTransactionRead
from ..types.label_monetary_account import LabelMonetaryAccount
from .raw_client import AsyncRawIdealMerchantTransactionClient, RawIdealMerchantTransactionClient


OMIT = typing.cast(typing.Any, ...)


class IdealMerchantTransactionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdealMerchantTransactionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdealMerchantTransactionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdealMerchantTransactionClient
        """
        return self._raw_client

    def list_all_ideal_merchant_transaction_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IdealMerchantTransactionListing]:
        """
        View for requesting iDEAL transactions and polling their status.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IdealMerchantTransactionListing]
            View for requesting iDEAL transactions and polling their status.

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
        client.ideal_merchant_transaction.list_all_ideal_merchant_transaction_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_ideal_merchant_transaction_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def create_ideal_merchant_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        amount_guaranteed: typing.Optional[Amount] = OMIT,
        amount_requested: typing.Optional[Amount] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        expiration: typing.Optional[str] = OMIT,
        issuer: typing.Optional[str] = OMIT,
        issuer_authentication_url: typing.Optional[str] = OMIT,
        issuer_name: typing.Optional[str] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        purchase_identifier: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        status_timestamp: typing.Optional[str] = OMIT,
        transaction_identifier: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdealMerchantTransactionCreate:
        """
        View for requesting iDEAL transactions and polling their status.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        alias : typing.Optional[LabelMonetaryAccount]
            The alias of the monetary account to add money to.

        amount_guaranteed : typing.Optional[Amount]
            In case of a successful transaction, the amount of money that will be transferred.

        amount_requested : typing.Optional[Amount]
            The requested amount of money to add.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The alias of the monetary account the money comes from.

        expiration : typing.Optional[str]
            When the transaction will expire.

        issuer : typing.Optional[str]
            The BIC of the issuer.

        issuer_authentication_url : typing.Optional[str]
            The URL to visit to

        issuer_name : typing.Optional[str]
            The Name of the issuer.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account this ideal merchant transaction links to.

        purchase_identifier : typing.Optional[str]
            The 'purchase ID' of the iDEAL transaction.

        status : typing.Optional[str]
            The status of the transaction.

        status_timestamp : typing.Optional[str]
            When the status was last updated.

        transaction_identifier : typing.Optional[str]
            The 'transaction ID' of the iDEAL transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdealMerchantTransactionCreate
            View for requesting iDEAL transactions and polling their status.

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
        client.ideal_merchant_transaction.create_ideal_merchant_transaction_for_user_monetary_account(
            user_id=1,
            monetary_account_id_=1,
        )
        """
        _response = self._raw_client.create_ideal_merchant_transaction_for_user_monetary_account(
            user_id,
            monetary_account_id_,
            alias=alias,
            amount_guaranteed=amount_guaranteed,
            amount_requested=amount_requested,
            counterparty_alias=counterparty_alias,
            expiration=expiration,
            issuer=issuer,
            issuer_authentication_url=issuer_authentication_url,
            issuer_name=issuer_name,
            monetary_account_id=monetary_account_id,
            purchase_identifier=purchase_identifier,
            status=status,
            status_timestamp=status_timestamp,
            transaction_identifier=transaction_identifier,
            request_options=request_options,
        )
        return _response.data

    def read_ideal_merchant_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdealMerchantTransactionRead:
        """
        View for requesting iDEAL transactions and polling their status.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdealMerchantTransactionRead
            View for requesting iDEAL transactions and polling their status.

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
        client.ideal_merchant_transaction.read_ideal_merchant_transaction_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_ideal_merchant_transaction_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncIdealMerchantTransactionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdealMerchantTransactionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdealMerchantTransactionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdealMerchantTransactionClient
        """
        return self._raw_client

    async def list_all_ideal_merchant_transaction_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IdealMerchantTransactionListing]:
        """
        View for requesting iDEAL transactions and polling their status.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IdealMerchantTransactionListing]
            View for requesting iDEAL transactions and polling their status.

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
            await client.ideal_merchant_transaction.list_all_ideal_merchant_transaction_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_ideal_merchant_transaction_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def create_ideal_merchant_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        amount_guaranteed: typing.Optional[Amount] = OMIT,
        amount_requested: typing.Optional[Amount] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        expiration: typing.Optional[str] = OMIT,
        issuer: typing.Optional[str] = OMIT,
        issuer_authentication_url: typing.Optional[str] = OMIT,
        issuer_name: typing.Optional[str] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        purchase_identifier: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        status_timestamp: typing.Optional[str] = OMIT,
        transaction_identifier: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdealMerchantTransactionCreate:
        """
        View for requesting iDEAL transactions and polling their status.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        alias : typing.Optional[LabelMonetaryAccount]
            The alias of the monetary account to add money to.

        amount_guaranteed : typing.Optional[Amount]
            In case of a successful transaction, the amount of money that will be transferred.

        amount_requested : typing.Optional[Amount]
            The requested amount of money to add.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The alias of the monetary account the money comes from.

        expiration : typing.Optional[str]
            When the transaction will expire.

        issuer : typing.Optional[str]
            The BIC of the issuer.

        issuer_authentication_url : typing.Optional[str]
            The URL to visit to

        issuer_name : typing.Optional[str]
            The Name of the issuer.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account this ideal merchant transaction links to.

        purchase_identifier : typing.Optional[str]
            The 'purchase ID' of the iDEAL transaction.

        status : typing.Optional[str]
            The status of the transaction.

        status_timestamp : typing.Optional[str]
            When the status was last updated.

        transaction_identifier : typing.Optional[str]
            The 'transaction ID' of the iDEAL transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdealMerchantTransactionCreate
            View for requesting iDEAL transactions and polling their status.

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
            await client.ideal_merchant_transaction.create_ideal_merchant_transaction_for_user_monetary_account(
                user_id=1,
                monetary_account_id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_ideal_merchant_transaction_for_user_monetary_account(
            user_id,
            monetary_account_id_,
            alias=alias,
            amount_guaranteed=amount_guaranteed,
            amount_requested=amount_requested,
            counterparty_alias=counterparty_alias,
            expiration=expiration,
            issuer=issuer,
            issuer_authentication_url=issuer_authentication_url,
            issuer_name=issuer_name,
            monetary_account_id=monetary_account_id,
            purchase_identifier=purchase_identifier,
            status=status,
            status_timestamp=status_timestamp,
            transaction_identifier=transaction_identifier,
            request_options=request_options,
        )
        return _response.data

    async def read_ideal_merchant_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IdealMerchantTransactionRead:
        """
        View for requesting iDEAL transactions and polling their status.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IdealMerchantTransactionRead
            View for requesting iDEAL transactions and polling their status.

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
            await client.ideal_merchant_transaction.read_ideal_merchant_transaction_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_ideal_merchant_transaction_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data
