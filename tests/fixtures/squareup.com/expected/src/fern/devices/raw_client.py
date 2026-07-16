

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.create_device_code_response import CreateDeviceCodeResponse
from ..types.device_code import DeviceCode
from ..types.get_device_code_response import GetDeviceCodeResponse
from ..types.list_device_codes_response import ListDeviceCodesResponse


OMIT = typing.cast(typing.Any, ...)


class RawDevicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_device_codes(
        self,
        *,
        cursor: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        product_type: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListDeviceCodesResponse]:
        """
        Lists all DeviceCodes associated with the merchant.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.

            See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.

        location_id : typing.Optional[str]
            If specified, only returns DeviceCodes of the specified location.
            Returns DeviceCodes of all locations if empty.

        product_type : typing.Optional[str]
            If specified, only returns DeviceCodes targeting the specified product type.
            Returns DeviceCodes of all product types if empty.

        status : typing.Optional[str]
            If specified, returns DeviceCodes with the specified statuses.
            Returns DeviceCodes of status `PAIRED` and `UNPAIRED` if empty.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListDeviceCodesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/devices/codes",
            method="GET",
            params={
                "cursor": cursor,
                "location_id": location_id,
                "product_type": product_type,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDeviceCodesResponse,
                    parse_obj_as(
                        type_=ListDeviceCodesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_device_code(
        self, *, device_code: DeviceCode, idempotency_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateDeviceCodeResponse]:
        """
        Creates a DeviceCode that can be used to login to a Square Terminal device to enter the connected
        terminal mode.

        Parameters
        ----------
        device_code : DeviceCode

        idempotency_key : str
            A unique string that identifies this CreateDeviceCode request. Keys can
            be any valid string but must be unique for every CreateDeviceCode request.

            See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateDeviceCodeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/devices/codes",
            method="POST",
            json={
                "device_code": convert_and_respect_annotation_metadata(
                    object_=device_code, annotation=DeviceCode, direction="write"
                ),
                "idempotency_key": idempotency_key,
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
                    CreateDeviceCodeResponse,
                    parse_obj_as(
                        type_=CreateDeviceCodeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_device_code(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetDeviceCodeResponse]:
        """
        Retrieves DeviceCode with the associated ID.

        Parameters
        ----------
        id : str
            The unique identifier for the device code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDeviceCodeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/devices/codes/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceCodeResponse,
                    parse_obj_as(
                        type_=GetDeviceCodeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawDevicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_device_codes(
        self,
        *,
        cursor: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        product_type: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListDeviceCodesResponse]:
        """
        Lists all DeviceCodes associated with the merchant.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.

            See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.

        location_id : typing.Optional[str]
            If specified, only returns DeviceCodes of the specified location.
            Returns DeviceCodes of all locations if empty.

        product_type : typing.Optional[str]
            If specified, only returns DeviceCodes targeting the specified product type.
            Returns DeviceCodes of all product types if empty.

        status : typing.Optional[str]
            If specified, returns DeviceCodes with the specified statuses.
            Returns DeviceCodes of status `PAIRED` and `UNPAIRED` if empty.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListDeviceCodesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/devices/codes",
            method="GET",
            params={
                "cursor": cursor,
                "location_id": location_id,
                "product_type": product_type,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListDeviceCodesResponse,
                    parse_obj_as(
                        type_=ListDeviceCodesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_device_code(
        self, *, device_code: DeviceCode, idempotency_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateDeviceCodeResponse]:
        """
        Creates a DeviceCode that can be used to login to a Square Terminal device to enter the connected
        terminal mode.

        Parameters
        ----------
        device_code : DeviceCode

        idempotency_key : str
            A unique string that identifies this CreateDeviceCode request. Keys can
            be any valid string but must be unique for every CreateDeviceCode request.

            See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateDeviceCodeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/devices/codes",
            method="POST",
            json={
                "device_code": convert_and_respect_annotation_metadata(
                    object_=device_code, annotation=DeviceCode, direction="write"
                ),
                "idempotency_key": idempotency_key,
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
                    CreateDeviceCodeResponse,
                    parse_obj_as(
                        type_=CreateDeviceCodeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_device_code(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetDeviceCodeResponse]:
        """
        Retrieves DeviceCode with the associated ID.

        Parameters
        ----------
        id : str
            The unique identifier for the device code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDeviceCodeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/devices/codes/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceCodeResponse,
                    parse_obj_as(
                        type_=GetDeviceCodeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
