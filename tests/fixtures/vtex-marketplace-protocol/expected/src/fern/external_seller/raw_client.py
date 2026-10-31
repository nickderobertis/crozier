

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.fulfillment_item import FulfillmentItem
from .types.fulfillment_simulation_response import FulfillmentSimulationResponse
from .types.order_placement_client_profile_data import OrderPlacementClientProfileData
from .types.order_placement_items_item import OrderPlacementItemsItem
from .types.order_placement_marketing_data import OrderPlacementMarketingData
from .types.order_placement_shipping_data import OrderPlacementShippingData
from .types.send_invoice_request_items_item import SendInvoiceRequestItemsItem
from .types.update_tracking_status_request_events_item import UpdateTrackingStatusRequestEventsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawExternalSellerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[FulfillmentSimulationResponse]:
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
        HttpResponse[FulfillmentSimulationResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(fulfillment_endpoint)}/pvt/orderForms/simulation",
            method="POST",
            json={
                "country": country,
                "geoCoordinates": geo_coordinates,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[FulfillmentItem], direction="write"
                ),
                "postalCode": postal_code,
                "sc": sc,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FulfillmentSimulationResponse,
                    parse_obj_as(
                        type_=FulfillmentSimulationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(fulfillment_endpoint)}/pvt/orders",
            method="POST",
            json={
                "clientProfileData": convert_and_respect_annotation_metadata(
                    object_=client_profile_data, annotation=OrderPlacementClientProfileData, direction="write"
                ),
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[OrderPlacementItemsItem], direction="write"
                ),
                "marketingData": convert_and_respect_annotation_metadata(
                    object_=marketing_data, annotation=OrderPlacementMarketingData, direction="write"
                ),
                "marketplaceOrderId": marketplace_order_id,
                "marketplacePaymentValue": marketplace_payment_value,
                "marketplaceServicesEndpoint": marketplace_services_endpoint,
                "openTextField": open_text_field,
                "paymentData": payment_data,
                "shippingData": convert_and_respect_annotation_metadata(
                    object_=shipping_data, annotation=OrderPlacementShippingData, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "authorization": str(authorization) if authorization is not None else None,
                "x-vtex-api-appkey": str(vtex_api_appkey) if vtex_api_appkey is not None else None,
                "x-vtex-api-apptoken": str(vtex_api_apptoken) if vtex_api_apptoken is not None else None,
                "accept": str(accept) if accept is not None else None,
                "accept-enconding": str(accept_enconding) if accept_enconding is not None else None,
                "x-vtex-operation-id": str(vtex_operation_id) if vtex_operation_id is not None else None,
                "x-forwarded-proto": str(forwarded_proto) if forwarded_proto is not None else None,
                "x-vtex-cache-client-bypass": str(vtex_cache_client_bypass)
                if vtex_cache_client_bypass is not None
                else None,
                "traceparent": str(traceparent) if traceparent is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mkp_order_cancellation(
        self,
        fulfillment_endpoint: str,
        order_id: str,
        *,
        marketplace_order_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(fulfillment_endpoint)}/pvt/orders/{encode_path_param(order_id)}/cancel",
            method="POST",
            json={
                "marketplaceOrderId": marketplace_order_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def authorize_fulfillment(
        self,
        fulfillment_endpoint: str,
        seller_order_id: str,
        *,
        marketplace_order_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(fulfillment_endpoint)}/pvt/orders/{encode_path_param(seller_order_id)}/fulfill",
            method="POST",
            json={
                "marketplaceOrderId": marketplace_order_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancel_order_in_marketplace(
        self,
        marketplace_services_endpoint: str,
        marketplace_order_id: str,
        *,
        reason: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(marketplace_services_endpoint)}/pvt/orders/{encode_path_param(marketplace_order_id)}/cancel",
            method="POST",
            json={
                "reason": reason,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(marketplace_services_endpoint)}/pvt/orders/{encode_path_param(marketplace_order_id)}/invoice",
            method="POST",
            json={
                "courier": courier,
                "invoiceNumber": invoice_number,
                "invoiceValue": invoice_value,
                "issuanceDate": issuance_date,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[SendInvoiceRequestItemsItem], direction="write"
                ),
                "trackingNumber": tracking_number,
                "trackingUrl": tracking_url,
                "type": type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(marketplace_services_endpoint)}/pvt/orders/{encode_path_param(marketplace_order_id)}/invoice/{encode_path_param(invoice_number)}",
            method="POST",
            json={
                "courier": courier,
                "dispatchedDate": dispatched_date,
                "trackingNumber": tracking_number,
                "trackingUrl": tracking_url,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_tracking_status(
        self,
        marketplace_services_endpoint: str,
        marketplace_order_id: str,
        invoice_number: str,
        *,
        is_delivered: bool,
        events: typing.Optional[typing.Sequence[UpdateTrackingStatusRequestEventsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(marketplace_services_endpoint)}/pvt/orders/{encode_path_param(marketplace_order_id)}/invoice/{encode_path_param(invoice_number)}/tracking",
            method="POST",
            json={
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=typing.Sequence[UpdateTrackingStatusRequestEventsItem], direction="write"
                ),
                "isDelivered": is_delivered,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawExternalSellerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[FulfillmentSimulationResponse]:
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
        AsyncHttpResponse[FulfillmentSimulationResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(fulfillment_endpoint)}/pvt/orderForms/simulation",
            method="POST",
            json={
                "country": country,
                "geoCoordinates": geo_coordinates,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[FulfillmentItem], direction="write"
                ),
                "postalCode": postal_code,
                "sc": sc,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FulfillmentSimulationResponse,
                    parse_obj_as(
                        type_=FulfillmentSimulationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(fulfillment_endpoint)}/pvt/orders",
            method="POST",
            json={
                "clientProfileData": convert_and_respect_annotation_metadata(
                    object_=client_profile_data, annotation=OrderPlacementClientProfileData, direction="write"
                ),
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[OrderPlacementItemsItem], direction="write"
                ),
                "marketingData": convert_and_respect_annotation_metadata(
                    object_=marketing_data, annotation=OrderPlacementMarketingData, direction="write"
                ),
                "marketplaceOrderId": marketplace_order_id,
                "marketplacePaymentValue": marketplace_payment_value,
                "marketplaceServicesEndpoint": marketplace_services_endpoint,
                "openTextField": open_text_field,
                "paymentData": payment_data,
                "shippingData": convert_and_respect_annotation_metadata(
                    object_=shipping_data, annotation=OrderPlacementShippingData, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "authorization": str(authorization) if authorization is not None else None,
                "x-vtex-api-appkey": str(vtex_api_appkey) if vtex_api_appkey is not None else None,
                "x-vtex-api-apptoken": str(vtex_api_apptoken) if vtex_api_apptoken is not None else None,
                "accept": str(accept) if accept is not None else None,
                "accept-enconding": str(accept_enconding) if accept_enconding is not None else None,
                "x-vtex-operation-id": str(vtex_operation_id) if vtex_operation_id is not None else None,
                "x-forwarded-proto": str(forwarded_proto) if forwarded_proto is not None else None,
                "x-vtex-cache-client-bypass": str(vtex_cache_client_bypass)
                if vtex_cache_client_bypass is not None
                else None,
                "traceparent": str(traceparent) if traceparent is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mkp_order_cancellation(
        self,
        fulfillment_endpoint: str,
        order_id: str,
        *,
        marketplace_order_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(fulfillment_endpoint)}/pvt/orders/{encode_path_param(order_id)}/cancel",
            method="POST",
            json={
                "marketplaceOrderId": marketplace_order_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def authorize_fulfillment(
        self,
        fulfillment_endpoint: str,
        seller_order_id: str,
        *,
        marketplace_order_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(fulfillment_endpoint)}/pvt/orders/{encode_path_param(seller_order_id)}/fulfill",
            method="POST",
            json={
                "marketplaceOrderId": marketplace_order_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancel_order_in_marketplace(
        self,
        marketplace_services_endpoint: str,
        marketplace_order_id: str,
        *,
        reason: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(marketplace_services_endpoint)}/pvt/orders/{encode_path_param(marketplace_order_id)}/cancel",
            method="POST",
            json={
                "reason": reason,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(marketplace_services_endpoint)}/pvt/orders/{encode_path_param(marketplace_order_id)}/invoice",
            method="POST",
            json={
                "courier": courier,
                "invoiceNumber": invoice_number,
                "invoiceValue": invoice_value,
                "issuanceDate": issuance_date,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[SendInvoiceRequestItemsItem], direction="write"
                ),
                "trackingNumber": tracking_number,
                "trackingUrl": tracking_url,
                "type": type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(marketplace_services_endpoint)}/pvt/orders/{encode_path_param(marketplace_order_id)}/invoice/{encode_path_param(invoice_number)}",
            method="POST",
            json={
                "courier": courier,
                "dispatchedDate": dispatched_date,
                "trackingNumber": tracking_number,
                "trackingUrl": tracking_url,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_tracking_status(
        self,
        marketplace_services_endpoint: str,
        marketplace_order_id: str,
        invoice_number: str,
        *,
        is_delivered: bool,
        events: typing.Optional[typing.Sequence[UpdateTrackingStatusRequestEventsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(marketplace_services_endpoint)}/pvt/orders/{encode_path_param(marketplace_order_id)}/invoice/{encode_path_param(invoice_number)}/tracking",
            method="POST",
            json={
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=typing.Sequence[UpdateTrackingStatusRequestEventsItem], direction="write"
                ),
                "isDelivered": is_delivered,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
