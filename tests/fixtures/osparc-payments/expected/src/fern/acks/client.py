

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.saved_payment_method import SavedPaymentMethod
from .raw_client import AsyncRawAcksClient, RawAcksClient


OMIT = typing.cast(typing.Any, ...)


class AcksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAcksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAcksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAcksClient
        """
        return self._raw_client

    def acknowledge_payment(
        self,
        payment_id: str,
        *,
        success: bool,
        message: typing.Optional[str] = OMIT,
        provider_payment_id: typing.Optional[str] = OMIT,
        invoice_url: typing.Optional[str] = OMIT,
        invoice_pdf: typing.Optional[str] = OMIT,
        stripe_invoice_id: typing.Optional[str] = OMIT,
        stripe_customer_id: typing.Optional[str] = OMIT,
        saved: typing.Optional[SavedPaymentMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        completes (ie. ack) request initiated by `/init` on the payments-gateway API

        Parameters
        ----------
        payment_id : str

        success : bool

        message : typing.Optional[str]

        provider_payment_id : typing.Optional[str]
            Payment ID from the provider (e.g. stripe payment ID)

        invoice_url : typing.Optional[str]
            Link to invoice is required when success=true

        invoice_pdf : typing.Optional[str]
            Link to invoice PDF

        stripe_invoice_id : typing.Optional[str]
            Stripe invoice ID

        stripe_customer_id : typing.Optional[str]
            Stripe customer ID

        saved : typing.Optional[SavedPaymentMethod]
            Gets the payment-method if user opted to save it during payment.If used did not opt to save of payment-method was already saved, then it defaults to None

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, SavedPaymentMethod

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.acks.acknowledge_payment(
            payment_id="payment_id",
            success=True,
            provider_payment_id="pi_123ABC",
            invoice_url="https://invoices.com/id=12345",
            saved=SavedPaymentMethod(
                success=True,
                payment_method_id="3FA85F64-5717-4562-B3FC-2C963F66AFA6",
            ),
        )
        """
        _response = self._raw_client.acknowledge_payment(
            payment_id,
            success=success,
            message=message,
            provider_payment_id=provider_payment_id,
            invoice_url=invoice_url,
            invoice_pdf=invoice_pdf,
            stripe_invoice_id=stripe_invoice_id,
            stripe_customer_id=stripe_customer_id,
            saved=saved,
            request_options=request_options,
        )
        return _response.data

    def acknowledge_payment_method(
        self,
        payment_method_id: str,
        *,
        success: bool,
        message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        completes (ie. ack) request initiated by `/payments-methods:init` on the payments-gateway API

        Parameters
        ----------
        payment_method_id : str

        success : bool

        message : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.acks.acknowledge_payment_method(
            payment_method_id="payment_method_id",
            success=True,
        )
        """
        _response = self._raw_client.acknowledge_payment_method(
            payment_method_id, success=success, message=message, request_options=request_options
        )
        return _response.data


class AsyncAcksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAcksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAcksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAcksClient
        """
        return self._raw_client

    async def acknowledge_payment(
        self,
        payment_id: str,
        *,
        success: bool,
        message: typing.Optional[str] = OMIT,
        provider_payment_id: typing.Optional[str] = OMIT,
        invoice_url: typing.Optional[str] = OMIT,
        invoice_pdf: typing.Optional[str] = OMIT,
        stripe_invoice_id: typing.Optional[str] = OMIT,
        stripe_customer_id: typing.Optional[str] = OMIT,
        saved: typing.Optional[SavedPaymentMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        completes (ie. ack) request initiated by `/init` on the payments-gateway API

        Parameters
        ----------
        payment_id : str

        success : bool

        message : typing.Optional[str]

        provider_payment_id : typing.Optional[str]
            Payment ID from the provider (e.g. stripe payment ID)

        invoice_url : typing.Optional[str]
            Link to invoice is required when success=true

        invoice_pdf : typing.Optional[str]
            Link to invoice PDF

        stripe_invoice_id : typing.Optional[str]
            Stripe invoice ID

        stripe_customer_id : typing.Optional[str]
            Stripe customer ID

        saved : typing.Optional[SavedPaymentMethod]
            Gets the payment-method if user opted to save it during payment.If used did not opt to save of payment-method was already saved, then it defaults to None

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SavedPaymentMethod

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.acks.acknowledge_payment(
                payment_id="payment_id",
                success=True,
                provider_payment_id="pi_123ABC",
                invoice_url="https://invoices.com/id=12345",
                saved=SavedPaymentMethod(
                    success=True,
                    payment_method_id="3FA85F64-5717-4562-B3FC-2C963F66AFA6",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.acknowledge_payment(
            payment_id,
            success=success,
            message=message,
            provider_payment_id=provider_payment_id,
            invoice_url=invoice_url,
            invoice_pdf=invoice_pdf,
            stripe_invoice_id=stripe_invoice_id,
            stripe_customer_id=stripe_customer_id,
            saved=saved,
            request_options=request_options,
        )
        return _response.data

    async def acknowledge_payment_method(
        self,
        payment_method_id: str,
        *,
        success: bool,
        message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        completes (ie. ack) request initiated by `/payments-methods:init` on the payments-gateway API

        Parameters
        ----------
        payment_method_id : str

        success : bool

        message : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.acks.acknowledge_payment_method(
                payment_method_id="payment_method_id",
                success=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.acknowledge_payment_method(
            payment_method_id, success=success, message=message, request_options=request_options
        )
        return _response.data
