

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.fulfillment_item import FulfillmentItem
from .raw_client import AsyncRawExternalSellerClient, RawExternalSellerClient
from .types.fulfillment_simulation_response import FulfillmentSimulationResponse
from .types.order_placement_client_profile_data import OrderPlacementClientProfileData
from .types.order_placement_items_item import OrderPlacementItemsItem
from .types.order_placement_marketing_data import OrderPlacementMarketingData
from .types.order_placement_shipping_data import OrderPlacementShippingData
from .types.send_invoice_request_items_item import SendInvoiceRequestItemsItem
from .types.update_tracking_status_request_events_item import UpdateTrackingStatusRequestEventsItem


OMIT = typing.cast(typing.Any, ...)


class ExternalSellerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExternalSellerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExternalSellerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExternalSellerClient
        """
        return self._raw_client

    def fulfillment_simulation(
        self,
        fulfillment_endpoint: str,
        *,
        postal_code: str,
        country: typing.Optional[str] = OMIT,
        geo_coordinates: typing.Optional[typing.Sequence[str]] = OMIT,
        items: typing.Optional[typing.Sequence[FulfillmentItem]] = OMIT,
        sc: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FulfillmentSimulationResponse:
        """
        This endpoint may be called upon by VTEX for fulfillment simulation in the external seller different contexts. See examples below.

        When a [price](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/price) or [inventory](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/inventory) notification request returns a response with status `200 OK`, it means that the SKU already exists in the marketplace. Whenever this happens, the marketplace will call the seller to get two updated information about the SKU: Price and Inventory.

        The seller needs to have an endpoint implemented in order to receive this call and send a response containing the requested information to the marketplace. We call it the Fulfillment Simulation endpoint.

        If the seller wishes to include other parameters in this call (like account name, or [sales channel](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV) ID), this should be done within their {fulfillmentEndpoint}. This path is then inserted in the marketplace's VTEX admin when [configuring a seller](https://help.vtex.com/en/tutorial/configurando-seller--tutorials_392).

        The marketplace will send an object containing an array of items. The seller must use this list to get the updated information about the referred SKUs and send them back to the marketplace, following the response format explained in the API Reference.

        This call is also applied in the Storefront simulation scenario, in which case the request from VTEX does not send the paramenters `country` and `postalCode`.
        The call's payload can be adapted into two scenarios:

        - **Displaying items in the storefront**: the address information can be nulled in the request, since they are not mandatory data for this context.
        - **Making a shopping cart simulation during checkout**: address information must be sent, since this data is needed to calculate freight values. If the address information (including `postalCode` and `country`) is not sent through the call, VTEX interprets the stock balance as zero. Without a valid stock balance, the seller will not be shown as an option during checkout.

        ## Request body example - Indexing simulation

        ```
        {
            "items": [
              {
                "id": "7908010136043",
                "quantity": 1,
                "seller": "1",
              }
            ],
            "isCheckedIn": false,
          }
        ```
        ## Request body example - Checkout simulation

        ```
        {
            "items": [
              {
                "id": "7908010136043",
                "quantity": 1,
                "seller": "1",
              }
            ],
            "postalCode": "22270-030",
            "country": "BRA",
          }
        ```

        Parameters
        ----------
        fulfillment_endpoint : str
            This is the fulfillment endpoint registered for each specific external seller in the **seller management** section of VTEX's admin panel.

        postal_code : str
            Delivery address postal code. This field is mandatory for shopping carts simulations, where both Country and Postal Code are required. This field should be sent as `null` for storefront simulations, where the information is not necessary.

        country : typing.Optional[str]
            ISO 3-digit code of the country where the delivery address is located.  This field is mandatory, for shopping carts simulations, where both Country and Postal Code are required. This field should be sent as `null` for storefront simulations, where the information is not necessary.

        geo_coordinates : typing.Optional[typing.Sequence[str]]
            Geographic coordinates of the delivery address. This may be used instead of the postalCode, in case the marketplace is configured to accept geolocation. Example of value: `[-22.9443504,-43.1825635]`.

        items : typing.Optional[typing.Sequence[FulfillmentItem]]
            Array containing the cart items.

        sc : typing.Optional[str]
            Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) associated to the seller account created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FulfillmentSimulationResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.external_seller.fulfillment_simulation(
            fulfillment_endpoint="marketplaceexample.externalseller.com",
            postal_code="12345678",
        )
        """
        _response = self._raw_client.fulfillment_simulation(
            fulfillment_endpoint,
            postal_code=postal_code,
            country=country,
            geo_coordinates=geo_coordinates,
            items=items,
            sc=sc,
            request_options=request_options,
        )
        return _response.data

    def order_placement(
        self,
        fulfillment_endpoint: str,
        *,
        authorization: str,
        vtex_api_appkey: str,
        vtex_api_apptoken: str,
        accept: str,
        accept_enconding: str,
        vtex_operation_id: str,
        forwarded_proto: str,
        vtex_cache_client_bypass: str,
        traceparent: str,
        client_profile_data: typing.Optional[OrderPlacementClientProfileData] = OMIT,
        items: typing.Optional[typing.Sequence[OrderPlacementItemsItem]] = OMIT,
        marketing_data: typing.Optional[OrderPlacementMarketingData] = OMIT,
        marketplace_order_id: typing.Optional[str] = OMIT,
        marketplace_payment_value: typing.Optional[int] = OMIT,
        marketplace_services_endpoint: typing.Optional[str] = OMIT,
        open_text_field: typing.Optional[str] = OMIT,
        payment_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        shipping_data: typing.Optional[OrderPlacementShippingData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This request is sent by VTEX to the external seller once the customer finishes their checkout, to let the seller know there is a newly placed order. It does that by calling the **Order Placement** endpoint, which needs to be implemented by the seller.

        The marketplace will send information such as the items contained in the cart, the client’s profile data, the shipping data, and the payment data. With all that, the seller will be able to create the order in their own store.

        Parameters
        ----------
        fulfillment_endpoint : str
            This is the fulfillment endpoint registered for each specific external seller in the **seller management** section of VTEX's admin panel.

        authorization : str
            Indicates authorization.

        vtex_api_appkey : str
            VTEX API app key.

        vtex_api_apptoken : str
            VTEX API app token.

        accept : str
            HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.

        accept_enconding : str
            Indicates the types of response enconding the client can understand.

        vtex_operation_id : str
            VTEX operation ID.

        forwarded_proto : str
            Determines the protocol used by the client in the request.

        vtex_cache_client_bypass : str
            VTEX cache client bypass.

        traceparent : str
            Identifies the incoming request in a tracing system.

        client_profile_data : typing.Optional[OrderPlacementClientProfileData]
            Customer's profile information.

        items : typing.Optional[typing.Sequence[OrderPlacementItemsItem]]
            Array of objects containing data about each SKU in the cart.

        marketing_data : typing.Optional[OrderPlacementMarketingData]
            Marketing tracking data. If the order has no tracking data, the value will be `null`.

        marketplace_order_id : typing.Optional[str]
            Identifies the order in the marketplace.

        marketplace_payment_value : typing.Optional[int]
            Amount that the marketplace agrees to pay to the seller. The last two digits are the cents. For example, $24.99 is represented 2499.

        marketplace_services_endpoint : typing.Optional[str]
            Endpoint sent by VTEX to the seller, that will be used to send the invoice and tracking data to the marketplace. This endpoint will also be used in [change order in Multilevel Omnichannel Inventory](https://developers.vtex.com/docs/guides/change-orders-multilevel-omnichannel-inventory-external-marketplaces#implementators) operations in external marketplaces.

        open_text_field : typing.Optional[str]
            Optional field meant to hold additional information about the order. We recommend using this field for text, not data formats such as `json` even if escaped. For that purpose, see [Creating customizable fields](https://developers.vtex.com/vtex-rest-api/docs/creating-customizable-fields-in-the-cart-with-checkout-api-1)

        payment_data : typing.Optional[typing.Dict[str, typing.Any]]
            In other contexts, this field tipically holds an object with payment information. However, since the payment is processed by the marketplace, it will be sent to the seller as `null` in this context.

        shipping_data : typing.Optional[OrderPlacementShippingData]
            Shipping information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.external_seller.order_placement(
            fulfillment_endpoint="https://marketplaceexample.externalseller.com",
            authorization='VTEX key="appKey" token="appToken"',
            vtex_api_appkey="appKey",
            vtex_api_apptoken="appToken",
            accept="application/json",
            accept_enconding="gzip, deflate",
            vtex_operation_id="8032114b-63e9-4e64-b30c-f7afcf676d7a",
            forwarded_proto="https",
            vtex_cache_client_bypass="1",
            traceparent="00-083c0ca18bc8d94183f333809a70cd64-bf5e9a641e230540-00",
        )
        """
        _response = self._raw_client.order_placement(
            fulfillment_endpoint,
            authorization=authorization,
            vtex_api_appkey=vtex_api_appkey,
            vtex_api_apptoken=vtex_api_apptoken,
            accept=accept,
            accept_enconding=accept_enconding,
            vtex_operation_id=vtex_operation_id,
            forwarded_proto=forwarded_proto,
            vtex_cache_client_bypass=vtex_cache_client_bypass,
            traceparent=traceparent,
            client_profile_data=client_profile_data,
            items=items,
            marketing_data=marketing_data,
            marketplace_order_id=marketplace_order_id,
            marketplace_payment_value=marketplace_payment_value,
            marketplace_services_endpoint=marketplace_services_endpoint,
            open_text_field=open_text_field,
            payment_data=payment_data,
            shipping_data=shipping_data,
            request_options=request_options,
        )
        return _response.data

    def mkp_order_cancellation(
        self,
        fulfillment_endpoint: str,
        order_id: str,
        *,
        marketplace_order_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This request may be sent from VTEX to the external seller in case of order cancelation. For that, the seller will need to implement the Marketplace order cancellation endpoint. Whenever this request is received by the seler, the order should be canceled and the fulfillment flow should not proceed.

        For the seller to:

        - **Evaluate a cancellation request:** it is possible to send an empty body as a response to the cancellation request, meaning that the seller is evaluating whether to proceed with the cancellation or not.

        - **Confirm the cancellation request:** it is possible to confirm the order cancellation by the marketplace by responding to the call with a body including only one information: the `marketplaceOrderId`, which identifies the order in the marketplace. The seller should use this ID to trigger the cancellation of the corresponding order. The seller should then respond with the same `marketplaceOrderId` and also with the `orderId`, which identifies the order in the seller, the date and time of the notification receipt, and a protocol code that confirms the receipt of the request (which may have the value `null`).

        - **Refuse a cancellation request:** it is possible to to [send the Invoice](https://developers.vtex.com/vtex-rest-api/reference/external-seller#send-invoice), meaning that the cancellation has been denied, and the flow continues to the [Order Invoicing](https://developers.vtex.com/vtex-rest-api/docs/external-seller-integration-connector#order-invoicing) step, and the ones that follow it.

        This call should be made twice: once for the *Evaluate cancellation request* scenario, and a second time to *Confirm cancellation* or *Refuse cancellation*.

        Parameters
        ----------
        fulfillment_endpoint : str
            This is the fulfillment endpoint registered for each specific external seller in the **seller management** section of VTEX's admin panel.

        order_id : str
            ID of the order being fulfilled

        marketplace_order_id : str
            Identifies the order. The seller should use this ID to trigger the cancellation of the corresponding order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.external_seller.mkp_order_cancellation(
            fulfillment_endpoint="marketplaceexample.externalseller.com",
            order_id="orderId",
            marketplace_order_id="1138342255777-01",
        )
        """
        _response = self._raw_client.mkp_order_cancellation(
            fulfillment_endpoint, order_id, marketplace_order_id=marketplace_order_id, request_options=request_options
        )
        return _response.data

    def authorize_fulfillment(
        self,
        fulfillment_endpoint: str,
        seller_order_id: str,
        *,
        marketplace_order_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This request is sent from VTEX to the seller after the payment is approved, to notify them that the fulfillment process can start.

        Parameters
        ----------
        fulfillment_endpoint : str
            This is the fulfillment endpoint registered for each specific external seller in the **seller management** section of VTEX's admin panel.

        seller_order_id : str
            Seller's order ID of the order ready for fulfillment. The seller can be a VTEX seller or an external one.

        marketplace_order_id : str
            Identifies the order. The seller should use this ID to trigger the fulfillment process of the corresponding order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.external_seller.authorize_fulfillment(
            fulfillment_endpoint="https://marketplaceexample.externalseller.com",
            seller_order_id="00-1268540501456-01",
            marketplace_order_id="1138342255777-01",
        )
        """
        _response = self._raw_client.authorize_fulfillment(
            fulfillment_endpoint,
            seller_order_id,
            marketplace_order_id=marketplace_order_id,
            request_options=request_options,
        )
        return _response.data

    def cancel_order_in_marketplace(
        self,
        marketplace_services_endpoint: str,
        marketplace_order_id: str,
        *,
        reason: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This request is sent by the external seller to the VTEX marketplace to cancel an order.

        Parameters
        ----------
        marketplace_services_endpoint : str
            This is an endpoint sent from VTEX to the external seller in the [Order placement request](https://developers.vtex.com/vtex-rest-api/reference/external-seller#order-placement).

        marketplace_order_id : str
            Identifies the order in the marketplace.

        reason : str
            Insert here the reason for the order's cancellation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.external_seller.cancel_order_in_marketplace(
            marketplace_services_endpoint="marketplaceservicesendpoint.myvtex.com",
            marketplace_order_id="1138342255777-01",
            reason="Product is unavailable",
        )
        """
        _response = self._raw_client.cancel_order_in_marketplace(
            marketplace_services_endpoint, marketplace_order_id, reason=reason, request_options=request_options
        )
        return _response.data

    def send_invoice(
        self,
        marketplace_services_endpoint: str,
        marketplace_order_id: str,
        *,
        invoice_number: str,
        items: typing.Sequence[SendInvoiceRequestItemsItem],
        type: str,
        courier: typing.Optional[str] = OMIT,
        invoice_value: typing.Optional[int] = OMIT,
        issuance_date: typing.Optional[str] = OMIT,
        tracking_number: typing.Optional[str] = OMIT,
        tracking_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This request is sent by the external seller to the VTEX marketplace to send invoice information.

        This can be necessary in a regular order or in the case of a return. The `type` field is used to indicate which of these is the case.

        Parameters
        ----------
        marketplace_services_endpoint : str
            This is an endpoint sent from VTEX to the external seller in the [Order placement request](https://developers.vtex.com/vtex-rest-api/reference/external-seller#order-placement).

        marketplace_order_id : str
            Identifies the order in the marketplace.

        invoice_number : str
            Invoice number

        items : typing.Sequence[SendInvoiceRequestItemsItem]
            Array containing the order items.

        type : str
            Indicates the type of the invoice. Use `"Output"` for regular orders and `"Input"` for returns.

        courier : typing.Optional[str]
            Courier, if available on invoice.

        invoice_value : typing.Optional[int]
            Invoice value.

        issuance_date : typing.Optional[str]
            Issuance date.

        tracking_number : typing.Optional[str]
            Tracking number.

        tracking_url : typing.Optional[str]
            Tracking URL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern.external_seller import SendInvoiceRequestItemsItem

        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.external_seller.send_invoice(
            marketplace_services_endpoint="marketplaceservicesendpoint.myvtex.com",
            marketplace_order_id="1138342255777-01",
            invoice_number="NFe-00002",
            items=[
                SendInvoiceRequestItemsItem(
                    id="6",
                    price=5500,
                    quantity=1,
                )
            ],
            type="Output",
        )
        """
        _response = self._raw_client.send_invoice(
            marketplace_services_endpoint,
            marketplace_order_id,
            invoice_number=invoice_number,
            items=items,
            type=type,
            courier=courier,
            invoice_value=invoice_value,
            issuance_date=issuance_date,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            request_options=request_options,
        )
        return _response.data

    def send_tracking_information(
        self,
        marketplace_services_endpoint: str,
        marketplace_order_id: str,
        invoice_number: str,
        *,
        courier: typing.Optional[str] = OMIT,
        dispatched_date: typing.Optional[str] = OMIT,
        tracking_number: typing.Optional[str] = OMIT,
        tracking_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This request is sent by the external seller to the VTEX marketplace to add tracking information to a given order's invoice, in case it is necessary to do so after the invoice has been sent.

        Parameters
        ----------
        marketplace_services_endpoint : str
            This is an endpoint sent from VTEX to the external seller in the [Order placement request](https://developers.vtex.com/vtex-rest-api/reference/external-seller#order-placement).

        marketplace_order_id : str
            Identifies the order in the marketplace.

        invoice_number : str
            Invoice number.

        courier : typing.Optional[str]
            Courier.

        dispatched_date : typing.Optional[str]
            Date of order dispatch.

        tracking_number : typing.Optional[str]
            Tracking number.

        tracking_url : typing.Optional[str]
            Tracking URL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.external_seller.send_tracking_information(
            marketplace_services_endpoint="marketplaceservicesendpoint.myvtex.com",
            marketplace_order_id="1138342255777-01",
            invoice_number="NFe-00002",
        )
        """
        _response = self._raw_client.send_tracking_information(
            marketplace_services_endpoint,
            marketplace_order_id,
            invoice_number,
            courier=courier,
            dispatched_date=dispatched_date,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            request_options=request_options,
        )
        return _response.data

    def update_tracking_status(
        self,
        marketplace_services_endpoint: str,
        marketplace_order_id: str,
        invoice_number: str,
        *,
        is_delivered: bool,
        events: typing.Optional[typing.Sequence[UpdateTrackingStatusRequestEventsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This request is sent by the external seller to the VTEX marketplace to update a given order's tracking status.

        Parameters
        ----------
        marketplace_services_endpoint : str
            This is an endpoint sent from VTEX to the external seller in the [Order placement request](https://developers.vtex.com/vtex-rest-api/reference/external-seller#order-placement).

        marketplace_order_id : str
            Identifies the order in the marketplace.

        invoice_number : str
            Invoice number.

        is_delivered : bool
            Indicates if order has been delivered. `false` if it is in transit.

        events : typing.Optional[typing.Sequence[UpdateTrackingStatusRequestEventsItem]]
            Array containing information on each tracking event received.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.external_seller.update_tracking_status(
            marketplace_services_endpoint="marketplaceservicesendpoint.myvtex.com",
            marketplace_order_id="1138342255777-01",
            invoice_number="NFe-00002",
            is_delivered=True,
        )
        """
        _response = self._raw_client.update_tracking_status(
            marketplace_services_endpoint,
            marketplace_order_id,
            invoice_number,
            is_delivered=is_delivered,
            events=events,
            request_options=request_options,
        )
        return _response.data


class AsyncExternalSellerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExternalSellerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExternalSellerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExternalSellerClient
        """
        return self._raw_client

    async def fulfillment_simulation(
        self,
        fulfillment_endpoint: str,
        *,
        postal_code: str,
        country: typing.Optional[str] = OMIT,
        geo_coordinates: typing.Optional[typing.Sequence[str]] = OMIT,
        items: typing.Optional[typing.Sequence[FulfillmentItem]] = OMIT,
        sc: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FulfillmentSimulationResponse:
        """
        This endpoint may be called upon by VTEX for fulfillment simulation in the external seller different contexts. See examples below.

        When a [price](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/price) or [inventory](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/inventory) notification request returns a response with status `200 OK`, it means that the SKU already exists in the marketplace. Whenever this happens, the marketplace will call the seller to get two updated information about the SKU: Price and Inventory.

        The seller needs to have an endpoint implemented in order to receive this call and send a response containing the requested information to the marketplace. We call it the Fulfillment Simulation endpoint.

        If the seller wishes to include other parameters in this call (like account name, or [sales channel](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV) ID), this should be done within their {fulfillmentEndpoint}. This path is then inserted in the marketplace's VTEX admin when [configuring a seller](https://help.vtex.com/en/tutorial/configurando-seller--tutorials_392).

        The marketplace will send an object containing an array of items. The seller must use this list to get the updated information about the referred SKUs and send them back to the marketplace, following the response format explained in the API Reference.

        This call is also applied in the Storefront simulation scenario, in which case the request from VTEX does not send the paramenters `country` and `postalCode`.
        The call's payload can be adapted into two scenarios:

        - **Displaying items in the storefront**: the address information can be nulled in the request, since they are not mandatory data for this context.
        - **Making a shopping cart simulation during checkout**: address information must be sent, since this data is needed to calculate freight values. If the address information (including `postalCode` and `country`) is not sent through the call, VTEX interprets the stock balance as zero. Without a valid stock balance, the seller will not be shown as an option during checkout.

        ## Request body example - Indexing simulation

        ```
        {
            "items": [
              {
                "id": "7908010136043",
                "quantity": 1,
                "seller": "1",
              }
            ],
            "isCheckedIn": false,
          }
        ```
        ## Request body example - Checkout simulation

        ```
        {
            "items": [
              {
                "id": "7908010136043",
                "quantity": 1,
                "seller": "1",
              }
            ],
            "postalCode": "22270-030",
            "country": "BRA",
          }
        ```

        Parameters
        ----------
        fulfillment_endpoint : str
            This is the fulfillment endpoint registered for each specific external seller in the **seller management** section of VTEX's admin panel.

        postal_code : str
            Delivery address postal code. This field is mandatory for shopping carts simulations, where both Country and Postal Code are required. This field should be sent as `null` for storefront simulations, where the information is not necessary.

        country : typing.Optional[str]
            ISO 3-digit code of the country where the delivery address is located.  This field is mandatory, for shopping carts simulations, where both Country and Postal Code are required. This field should be sent as `null` for storefront simulations, where the information is not necessary.

        geo_coordinates : typing.Optional[typing.Sequence[str]]
            Geographic coordinates of the delivery address. This may be used instead of the postalCode, in case the marketplace is configured to accept geolocation. Example of value: `[-22.9443504,-43.1825635]`.

        items : typing.Optional[typing.Sequence[FulfillmentItem]]
            Array containing the cart items.

        sc : typing.Optional[str]
            Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) associated to the seller account created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FulfillmentSimulationResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.external_seller.fulfillment_simulation(
                fulfillment_endpoint="marketplaceexample.externalseller.com",
                postal_code="12345678",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fulfillment_simulation(
            fulfillment_endpoint,
            postal_code=postal_code,
            country=country,
            geo_coordinates=geo_coordinates,
            items=items,
            sc=sc,
            request_options=request_options,
        )
        return _response.data

    async def order_placement(
        self,
        fulfillment_endpoint: str,
        *,
        authorization: str,
        vtex_api_appkey: str,
        vtex_api_apptoken: str,
        accept: str,
        accept_enconding: str,
        vtex_operation_id: str,
        forwarded_proto: str,
        vtex_cache_client_bypass: str,
        traceparent: str,
        client_profile_data: typing.Optional[OrderPlacementClientProfileData] = OMIT,
        items: typing.Optional[typing.Sequence[OrderPlacementItemsItem]] = OMIT,
        marketing_data: typing.Optional[OrderPlacementMarketingData] = OMIT,
        marketplace_order_id: typing.Optional[str] = OMIT,
        marketplace_payment_value: typing.Optional[int] = OMIT,
        marketplace_services_endpoint: typing.Optional[str] = OMIT,
        open_text_field: typing.Optional[str] = OMIT,
        payment_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        shipping_data: typing.Optional[OrderPlacementShippingData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This request is sent by VTEX to the external seller once the customer finishes their checkout, to let the seller know there is a newly placed order. It does that by calling the **Order Placement** endpoint, which needs to be implemented by the seller.

        The marketplace will send information such as the items contained in the cart, the client’s profile data, the shipping data, and the payment data. With all that, the seller will be able to create the order in their own store.

        Parameters
        ----------
        fulfillment_endpoint : str
            This is the fulfillment endpoint registered for each specific external seller in the **seller management** section of VTEX's admin panel.

        authorization : str
            Indicates authorization.

        vtex_api_appkey : str
            VTEX API app key.

        vtex_api_apptoken : str
            VTEX API app token.

        accept : str
            HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.

        accept_enconding : str
            Indicates the types of response enconding the client can understand.

        vtex_operation_id : str
            VTEX operation ID.

        forwarded_proto : str
            Determines the protocol used by the client in the request.

        vtex_cache_client_bypass : str
            VTEX cache client bypass.

        traceparent : str
            Identifies the incoming request in a tracing system.

        client_profile_data : typing.Optional[OrderPlacementClientProfileData]
            Customer's profile information.

        items : typing.Optional[typing.Sequence[OrderPlacementItemsItem]]
            Array of objects containing data about each SKU in the cart.

        marketing_data : typing.Optional[OrderPlacementMarketingData]
            Marketing tracking data. If the order has no tracking data, the value will be `null`.

        marketplace_order_id : typing.Optional[str]
            Identifies the order in the marketplace.

        marketplace_payment_value : typing.Optional[int]
            Amount that the marketplace agrees to pay to the seller. The last two digits are the cents. For example, $24.99 is represented 2499.

        marketplace_services_endpoint : typing.Optional[str]
            Endpoint sent by VTEX to the seller, that will be used to send the invoice and tracking data to the marketplace. This endpoint will also be used in [change order in Multilevel Omnichannel Inventory](https://developers.vtex.com/docs/guides/change-orders-multilevel-omnichannel-inventory-external-marketplaces#implementators) operations in external marketplaces.

        open_text_field : typing.Optional[str]
            Optional field meant to hold additional information about the order. We recommend using this field for text, not data formats such as `json` even if escaped. For that purpose, see [Creating customizable fields](https://developers.vtex.com/vtex-rest-api/docs/creating-customizable-fields-in-the-cart-with-checkout-api-1)

        payment_data : typing.Optional[typing.Dict[str, typing.Any]]
            In other contexts, this field tipically holds an object with payment information. However, since the payment is processed by the marketplace, it will be sent to the seller as `null` in this context.

        shipping_data : typing.Optional[OrderPlacementShippingData]
            Shipping information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.external_seller.order_placement(
                fulfillment_endpoint="https://marketplaceexample.externalseller.com",
                authorization='VTEX key="appKey" token="appToken"',
                vtex_api_appkey="appKey",
                vtex_api_apptoken="appToken",
                accept="application/json",
                accept_enconding="gzip, deflate",
                vtex_operation_id="8032114b-63e9-4e64-b30c-f7afcf676d7a",
                forwarded_proto="https",
                vtex_cache_client_bypass="1",
                traceparent="00-083c0ca18bc8d94183f333809a70cd64-bf5e9a641e230540-00",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.order_placement(
            fulfillment_endpoint,
            authorization=authorization,
            vtex_api_appkey=vtex_api_appkey,
            vtex_api_apptoken=vtex_api_apptoken,
            accept=accept,
            accept_enconding=accept_enconding,
            vtex_operation_id=vtex_operation_id,
            forwarded_proto=forwarded_proto,
            vtex_cache_client_bypass=vtex_cache_client_bypass,
            traceparent=traceparent,
            client_profile_data=client_profile_data,
            items=items,
            marketing_data=marketing_data,
            marketplace_order_id=marketplace_order_id,
            marketplace_payment_value=marketplace_payment_value,
            marketplace_services_endpoint=marketplace_services_endpoint,
            open_text_field=open_text_field,
            payment_data=payment_data,
            shipping_data=shipping_data,
            request_options=request_options,
        )
        return _response.data

    async def mkp_order_cancellation(
        self,
        fulfillment_endpoint: str,
        order_id: str,
        *,
        marketplace_order_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This request may be sent from VTEX to the external seller in case of order cancelation. For that, the seller will need to implement the Marketplace order cancellation endpoint. Whenever this request is received by the seler, the order should be canceled and the fulfillment flow should not proceed.

        For the seller to:

        - **Evaluate a cancellation request:** it is possible to send an empty body as a response to the cancellation request, meaning that the seller is evaluating whether to proceed with the cancellation or not.

        - **Confirm the cancellation request:** it is possible to confirm the order cancellation by the marketplace by responding to the call with a body including only one information: the `marketplaceOrderId`, which identifies the order in the marketplace. The seller should use this ID to trigger the cancellation of the corresponding order. The seller should then respond with the same `marketplaceOrderId` and also with the `orderId`, which identifies the order in the seller, the date and time of the notification receipt, and a protocol code that confirms the receipt of the request (which may have the value `null`).

        - **Refuse a cancellation request:** it is possible to to [send the Invoice](https://developers.vtex.com/vtex-rest-api/reference/external-seller#send-invoice), meaning that the cancellation has been denied, and the flow continues to the [Order Invoicing](https://developers.vtex.com/vtex-rest-api/docs/external-seller-integration-connector#order-invoicing) step, and the ones that follow it.

        This call should be made twice: once for the *Evaluate cancellation request* scenario, and a second time to *Confirm cancellation* or *Refuse cancellation*.

        Parameters
        ----------
        fulfillment_endpoint : str
            This is the fulfillment endpoint registered for each specific external seller in the **seller management** section of VTEX's admin panel.

        order_id : str
            ID of the order being fulfilled

        marketplace_order_id : str
            Identifies the order. The seller should use this ID to trigger the cancellation of the corresponding order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.external_seller.mkp_order_cancellation(
                fulfillment_endpoint="marketplaceexample.externalseller.com",
                order_id="orderId",
                marketplace_order_id="1138342255777-01",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mkp_order_cancellation(
            fulfillment_endpoint, order_id, marketplace_order_id=marketplace_order_id, request_options=request_options
        )
        return _response.data

    async def authorize_fulfillment(
        self,
        fulfillment_endpoint: str,
        seller_order_id: str,
        *,
        marketplace_order_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This request is sent from VTEX to the seller after the payment is approved, to notify them that the fulfillment process can start.

        Parameters
        ----------
        fulfillment_endpoint : str
            This is the fulfillment endpoint registered for each specific external seller in the **seller management** section of VTEX's admin panel.

        seller_order_id : str
            Seller's order ID of the order ready for fulfillment. The seller can be a VTEX seller or an external one.

        marketplace_order_id : str
            Identifies the order. The seller should use this ID to trigger the fulfillment process of the corresponding order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.external_seller.authorize_fulfillment(
                fulfillment_endpoint="https://marketplaceexample.externalseller.com",
                seller_order_id="00-1268540501456-01",
                marketplace_order_id="1138342255777-01",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.authorize_fulfillment(
            fulfillment_endpoint,
            seller_order_id,
            marketplace_order_id=marketplace_order_id,
            request_options=request_options,
        )
        return _response.data

    async def cancel_order_in_marketplace(
        self,
        marketplace_services_endpoint: str,
        marketplace_order_id: str,
        *,
        reason: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This request is sent by the external seller to the VTEX marketplace to cancel an order.

        Parameters
        ----------
        marketplace_services_endpoint : str
            This is an endpoint sent from VTEX to the external seller in the [Order placement request](https://developers.vtex.com/vtex-rest-api/reference/external-seller#order-placement).

        marketplace_order_id : str
            Identifies the order in the marketplace.

        reason : str
            Insert here the reason for the order's cancellation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.external_seller.cancel_order_in_marketplace(
                marketplace_services_endpoint="marketplaceservicesendpoint.myvtex.com",
                marketplace_order_id="1138342255777-01",
                reason="Product is unavailable",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_order_in_marketplace(
            marketplace_services_endpoint, marketplace_order_id, reason=reason, request_options=request_options
        )
        return _response.data

    async def send_invoice(
        self,
        marketplace_services_endpoint: str,
        marketplace_order_id: str,
        *,
        invoice_number: str,
        items: typing.Sequence[SendInvoiceRequestItemsItem],
        type: str,
        courier: typing.Optional[str] = OMIT,
        invoice_value: typing.Optional[int] = OMIT,
        issuance_date: typing.Optional[str] = OMIT,
        tracking_number: typing.Optional[str] = OMIT,
        tracking_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This request is sent by the external seller to the VTEX marketplace to send invoice information.

        This can be necessary in a regular order or in the case of a return. The `type` field is used to indicate which of these is the case.

        Parameters
        ----------
        marketplace_services_endpoint : str
            This is an endpoint sent from VTEX to the external seller in the [Order placement request](https://developers.vtex.com/vtex-rest-api/reference/external-seller#order-placement).

        marketplace_order_id : str
            Identifies the order in the marketplace.

        invoice_number : str
            Invoice number

        items : typing.Sequence[SendInvoiceRequestItemsItem]
            Array containing the order items.

        type : str
            Indicates the type of the invoice. Use `"Output"` for regular orders and `"Input"` for returns.

        courier : typing.Optional[str]
            Courier, if available on invoice.

        invoice_value : typing.Optional[int]
            Invoice value.

        issuance_date : typing.Optional[str]
            Issuance date.

        tracking_number : typing.Optional[str]
            Tracking number.

        tracking_url : typing.Optional[str]
            Tracking URL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern.external_seller import SendInvoiceRequestItemsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.external_seller.send_invoice(
                marketplace_services_endpoint="marketplaceservicesendpoint.myvtex.com",
                marketplace_order_id="1138342255777-01",
                invoice_number="NFe-00002",
                items=[
                    SendInvoiceRequestItemsItem(
                        id="6",
                        price=5500,
                        quantity=1,
                    )
                ],
                type="Output",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_invoice(
            marketplace_services_endpoint,
            marketplace_order_id,
            invoice_number=invoice_number,
            items=items,
            type=type,
            courier=courier,
            invoice_value=invoice_value,
            issuance_date=issuance_date,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            request_options=request_options,
        )
        return _response.data

    async def send_tracking_information(
        self,
        marketplace_services_endpoint: str,
        marketplace_order_id: str,
        invoice_number: str,
        *,
        courier: typing.Optional[str] = OMIT,
        dispatched_date: typing.Optional[str] = OMIT,
        tracking_number: typing.Optional[str] = OMIT,
        tracking_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This request is sent by the external seller to the VTEX marketplace to add tracking information to a given order's invoice, in case it is necessary to do so after the invoice has been sent.

        Parameters
        ----------
        marketplace_services_endpoint : str
            This is an endpoint sent from VTEX to the external seller in the [Order placement request](https://developers.vtex.com/vtex-rest-api/reference/external-seller#order-placement).

        marketplace_order_id : str
            Identifies the order in the marketplace.

        invoice_number : str
            Invoice number.

        courier : typing.Optional[str]
            Courier.

        dispatched_date : typing.Optional[str]
            Date of order dispatch.

        tracking_number : typing.Optional[str]
            Tracking number.

        tracking_url : typing.Optional[str]
            Tracking URL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.external_seller.send_tracking_information(
                marketplace_services_endpoint="marketplaceservicesendpoint.myvtex.com",
                marketplace_order_id="1138342255777-01",
                invoice_number="NFe-00002",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_tracking_information(
            marketplace_services_endpoint,
            marketplace_order_id,
            invoice_number,
            courier=courier,
            dispatched_date=dispatched_date,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            request_options=request_options,
        )
        return _response.data

    async def update_tracking_status(
        self,
        marketplace_services_endpoint: str,
        marketplace_order_id: str,
        invoice_number: str,
        *,
        is_delivered: bool,
        events: typing.Optional[typing.Sequence[UpdateTrackingStatusRequestEventsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This request is sent by the external seller to the VTEX marketplace to update a given order's tracking status.

        Parameters
        ----------
        marketplace_services_endpoint : str
            This is an endpoint sent from VTEX to the external seller in the [Order placement request](https://developers.vtex.com/vtex-rest-api/reference/external-seller#order-placement).

        marketplace_order_id : str
            Identifies the order in the marketplace.

        invoice_number : str
            Invoice number.

        is_delivered : bool
            Indicates if order has been delivered. `false` if it is in transit.

        events : typing.Optional[typing.Sequence[UpdateTrackingStatusRequestEventsItem]]
            Array containing information on each tracking event received.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.external_seller.update_tracking_status(
                marketplace_services_endpoint="marketplaceservicesendpoint.myvtex.com",
                marketplace_order_id="1138342255777-01",
                invoice_number="NFe-00002",
                is_delivered=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_tracking_status(
            marketplace_services_endpoint,
            marketplace_order_id,
            invoice_number,
            is_delivered=is_delivered,
            events=events,
            request_options=request_options,
        )
        return _response.data
