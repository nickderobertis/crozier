

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.approveorder import Approveorder
from ..types.client_profile_data import ClientProfileData
from ..types.custom_data import CustomData
from ..types.deliverybyseller import Deliverybyseller
from ..types.invoice_data import InvoiceData
from ..types.item import Item
from ..types.shipping_data import ShippingData
from .raw_client import AsyncRawExternalMarketplaceClient, RawExternalMarketplaceClient
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


OMIT = typing.cast(typing.Any, ...)


class ExternalMarketplaceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExternalMarketplaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExternalMarketplaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExternalMarketplaceClient
        """
        return self._raw_client

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
    ) -> FulfillmentSimulationExternalMarketplaceResponse:
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
        FulfillmentSimulationExternalMarketplaceResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.external_marketplace.fulfillment_simulation_external_marketplace(
            sc=1,
        )
        """
        _response = self._raw_client.fulfillment_simulation_external_marketplace(
            affiliate_id=affiliate_id,
            sc=sc,
            client_profile_data=client_profile_data,
            country=country,
            geo_coordinates=geo_coordinates,
            is_checked_in=is_checked_in,
            items=items,
            marketing_data=marketing_data,
            postal_code=postal_code,
            selected_sla=selected_sla,
            store_id=store_id,
            request_options=request_options,
        )
        return _response.data

    def send_category_mapping_vtex_mapper(
        self,
        id: str,
        *,
        categories: typing.Sequence[SendCategoryMappingToVtexMapperCategoriesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern.external_marketplace import (
            SendCategoryMappingToVtexMapperCategoriesItem,
        )

        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.external_marketplace.send_category_mapping_vtex_mapper(
            id="id",
            categories=[SendCategoryMappingToVtexMapperCategoriesItem()],
        )
        """
        _response = self._raw_client.send_category_mapping_vtex_mapper(
            id, categories=categories, request_options=request_options
        )
        return _response.data

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
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.external_marketplace.vtex_mapper_registration(
            an="accountName",
            category_tree_end_point="http://api.vtexinternal.com.br/api/{{marketplaceName}}/mapper/categories",
            display_name="Marketplace A",
            mapping_end_point="http://api.vtexinternal.com.br/api/{{marketplaceName}}/mapper/mapping",
            properties={"key": "value"},
        )
        """
        _response = self._raw_client.vtex_mapper_registration(
            an=an,
            category_tree_end_point=category_tree_end_point,
            display_name=display_name,
            mapping_end_point=mapping_end_point,
            properties=properties,
            category_tree_processing_notification_endpoint=category_tree_processing_notification_endpoint,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Deliverybyseller:
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
        Deliverybyseller
            OK

        Examples
        --------
        from fern import (
            ClientProfileData,
            CustomApp,
            CustomData,
            DeliveryIds,
            FernApi,
            Fields,
            GeoCoordinates,
            InvoiceData,
            Item,
            LogisticsInfo,
            SelectedAddress,
            ShippingData,
            UserPaymentInfo,
        )

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.external_marketplace.enqueue_new_order(
            account_name="accountName",
            an="apiexamples",
            affiliate_id="MKP",
            allow_franchises=False,
            client_profile_data=ClientProfileData(
                document="99999999999",
                email="email@email.com.br",
                first_name="John",
                last_name="Doe",
                phone="99999999999",
            ),
            connector_endpoint="https://connector-endpoint.com/api/vtex",
            connector_name="SkyHub",
            custom_data=CustomData(
                custom_apps=[
                    CustomApp(
                        fields=Fields(
                            marketplace_payment_method="credit card",
                        ),
                        id="marketplace-integration",
                        major=1,
                    )
                ],
            ),
            invoice_data=InvoiceData(
                user_payment_info=UserPaymentInfo(
                    payment_methods=["creditCardPaymentGroup"],
                ),
            ),
            items=[
                Item(
                    id="1",
                    price=975,
                    quantity=1,
                )
            ],
            marketplace_order_id="{{$guid}}",
            marketplace_order_status="NEW",
            marketplace_payment_value=3025,
            pickup_account_name="",
            shipping_data=ShippingData(
                is_fob=True,
                is_marketplace_fulfillment=True,
                logistics_info=[
                    LogisticsInfo(
                        delivery_ids=DeliveryIds(
                            warehouse_id="AR1",
                        ),
                        lock_ttl="1d",
                        price=2050,
                        selected_delivery_channel="delivery",
                        selected_sla="Express",
                        shipping_estimate="2d",
                    )
                ],
                selected_addresses=[
                    SelectedAddress(
                        address_id="1",
                        address_type="Residential",
                        city="Curitiba",
                        complement="101",
                        country="BRA",
                        geo_coordinates=GeoCoordinates(
                            latitude="-29.5",
                            longitude="-45.8",
                        ),
                        neighborhood="Portão",
                        number="4125",
                        postal_code="81020-235",
                        receiver_name="John Doe",
                        state="PR",
                        street="Rua Eduardo Carlos Pereira",
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.enqueue_new_order(
            account_name,
            affiliate_id=affiliate_id,
            allow_franchises=allow_franchises,
            client_profile_data=client_profile_data,
            invoice_data=invoice_data,
            items=items,
            marketplace_order_id=marketplace_order_id,
            marketplace_order_status=marketplace_order_status,
            marketplace_payment_value=marketplace_payment_value,
            shipping_data=shipping_data,
            an=an,
            connector_endpoint=connector_endpoint,
            connector_name=connector_name,
            custom_data=custom_data,
            pickup_account_name=pickup_account_name,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Approveorder:
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
        Approveorder
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.external_marketplace.update_order_status(
            account_name="accountName",
            an="apiexamples",
            connector_endpoint="https://connector-endpoint.com/api/vtex",
            connector_name="Skyhub",
            marketplace_order_id="{{$guid}}",
            marketplace_order_status="APPROVED",
        )
        """
        _response = self._raw_client.update_order_status(
            account_name,
            connector_endpoint=connector_endpoint,
            connector_name=connector_name,
            marketplace_order_id=marketplace_order_id,
            marketplace_order_status=marketplace_order_status,
            an=an,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
                typing.Any
                    OK

                Examples
                --------
                from fern.external_marketplace import (
                    PlaceFulfillmentOrderRequestClientProfileData,
                    PlaceFulfillmentOrderRequestItemsItem,
                    PlaceFulfillmentOrderRequestShippingData,
                )

                from fern import FernApi

                client = FernApi(
                    accept="YOUR_ACCEPT",
                    vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
                    api_key="YOUR_API_KEY",
                )
                client.external_marketplace.place_fulfillment_order(
                    account_name="accountName",
                    environment="environment",
                    sc="1",
                    affiliate_id="MKP",
                    client_profile_data=PlaceFulfillmentOrderRequestClientProfileData(
                        document="123456789",
                        document_type="cpf",
                        email="customer@examplemail.com",
                        first_name="first-name",
                        last_name="last-name",
                    ),
                    items=[
                        PlaceFulfillmentOrderRequestItemsItem(
                            id="123456789",
                            quantity=1,
                            seller="1",
                        )
                    ],
                    marketplace_order_id="123456789",
                    marketplace_payment_value=100,
                    marketplace_services_endpoint="https://exampleseller.marketplaceservices.com",
                    shipping_data=PlaceFulfillmentOrderRequestShippingData(),
                )
        """
        _response = self._raw_client.place_fulfillment_order(
            account_name,
            environment,
            affiliate_id=affiliate_id,
            client_profile_data=client_profile_data,
            items=items,
            marketplace_order_id=marketplace_order_id,
            marketplace_payment_value=marketplace_payment_value,
            marketplace_services_endpoint=marketplace_services_endpoint,
            shipping_data=shipping_data,
            sc=sc,
            is_created_async=is_created_async,
            marketing_data=marketing_data,
            open_text_field=open_text_field,
            payment_data=payment_data,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        client.external_marketplace.authorize_dispatch_for_fulfillment_order(
            account_name="accountName",
            environment="environment",
            order_id="orderId",
            sc="1",
            affiliate_id="MKP",
        )
        """
        _response = self._raw_client.authorize_dispatch_for_fulfillment_order(
            account_name,
            environment,
            order_id,
            affiliate_id=affiliate_id,
            sc=sc,
            marketplace_order_id=marketplace_order_id,
            request_options=request_options,
        )
        return _response.data


class AsyncExternalMarketplaceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExternalMarketplaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExternalMarketplaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExternalMarketplaceClient
        """
        return self._raw_client

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
    ) -> FulfillmentSimulationExternalMarketplaceResponse:
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
        FulfillmentSimulationExternalMarketplaceResponse
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
            await client.external_marketplace.fulfillment_simulation_external_marketplace(
                sc=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fulfillment_simulation_external_marketplace(
            affiliate_id=affiliate_id,
            sc=sc,
            client_profile_data=client_profile_data,
            country=country,
            geo_coordinates=geo_coordinates,
            is_checked_in=is_checked_in,
            items=items,
            marketing_data=marketing_data,
            postal_code=postal_code,
            selected_sla=selected_sla,
            store_id=store_id,
            request_options=request_options,
        )
        return _response.data

    async def send_category_mapping_vtex_mapper(
        self,
        id: str,
        *,
        categories: typing.Sequence[SendCategoryMappingToVtexMapperCategoriesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern.external_marketplace import (
            SendCategoryMappingToVtexMapperCategoriesItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.external_marketplace.send_category_mapping_vtex_mapper(
                id="id",
                categories=[SendCategoryMappingToVtexMapperCategoriesItem()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_category_mapping_vtex_mapper(
            id, categories=categories, request_options=request_options
        )
        return _response.data

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
    ) -> None:
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
        None

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
            await client.external_marketplace.vtex_mapper_registration(
                an="accountName",
                category_tree_end_point="http://api.vtexinternal.com.br/api/{{marketplaceName}}/mapper/categories",
                display_name="Marketplace A",
                mapping_end_point="http://api.vtexinternal.com.br/api/{{marketplaceName}}/mapper/mapping",
                properties={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vtex_mapper_registration(
            an=an,
            category_tree_end_point=category_tree_end_point,
            display_name=display_name,
            mapping_end_point=mapping_end_point,
            properties=properties,
            category_tree_processing_notification_endpoint=category_tree_processing_notification_endpoint,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Deliverybyseller:
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
        Deliverybyseller
            OK

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ClientProfileData,
            CustomApp,
            CustomData,
            DeliveryIds,
            Fields,
            GeoCoordinates,
            InvoiceData,
            Item,
            LogisticsInfo,
            SelectedAddress,
            ShippingData,
            UserPaymentInfo,
        )

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
            vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.external_marketplace.enqueue_new_order(
                account_name="accountName",
                an="apiexamples",
                affiliate_id="MKP",
                allow_franchises=False,
                client_profile_data=ClientProfileData(
                    document="99999999999",
                    email="email@email.com.br",
                    first_name="John",
                    last_name="Doe",
                    phone="99999999999",
                ),
                connector_endpoint="https://connector-endpoint.com/api/vtex",
                connector_name="SkyHub",
                custom_data=CustomData(
                    custom_apps=[
                        CustomApp(
                            fields=Fields(
                                marketplace_payment_method="credit card",
                            ),
                            id="marketplace-integration",
                            major=1,
                        )
                    ],
                ),
                invoice_data=InvoiceData(
                    user_payment_info=UserPaymentInfo(
                        payment_methods=["creditCardPaymentGroup"],
                    ),
                ),
                items=[
                    Item(
                        id="1",
                        price=975,
                        quantity=1,
                    )
                ],
                marketplace_order_id="{{$guid}}",
                marketplace_order_status="NEW",
                marketplace_payment_value=3025,
                pickup_account_name="",
                shipping_data=ShippingData(
                    is_fob=True,
                    is_marketplace_fulfillment=True,
                    logistics_info=[
                        LogisticsInfo(
                            delivery_ids=DeliveryIds(
                                warehouse_id="AR1",
                            ),
                            lock_ttl="1d",
                            price=2050,
                            selected_delivery_channel="delivery",
                            selected_sla="Express",
                            shipping_estimate="2d",
                        )
                    ],
                    selected_addresses=[
                        SelectedAddress(
                            address_id="1",
                            address_type="Residential",
                            city="Curitiba",
                            complement="101",
                            country="BRA",
                            geo_coordinates=GeoCoordinates(
                                latitude="-29.5",
                                longitude="-45.8",
                            ),
                            neighborhood="Portão",
                            number="4125",
                            postal_code="81020-235",
                            receiver_name="John Doe",
                            state="PR",
                            street="Rua Eduardo Carlos Pereira",
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enqueue_new_order(
            account_name,
            affiliate_id=affiliate_id,
            allow_franchises=allow_franchises,
            client_profile_data=client_profile_data,
            invoice_data=invoice_data,
            items=items,
            marketplace_order_id=marketplace_order_id,
            marketplace_order_status=marketplace_order_status,
            marketplace_payment_value=marketplace_payment_value,
            shipping_data=shipping_data,
            an=an,
            connector_endpoint=connector_endpoint,
            connector_name=connector_name,
            custom_data=custom_data,
            pickup_account_name=pickup_account_name,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Approveorder:
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
        Approveorder
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
            await client.external_marketplace.update_order_status(
                account_name="accountName",
                an="apiexamples",
                connector_endpoint="https://connector-endpoint.com/api/vtex",
                connector_name="Skyhub",
                marketplace_order_id="{{$guid}}",
                marketplace_order_status="APPROVED",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_order_status(
            account_name,
            connector_endpoint=connector_endpoint,
            connector_name=connector_name,
            marketplace_order_id=marketplace_order_id,
            marketplace_order_status=marketplace_order_status,
            an=an,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
                typing.Any
                    OK

                Examples
                --------
                import asyncio

                from fern.external_marketplace import (
                    PlaceFulfillmentOrderRequestClientProfileData,
                    PlaceFulfillmentOrderRequestItemsItem,
                    PlaceFulfillmentOrderRequestShippingData,
                )

                from fern import AsyncFernApi

                client = AsyncFernApi(
                    accept="YOUR_ACCEPT",
                    vtex_api_app_token="YOUR_VTEX_API_APP_TOKEN",
                    api_key="YOUR_API_KEY",
                )


                async def main() -> None:
                    await client.external_marketplace.place_fulfillment_order(
                        account_name="accountName",
                        environment="environment",
                        sc="1",
                        affiliate_id="MKP",
                        client_profile_data=PlaceFulfillmentOrderRequestClientProfileData(
                            document="123456789",
                            document_type="cpf",
                            email="customer@examplemail.com",
                            first_name="first-name",
                            last_name="last-name",
                        ),
                        items=[
                            PlaceFulfillmentOrderRequestItemsItem(
                                id="123456789",
                                quantity=1,
                                seller="1",
                            )
                        ],
                        marketplace_order_id="123456789",
                        marketplace_payment_value=100,
                        marketplace_services_endpoint="https://exampleseller.marketplaceservices.com",
                        shipping_data=PlaceFulfillmentOrderRequestShippingData(),
                    )


                asyncio.run(main())
        """
        _response = await self._raw_client.place_fulfillment_order(
            account_name,
            environment,
            affiliate_id=affiliate_id,
            client_profile_data=client_profile_data,
            items=items,
            marketplace_order_id=marketplace_order_id,
            marketplace_payment_value=marketplace_payment_value,
            marketplace_services_endpoint=marketplace_services_endpoint,
            shipping_data=shipping_data,
            sc=sc,
            is_created_async=is_created_async,
            marketing_data=marketing_data,
            open_text_field=open_text_field,
            payment_data=payment_data,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
            await client.external_marketplace.authorize_dispatch_for_fulfillment_order(
                account_name="accountName",
                environment="environment",
                order_id="orderId",
                sc="1",
                affiliate_id="MKP",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.authorize_dispatch_for_fulfillment_order(
            account_name,
            environment,
            order_id,
            affiliate_id=affiliate_id,
            sc=sc,
            marketplace_order_id=marketplace_order_id,
            request_options=request_options,
        )
        return _response.data
