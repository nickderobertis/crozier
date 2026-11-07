

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.card import Card
from ..types.checkout import Checkout
from ..types.checkout_success import CheckoutSuccess
from ..types.currency import Currency
from ..types.hosted_checkout import HostedCheckout
from ..types.mandate_payload import MandatePayload
from ..types.personal_details import PersonalDetails
from .raw_client import AsyncRawCheckoutsClient, RawCheckoutsClient
from .types.checkout_create_request_purpose import CheckoutCreateRequestPurpose
from .types.get_payment_methods_response import GetPaymentMethodsResponse
from .types.process_checkout_payment_type import ProcessCheckoutPaymentType
from .types.process_checkout_response import ProcessCheckoutResponse


OMIT = typing.cast(typing.Any, ...)


class CheckoutsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCheckoutsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCheckoutsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCheckoutsClient
        """
        return self._raw_client

    def get_payment_methods(
        self,
        merchant_code: str,
        *,
        amount: typing.Optional[float] = None,
        currency: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPaymentMethodsResponse:
        """
        Get payment methods available for the given merchant to use with a checkout.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        amount : typing.Optional[float]
            The amount for which the payment methods should be eligible, in major units.

        currency : typing.Optional[str]
            The currency for which the payment methods should be eligible.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPaymentMethodsResponse
            Available payment methods

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.checkouts.get_payment_methods(
            merchant_code="MH4H92C7",
            amount=9.99,
            currency="EUR",
        )
        """
        _response = self._raw_client.get_payment_methods(
            merchant_code, amount=amount, currency=currency, request_options=request_options
        )
        return _response.data

    def list_checkouts(
        self,
        *,
        checkout_reference: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CheckoutSuccess]:
        """
        Lists created checkout resources according to the applied `checkout_reference`.

        Parameters
        ----------
        checkout_reference : typing.Optional[str]
            Filters the list of checkout resources by the unique reference of the checkout.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CheckoutSuccess]
            Returns a list of checkout resources.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.checkouts.list_checkouts(
            checkout_reference="f00a8f74-b05d-4605-bd73-2a901bae5802",
        )
        """
        _response = self._raw_client.list_checkouts(
            checkout_reference=checkout_reference, request_options=request_options
        )
        return _response.data

    def create_checkout(
        self,
        *,
        checkout_reference: str,
        amount: float,
        currency: Currency,
        merchant_code: str,
        description: typing.Optional[str] = OMIT,
        return_url: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        purpose: typing.Optional[CheckoutCreateRequestPurpose] = OMIT,
        valid_until: typing.Optional[dt.datetime] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        hosted_checkout: typing.Optional[HostedCheckout] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Checkout:
        """
        Creates a payment checkout for the specified merchant, amount, and currency. Supply a `checkout_reference` to identify the payment attempt in your own systems. Creating a checkout does not charge a payment instrument.

        Set `hosted_checkout.enabled` to `true` to receive a [Hosted Checkout](https://developer.sumup.com/online-payments/checkouts/hosted-checkout/) URL where the customer can complete the payment.
        Use `redirect_url` for redirect-based payment and 3DS flows. If `return_url` is provided, SumUp sends processing updates to that backend callback URL.

        Complete the payment through [Hosted Checkout](https://developer.sumup.com/online-payments/checkouts/hosted-checkout/) or the [Payment Widget](https://developer.sumup.com/online-payments/checkouts/card-widget).

        Parameters
        ----------
        checkout_reference : str
            Merchant-defined reference for the new checkout. It should be unique enough for you to identify the payment attempt in your own systems.

        amount : float
            Amount to be charged to the payer, expressed in major units.

        currency : Currency

        merchant_code : str
            Short unique identifier for the merchant that should receive the payment.

        description : typing.Optional[str]
            Short merchant-defined description shown in SumUp tools and reporting for easier identification of the checkout.

        return_url : typing.Optional[str]
            Optional backend callback URL used by SumUp to notify your platform about processing updates for the checkout.

        customer_id : typing.Optional[str]
            Merchant-scoped customer identifier. Required when setting up recurring payments and useful when the checkout should be linked to a returning payer.

        purpose : typing.Optional[CheckoutCreateRequestPurpose]
            Business purpose of the checkout. Use `CHECKOUT` for a standard payment and `SETUP_RECURRING_PAYMENT` when collecting consent and payment details for future recurring charges.

        valid_until : typing.Optional[dt.datetime]
            Optional expiration timestamp. The checkout must be processed before this moment, otherwise it becomes unusable. If omitted, the checkout does not have an explicit expiry time.

        redirect_url : typing.Optional[str]
            URL where the payer should be sent after a redirect-based payment or SCA flow completes. This is required for [APMs](https://developer.sumup.com/online-payments/apm/introduction) and recommended for card checkouts that may require [3DS](https://developer.sumup.com/online-payments/features/3ds). If it is omitted, the [Payment Widget](https://developer.sumup.com/online-payments/checkouts) can render the challenge in an iframe instead of using a full-page redirect.

        hosted_checkout : typing.Optional[HostedCheckout]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Checkout
            Returns the created checkout resource.

        Examples
        --------
        import datetime

        from fern import Currency, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.checkouts.create_checkout(
            checkout_reference="f00a8f74-b05d-4605-bd73-2a901bae5802",
            amount=10.1,
            currency=Currency.EUR,
            merchant_code="MH4H92C7",
            description="Purchase",
            valid_until=datetime.datetime.fromisoformat(
                "2020-02-29 10:56:56+00:00",
            ),
            redirect_url="https://sumup.com",
        )
        """
        _response = self._raw_client.create_checkout(
            checkout_reference=checkout_reference,
            amount=amount,
            currency=currency,
            merchant_code=merchant_code,
            description=description,
            return_url=return_url,
            customer_id=customer_id,
            purpose=purpose,
            valid_until=valid_until,
            redirect_url=redirect_url,
            hosted_checkout=hosted_checkout,
            request_options=request_options,
        )
        return _response.data

    def get_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckoutSuccess:
        """
        Retrieves an identified checkout resource. Use this request after processing a checkout to confirm its status and inform the end user respectively.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckoutSuccess
            Returns the requested checkout resource.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.checkouts.get_checkout(
            checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
        )
        """
        _response = self._raw_client.get_checkout(checkout_id, request_options=request_options)
        return _response.data

    def process_checkout(
        self,
        checkout_id: str,
        *,
        payment_type: ProcessCheckoutPaymentType,
        installments: typing.Optional[int] = OMIT,
        mandate: typing.Optional[MandatePayload] = OMIT,
        card: typing.Optional[Card] = OMIT,
        google_pay: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        apple_pay: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        token: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        personal_details: typing.Optional[PersonalDetails] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessCheckoutResponse:
        """
        :::caution[PCI DSS compliance required]
        When you submit raw card details directly to the Checkout API, your systems store, process, or transmit cardholder data and are therefore subject to applicable [PCI DSS requirements](https://www.pcisecuritystandards.org/document_library/). You should only use this integration if your environment is appropriately PCI DSS compliant.
        :::

        Processing a checkout will attempt to charge the provided payment instrument for the amount of the specified checkout resource initiated in the `Create a checkout` endpoint.

        Follow this request with `Retrieve a checkout` to confirm its status.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        payment_type : ProcessCheckoutPaymentType
            Payment method used for this processing attempt. It determines which additional request fields are required.

        installments : typing.Optional[int]
            Number of installments for deferred payments. Available only to merchant users in Brazil.

        mandate : typing.Optional[MandatePayload]

        card : typing.Optional[Card]

        google_pay : typing.Optional[typing.Dict[str, typing.Any]]
            Raw `PaymentData` object received from Google Pay. Send the Google Pay response payload as-is.

        apple_pay : typing.Optional[typing.Dict[str, typing.Any]]
            Raw payment token object received from Apple Pay. Send the Apple Pay response payload as-is.

        token : typing.Optional[str]
            Saved-card token to use instead of raw card details when processing with a previously stored payment instrument.

        customer_id : typing.Optional[str]
            Customer identifier associated with the saved payment instrument. Required when `token` is provided.

        personal_details : typing.Optional[PersonalDetails]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessCheckoutResponse
            Returns the checkout resource after a processing attempt.

        Examples
        --------
        from fern.checkouts import ProcessCheckoutPaymentType

        from fern import Card, CardType, FernApi, MandatePayload, MandatePayloadType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.checkouts.process_checkout(
            checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
            payment_type=ProcessCheckoutPaymentType.CARD,
            installments=1,
            mandate=MandatePayload(
                type=MandatePayloadType.RECURRENT,
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
                user_ip="172.217.169.174",
            ),
            card=Card(
                name="John Doe",
                number="1234567890123456",
                expiry_year="2023",
                expiry_month="01",
                cvv="123",
                zip_code="12345",
                type=CardType.VISA,
            ),
        )
        """
        _response = self._raw_client.process_checkout(
            checkout_id,
            payment_type=payment_type,
            installments=installments,
            mandate=mandate,
            card=card,
            google_pay=google_pay,
            apple_pay=apple_pay,
            token=token,
            customer_id=customer_id,
            personal_details=personal_details,
            request_options=request_options,
        )
        return _response.data

    def deactivate_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Checkout:
        """
        Deactivates an identified checkout resource. If the checkout has already been processed it can not be deactivated.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Checkout
            Returns the checkout object after successful deactivation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.checkouts.deactivate_checkout(
            checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
        )
        """
        _response = self._raw_client.deactivate_checkout(checkout_id, request_options=request_options)
        return _response.data

    def update_checkout(
        self,
        checkout_id: str,
        *,
        amount: typing.Optional[float] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        description: typing.Optional[str] = OMIT,
        checkout_reference: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[dt.datetime] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Checkout:
        """
        Updates the amount, currency, description, reference, expiration, or customer associated with an existing checkout. Only the supplied fields are updated.

        This request changes the checkout details; it does not charge a payment instrument. Process the checkout separately to attempt a payment.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        amount : typing.Optional[float]
            Updated amount to be charged to the payer, expressed in major units.

        currency : typing.Optional[Currency]

        description : typing.Optional[str]
            Updated short merchant-defined description shown in SumUp tools and reporting.

        checkout_reference : typing.Optional[str]
            Updated merchant-defined reference for the checkout.

        valid_until : typing.Optional[dt.datetime]
            Updated expiration timestamp. The checkout must be processed before this moment, otherwise it becomes unusable.

        customer_id : typing.Optional[str]
            Updated merchant-scoped customer identifier associated with the checkout.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Checkout
            Returns the updated checkout resource.

        Examples
        --------
        import datetime

        from fern import Currency, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.checkouts.update_checkout(
            checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
            amount=12.5,
            currency=Currency.EUR,
            description="Updated purchase",
            checkout_reference="f00a8f74-b05d-4605-bd73-2a901bae5802",
            valid_until=datetime.datetime.fromisoformat(
                "2020-02-29 10:56:56+00:00",
            ),
            customer_id="831ff8d4cd5958ab5670",
        )
        """
        _response = self._raw_client.update_checkout(
            checkout_id,
            amount=amount,
            currency=currency,
            description=description,
            checkout_reference=checkout_reference,
            valid_until=valid_until,
            customer_id=customer_id,
            request_options=request_options,
        )
        return _response.data

    def create_apple_pay_session(
        self, checkout_id: str, *, context: str, target: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Creates an Apple Pay merchant session for the specified checkout.

        Use this endpoint after the customer selects Apple Pay and before calling
        `ApplePaySession.completeMerchantValidation(...)` in the browser.
        SumUp validates the merchant session request and returns the Apple Pay
        session object that your frontend should pass to Apple's JavaScript API.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        context : str
            the context to create this apple pay session.

        target : str
            The target url to create this apple pay session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful request. Returns the Apple Pay merchant session object
            that should be forwarded to the Apple Pay JS SDK to complete merchant
            validation and continue the payment flow.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.checkouts.create_apple_pay_session(
            checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
            context="example.com",
            target="https://apple-pay-gateway-cert.apple.com/paymentservices/startSession",
        )
        """
        _response = self._raw_client.create_apple_pay_session(
            checkout_id, context=context, target=target, request_options=request_options
        )
        return _response.data


class AsyncCheckoutsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCheckoutsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCheckoutsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCheckoutsClient
        """
        return self._raw_client

    async def get_payment_methods(
        self,
        merchant_code: str,
        *,
        amount: typing.Optional[float] = None,
        currency: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPaymentMethodsResponse:
        """
        Get payment methods available for the given merchant to use with a checkout.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        amount : typing.Optional[float]
            The amount for which the payment methods should be eligible, in major units.

        currency : typing.Optional[str]
            The currency for which the payment methods should be eligible.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPaymentMethodsResponse
            Available payment methods

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkouts.get_payment_methods(
                merchant_code="MH4H92C7",
                amount=9.99,
                currency="EUR",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_payment_methods(
            merchant_code, amount=amount, currency=currency, request_options=request_options
        )
        return _response.data

    async def list_checkouts(
        self,
        *,
        checkout_reference: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CheckoutSuccess]:
        """
        Lists created checkout resources according to the applied `checkout_reference`.

        Parameters
        ----------
        checkout_reference : typing.Optional[str]
            Filters the list of checkout resources by the unique reference of the checkout.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CheckoutSuccess]
            Returns a list of checkout resources.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkouts.list_checkouts(
                checkout_reference="f00a8f74-b05d-4605-bd73-2a901bae5802",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_checkouts(
            checkout_reference=checkout_reference, request_options=request_options
        )
        return _response.data

    async def create_checkout(
        self,
        *,
        checkout_reference: str,
        amount: float,
        currency: Currency,
        merchant_code: str,
        description: typing.Optional[str] = OMIT,
        return_url: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        purpose: typing.Optional[CheckoutCreateRequestPurpose] = OMIT,
        valid_until: typing.Optional[dt.datetime] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        hosted_checkout: typing.Optional[HostedCheckout] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Checkout:
        """
        Creates a payment checkout for the specified merchant, amount, and currency. Supply a `checkout_reference` to identify the payment attempt in your own systems. Creating a checkout does not charge a payment instrument.

        Set `hosted_checkout.enabled` to `true` to receive a [Hosted Checkout](https://developer.sumup.com/online-payments/checkouts/hosted-checkout/) URL where the customer can complete the payment.
        Use `redirect_url` for redirect-based payment and 3DS flows. If `return_url` is provided, SumUp sends processing updates to that backend callback URL.

        Complete the payment through [Hosted Checkout](https://developer.sumup.com/online-payments/checkouts/hosted-checkout/) or the [Payment Widget](https://developer.sumup.com/online-payments/checkouts/card-widget).

        Parameters
        ----------
        checkout_reference : str
            Merchant-defined reference for the new checkout. It should be unique enough for you to identify the payment attempt in your own systems.

        amount : float
            Amount to be charged to the payer, expressed in major units.

        currency : Currency

        merchant_code : str
            Short unique identifier for the merchant that should receive the payment.

        description : typing.Optional[str]
            Short merchant-defined description shown in SumUp tools and reporting for easier identification of the checkout.

        return_url : typing.Optional[str]
            Optional backend callback URL used by SumUp to notify your platform about processing updates for the checkout.

        customer_id : typing.Optional[str]
            Merchant-scoped customer identifier. Required when setting up recurring payments and useful when the checkout should be linked to a returning payer.

        purpose : typing.Optional[CheckoutCreateRequestPurpose]
            Business purpose of the checkout. Use `CHECKOUT` for a standard payment and `SETUP_RECURRING_PAYMENT` when collecting consent and payment details for future recurring charges.

        valid_until : typing.Optional[dt.datetime]
            Optional expiration timestamp. The checkout must be processed before this moment, otherwise it becomes unusable. If omitted, the checkout does not have an explicit expiry time.

        redirect_url : typing.Optional[str]
            URL where the payer should be sent after a redirect-based payment or SCA flow completes. This is required for [APMs](https://developer.sumup.com/online-payments/apm/introduction) and recommended for card checkouts that may require [3DS](https://developer.sumup.com/online-payments/features/3ds). If it is omitted, the [Payment Widget](https://developer.sumup.com/online-payments/checkouts) can render the challenge in an iframe instead of using a full-page redirect.

        hosted_checkout : typing.Optional[HostedCheckout]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Checkout
            Returns the created checkout resource.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, Currency

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkouts.create_checkout(
                checkout_reference="f00a8f74-b05d-4605-bd73-2a901bae5802",
                amount=10.1,
                currency=Currency.EUR,
                merchant_code="MH4H92C7",
                description="Purchase",
                valid_until=datetime.datetime.fromisoformat(
                    "2020-02-29 10:56:56+00:00",
                ),
                redirect_url="https://sumup.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_checkout(
            checkout_reference=checkout_reference,
            amount=amount,
            currency=currency,
            merchant_code=merchant_code,
            description=description,
            return_url=return_url,
            customer_id=customer_id,
            purpose=purpose,
            valid_until=valid_until,
            redirect_url=redirect_url,
            hosted_checkout=hosted_checkout,
            request_options=request_options,
        )
        return _response.data

    async def get_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckoutSuccess:
        """
        Retrieves an identified checkout resource. Use this request after processing a checkout to confirm its status and inform the end user respectively.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckoutSuccess
            Returns the requested checkout resource.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkouts.get_checkout(
                checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_checkout(checkout_id, request_options=request_options)
        return _response.data

    async def process_checkout(
        self,
        checkout_id: str,
        *,
        payment_type: ProcessCheckoutPaymentType,
        installments: typing.Optional[int] = OMIT,
        mandate: typing.Optional[MandatePayload] = OMIT,
        card: typing.Optional[Card] = OMIT,
        google_pay: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        apple_pay: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        token: typing.Optional[str] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        personal_details: typing.Optional[PersonalDetails] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessCheckoutResponse:
        """
        :::caution[PCI DSS compliance required]
        When you submit raw card details directly to the Checkout API, your systems store, process, or transmit cardholder data and are therefore subject to applicable [PCI DSS requirements](https://www.pcisecuritystandards.org/document_library/). You should only use this integration if your environment is appropriately PCI DSS compliant.
        :::

        Processing a checkout will attempt to charge the provided payment instrument for the amount of the specified checkout resource initiated in the `Create a checkout` endpoint.

        Follow this request with `Retrieve a checkout` to confirm its status.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        payment_type : ProcessCheckoutPaymentType
            Payment method used for this processing attempt. It determines which additional request fields are required.

        installments : typing.Optional[int]
            Number of installments for deferred payments. Available only to merchant users in Brazil.

        mandate : typing.Optional[MandatePayload]

        card : typing.Optional[Card]

        google_pay : typing.Optional[typing.Dict[str, typing.Any]]
            Raw `PaymentData` object received from Google Pay. Send the Google Pay response payload as-is.

        apple_pay : typing.Optional[typing.Dict[str, typing.Any]]
            Raw payment token object received from Apple Pay. Send the Apple Pay response payload as-is.

        token : typing.Optional[str]
            Saved-card token to use instead of raw card details when processing with a previously stored payment instrument.

        customer_id : typing.Optional[str]
            Customer identifier associated with the saved payment instrument. Required when `token` is provided.

        personal_details : typing.Optional[PersonalDetails]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessCheckoutResponse
            Returns the checkout resource after a processing attempt.

        Examples
        --------
        import asyncio

        from fern.checkouts import ProcessCheckoutPaymentType

        from fern import (
            AsyncFernApi,
            Card,
            CardType,
            MandatePayload,
            MandatePayloadType,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkouts.process_checkout(
                checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
                payment_type=ProcessCheckoutPaymentType.CARD,
                installments=1,
                mandate=MandatePayload(
                    type=MandatePayloadType.RECURRENT,
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
                    user_ip="172.217.169.174",
                ),
                card=Card(
                    name="John Doe",
                    number="1234567890123456",
                    expiry_year="2023",
                    expiry_month="01",
                    cvv="123",
                    zip_code="12345",
                    type=CardType.VISA,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.process_checkout(
            checkout_id,
            payment_type=payment_type,
            installments=installments,
            mandate=mandate,
            card=card,
            google_pay=google_pay,
            apple_pay=apple_pay,
            token=token,
            customer_id=customer_id,
            personal_details=personal_details,
            request_options=request_options,
        )
        return _response.data

    async def deactivate_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Checkout:
        """
        Deactivates an identified checkout resource. If the checkout has already been processed it can not be deactivated.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Checkout
            Returns the checkout object after successful deactivation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkouts.deactivate_checkout(
                checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deactivate_checkout(checkout_id, request_options=request_options)
        return _response.data

    async def update_checkout(
        self,
        checkout_id: str,
        *,
        amount: typing.Optional[float] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        description: typing.Optional[str] = OMIT,
        checkout_reference: typing.Optional[str] = OMIT,
        valid_until: typing.Optional[dt.datetime] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Checkout:
        """
        Updates the amount, currency, description, reference, expiration, or customer associated with an existing checkout. Only the supplied fields are updated.

        This request changes the checkout details; it does not charge a payment instrument. Process the checkout separately to attempt a payment.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        amount : typing.Optional[float]
            Updated amount to be charged to the payer, expressed in major units.

        currency : typing.Optional[Currency]

        description : typing.Optional[str]
            Updated short merchant-defined description shown in SumUp tools and reporting.

        checkout_reference : typing.Optional[str]
            Updated merchant-defined reference for the checkout.

        valid_until : typing.Optional[dt.datetime]
            Updated expiration timestamp. The checkout must be processed before this moment, otherwise it becomes unusable.

        customer_id : typing.Optional[str]
            Updated merchant-scoped customer identifier associated with the checkout.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Checkout
            Returns the updated checkout resource.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, Currency

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkouts.update_checkout(
                checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
                amount=12.5,
                currency=Currency.EUR,
                description="Updated purchase",
                checkout_reference="f00a8f74-b05d-4605-bd73-2a901bae5802",
                valid_until=datetime.datetime.fromisoformat(
                    "2020-02-29 10:56:56+00:00",
                ),
                customer_id="831ff8d4cd5958ab5670",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_checkout(
            checkout_id,
            amount=amount,
            currency=currency,
            description=description,
            checkout_reference=checkout_reference,
            valid_until=valid_until,
            customer_id=customer_id,
            request_options=request_options,
        )
        return _response.data

    async def create_apple_pay_session(
        self, checkout_id: str, *, context: str, target: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Creates an Apple Pay merchant session for the specified checkout.

        Use this endpoint after the customer selects Apple Pay and before calling
        `ApplePaySession.completeMerchantValidation(...)` in the browser.
        SumUp validates the merchant session request and returns the Apple Pay
        session object that your frontend should pass to Apple's JavaScript API.

        Parameters
        ----------
        checkout_id : str
            Unique identifier of the checkout resource.

        context : str
            the context to create this apple pay session.

        target : str
            The target url to create this apple pay session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful request. Returns the Apple Pay merchant session object
            that should be forwarded to the Apple Pay JS SDK to complete merchant
            validation and continue the payment flow.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkouts.create_apple_pay_session(
                checkout_id="4e425463-3e1b-431d-83fa-1e51c2925e99",
                context="example.com",
                target="https://apple-pay-gateway-cert.apple.com/paymentservices/startSession",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_apple_pay_session(
            checkout_id, context=context, target=target, request_options=request_options
        )
        return _response.data
