

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.affiliate_attribution import AffiliateAttribution
from ..types.authentication_result import AuthenticationResult
from ..types.buyer import Buyer
from ..types.checkout_session import CheckoutSession
from ..types.checkout_session_with_order import CheckoutSessionWithOrder
from ..types.fulfillment_details import FulfillmentDetails
from ..types.intent_trace import IntentTrace
from ..types.item import Item
from ..types.payment_data import PaymentData
from ..types.selected_fulfillment_option import SelectedFulfillmentOption
from .raw_client import AsyncRawCheckoutSessionsClient, RawCheckoutSessionsClient


OMIT = typing.cast(typing.Any, ...)


class CheckoutSessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCheckoutSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCheckoutSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCheckoutSessionsClient
        """
        return self._raw_client

    def create_checkout_session(
        self,
        *,
        items: typing.Sequence[Item],
        buyer: typing.Optional[Buyer] = OMIT,
        fulfillment_details: typing.Optional[FulfillmentDetails] = OMIT,
        affiliate_attribution: typing.Optional[AffiliateAttribution] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckoutSession:
        """
        Initializes a new checkout session from items and (optionally) buyer and fulfillment info.
        MUST return 201 with a rich, authoritative cart state.

        Agents MAY include `affiliate_attribution` with `touchpoint: "first"` to record first-touch attribution.
        This enables multi-touch attribution models where networks can capture both first and last touch.

        Parameters
        ----------
        items : typing.Sequence[Item]

        buyer : typing.Optional[Buyer]

        fulfillment_details : typing.Optional[FulfillmentDetails]

        affiliate_attribution : typing.Optional[AffiliateAttribution]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckoutSession
            Created

        Examples
        --------
        from fern import FernApi, Item

        client = FernApi(
            accept_language="YOUR_ACCEPT_LANGUAGE",
            idempotency_key="YOUR_IDEMPOTENCY_KEY",
            request_id="YOUR_REQUEST_ID",
            signature="YOUR_SIGNATURE",
            timestamp="YOUR_TIMESTAMP",
            api_version="YOUR_API_VERSION",
            token="YOUR_TOKEN",
        )
        client.checkout_sessions.create_checkout_session(
            items=[
                Item(
                    id="item_123",
                    quantity=1,
                )
            ],
        )
        """
        _response = self._raw_client.create_checkout_session(
            items=items,
            buyer=buyer,
            fulfillment_details=fulfillment_details,
            affiliate_attribution=affiliate_attribution,
            request_options=request_options,
        )
        return _response.data

    def get_checkout_session(
        self, checkout_session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckoutSession:
        """
        Returns the latest authoritative state for the checkout session.

        Parameters
        ----------
        checkout_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckoutSession
            Current session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept_language="YOUR_ACCEPT_LANGUAGE",
            idempotency_key="YOUR_IDEMPOTENCY_KEY",
            request_id="YOUR_REQUEST_ID",
            signature="YOUR_SIGNATURE",
            timestamp="YOUR_TIMESTAMP",
            api_version="YOUR_API_VERSION",
            token="YOUR_TOKEN",
        )
        client.checkout_sessions.get_checkout_session(
            checkout_session_id="checkout_session_id",
        )
        """
        _response = self._raw_client.get_checkout_session(checkout_session_id, request_options=request_options)
        return _response.data

    def update_checkout_session(
        self,
        checkout_session_id: str,
        *,
        buyer: typing.Optional[Buyer] = OMIT,
        items: typing.Optional[typing.Sequence[Item]] = OMIT,
        fulfillment_details: typing.Optional[FulfillmentDetails] = OMIT,
        selected_fulfillment_options: typing.Optional[typing.Sequence[SelectedFulfillmentOption]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckoutSession:
        """
        Applies changes (items, fulfillment address, fulfillment option) and returns an updated authoritative cart state.

        Parameters
        ----------
        checkout_session_id : str

        buyer : typing.Optional[Buyer]

        items : typing.Optional[typing.Sequence[Item]]

        fulfillment_details : typing.Optional[FulfillmentDetails]

        selected_fulfillment_options : typing.Optional[typing.Sequence[SelectedFulfillmentOption]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckoutSession
            Updated session

        Examples
        --------
        from fern import FernApi, SelectedFulfillmentOptionZero

        client = FernApi(
            accept_language="YOUR_ACCEPT_LANGUAGE",
            idempotency_key="YOUR_IDEMPOTENCY_KEY",
            request_id="YOUR_REQUEST_ID",
            signature="YOUR_SIGNATURE",
            timestamp="YOUR_TIMESTAMP",
            api_version="YOUR_API_VERSION",
            token="YOUR_TOKEN",
        )
        client.checkout_sessions.update_checkout_session(
            checkout_session_id="checkout_session_id",
            selected_fulfillment_options=[
                SelectedFulfillmentOptionZero(
                    type="shipping",
                )
            ],
        )
        """
        _response = self._raw_client.update_checkout_session(
            checkout_session_id,
            buyer=buyer,
            items=items,
            fulfillment_details=fulfillment_details,
            selected_fulfillment_options=selected_fulfillment_options,
            request_options=request_options,
        )
        return _response.data

    def complete_checkout_session(
        self,
        checkout_session_id: str,
        *,
        payment_data: PaymentData,
        buyer: typing.Optional[Buyer] = OMIT,
        authentication_result: typing.Optional[AuthenticationResult] = OMIT,
        affiliate_attribution: typing.Optional[AffiliateAttribution] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckoutSessionWithOrder:
        """
        Finalizes the checkout by applying a payment method. MUST create an order and return completed state on success.

        Agents MAY include `affiliate_attribution` to ensure the merchant receives final attribution context.
        Attribution is stored alongside the resulting order but not returned in the response.

        Parameters
        ----------
        checkout_session_id : str

        payment_data : PaymentData

        buyer : typing.Optional[Buyer]

        authentication_result : typing.Optional[AuthenticationResult]

        affiliate_attribution : typing.Optional[AffiliateAttribution]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckoutSessionWithOrder
            Completed session with order

        Examples
        --------
        from fern import Buyer, FernApi, PaymentData

        client = FernApi(
            accept_language="YOUR_ACCEPT_LANGUAGE",
            idempotency_key="YOUR_IDEMPOTENCY_KEY",
            request_id="YOUR_REQUEST_ID",
            signature="YOUR_SIGNATURE",
            timestamp="YOUR_TIMESTAMP",
            api_version="YOUR_API_VERSION",
            token="YOUR_TOKEN",
        )
        client.checkout_sessions.complete_checkout_session(
            checkout_session_id="checkout_session_id",
            buyer=Buyer(
                first_name="John",
                last_name="Smith",
                email="johnsmith@mail.com",
            ),
            payment_data=PaymentData(
                token="spt_123",
                provider="stripe",
            ),
        )
        """
        _response = self._raw_client.complete_checkout_session(
            checkout_session_id,
            payment_data=payment_data,
            buyer=buyer,
            authentication_result=authentication_result,
            affiliate_attribution=affiliate_attribution,
            request_options=request_options,
        )
        return _response.data

    def cancel_checkout_session(
        self,
        checkout_session_id: str,
        *,
        intent_trace: typing.Optional[IntentTrace] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckoutSession:
        """
        Cancels a session if not already completed or canceled.
        Agents MAY include an intent_trace to communicate why the session is being abandoned.

        Parameters
        ----------
        checkout_session_id : str

        intent_trace : typing.Optional[IntentTrace]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckoutSession
            Canceled session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept_language="YOUR_ACCEPT_LANGUAGE",
            idempotency_key="YOUR_IDEMPOTENCY_KEY",
            request_id="YOUR_REQUEST_ID",
            signature="YOUR_SIGNATURE",
            timestamp="YOUR_TIMESTAMP",
            api_version="YOUR_API_VERSION",
            token="YOUR_TOKEN",
        )
        client.checkout_sessions.cancel_checkout_session(
            checkout_session_id="checkout_session_id",
        )
        """
        _response = self._raw_client.cancel_checkout_session(
            checkout_session_id, intent_trace=intent_trace, request_options=request_options
        )
        return _response.data


class AsyncCheckoutSessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCheckoutSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCheckoutSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCheckoutSessionsClient
        """
        return self._raw_client

    async def create_checkout_session(
        self,
        *,
        items: typing.Sequence[Item],
        buyer: typing.Optional[Buyer] = OMIT,
        fulfillment_details: typing.Optional[FulfillmentDetails] = OMIT,
        affiliate_attribution: typing.Optional[AffiliateAttribution] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckoutSession:
        """
        Initializes a new checkout session from items and (optionally) buyer and fulfillment info.
        MUST return 201 with a rich, authoritative cart state.

        Agents MAY include `affiliate_attribution` with `touchpoint: "first"` to record first-touch attribution.
        This enables multi-touch attribution models where networks can capture both first and last touch.

        Parameters
        ----------
        items : typing.Sequence[Item]

        buyer : typing.Optional[Buyer]

        fulfillment_details : typing.Optional[FulfillmentDetails]

        affiliate_attribution : typing.Optional[AffiliateAttribution]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckoutSession
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Item

        client = AsyncFernApi(
            accept_language="YOUR_ACCEPT_LANGUAGE",
            idempotency_key="YOUR_IDEMPOTENCY_KEY",
            request_id="YOUR_REQUEST_ID",
            signature="YOUR_SIGNATURE",
            timestamp="YOUR_TIMESTAMP",
            api_version="YOUR_API_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkout_sessions.create_checkout_session(
                items=[
                    Item(
                        id="item_123",
                        quantity=1,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_checkout_session(
            items=items,
            buyer=buyer,
            fulfillment_details=fulfillment_details,
            affiliate_attribution=affiliate_attribution,
            request_options=request_options,
        )
        return _response.data

    async def get_checkout_session(
        self, checkout_session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckoutSession:
        """
        Returns the latest authoritative state for the checkout session.

        Parameters
        ----------
        checkout_session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckoutSession
            Current session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept_language="YOUR_ACCEPT_LANGUAGE",
            idempotency_key="YOUR_IDEMPOTENCY_KEY",
            request_id="YOUR_REQUEST_ID",
            signature="YOUR_SIGNATURE",
            timestamp="YOUR_TIMESTAMP",
            api_version="YOUR_API_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkout_sessions.get_checkout_session(
                checkout_session_id="checkout_session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_checkout_session(checkout_session_id, request_options=request_options)
        return _response.data

    async def update_checkout_session(
        self,
        checkout_session_id: str,
        *,
        buyer: typing.Optional[Buyer] = OMIT,
        items: typing.Optional[typing.Sequence[Item]] = OMIT,
        fulfillment_details: typing.Optional[FulfillmentDetails] = OMIT,
        selected_fulfillment_options: typing.Optional[typing.Sequence[SelectedFulfillmentOption]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckoutSession:
        """
        Applies changes (items, fulfillment address, fulfillment option) and returns an updated authoritative cart state.

        Parameters
        ----------
        checkout_session_id : str

        buyer : typing.Optional[Buyer]

        items : typing.Optional[typing.Sequence[Item]]

        fulfillment_details : typing.Optional[FulfillmentDetails]

        selected_fulfillment_options : typing.Optional[typing.Sequence[SelectedFulfillmentOption]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckoutSession
            Updated session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SelectedFulfillmentOptionZero

        client = AsyncFernApi(
            accept_language="YOUR_ACCEPT_LANGUAGE",
            idempotency_key="YOUR_IDEMPOTENCY_KEY",
            request_id="YOUR_REQUEST_ID",
            signature="YOUR_SIGNATURE",
            timestamp="YOUR_TIMESTAMP",
            api_version="YOUR_API_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkout_sessions.update_checkout_session(
                checkout_session_id="checkout_session_id",
                selected_fulfillment_options=[
                    SelectedFulfillmentOptionZero(
                        type="shipping",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_checkout_session(
            checkout_session_id,
            buyer=buyer,
            items=items,
            fulfillment_details=fulfillment_details,
            selected_fulfillment_options=selected_fulfillment_options,
            request_options=request_options,
        )
        return _response.data

    async def complete_checkout_session(
        self,
        checkout_session_id: str,
        *,
        payment_data: PaymentData,
        buyer: typing.Optional[Buyer] = OMIT,
        authentication_result: typing.Optional[AuthenticationResult] = OMIT,
        affiliate_attribution: typing.Optional[AffiliateAttribution] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckoutSessionWithOrder:
        """
        Finalizes the checkout by applying a payment method. MUST create an order and return completed state on success.

        Agents MAY include `affiliate_attribution` to ensure the merchant receives final attribution context.
        Attribution is stored alongside the resulting order but not returned in the response.

        Parameters
        ----------
        checkout_session_id : str

        payment_data : PaymentData

        buyer : typing.Optional[Buyer]

        authentication_result : typing.Optional[AuthenticationResult]

        affiliate_attribution : typing.Optional[AffiliateAttribution]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckoutSessionWithOrder
            Completed session with order

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Buyer, PaymentData

        client = AsyncFernApi(
            accept_language="YOUR_ACCEPT_LANGUAGE",
            idempotency_key="YOUR_IDEMPOTENCY_KEY",
            request_id="YOUR_REQUEST_ID",
            signature="YOUR_SIGNATURE",
            timestamp="YOUR_TIMESTAMP",
            api_version="YOUR_API_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkout_sessions.complete_checkout_session(
                checkout_session_id="checkout_session_id",
                buyer=Buyer(
                    first_name="John",
                    last_name="Smith",
                    email="johnsmith@mail.com",
                ),
                payment_data=PaymentData(
                    token="spt_123",
                    provider="stripe",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_checkout_session(
            checkout_session_id,
            payment_data=payment_data,
            buyer=buyer,
            authentication_result=authentication_result,
            affiliate_attribution=affiliate_attribution,
            request_options=request_options,
        )
        return _response.data

    async def cancel_checkout_session(
        self,
        checkout_session_id: str,
        *,
        intent_trace: typing.Optional[IntentTrace] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckoutSession:
        """
        Cancels a session if not already completed or canceled.
        Agents MAY include an intent_trace to communicate why the session is being abandoned.

        Parameters
        ----------
        checkout_session_id : str

        intent_trace : typing.Optional[IntentTrace]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckoutSession
            Canceled session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept_language="YOUR_ACCEPT_LANGUAGE",
            idempotency_key="YOUR_IDEMPOTENCY_KEY",
            request_id="YOUR_REQUEST_ID",
            signature="YOUR_SIGNATURE",
            timestamp="YOUR_TIMESTAMP",
            api_version="YOUR_API_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.checkout_sessions.cancel_checkout_session(
                checkout_session_id="checkout_session_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_checkout_session(
            checkout_session_id, intent_trace=intent_trace, request_options=request_options
        )
        return _response.data
