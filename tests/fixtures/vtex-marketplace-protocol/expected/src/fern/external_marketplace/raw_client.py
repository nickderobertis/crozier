

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
from ..types.approveorder import Approveorder
from ..types.client_profile_data import ClientProfileData
from ..types.custom_data import CustomData
from ..types.deliverybyseller import Deliverybyseller
from ..types.invoice_data import InvoiceData
from ..types.item import Item
from ..types.shipping_data import ShippingData
from .types.fulfillment_simulation_external_marketplace_request_client_profile_data import (
    FulfillmentSimulationExternalMarketplaceRequestClientProfileData,
)
from .types.fulfillment_simulation_external_marketplace_request_items_item import (
    FulfillmentSimulationExternalMarketplaceRequestItemsItem,
)
from .types.fulfillment_simulation_external_marketplace_request_marketing_data import (
    FulfillmentSimulationExternalMarketplaceRequestMarketingData,
)
from .types.fulfillment_simulation_external_marketplace_response import FulfillmentSimulationExternalMarketplaceResponse
from .types.place_fulfillment_order_request_client_profile_data import PlaceFulfillmentOrderRequestClientProfileData
from .types.place_fulfillment_order_request_items_item import PlaceFulfillmentOrderRequestItemsItem
from .types.place_fulfillment_order_request_marketing_data import PlaceFulfillmentOrderRequestMarketingData
from .types.place_fulfillment_order_request_shipping_data import PlaceFulfillmentOrderRequestShippingData
from .types.send_category_mapping_to_vtex_mapper_categories_item import SendCategoryMappingToVtexMapperCategoriesItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawExternalMarketplaceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fulfillment_simulation_external_marketplace(
        self,
        *,
        affiliate_id: typing.Optional[str] = None,
        sc: typing.Optional[int] = None,
        client_profile_data: typing.Optional[FulfillmentSimulationExternalMarketplaceRequestClientProfileData] = OMIT,
        country: typing.Optional[str] = OMIT,
        geo_coordinates: typing.Optional[typing.Sequence[float]] = OMIT,
        is_checked_in: typing.Optional[bool] = OMIT,
        items: typing.Optional[typing.Sequence[FulfillmentSimulationExternalMarketplaceRequestItemsItem]] = OMIT,
        marketing_data: typing.Optional[FulfillmentSimulationExternalMarketplaceRequestMarketingData] = OMIT,
        postal_code: typing.Optional[str] = OMIT,
        selected_sla: typing.Optional[str] = OMIT,
        store_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FulfillmentSimulationExternalMarketplaceResponse]:
        """
        This endpoint can be triggered by marketplaces to simulate the fulfillment of an item in the cart.

        The fulfillment information is useful whenever you need to know the availability of fulfilling an order for a specific cart setting, since the API response will let you know the updated price, inventory and shipping data.

        Parameters
        ----------
        affiliate_id : typing.Optional[str]
            The affiliate ID code created by the seller.

        sc : typing.Optional[int]
            Trade Policy (Sales Channel) identification.

        client_profile_data : typing.Optional[FulfillmentSimulationExternalMarketplaceRequestClientProfileData]
            Customer's profile information.

        country : typing.Optional[str]
            Three letter ISO code of the country of the shipping address. This value must be sent along with the `postalCode` or `geoCoordinates` values.

        geo_coordinates : typing.Optional[typing.Sequence[float]]
            Array containing two floats with geocoordinates, first longitude, then latitude.

        is_checked_in : typing.Optional[bool]
            Indicates whether order is checked in.

        items : typing.Optional[typing.Sequence[FulfillmentSimulationExternalMarketplaceRequestItemsItem]]
            Array containing information about the SKUs inside the cart to be simulated.

        marketing_data : typing.Optional[FulfillmentSimulationExternalMarketplaceRequestMarketingData]
            Object containing promotion data such as coupon tracking information and internal or external UTMs.

        postal_code : typing.Optional[str]
            Postal code.

        selected_sla : typing.Optional[str]
            SLA selected by the customer.

        store_id : typing.Optional[str]
            ID of the store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FulfillmentSimulationExternalMarketplaceResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/checkout/pub/orderForms/simulation",
            method="POST",
            params={
                "affiliateId": affiliate_id,
                "sc": sc,
            },
            json={
                "clientProfileData": convert_and_respect_annotation_metadata(
                    object_=client_profile_data,
                    annotation=FulfillmentSimulationExternalMarketplaceRequestClientProfileData,
                    direction="write",
                ),
                "country": country,
                "geoCoordinates": geo_coordinates,
                "isCheckedIn": is_checked_in,
                "items": convert_and_respect_annotation_metadata(
                    object_=items,
                    annotation=typing.Sequence[FulfillmentSimulationExternalMarketplaceRequestItemsItem],
                    direction="write",
                ),
                "marketingData": convert_and_respect_annotation_metadata(
                    object_=marketing_data,
                    annotation=FulfillmentSimulationExternalMarketplaceRequestMarketingData,
                    direction="write",
                ),
                "postalCode": postal_code,
                "selectedSla": selected_sla,
                "storeId": store_id,
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
                    FulfillmentSimulationExternalMarketplaceResponse,
                    parse_obj_as(
                        type_=FulfillmentSimulationExternalMarketplaceResponse,
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

    def send_category_mapping_vtex_mapper(
        self,
        id: str,
        *,
        categories: typing.Sequence[SendCategoryMappingToVtexMapperCategoriesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Mapping categories guarantees that the VTEX category tree has a correct association with the marketplace’s category tree.

        To perform this association, VTEX made VTEX Mapper available. It is a tool integrated to the VTEX platform that allows the user to relate categories created in VTEX to categories from the marketplace.

        This endpoint allows connectors to send the marketplace's category tree mapped in the integration.

        Connectors should send the payload compacted in .gzip format.

        For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).

        Parameters
        ----------
        id : str
            Code identifying returned in the *VTEX Mapper Registration* endpoint.

        categories : typing.Sequence[SendCategoryMappingToVtexMapperCategoriesItem]
            Array with Marketplace parent categories and their information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"portal.vtexcommercestable.com.br/api/mkp-category-mapper/categories/marketplace/{encode_path_param(id)}",
            method="POST",
            json={
                "categories": convert_and_respect_annotation_metadata(
                    object_=categories,
                    annotation=typing.Sequence[SendCategoryMappingToVtexMapperCategoriesItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def vtex_mapper_registration(
        self,
        *,
        an: str,
        category_tree_end_point: str,
        display_name: str,
        mapping_end_point: str,
        properties: typing.Dict[str, typing.Any],
        category_tree_processing_notification_endpoint: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Mapping categories guarantees that the VTEX category tree has a correct association with the marketplace’s category tree.

        To perform this association, VTEX made VTEX Mapper available. It is a tool integrated to the VTEX platform that allows the user to relate categories created in VTEX to categories from the marketplace.

        This endpoint allows connectors to register the external marketplace integration in VTEX Mapper.

        In case VTEX Mapper detects an error and the call fails, the connector should check if mandatory information was sent correctly. Ex. are URLs correctly registered in the properties categoryTreeEndPoint and mappingEndPoint?

        For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).

        Parameters
        ----------
        an : str
            Name of the VTEX account. Used as part of the URL.

        category_tree_end_point : str
            Endpoint that returns categories and attributes according to VTEX  Mapper specifications.

        display_name : str
            Marketplace Name, that will be displayed in VTEX Mapper.

        mapping_end_point : str
            Secure endpoint that will receive the category mapping sent by VTEX Mapper.

        properties : typing.Dict[str, typing.Any]
            Refers to the `allowsRemap` property.

        category_tree_processing_notification_endpoint : typing.Optional[str]
            The `CategoryTreeProcessingNotificationEndpoint` is optional, and should be an endpoint from the external marketplace, that will be notified after the marketplace's category tree is successfully processed or not.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "portal.vtexcommercestable.com.br/api/mkp-category-mapper/connector/register",
            method="POST",
            params={
                "an": an,
            },
            json={
                "CategoryTreeProcessingNotificationEndpoint": category_tree_processing_notification_endpoint,
                "categoryTreeEndPoint": category_tree_end_point,
                "displayName": display_name,
                "mappingEndPoint": mapping_end_point,
                "properties": properties,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def enqueue_new_order(
        self,
        account_name: str,
        *,
        affiliate_id: str,
        allow_franchises: bool,
        client_profile_data: ClientProfileData,
        invoice_data: InvoiceData,
        items: typing.Sequence[Item],
        marketplace_order_id: str,
        marketplace_order_status: str,
        marketplace_payment_value: int,
        shipping_data: ShippingData,
        an: typing.Optional[str] = None,
        connector_endpoint: typing.Optional[str] = OMIT,
        connector_name: typing.Optional[str] = OMIT,
        custom_data: typing.Optional[CustomData] = OMIT,
        pickup_account_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Deliverybyseller]:
        """
        API to integrate an external channel's order into the VTEX plataform.

        This process is asynchronous and a notification with the order's integration results will be sent to the endpoint specified in the **connectorEndpoint** field in [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template), if the connector uses our App template. The field **connectorName** is also optional for connectors that use our App Template and authenticate using the app's auth cookie. If the account is not informed in the URL host, it should also be defined as a query string parameter in the route: `an={account}`.

        For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).

        Parameters
        ----------
        account_name : str
            Parameter should indicate the name of the VTEX account where the order is being integrated or updated, meaning the seller responsible for the order.

        affiliate_id : str
            ID identifying the marketplace where the order originates. This ID is configured in the seller's VTEX account, and should be informed to the marketplace.

        allow_franchises : bool
            Boolean indicating whether franchise accounts linked to the main seller should be considered. That is, if the order delivery pickup/SLA can belong to a [franchise account](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl), for example. This field is optional and defaults to `false`.

        client_profile_data : ClientProfileData

        invoice_data : InvoiceData

        items : typing.Sequence[Item]

        marketplace_order_id : str
            String that indicates the order's ID in the marketplace.

        marketplace_order_status : str
            Required field including a string with the order’s status in the marketplace. If you send an order with the status APPROVED to integrate, our service will automatically try to advance it’s status in VTEX after integrating it. This field accepts the following values:

            - `new`

            - `approved`

        marketplace_payment_value : int
            Integer that indicates the order’s total value, which the marketplace will pay to the seller. It’s important to note that this value should include interest, if that’s the case. If the value is `USD110.50`, convert it to the format → `11050`.

        shipping_data : ShippingData

        an : typing.Optional[str]
            Parameter should indicate the name of the VTEX account where the order is being integrated or updated, meaning the seller responsible for the order.

        connector_endpoint : typing.Optional[str]
            String with the connector's base endpoint that will receive notifications about the orders processing results, as well as status updates from VTEX OMS. This field accepts query strings. You can use the models below:

            - `https://{{externalconnector}}.com`

            - `https://{{externalconnector.com}}/api/vtex` if you additionaly want to send a relative URL with the endpoint.

            This field is optional if the connector uses the [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template) and authenticates on our request via `VtexIdclientAutCookie`.

            It is required if the connector is native or does not use the App Template.

        connector_name : typing.Optional[str]
            String with the identifier code of the connector responsible for the order.

            This field is optional if the connector uses the [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template) and authenticates on our request via `VtexIdclientAutCookie`.

            It is required if the connector is native or does not use the App Template.

        custom_data : typing.Optional[CustomData]

        pickup_account_name : typing.Optional[str]
            String that indicates the name of the account responsible for the order’s pickup point. It is only required for pickup-in-point orders from franchise accounts, when franchise accounts `allowFranchises` is `true` and the order in question has a `pickup-in-point` delivery type. It is optional otherwise.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Deliverybyseller]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(account_name)}.vtexcommercestable.com.br/api/order-integration/orders",
            method="POST",
            params={
                "an": an,
                "affiliateId": affiliate_id,
            },
            json={
                "allowFranchises": allow_franchises,
                "clientProfileData": convert_and_respect_annotation_metadata(
                    object_=client_profile_data, annotation=ClientProfileData, direction="write"
                ),
                "connectorEndpoint": connector_endpoint,
                "connectorName": connector_name,
                "customData": convert_and_respect_annotation_metadata(
                    object_=custom_data, annotation=CustomData, direction="write"
                ),
                "invoiceData": convert_and_respect_annotation_metadata(
                    object_=invoice_data, annotation=InvoiceData, direction="write"
                ),
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[Item], direction="write"
                ),
                "marketplaceOrderId": marketplace_order_id,
                "marketplaceOrderStatus": marketplace_order_status,
                "marketplacePaymentValue": marketplace_payment_value,
                "pickupAccountName": pickup_account_name,
                "shippingData": convert_and_respect_annotation_metadata(
                    object_=shipping_data, annotation=ShippingData, direction="write"
                ),
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
                    Deliverybyseller,
                    parse_obj_as(
                        type_=Deliverybyseller,
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

    def update_order_status(
        self,
        account_name: str,
        *,
        connector_endpoint: str,
        connector_name: str,
        marketplace_order_id: str,
        marketplace_order_status: str,
        an: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Approveorder]:
        """
        API request used to update an order status in VTEX.

        This process is asynchronous and a notification with the order's integration results will be sent to the endpoint specified in the **connectiorEndpoint** field or the **connectiorEndpoint** [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template), if the connector uses our App template. The field **connectorName** is also optional for connectors that use our App Template and authenticate using the app's auth cookie.

        For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).

        Parameters
        ----------
        account_name : str
            Parameter should indicate the name of the VTEX account where the order is being integrated or updated, meaning the seller responsible for the order.

        connector_endpoint : str
            String with the connector's base endpoint that will receive notifications about the orders processing results, as well as status updates from VTEX OMS. This field does not accept query strings. You can use the models below:

            - `https://{{externalconnector}}.com`

            - `https://{{externalconnector.com}}/api/vtex` if you additionaly want to send a relative URL with the endpoint.

            This field is optional if the connector uses the [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template) and authenticates on our request via `VtexIdclientAutCookie`.

            It is required if the connector is native or does not use the App Template.

        connector_name : str
            String with the identifier code of the connector responsible for the order.

            This field is optional if the connector uses the [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template) and authenticates on our request via `VtexIdclientAutCookie`.

            It is required if the connector is native or does not use the App Template.

        marketplace_order_id : str
            String that indicates the order's ID in the marketplace.

        marketplace_order_status : str
            Required field including a string with the order’s status in the marketplace. If you send an order with the status APPROVED to integrate, our service will automatically try to advance its status in VTEX after integrating it. This field accepts the following values:

            - `new`

            - `approved`.

        an : typing.Optional[str]
            Parameter should indicate the name of the VTEX account where the order is being integrated or updated, meaning the seller responsible for the order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Approveorder]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(account_name)}.vtexcommercestable.com.br/api/order-integration/orders/status",
            method="PUT",
            params={
                "an": an,
            },
            json={
                "connectorEndpoint": connector_endpoint,
                "connectorName": connector_name,
                "marketplaceOrderId": marketplace_order_id,
                "marketplaceOrderStatus": marketplace_order_status,
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
                    Approveorder,
                    parse_obj_as(
                        type_=Approveorder,
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

    def place_fulfillment_order(
        self,
        account_name: str,
        environment: str,
        *,
        affiliate_id: str,
        client_profile_data: PlaceFulfillmentOrderRequestClientProfileData,
        items: typing.Sequence[PlaceFulfillmentOrderRequestItemsItem],
        marketplace_order_id: str,
        marketplace_payment_value: int,
        marketplace_services_endpoint: str,
        shipping_data: PlaceFulfillmentOrderRequestShippingData,
        sc: typing.Optional[str] = None,
        is_created_async: typing.Optional[bool] = OMIT,
        marketing_data: typing.Optional[PlaceFulfillmentOrderRequestMarketingData] = OMIT,
        open_text_field: typing.Optional[str] = OMIT,
        payment_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
                Creates fulfillment order, meaning that it is an order for the seller's side in a sale made through a marketplace. This order assumes the transaction itself has already happened on the marketplace's side and, therfore, cares only about the fulfillment side.


        > If you plan to integrate external orders with possible [Price divergence](https://help.vtex.com/en/tutorial/price-divergence-rule--6RlFLhD1rIRRshl83KnCjW#) be mindful of the `isCreatedAsync` request body field.

                For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).

                Parameters
                ----------
                account_name : str
                    Name of the VTEX account. Used as part of the URL.

                environment : str
                    Environment to be used. It is passed as part of the URL.

                affiliate_id : str
                    ID identifying the marketplace where the order originates. This ID is configured in the seller's VTEX account, and should be informed to the marketplace.

                client_profile_data : PlaceFulfillmentOrderRequestClientProfileData
                    Customer's profile information.

                items : typing.Sequence[PlaceFulfillmentOrderRequestItemsItem]
                    Array of objects containing information on each of the order's items.

                marketplace_order_id : str
                    ID of the order in the marketplace.

                marketplace_payment_value : int
                    Value of the payment made to the marketplace.

                marketplace_services_endpoint : str
                    Endpoint provided by the marketplace for post purchase communication. Should be an URL, containing protocol, host, path and query string (in case it applies).

                shipping_data : PlaceFulfillmentOrderRequestShippingData
                    Shipping information.

                sc : typing.Optional[str]
                    Sales channel.

                is_created_async : typing.Optional[bool]
                    Indicates whether an order is created. It must be `true` if an order is being placed with [Price divergence](https://help.vtex.com/en/tutorial/price-divergence-rule--6RlFLhD1rIRRshl83KnCjW#), otherwise the request will not work.

                marketing_data : typing.Optional[PlaceFulfillmentOrderRequestMarketingData]

                open_text_field : typing.Optional[str]
                    Optional field meant to hold additional information about the order. We recommend using this field for text, not data formats such as `JSON` even if escaped. For that purpose, see [Creating customizable fields](https://developers.vtex.com/vtex-rest-api/docs/creating-customizable-fields-in-the-cart-with-checkout-api-1)

                payment_data : typing.Optional[typing.Dict[str, typing.Any]]
                    In other contexts, this field tipically holds an object with payment information. However, since the payment is processed by the marketplace, it will be sent to the seller as `null` in this context.

                request_options : typing.Optional[RequestOptions]
                    Request-specific configuration.

                Returns
                -------
                HttpResponse[typing.Any]
                    OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(account_name)}.{encode_path_param(environment)}.com.br/api/fulfillment/pvt/orders",
            method="POST",
            params={
                "sc": sc,
                "affiliateId": affiliate_id,
            },
            json={
                "clientProfileData": convert_and_respect_annotation_metadata(
                    object_=client_profile_data,
                    annotation=PlaceFulfillmentOrderRequestClientProfileData,
                    direction="write",
                ),
                "isCreatedAsync": is_created_async,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[PlaceFulfillmentOrderRequestItemsItem], direction="write"
                ),
                "marketingData": convert_and_respect_annotation_metadata(
                    object_=marketing_data, annotation=PlaceFulfillmentOrderRequestMarketingData, direction="write"
                ),
                "marketplaceOrderId": marketplace_order_id,
                "marketplacePaymentValue": marketplace_payment_value,
                "marketplaceServicesEndpoint": marketplace_services_endpoint,
                "openTextField": open_text_field,
                "paymentData": payment_data,
                "shippingData": convert_and_respect_annotation_metadata(
                    object_=shipping_data, annotation=PlaceFulfillmentOrderRequestShippingData, direction="write"
                ),
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

    def authorize_dispatch_for_fulfillment_order(
        self,
        account_name: str,
        environment: str,
        order_id: str,
        *,
        affiliate_id: str,
        sc: typing.Optional[str] = None,
        marketplace_order_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Creates fulfillment order, meaning that it is an order for the seller's side in a sale made through a marketplace. This order assumes the transaction itself has already happened on the marketplace's side and, therfore, cares only about the fulfillment side.

        For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).

        Parameters
        ----------
        account_name : str
            Name of the VTEX account. Used as part of the URL.

        environment : str
            Environment to be used. It is passed as part of the URL.

        order_id : str
            ID of the order that is to be authorized. It is composed of the `afilliateId` and the `marketplaceOrderId` joined with a `-`. For instance, an order with an ID `"123"` coming from the marketplace `"MKP"` has an `orderId` of `"MKP-123"`.

        affiliate_id : str
            ID identifying the marketplace where the order originates. This ID is configured in the seller's VTEX account, and should be informed to the marketplace.

        sc : typing.Optional[str]
            Sales channel.

        marketplace_order_id : typing.Optional[str]
            ID of the order in the marketplace. It is the same as the `orderId` without the `afilliateId` at the beginning. For instance, if the `orderId` is `"MKP-123"`, the `marketplaceOrderId` is `"123"`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(account_name)}.{encode_path_param(environment)}.com.br/api/fulfillment/pvt/orders/{encode_path_param(order_id)}/fulfill",
            method="POST",
            params={
                "sc": sc,
                "affiliateId": affiliate_id,
            },
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


class AsyncRawExternalMarketplaceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def fulfillment_simulation_external_marketplace(
        self,
        *,
        affiliate_id: typing.Optional[str] = None,
        sc: typing.Optional[int] = None,
        client_profile_data: typing.Optional[FulfillmentSimulationExternalMarketplaceRequestClientProfileData] = OMIT,
        country: typing.Optional[str] = OMIT,
        geo_coordinates: typing.Optional[typing.Sequence[float]] = OMIT,
        is_checked_in: typing.Optional[bool] = OMIT,
        items: typing.Optional[typing.Sequence[FulfillmentSimulationExternalMarketplaceRequestItemsItem]] = OMIT,
        marketing_data: typing.Optional[FulfillmentSimulationExternalMarketplaceRequestMarketingData] = OMIT,
        postal_code: typing.Optional[str] = OMIT,
        selected_sla: typing.Optional[str] = OMIT,
        store_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FulfillmentSimulationExternalMarketplaceResponse]:
        """
        This endpoint can be triggered by marketplaces to simulate the fulfillment of an item in the cart.

        The fulfillment information is useful whenever you need to know the availability of fulfilling an order for a specific cart setting, since the API response will let you know the updated price, inventory and shipping data.

        Parameters
        ----------
        affiliate_id : typing.Optional[str]
            The affiliate ID code created by the seller.

        sc : typing.Optional[int]
            Trade Policy (Sales Channel) identification.

        client_profile_data : typing.Optional[FulfillmentSimulationExternalMarketplaceRequestClientProfileData]
            Customer's profile information.

        country : typing.Optional[str]
            Three letter ISO code of the country of the shipping address. This value must be sent along with the `postalCode` or `geoCoordinates` values.

        geo_coordinates : typing.Optional[typing.Sequence[float]]
            Array containing two floats with geocoordinates, first longitude, then latitude.

        is_checked_in : typing.Optional[bool]
            Indicates whether order is checked in.

        items : typing.Optional[typing.Sequence[FulfillmentSimulationExternalMarketplaceRequestItemsItem]]
            Array containing information about the SKUs inside the cart to be simulated.

        marketing_data : typing.Optional[FulfillmentSimulationExternalMarketplaceRequestMarketingData]
            Object containing promotion data such as coupon tracking information and internal or external UTMs.

        postal_code : typing.Optional[str]
            Postal code.

        selected_sla : typing.Optional[str]
            SLA selected by the customer.

        store_id : typing.Optional[str]
            ID of the store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FulfillmentSimulationExternalMarketplaceResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/checkout/pub/orderForms/simulation",
            method="POST",
            params={
                "affiliateId": affiliate_id,
                "sc": sc,
            },
            json={
                "clientProfileData": convert_and_respect_annotation_metadata(
                    object_=client_profile_data,
                    annotation=FulfillmentSimulationExternalMarketplaceRequestClientProfileData,
                    direction="write",
                ),
                "country": country,
                "geoCoordinates": geo_coordinates,
                "isCheckedIn": is_checked_in,
                "items": convert_and_respect_annotation_metadata(
                    object_=items,
                    annotation=typing.Sequence[FulfillmentSimulationExternalMarketplaceRequestItemsItem],
                    direction="write",
                ),
                "marketingData": convert_and_respect_annotation_metadata(
                    object_=marketing_data,
                    annotation=FulfillmentSimulationExternalMarketplaceRequestMarketingData,
                    direction="write",
                ),
                "postalCode": postal_code,
                "selectedSla": selected_sla,
                "storeId": store_id,
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
                    FulfillmentSimulationExternalMarketplaceResponse,
                    parse_obj_as(
                        type_=FulfillmentSimulationExternalMarketplaceResponse,
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

    async def send_category_mapping_vtex_mapper(
        self,
        id: str,
        *,
        categories: typing.Sequence[SendCategoryMappingToVtexMapperCategoriesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Mapping categories guarantees that the VTEX category tree has a correct association with the marketplace’s category tree.

        To perform this association, VTEX made VTEX Mapper available. It is a tool integrated to the VTEX platform that allows the user to relate categories created in VTEX to categories from the marketplace.

        This endpoint allows connectors to send the marketplace's category tree mapped in the integration.

        Connectors should send the payload compacted in .gzip format.

        For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).

        Parameters
        ----------
        id : str
            Code identifying returned in the *VTEX Mapper Registration* endpoint.

        categories : typing.Sequence[SendCategoryMappingToVtexMapperCategoriesItem]
            Array with Marketplace parent categories and their information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"portal.vtexcommercestable.com.br/api/mkp-category-mapper/categories/marketplace/{encode_path_param(id)}",
            method="POST",
            json={
                "categories": convert_and_respect_annotation_metadata(
                    object_=categories,
                    annotation=typing.Sequence[SendCategoryMappingToVtexMapperCategoriesItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def vtex_mapper_registration(
        self,
        *,
        an: str,
        category_tree_end_point: str,
        display_name: str,
        mapping_end_point: str,
        properties: typing.Dict[str, typing.Any],
        category_tree_processing_notification_endpoint: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Mapping categories guarantees that the VTEX category tree has a correct association with the marketplace’s category tree.

        To perform this association, VTEX made VTEX Mapper available. It is a tool integrated to the VTEX platform that allows the user to relate categories created in VTEX to categories from the marketplace.

        This endpoint allows connectors to register the external marketplace integration in VTEX Mapper.

        In case VTEX Mapper detects an error and the call fails, the connector should check if mandatory information was sent correctly. Ex. are URLs correctly registered in the properties categoryTreeEndPoint and mappingEndPoint?

        For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).

        Parameters
        ----------
        an : str
            Name of the VTEX account. Used as part of the URL.

        category_tree_end_point : str
            Endpoint that returns categories and attributes according to VTEX  Mapper specifications.

        display_name : str
            Marketplace Name, that will be displayed in VTEX Mapper.

        mapping_end_point : str
            Secure endpoint that will receive the category mapping sent by VTEX Mapper.

        properties : typing.Dict[str, typing.Any]
            Refers to the `allowsRemap` property.

        category_tree_processing_notification_endpoint : typing.Optional[str]
            The `CategoryTreeProcessingNotificationEndpoint` is optional, and should be an endpoint from the external marketplace, that will be notified after the marketplace's category tree is successfully processed or not.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portal.vtexcommercestable.com.br/api/mkp-category-mapper/connector/register",
            method="POST",
            params={
                "an": an,
            },
            json={
                "CategoryTreeProcessingNotificationEndpoint": category_tree_processing_notification_endpoint,
                "categoryTreeEndPoint": category_tree_end_point,
                "displayName": display_name,
                "mappingEndPoint": mapping_end_point,
                "properties": properties,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def enqueue_new_order(
        self,
        account_name: str,
        *,
        affiliate_id: str,
        allow_franchises: bool,
        client_profile_data: ClientProfileData,
        invoice_data: InvoiceData,
        items: typing.Sequence[Item],
        marketplace_order_id: str,
        marketplace_order_status: str,
        marketplace_payment_value: int,
        shipping_data: ShippingData,
        an: typing.Optional[str] = None,
        connector_endpoint: typing.Optional[str] = OMIT,
        connector_name: typing.Optional[str] = OMIT,
        custom_data: typing.Optional[CustomData] = OMIT,
        pickup_account_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Deliverybyseller]:
        """
        API to integrate an external channel's order into the VTEX plataform.

        This process is asynchronous and a notification with the order's integration results will be sent to the endpoint specified in the **connectorEndpoint** field in [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template), if the connector uses our App template. The field **connectorName** is also optional for connectors that use our App Template and authenticate using the app's auth cookie. If the account is not informed in the URL host, it should also be defined as a query string parameter in the route: `an={account}`.

        For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).

        Parameters
        ----------
        account_name : str
            Parameter should indicate the name of the VTEX account where the order is being integrated or updated, meaning the seller responsible for the order.

        affiliate_id : str
            ID identifying the marketplace where the order originates. This ID is configured in the seller's VTEX account, and should be informed to the marketplace.

        allow_franchises : bool
            Boolean indicating whether franchise accounts linked to the main seller should be considered. That is, if the order delivery pickup/SLA can belong to a [franchise account](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl), for example. This field is optional and defaults to `false`.

        client_profile_data : ClientProfileData

        invoice_data : InvoiceData

        items : typing.Sequence[Item]

        marketplace_order_id : str
            String that indicates the order's ID in the marketplace.

        marketplace_order_status : str
            Required field including a string with the order’s status in the marketplace. If you send an order with the status APPROVED to integrate, our service will automatically try to advance it’s status in VTEX after integrating it. This field accepts the following values:

            - `new`

            - `approved`

        marketplace_payment_value : int
            Integer that indicates the order’s total value, which the marketplace will pay to the seller. It’s important to note that this value should include interest, if that’s the case. If the value is `USD110.50`, convert it to the format → `11050`.

        shipping_data : ShippingData

        an : typing.Optional[str]
            Parameter should indicate the name of the VTEX account where the order is being integrated or updated, meaning the seller responsible for the order.

        connector_endpoint : typing.Optional[str]
            String with the connector's base endpoint that will receive notifications about the orders processing results, as well as status updates from VTEX OMS. This field accepts query strings. You can use the models below:

            - `https://{{externalconnector}}.com`

            - `https://{{externalconnector.com}}/api/vtex` if you additionaly want to send a relative URL with the endpoint.

            This field is optional if the connector uses the [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template) and authenticates on our request via `VtexIdclientAutCookie`.

            It is required if the connector is native or does not use the App Template.

        connector_name : typing.Optional[str]
            String with the identifier code of the connector responsible for the order.

            This field is optional if the connector uses the [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template) and authenticates on our request via `VtexIdclientAutCookie`.

            It is required if the connector is native or does not use the App Template.

        custom_data : typing.Optional[CustomData]

        pickup_account_name : typing.Optional[str]
            String that indicates the name of the account responsible for the order’s pickup point. It is only required for pickup-in-point orders from franchise accounts, when franchise accounts `allowFranchises` is `true` and the order in question has a `pickup-in-point` delivery type. It is optional otherwise.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Deliverybyseller]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(account_name)}.vtexcommercestable.com.br/api/order-integration/orders",
            method="POST",
            params={
                "an": an,
                "affiliateId": affiliate_id,
            },
            json={
                "allowFranchises": allow_franchises,
                "clientProfileData": convert_and_respect_annotation_metadata(
                    object_=client_profile_data, annotation=ClientProfileData, direction="write"
                ),
                "connectorEndpoint": connector_endpoint,
                "connectorName": connector_name,
                "customData": convert_and_respect_annotation_metadata(
                    object_=custom_data, annotation=CustomData, direction="write"
                ),
                "invoiceData": convert_and_respect_annotation_metadata(
                    object_=invoice_data, annotation=InvoiceData, direction="write"
                ),
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[Item], direction="write"
                ),
                "marketplaceOrderId": marketplace_order_id,
                "marketplaceOrderStatus": marketplace_order_status,
                "marketplacePaymentValue": marketplace_payment_value,
                "pickupAccountName": pickup_account_name,
                "shippingData": convert_and_respect_annotation_metadata(
                    object_=shipping_data, annotation=ShippingData, direction="write"
                ),
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
                    Deliverybyseller,
                    parse_obj_as(
                        type_=Deliverybyseller,
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

    async def update_order_status(
        self,
        account_name: str,
        *,
        connector_endpoint: str,
        connector_name: str,
        marketplace_order_id: str,
        marketplace_order_status: str,
        an: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Approveorder]:
        """
        API request used to update an order status in VTEX.

        This process is asynchronous and a notification with the order's integration results will be sent to the endpoint specified in the **connectiorEndpoint** field or the **connectiorEndpoint** [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template), if the connector uses our App template. The field **connectorName** is also optional for connectors that use our App Template and authenticate using the app's auth cookie.

        For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).

        Parameters
        ----------
        account_name : str
            Parameter should indicate the name of the VTEX account where the order is being integrated or updated, meaning the seller responsible for the order.

        connector_endpoint : str
            String with the connector's base endpoint that will receive notifications about the orders processing results, as well as status updates from VTEX OMS. This field does not accept query strings. You can use the models below:

            - `https://{{externalconnector}}.com`

            - `https://{{externalconnector.com}}/api/vtex` if you additionaly want to send a relative URL with the endpoint.

            This field is optional if the connector uses the [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template) and authenticates on our request via `VtexIdclientAutCookie`.

            It is required if the connector is native or does not use the App Template.

        connector_name : str
            String with the identifier code of the connector responsible for the order.

            This field is optional if the connector uses the [App Template](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-app-template) and authenticates on our request via `VtexIdclientAutCookie`.

            It is required if the connector is native or does not use the App Template.

        marketplace_order_id : str
            String that indicates the order's ID in the marketplace.

        marketplace_order_status : str
            Required field including a string with the order’s status in the marketplace. If you send an order with the status APPROVED to integrate, our service will automatically try to advance its status in VTEX after integrating it. This field accepts the following values:

            - `new`

            - `approved`.

        an : typing.Optional[str]
            Parameter should indicate the name of the VTEX account where the order is being integrated or updated, meaning the seller responsible for the order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Approveorder]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(account_name)}.vtexcommercestable.com.br/api/order-integration/orders/status",
            method="PUT",
            params={
                "an": an,
            },
            json={
                "connectorEndpoint": connector_endpoint,
                "connectorName": connector_name,
                "marketplaceOrderId": marketplace_order_id,
                "marketplaceOrderStatus": marketplace_order_status,
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
                    Approveorder,
                    parse_obj_as(
                        type_=Approveorder,
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

    async def place_fulfillment_order(
        self,
        account_name: str,
        environment: str,
        *,
        affiliate_id: str,
        client_profile_data: PlaceFulfillmentOrderRequestClientProfileData,
        items: typing.Sequence[PlaceFulfillmentOrderRequestItemsItem],
        marketplace_order_id: str,
        marketplace_payment_value: int,
        marketplace_services_endpoint: str,
        shipping_data: PlaceFulfillmentOrderRequestShippingData,
        sc: typing.Optional[str] = None,
        is_created_async: typing.Optional[bool] = OMIT,
        marketing_data: typing.Optional[PlaceFulfillmentOrderRequestMarketingData] = OMIT,
        open_text_field: typing.Optional[str] = OMIT,
        payment_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
                Creates fulfillment order, meaning that it is an order for the seller's side in a sale made through a marketplace. This order assumes the transaction itself has already happened on the marketplace's side and, therfore, cares only about the fulfillment side.


        > If you plan to integrate external orders with possible [Price divergence](https://help.vtex.com/en/tutorial/price-divergence-rule--6RlFLhD1rIRRshl83KnCjW#) be mindful of the `isCreatedAsync` request body field.

                For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).

                Parameters
                ----------
                account_name : str
                    Name of the VTEX account. Used as part of the URL.

                environment : str
                    Environment to be used. It is passed as part of the URL.

                affiliate_id : str
                    ID identifying the marketplace where the order originates. This ID is configured in the seller's VTEX account, and should be informed to the marketplace.

                client_profile_data : PlaceFulfillmentOrderRequestClientProfileData
                    Customer's profile information.

                items : typing.Sequence[PlaceFulfillmentOrderRequestItemsItem]
                    Array of objects containing information on each of the order's items.

                marketplace_order_id : str
                    ID of the order in the marketplace.

                marketplace_payment_value : int
                    Value of the payment made to the marketplace.

                marketplace_services_endpoint : str
                    Endpoint provided by the marketplace for post purchase communication. Should be an URL, containing protocol, host, path and query string (in case it applies).

                shipping_data : PlaceFulfillmentOrderRequestShippingData
                    Shipping information.

                sc : typing.Optional[str]
                    Sales channel.

                is_created_async : typing.Optional[bool]
                    Indicates whether an order is created. It must be `true` if an order is being placed with [Price divergence](https://help.vtex.com/en/tutorial/price-divergence-rule--6RlFLhD1rIRRshl83KnCjW#), otherwise the request will not work.

                marketing_data : typing.Optional[PlaceFulfillmentOrderRequestMarketingData]

                open_text_field : typing.Optional[str]
                    Optional field meant to hold additional information about the order. We recommend using this field for text, not data formats such as `JSON` even if escaped. For that purpose, see [Creating customizable fields](https://developers.vtex.com/vtex-rest-api/docs/creating-customizable-fields-in-the-cart-with-checkout-api-1)

                payment_data : typing.Optional[typing.Dict[str, typing.Any]]
                    In other contexts, this field tipically holds an object with payment information. However, since the payment is processed by the marketplace, it will be sent to the seller as `null` in this context.

                request_options : typing.Optional[RequestOptions]
                    Request-specific configuration.

                Returns
                -------
                AsyncHttpResponse[typing.Any]
                    OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(account_name)}.{encode_path_param(environment)}.com.br/api/fulfillment/pvt/orders",
            method="POST",
            params={
                "sc": sc,
                "affiliateId": affiliate_id,
            },
            json={
                "clientProfileData": convert_and_respect_annotation_metadata(
                    object_=client_profile_data,
                    annotation=PlaceFulfillmentOrderRequestClientProfileData,
                    direction="write",
                ),
                "isCreatedAsync": is_created_async,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[PlaceFulfillmentOrderRequestItemsItem], direction="write"
                ),
                "marketingData": convert_and_respect_annotation_metadata(
                    object_=marketing_data, annotation=PlaceFulfillmentOrderRequestMarketingData, direction="write"
                ),
                "marketplaceOrderId": marketplace_order_id,
                "marketplacePaymentValue": marketplace_payment_value,
                "marketplaceServicesEndpoint": marketplace_services_endpoint,
                "openTextField": open_text_field,
                "paymentData": payment_data,
                "shippingData": convert_and_respect_annotation_metadata(
                    object_=shipping_data, annotation=PlaceFulfillmentOrderRequestShippingData, direction="write"
                ),
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

    async def authorize_dispatch_for_fulfillment_order(
        self,
        account_name: str,
        environment: str,
        order_id: str,
        *,
        affiliate_id: str,
        sc: typing.Optional[str] = None,
        marketplace_order_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Creates fulfillment order, meaning that it is an order for the seller's side in a sale made through a marketplace. This order assumes the transaction itself has already happened on the marketplace's side and, therfore, cares only about the fulfillment side.

        For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).

        Parameters
        ----------
        account_name : str
            Name of the VTEX account. Used as part of the URL.

        environment : str
            Environment to be used. It is passed as part of the URL.

        order_id : str
            ID of the order that is to be authorized. It is composed of the `afilliateId` and the `marketplaceOrderId` joined with a `-`. For instance, an order with an ID `"123"` coming from the marketplace `"MKP"` has an `orderId` of `"MKP-123"`.

        affiliate_id : str
            ID identifying the marketplace where the order originates. This ID is configured in the seller's VTEX account, and should be informed to the marketplace.

        sc : typing.Optional[str]
            Sales channel.

        marketplace_order_id : typing.Optional[str]
            ID of the order in the marketplace. It is the same as the `orderId` without the `afilliateId` at the beginning. For instance, if the `orderId` is `"MKP-123"`, the `marketplaceOrderId` is `"123"`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(account_name)}.{encode_path_param(environment)}.com.br/api/fulfillment/pvt/orders/{encode_path_param(order_id)}/fulfill",
            method="POST",
            params={
                "sc": sc,
                "affiliateId": affiliate_id,
            },
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
