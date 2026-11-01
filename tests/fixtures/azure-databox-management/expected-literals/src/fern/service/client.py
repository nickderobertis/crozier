

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address_validation_output import AddressValidationOutput
from ..types.available_sku_request_sku_names_item import AvailableSkuRequestSkuNamesItem
from ..types.available_sku_request_transfer_type import AvailableSkuRequestTransferType
from ..types.available_skus_result import AvailableSkusResult
from ..types.region_configuration_response import RegionConfigurationResponse
from ..types.schedule_availability_request import ScheduleAvailabilityRequest
from ..types.shipping_address import ShippingAddress
from ..types.transport_availability_request import TransportAvailabilityRequest
from ..types.transport_preferences import TransportPreferences
from ..types.validation_input_request import ValidationInputRequest
from ..types.validation_input_request_validation_type import ValidationInputRequestValidationType
from ..types.validation_request_validation_category import ValidationRequestValidationCategory
from ..types.validation_response import ValidationResponse
from .raw_client import AsyncRawServiceClient, RawServiceClient
from .types.validate_address_device_type import ValidateAddressDeviceType


OMIT = typing.cast(typing.Any, ...)


class ServiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServiceClient
        """
        return self._raw_client

    def listavailableskus(
        self,
        subscription_id: str,
        location_: str,
        *,
        api_version: str,
        country: str,
        location: str,
        transfer_type: AvailableSkuRequestTransferType,
        sku_names: typing.Optional[typing.Sequence[AvailableSkuRequestSkuNamesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AvailableSkusResult:
        """
        This method provides the list of available skus for the given subscription and location.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        location_ : str
            The location of the resource

        api_version : str
            The API Version

        country : str
            ISO country code. Country for hardware shipment. For codes check: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements

        location : str
            Location for data transfer. For locations check: https://management.azure.com/subscriptions/SUBSCRIPTIONID/locations?api-version=2018-01-01

        transfer_type : AvailableSkuRequestTransferType
            Type of the transfer.

        sku_names : typing.Optional[typing.Sequence[AvailableSkuRequestSkuNamesItem]]
            Sku Names to filter for available skus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AvailableSkusResult
            The list of available skus under subscription.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.service.listavailableskus(
            subscription_id="subscriptionId",
            location_="location",
            api_version="api-version",
            country="country",
            location="location",
            transfer_type="ImportToAzure",
        )
        """
        _response = self._raw_client.listavailableskus(
            subscription_id,
            location_,
            api_version=api_version,
            country=country,
            location=location,
            transfer_type=transfer_type,
            sku_names=sku_names,
            request_options=request_options,
        )
        return _response.data

    def regionconfiguration(
        self,
        subscription_id: str,
        location: str,
        *,
        api_version: str,
        schedule_availability_request: typing.Optional[ScheduleAvailabilityRequest] = OMIT,
        transport_availability_request: typing.Optional[TransportAvailabilityRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegionConfigurationResponse:
        """
        This API provides configuration details specific to given region/location.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        location : str
            The location of the resource

        api_version : str
            The API Version

        schedule_availability_request : typing.Optional[ScheduleAvailabilityRequest]
            Request body to get the availability for scheduling orders.

        transport_availability_request : typing.Optional[TransportAvailabilityRequest]
            Request body to get the transport availability for given sku.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegionConfigurationResponse
            Region configuration response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.service.regionconfiguration(
            subscription_id="subscriptionId",
            location="location",
            api_version="api-version",
        )
        """
        _response = self._raw_client.regionconfiguration(
            subscription_id,
            location,
            api_version=api_version,
            schedule_availability_request=schedule_availability_request,
            transport_availability_request=transport_availability_request,
            request_options=request_options,
        )
        return _response.data

    def validateaddress(
        self,
        subscription_id: str,
        location: str,
        *,
        api_version: str,
        device_type: ValidateAddressDeviceType,
        shipping_address: ShippingAddress,
        validation_type: ValidationInputRequestValidationType,
        transport_preferences: typing.Optional[TransportPreferences] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddressValidationOutput:
        """
        [DEPRECATED NOTICE: This operation will soon be removed] This method validates the customer shipping address and provide alternate addresses if any.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        location : str
            The location of the resource

        api_version : str
            The API Version

        device_type : ValidateAddressDeviceType
            Device type to be used for the job.

        shipping_address : ShippingAddress
            Shipping address of the customer.

        validation_type : ValidationInputRequestValidationType
            Identifies the type of validation request.

        transport_preferences : typing.Optional[TransportPreferences]
            Preferences related to the shipment logistics of the sku.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressValidationOutput
            The valid and alternate addresses.

        Examples
        --------
        from fern import FernApi, ShippingAddress

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.service.validateaddress(
            subscription_id="subscriptionId",
            location="location",
            api_version="api-version",
            validation_type="ValidateAddress",
            device_type="DataBox",
            shipping_address=ShippingAddress(
                country="country",
                postal_code="postalCode",
                street_address1="streetAddress1",
            ),
        )
        """
        _response = self._raw_client.validateaddress(
            subscription_id,
            location,
            api_version=api_version,
            device_type=device_type,
            shipping_address=shipping_address,
            validation_type=validation_type,
            transport_preferences=transport_preferences,
            request_options=request_options,
        )
        return _response.data

    def validateinputs(
        self,
        subscription_id: str,
        location: str,
        *,
        api_version: str,
        individual_request_details: typing.Sequence[ValidationInputRequest],
        validation_category: ValidationRequestValidationCategory,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationResponse:
        """
        This method does all necessary pre-job creation validation under subscription.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        location : str
            The location of the resource

        api_version : str
            The API Version

        individual_request_details : typing.Sequence[ValidationInputRequest]
            List of request details contain validationType and its request as key and value respectively.

        validation_category : ValidationRequestValidationCategory
            Identify the nature of validation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationResponse
            The validation status and responses of each validating parameter.

        Examples
        --------
        from fern import FernApi, ValidationInputRequest

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.service.validateinputs(
            subscription_id="subscriptionId",
            location="location",
            api_version="api-version",
            individual_request_details=[
                ValidationInputRequest(
                    validation_type="ValidateAddress",
                )
            ],
            validation_category="JobCreationValidation",
        )
        """
        _response = self._raw_client.validateinputs(
            subscription_id,
            location,
            api_version=api_version,
            individual_request_details=individual_request_details,
            validation_category=validation_category,
            request_options=request_options,
        )
        return _response.data

    def listavailableskusbyresourcegroup(
        self,
        subscription_id: str,
        resource_group_name: str,
        location_: str,
        *,
        api_version: str,
        country: str,
        location: str,
        transfer_type: AvailableSkuRequestTransferType,
        sku_names: typing.Optional[typing.Sequence[AvailableSkuRequestSkuNamesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AvailableSkusResult:
        """
        This method provides the list of available skus for the given subscription, resource group and location.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        location_ : str
            The location of the resource

        api_version : str
            The API Version

        country : str
            ISO country code. Country for hardware shipment. For codes check: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements

        location : str
            Location for data transfer. For locations check: https://management.azure.com/subscriptions/SUBSCRIPTIONID/locations?api-version=2018-01-01

        transfer_type : AvailableSkuRequestTransferType
            Type of the transfer.

        sku_names : typing.Optional[typing.Sequence[AvailableSkuRequestSkuNamesItem]]
            Sku Names to filter for available skus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AvailableSkusResult
            The list of available skus under Resource group.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.service.listavailableskusbyresourcegroup(
            subscription_id="subscriptionId",
            resource_group_name="resourceGroupName",
            location_="location",
            api_version="api-version",
            country="country",
            location="location",
            transfer_type="ImportToAzure",
        )
        """
        _response = self._raw_client.listavailableskusbyresourcegroup(
            subscription_id,
            resource_group_name,
            location_,
            api_version=api_version,
            country=country,
            location=location,
            transfer_type=transfer_type,
            sku_names=sku_names,
            request_options=request_options,
        )
        return _response.data

    def validateinputsbyresourcegroup(
        self,
        subscription_id: str,
        resource_group_name: str,
        location: str,
        *,
        api_version: str,
        individual_request_details: typing.Sequence[ValidationInputRequest],
        validation_category: ValidationRequestValidationCategory,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationResponse:
        """
        This method does all necessary pre-job creation validation under resource group.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        location : str
            The location of the resource

        api_version : str
            The API Version

        individual_request_details : typing.Sequence[ValidationInputRequest]
            List of request details contain validationType and its request as key and value respectively.

        validation_category : ValidationRequestValidationCategory
            Identify the nature of validation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationResponse
            The validation status and responses of each validating parameter.

        Examples
        --------
        from fern import FernApi, ValidationInputRequest

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.service.validateinputsbyresourcegroup(
            subscription_id="subscriptionId",
            resource_group_name="resourceGroupName",
            location="location",
            api_version="api-version",
            individual_request_details=[
                ValidationInputRequest(
                    validation_type="ValidateAddress",
                )
            ],
            validation_category="JobCreationValidation",
        )
        """
        _response = self._raw_client.validateinputsbyresourcegroup(
            subscription_id,
            resource_group_name,
            location,
            api_version=api_version,
            individual_request_details=individual_request_details,
            validation_category=validation_category,
            request_options=request_options,
        )
        return _response.data


class AsyncServiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServiceClient
        """
        return self._raw_client

    async def listavailableskus(
        self,
        subscription_id: str,
        location_: str,
        *,
        api_version: str,
        country: str,
        location: str,
        transfer_type: AvailableSkuRequestTransferType,
        sku_names: typing.Optional[typing.Sequence[AvailableSkuRequestSkuNamesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AvailableSkusResult:
        """
        This method provides the list of available skus for the given subscription and location.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        location_ : str
            The location of the resource

        api_version : str
            The API Version

        country : str
            ISO country code. Country for hardware shipment. For codes check: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements

        location : str
            Location for data transfer. For locations check: https://management.azure.com/subscriptions/SUBSCRIPTIONID/locations?api-version=2018-01-01

        transfer_type : AvailableSkuRequestTransferType
            Type of the transfer.

        sku_names : typing.Optional[typing.Sequence[AvailableSkuRequestSkuNamesItem]]
            Sku Names to filter for available skus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AvailableSkusResult
            The list of available skus under subscription.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.service.listavailableskus(
                subscription_id="subscriptionId",
                location_="location",
                api_version="api-version",
                country="country",
                location="location",
                transfer_type="ImportToAzure",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listavailableskus(
            subscription_id,
            location_,
            api_version=api_version,
            country=country,
            location=location,
            transfer_type=transfer_type,
            sku_names=sku_names,
            request_options=request_options,
        )
        return _response.data

    async def regionconfiguration(
        self,
        subscription_id: str,
        location: str,
        *,
        api_version: str,
        schedule_availability_request: typing.Optional[ScheduleAvailabilityRequest] = OMIT,
        transport_availability_request: typing.Optional[TransportAvailabilityRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegionConfigurationResponse:
        """
        This API provides configuration details specific to given region/location.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        location : str
            The location of the resource

        api_version : str
            The API Version

        schedule_availability_request : typing.Optional[ScheduleAvailabilityRequest]
            Request body to get the availability for scheduling orders.

        transport_availability_request : typing.Optional[TransportAvailabilityRequest]
            Request body to get the transport availability for given sku.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegionConfigurationResponse
            Region configuration response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.service.regionconfiguration(
                subscription_id="subscriptionId",
                location="location",
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.regionconfiguration(
            subscription_id,
            location,
            api_version=api_version,
            schedule_availability_request=schedule_availability_request,
            transport_availability_request=transport_availability_request,
            request_options=request_options,
        )
        return _response.data

    async def validateaddress(
        self,
        subscription_id: str,
        location: str,
        *,
        api_version: str,
        device_type: ValidateAddressDeviceType,
        shipping_address: ShippingAddress,
        validation_type: ValidationInputRequestValidationType,
        transport_preferences: typing.Optional[TransportPreferences] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddressValidationOutput:
        """
        [DEPRECATED NOTICE: This operation will soon be removed] This method validates the customer shipping address and provide alternate addresses if any.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        location : str
            The location of the resource

        api_version : str
            The API Version

        device_type : ValidateAddressDeviceType
            Device type to be used for the job.

        shipping_address : ShippingAddress
            Shipping address of the customer.

        validation_type : ValidationInputRequestValidationType
            Identifies the type of validation request.

        transport_preferences : typing.Optional[TransportPreferences]
            Preferences related to the shipment logistics of the sku.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressValidationOutput
            The valid and alternate addresses.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ShippingAddress

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.service.validateaddress(
                subscription_id="subscriptionId",
                location="location",
                api_version="api-version",
                validation_type="ValidateAddress",
                device_type="DataBox",
                shipping_address=ShippingAddress(
                    country="country",
                    postal_code="postalCode",
                    street_address1="streetAddress1",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.validateaddress(
            subscription_id,
            location,
            api_version=api_version,
            device_type=device_type,
            shipping_address=shipping_address,
            validation_type=validation_type,
            transport_preferences=transport_preferences,
            request_options=request_options,
        )
        return _response.data

    async def validateinputs(
        self,
        subscription_id: str,
        location: str,
        *,
        api_version: str,
        individual_request_details: typing.Sequence[ValidationInputRequest],
        validation_category: ValidationRequestValidationCategory,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationResponse:
        """
        This method does all necessary pre-job creation validation under subscription.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        location : str
            The location of the resource

        api_version : str
            The API Version

        individual_request_details : typing.Sequence[ValidationInputRequest]
            List of request details contain validationType and its request as key and value respectively.

        validation_category : ValidationRequestValidationCategory
            Identify the nature of validation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationResponse
            The validation status and responses of each validating parameter.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ValidationInputRequest

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.service.validateinputs(
                subscription_id="subscriptionId",
                location="location",
                api_version="api-version",
                individual_request_details=[
                    ValidationInputRequest(
                        validation_type="ValidateAddress",
                    )
                ],
                validation_category="JobCreationValidation",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.validateinputs(
            subscription_id,
            location,
            api_version=api_version,
            individual_request_details=individual_request_details,
            validation_category=validation_category,
            request_options=request_options,
        )
        return _response.data

    async def listavailableskusbyresourcegroup(
        self,
        subscription_id: str,
        resource_group_name: str,
        location_: str,
        *,
        api_version: str,
        country: str,
        location: str,
        transfer_type: AvailableSkuRequestTransferType,
        sku_names: typing.Optional[typing.Sequence[AvailableSkuRequestSkuNamesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AvailableSkusResult:
        """
        This method provides the list of available skus for the given subscription, resource group and location.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        location_ : str
            The location of the resource

        api_version : str
            The API Version

        country : str
            ISO country code. Country for hardware shipment. For codes check: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements

        location : str
            Location for data transfer. For locations check: https://management.azure.com/subscriptions/SUBSCRIPTIONID/locations?api-version=2018-01-01

        transfer_type : AvailableSkuRequestTransferType
            Type of the transfer.

        sku_names : typing.Optional[typing.Sequence[AvailableSkuRequestSkuNamesItem]]
            Sku Names to filter for available skus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AvailableSkusResult
            The list of available skus under Resource group.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.service.listavailableskusbyresourcegroup(
                subscription_id="subscriptionId",
                resource_group_name="resourceGroupName",
                location_="location",
                api_version="api-version",
                country="country",
                location="location",
                transfer_type="ImportToAzure",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listavailableskusbyresourcegroup(
            subscription_id,
            resource_group_name,
            location_,
            api_version=api_version,
            country=country,
            location=location,
            transfer_type=transfer_type,
            sku_names=sku_names,
            request_options=request_options,
        )
        return _response.data

    async def validateinputsbyresourcegroup(
        self,
        subscription_id: str,
        resource_group_name: str,
        location: str,
        *,
        api_version: str,
        individual_request_details: typing.Sequence[ValidationInputRequest],
        validation_category: ValidationRequestValidationCategory,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidationResponse:
        """
        This method does all necessary pre-job creation validation under resource group.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        location : str
            The location of the resource

        api_version : str
            The API Version

        individual_request_details : typing.Sequence[ValidationInputRequest]
            List of request details contain validationType and its request as key and value respectively.

        validation_category : ValidationRequestValidationCategory
            Identify the nature of validation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidationResponse
            The validation status and responses of each validating parameter.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ValidationInputRequest

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.service.validateinputsbyresourcegroup(
                subscription_id="subscriptionId",
                resource_group_name="resourceGroupName",
                location="location",
                api_version="api-version",
                individual_request_details=[
                    ValidationInputRequest(
                        validation_type="ValidateAddress",
                    )
                ],
                validation_category="JobCreationValidation",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.validateinputsbyresourcegroup(
            subscription_id,
            resource_group_name,
            location,
            api_version=api_version,
            individual_request_details=individual_request_details,
            validation_category=validation_category,
            request_options=request_options,
        )
        return _response.data
