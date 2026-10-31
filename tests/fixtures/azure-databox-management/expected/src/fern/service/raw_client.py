

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
from .types.validate_address_device_type import ValidateAddressDeviceType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawServiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[AvailableSkusResult]:
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
        HttpResponse[AvailableSkusResult]
            The list of available skus under subscription.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.DataBox/locations/{encode_path_param(location_)}/availableSkus",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "country": country,
                "location": location,
                "skuNames": sku_names,
                "transferType": transfer_type,
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
                    AvailableSkusResult,
                    parse_obj_as(
                        type_=AvailableSkusResult,
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

    def regionconfiguration(
        self,
        subscription_id: str,
        location: str,
        *,
        api_version: str,
        schedule_availability_request: typing.Optional[ScheduleAvailabilityRequest] = OMIT,
        transport_availability_request: typing.Optional[TransportAvailabilityRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RegionConfigurationResponse]:
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
        HttpResponse[RegionConfigurationResponse]
            Region configuration response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.DataBox/locations/{encode_path_param(location)}/regionConfiguration",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "scheduleAvailabilityRequest": convert_and_respect_annotation_metadata(
                    object_=schedule_availability_request, annotation=ScheduleAvailabilityRequest, direction="write"
                ),
                "transportAvailabilityRequest": convert_and_respect_annotation_metadata(
                    object_=transport_availability_request, annotation=TransportAvailabilityRequest, direction="write"
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
                    RegionConfigurationResponse,
                    parse_obj_as(
                        type_=RegionConfigurationResponse,
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
    ) -> HttpResponse[AddressValidationOutput]:
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
        HttpResponse[AddressValidationOutput]
            The valid and alternate addresses.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.DataBox/locations/{encode_path_param(location)}/validateAddress",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "deviceType": device_type,
                "shippingAddress": convert_and_respect_annotation_metadata(
                    object_=shipping_address, annotation=ShippingAddress, direction="write"
                ),
                "transportPreferences": convert_and_respect_annotation_metadata(
                    object_=transport_preferences, annotation=TransportPreferences, direction="write"
                ),
                "validationType": validation_type,
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
                    AddressValidationOutput,
                    parse_obj_as(
                        type_=AddressValidationOutput,
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

    def validateinputs(
        self,
        subscription_id: str,
        location: str,
        *,
        api_version: str,
        individual_request_details: typing.Sequence[ValidationInputRequest],
        validation_category: ValidationRequestValidationCategory,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ValidationResponse]:
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
        HttpResponse[ValidationResponse]
            The validation status and responses of each validating parameter.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.DataBox/locations/{encode_path_param(location)}/validateInputs",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "individualRequestDetails": convert_and_respect_annotation_metadata(
                    object_=individual_request_details,
                    annotation=typing.Sequence[ValidationInputRequest],
                    direction="write",
                ),
                "validationCategory": validation_category,
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
                    ValidationResponse,
                    parse_obj_as(
                        type_=ValidationResponse,
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
    ) -> HttpResponse[AvailableSkusResult]:
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
        HttpResponse[AvailableSkusResult]
            The list of available skus under Resource group.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/locations/{encode_path_param(location_)}/availableSkus",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "country": country,
                "location": location,
                "skuNames": sku_names,
                "transferType": transfer_type,
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
                    AvailableSkusResult,
                    parse_obj_as(
                        type_=AvailableSkusResult,
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
    ) -> HttpResponse[ValidationResponse]:
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
        HttpResponse[ValidationResponse]
            The validation status and responses of each validating parameter.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/locations/{encode_path_param(location)}/validateInputs",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "individualRequestDetails": convert_and_respect_annotation_metadata(
                    object_=individual_request_details,
                    annotation=typing.Sequence[ValidationInputRequest],
                    direction="write",
                ),
                "validationCategory": validation_category,
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
                    ValidationResponse,
                    parse_obj_as(
                        type_=ValidationResponse,
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


class AsyncRawServiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[AvailableSkusResult]:
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
        AsyncHttpResponse[AvailableSkusResult]
            The list of available skus under subscription.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.DataBox/locations/{encode_path_param(location_)}/availableSkus",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "country": country,
                "location": location,
                "skuNames": sku_names,
                "transferType": transfer_type,
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
                    AvailableSkusResult,
                    parse_obj_as(
                        type_=AvailableSkusResult,
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

    async def regionconfiguration(
        self,
        subscription_id: str,
        location: str,
        *,
        api_version: str,
        schedule_availability_request: typing.Optional[ScheduleAvailabilityRequest] = OMIT,
        transport_availability_request: typing.Optional[TransportAvailabilityRequest] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RegionConfigurationResponse]:
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
        AsyncHttpResponse[RegionConfigurationResponse]
            Region configuration response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.DataBox/locations/{encode_path_param(location)}/regionConfiguration",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "scheduleAvailabilityRequest": convert_and_respect_annotation_metadata(
                    object_=schedule_availability_request, annotation=ScheduleAvailabilityRequest, direction="write"
                ),
                "transportAvailabilityRequest": convert_and_respect_annotation_metadata(
                    object_=transport_availability_request, annotation=TransportAvailabilityRequest, direction="write"
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
                    RegionConfigurationResponse,
                    parse_obj_as(
                        type_=RegionConfigurationResponse,
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
    ) -> AsyncHttpResponse[AddressValidationOutput]:
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
        AsyncHttpResponse[AddressValidationOutput]
            The valid and alternate addresses.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.DataBox/locations/{encode_path_param(location)}/validateAddress",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "deviceType": device_type,
                "shippingAddress": convert_and_respect_annotation_metadata(
                    object_=shipping_address, annotation=ShippingAddress, direction="write"
                ),
                "transportPreferences": convert_and_respect_annotation_metadata(
                    object_=transport_preferences, annotation=TransportPreferences, direction="write"
                ),
                "validationType": validation_type,
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
                    AddressValidationOutput,
                    parse_obj_as(
                        type_=AddressValidationOutput,
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

    async def validateinputs(
        self,
        subscription_id: str,
        location: str,
        *,
        api_version: str,
        individual_request_details: typing.Sequence[ValidationInputRequest],
        validation_category: ValidationRequestValidationCategory,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ValidationResponse]:
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
        AsyncHttpResponse[ValidationResponse]
            The validation status and responses of each validating parameter.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.DataBox/locations/{encode_path_param(location)}/validateInputs",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "individualRequestDetails": convert_and_respect_annotation_metadata(
                    object_=individual_request_details,
                    annotation=typing.Sequence[ValidationInputRequest],
                    direction="write",
                ),
                "validationCategory": validation_category,
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
                    ValidationResponse,
                    parse_obj_as(
                        type_=ValidationResponse,
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
    ) -> AsyncHttpResponse[AvailableSkusResult]:
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
        AsyncHttpResponse[AvailableSkusResult]
            The list of available skus under Resource group.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/locations/{encode_path_param(location_)}/availableSkus",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "country": country,
                "location": location,
                "skuNames": sku_names,
                "transferType": transfer_type,
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
                    AvailableSkusResult,
                    parse_obj_as(
                        type_=AvailableSkusResult,
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
    ) -> AsyncHttpResponse[ValidationResponse]:
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
        AsyncHttpResponse[ValidationResponse]
            The validation status and responses of each validating parameter.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/locations/{encode_path_param(location)}/validateInputs",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "individualRequestDetails": convert_and_respect_annotation_metadata(
                    object_=individual_request_details,
                    annotation=typing.Sequence[ValidationInputRequest],
                    direction="write",
                ),
                "validationCategory": validation_category,
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
                    ValidationResponse,
                    parse_obj_as(
                        type_=ValidationResponse,
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
