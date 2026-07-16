

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.charge_request_additional_recipient import ChargeRequestAdditionalRecipient
from ..types.create_checkout_response import CreateCheckoutResponse
from ..types.create_order_request import CreateOrderRequest
from .raw_client import AsyncRawCheckoutClient, RawCheckoutClient


OMIT = typing.cast(typing.Any, ...)


class CheckoutClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCheckoutClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCheckoutClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCheckoutClient
        """
        return self._raw_client

    def create_checkout(
        self,
        location_id: str,
        *,
        idempotency_key: str,
        order: CreateOrderRequest,
        additional_recipients: typing.Optional[typing.Sequence[ChargeRequestAdditionalRecipient]] = OMIT,
        ask_for_shipping_address: typing.Optional[bool] = OMIT,
        merchant_support_email: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        pre_populate_buyer_email: typing.Optional[str] = OMIT,
        pre_populate_shipping_address: typing.Optional[Address] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCheckoutResponse:
        """
        Links a `checkoutId` to a `checkout_page_url` that customers are
        directed to in order to provide their payment information using a
        payment processing workflow hosted on connect.squareup.com.

        Parameters
        ----------
        location_id : str
            The ID of the business location to associate the checkout with.

        idempotency_key : str
            A unique string that identifies this checkout among others you have created. It can be
            any valid string but must be unique for every order sent to Square Checkout for a given location ID.

            The idempotency key is used to avoid processing the same order more than once. If you are
            unsure whether a particular checkout was created successfully, you can attempt it again with
            the same idempotency key and all the same other parameters without worrying about creating duplicates.

            You should use a random number/string generator native to the language
            you are working in to generate strings for your idempotency keys.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        order : CreateOrderRequest

        additional_recipients : typing.Optional[typing.Sequence[ChargeRequestAdditionalRecipient]]
            The basic primitive of a multi-party transaction. The value is optional.
            The transaction facilitated by you can be split from here.

            If you provide this value, the `amount_money` value in your `additional_recipients` field
            cannot be more than 90% of the `total_money` calculated by Square for your order.
            The `location_id` must be a valid seller location where the checkout is occurring.

            This field requires `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission.

            This field is currently not supported in the Square Sandbox.

        ask_for_shipping_address : typing.Optional[bool]
            If `true`, Square Checkout collects shipping information on your behalf and stores
            that information with the transaction information in the Square Seller Dashboard.

            Default: `false`.

        merchant_support_email : typing.Optional[str]
            The email address to display on the Square Checkout confirmation page
            and confirmation email that the buyer can use to contact the seller.

            If this value is not set, the confirmation page and email display the
            primary email address associated with the seller's Square account.

            Default: none; only exists if explicitly set.

        note : typing.Optional[str]
            An optional note to associate with the `checkout` object.

            This value cannot exceed 60 characters.

        pre_populate_buyer_email : typing.Optional[str]
            If provided, the buyer's email is prepopulated on the checkout page
            as an editable text field.

            Default: none; only exists if explicitly set.

        pre_populate_shipping_address : typing.Optional[Address]

        redirect_url : typing.Optional[str]
            The URL to redirect to after the checkout is completed with `checkoutId`,
            `transactionId`, and `referenceId` appended as URL parameters. For example,
            if the provided redirect URL is `http://www.example.com/order-complete`, a
            successful transaction redirects the customer to:

            <pre><code>http://www.example.com/order-complete?checkoutId=xxxxxx&amp;referenceId=xxxxxx&amp;transactionId=xxxxxx</code></pre>

            If you do not provide a redirect URL, Square Checkout displays an order
            confirmation page on your behalf; however, it is strongly recommended that
            you provide a redirect URL so you can verify the transaction results and
            finalize the order through your existing/normal confirmation workflow.

            Default: none; only exists if explicitly set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCheckoutResponse
            Success

        Examples
        --------
        from fern import CreateOrderRequest, FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.checkout.create_checkout(
            location_id="location_id",
            idempotency_key="idempotency_key",
            order=CreateOrderRequest(),
        )
        """
        _response = self._raw_client.create_checkout(
            location_id,
            idempotency_key=idempotency_key,
            order=order,
            additional_recipients=additional_recipients,
            ask_for_shipping_address=ask_for_shipping_address,
            merchant_support_email=merchant_support_email,
            note=note,
            pre_populate_buyer_email=pre_populate_buyer_email,
            pre_populate_shipping_address=pre_populate_shipping_address,
            redirect_url=redirect_url,
            request_options=request_options,
        )
        return _response.data


class AsyncCheckoutClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCheckoutClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCheckoutClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCheckoutClient
        """
        return self._raw_client

    async def create_checkout(
        self,
        location_id: str,
        *,
        idempotency_key: str,
        order: CreateOrderRequest,
        additional_recipients: typing.Optional[typing.Sequence[ChargeRequestAdditionalRecipient]] = OMIT,
        ask_for_shipping_address: typing.Optional[bool] = OMIT,
        merchant_support_email: typing.Optional[str] = OMIT,
        note: typing.Optional[str] = OMIT,
        pre_populate_buyer_email: typing.Optional[str] = OMIT,
        pre_populate_shipping_address: typing.Optional[Address] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCheckoutResponse:
        """
        Links a `checkoutId` to a `checkout_page_url` that customers are
        directed to in order to provide their payment information using a
        payment processing workflow hosted on connect.squareup.com.

        Parameters
        ----------
        location_id : str
            The ID of the business location to associate the checkout with.

        idempotency_key : str
            A unique string that identifies this checkout among others you have created. It can be
            any valid string but must be unique for every order sent to Square Checkout for a given location ID.

            The idempotency key is used to avoid processing the same order more than once. If you are
            unsure whether a particular checkout was created successfully, you can attempt it again with
            the same idempotency key and all the same other parameters without worrying about creating duplicates.

            You should use a random number/string generator native to the language
            you are working in to generate strings for your idempotency keys.

            For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).

        order : CreateOrderRequest

        additional_recipients : typing.Optional[typing.Sequence[ChargeRequestAdditionalRecipient]]
            The basic primitive of a multi-party transaction. The value is optional.
            The transaction facilitated by you can be split from here.

            If you provide this value, the `amount_money` value in your `additional_recipients` field
            cannot be more than 90% of the `total_money` calculated by Square for your order.
            The `location_id` must be a valid seller location where the checkout is occurring.

            This field requires `PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS` OAuth permission.

            This field is currently not supported in the Square Sandbox.

        ask_for_shipping_address : typing.Optional[bool]
            If `true`, Square Checkout collects shipping information on your behalf and stores
            that information with the transaction information in the Square Seller Dashboard.

            Default: `false`.

        merchant_support_email : typing.Optional[str]
            The email address to display on the Square Checkout confirmation page
            and confirmation email that the buyer can use to contact the seller.

            If this value is not set, the confirmation page and email display the
            primary email address associated with the seller's Square account.

            Default: none; only exists if explicitly set.

        note : typing.Optional[str]
            An optional note to associate with the `checkout` object.

            This value cannot exceed 60 characters.

        pre_populate_buyer_email : typing.Optional[str]
            If provided, the buyer's email is prepopulated on the checkout page
            as an editable text field.

            Default: none; only exists if explicitly set.

        pre_populate_shipping_address : typing.Optional[Address]

        redirect_url : typing.Optional[str]
            The URL to redirect to after the checkout is completed with `checkoutId`,
            `transactionId`, and `referenceId` appended as URL parameters. For example,
            if the provided redirect URL is `http://www.example.com/order-complete`, a
            successful transaction redirects the customer to:

            <pre><code>http://www.example.com/order-complete?checkoutId=xxxxxx&amp;referenceId=xxxxxx&amp;transactionId=xxxxxx</code></pre>

            If you do not provide a redirect URL, Square Checkout displays an order
            confirmation page on your behalf; however, it is strongly recommended that
            you provide a redirect URL so you can verify the transaction results and
            finalize the order through your existing/normal confirmation workflow.

            Default: none; only exists if explicitly set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCheckoutResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CreateOrderRequest

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkout.create_checkout(
                location_id="location_id",
                idempotency_key="idempotency_key",
                order=CreateOrderRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_checkout(
            location_id,
            idempotency_key=idempotency_key,
            order=order,
            additional_recipients=additional_recipients,
            ask_for_shipping_address=ask_for_shipping_address,
            merchant_support_email=merchant_support_email,
            note=note,
            pre_populate_buyer_email=pre_populate_buyer_email,
            pre_populate_shipping_address=pre_populate_shipping_address,
            redirect_url=redirect_url,
            request_options=request_options,
        )
        return _response.data
