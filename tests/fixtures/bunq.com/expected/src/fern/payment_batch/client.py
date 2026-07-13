

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.payment_batch_anchored_payment import PaymentBatchAnchoredPayment
from ..types.payment_batch_create import PaymentBatchCreate
from ..types.payment_batch_listing import PaymentBatchListing
from ..types.payment_batch_read import PaymentBatchRead
from ..types.payment_batch_update import PaymentBatchUpdate
from .raw_client import AsyncRawPaymentBatchClient, RawPaymentBatchClient


OMIT = typing.cast(typing.Any, ...)


class PaymentBatchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPaymentBatchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPaymentBatchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPaymentBatchClient
        """
        return self._raw_client

    def list_all_payment_batch_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PaymentBatchListing]:
        """
        Return all the payment batches for a monetary account.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PaymentBatchListing]
            Create a payment batch, or show the payment batches of a monetary account.

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
        client.payment_batch.list_all_payment_batch_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.list_all_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    def create_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        payments: typing.Optional[PaymentBatchAnchoredPayment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentBatchCreate:
        """
        Create a payment batch by sending an array of single payment objects, that will become part of the batch.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payments : typing.Optional[PaymentBatchAnchoredPayment]
            The list of mutations that were made.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentBatchCreate
            Create a payment batch, or show the payment batches of a monetary account.

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
        client.payment_batch.create_payment_batch_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
        )
        """
        _response = self._raw_client.create_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, payments=payments, request_options=request_options
        )
        return _response.data

    def read_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentBatchRead:
        """
        Return the details of a specific payment batch.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentBatchRead
            Create a payment batch, or show the payment batches of a monetary account.

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
        client.payment_batch.read_payment_batch_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    def update_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        payments: typing.Optional[PaymentBatchAnchoredPayment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentBatchUpdate:
        """
        Revoke a bunq.to payment batch. The status of all the payments will be set to REVOKED.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        payments : typing.Optional[PaymentBatchAnchoredPayment]
            The list of mutations that were made.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentBatchUpdate
            Create a payment batch, or show the payment batches of a monetary account.

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
        client.payment_batch.update_payment_batch_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, item_id, payments=payments, request_options=request_options
        )
        return _response.data


class AsyncPaymentBatchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPaymentBatchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPaymentBatchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPaymentBatchClient
        """
        return self._raw_client

    async def list_all_payment_batch_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PaymentBatchListing]:
        """
        Return all the payment batches for a monetary account.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PaymentBatchListing]
            Create a payment batch, or show the payment batches of a monetary account.

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
            await client.payment_batch.list_all_payment_batch_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, request_options=request_options
        )
        return _response.data

    async def create_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        payments: typing.Optional[PaymentBatchAnchoredPayment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentBatchCreate:
        """
        Create a payment batch by sending an array of single payment objects, that will become part of the batch.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        payments : typing.Optional[PaymentBatchAnchoredPayment]
            The list of mutations that were made.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentBatchCreate
            Create a payment batch, or show the payment batches of a monetary account.

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
            await client.payment_batch.create_payment_batch_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, payments=payments, request_options=request_options
        )
        return _response.data

    async def read_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentBatchRead:
        """
        Return the details of a specific payment batch.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentBatchRead
            Create a payment batch, or show the payment batches of a monetary account.

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
            await client.payment_batch.read_payment_batch_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_payment_batch_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        payments: typing.Optional[PaymentBatchAnchoredPayment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaymentBatchUpdate:
        """
        Revoke a bunq.to payment batch. The status of all the payments will be set to REVOKED.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        payments : typing.Optional[PaymentBatchAnchoredPayment]
            The list of mutations that were made.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaymentBatchUpdate
            Create a payment batch, or show the payment batches of a monetary account.

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
            await client.payment_batch.update_payment_batch_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_payment_batch_for_user_monetary_account(
            user_id, monetary_account_id, item_id, payments=payments, request_options=request_options
        )
        return _response.data
