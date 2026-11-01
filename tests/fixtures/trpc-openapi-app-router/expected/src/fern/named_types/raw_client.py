

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.named_types_deep_nested_response import NamedTypesDeepNestedResponse
from .types.named_types_order_items_response import NamedTypesOrderItemsResponse
from .types.named_types_profile_and_address_response import NamedTypesProfileAndAddressResponse
from .types.named_types_with_address_response import NamedTypesWithAddressResponse
from .types.named_types_with_profile_response import NamedTypesWithProfileResponse
from pydantic import ValidationError


class RawNamedTypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def named_types_with_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NamedTypesWithProfileResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NamedTypesWithProfileResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "namedTypes.withProfile",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamedTypesWithProfileResponse,
                    parse_obj_as(
                        type_=NamedTypesWithProfileResponse,
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

    def named_types_order_items(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NamedTypesOrderItemsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NamedTypesOrderItemsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "namedTypes.orderItems",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamedTypesOrderItemsResponse,
                    parse_obj_as(
                        type_=NamedTypesOrderItemsResponse,
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

    def named_types_with_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NamedTypesWithAddressResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NamedTypesWithAddressResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "namedTypes.withAddress",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamedTypesWithAddressResponse,
                    parse_obj_as(
                        type_=NamedTypesWithAddressResponse,
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

    def named_types_profile_and_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NamedTypesProfileAndAddressResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NamedTypesProfileAndAddressResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "namedTypes.profileAndAddress",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamedTypesProfileAndAddressResponse,
                    parse_obj_as(
                        type_=NamedTypesProfileAndAddressResponse,
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

    def named_types_deep_nested(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NamedTypesDeepNestedResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NamedTypesDeepNestedResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "namedTypes.deepNested",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamedTypesDeepNestedResponse,
                    parse_obj_as(
                        type_=NamedTypesDeepNestedResponse,
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


class AsyncRawNamedTypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def named_types_with_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NamedTypesWithProfileResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NamedTypesWithProfileResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "namedTypes.withProfile",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamedTypesWithProfileResponse,
                    parse_obj_as(
                        type_=NamedTypesWithProfileResponse,
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

    async def named_types_order_items(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NamedTypesOrderItemsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NamedTypesOrderItemsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "namedTypes.orderItems",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamedTypesOrderItemsResponse,
                    parse_obj_as(
                        type_=NamedTypesOrderItemsResponse,
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

    async def named_types_with_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NamedTypesWithAddressResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NamedTypesWithAddressResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "namedTypes.withAddress",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamedTypesWithAddressResponse,
                    parse_obj_as(
                        type_=NamedTypesWithAddressResponse,
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

    async def named_types_profile_and_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NamedTypesProfileAndAddressResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NamedTypesProfileAndAddressResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "namedTypes.profileAndAddress",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamedTypesProfileAndAddressResponse,
                    parse_obj_as(
                        type_=NamedTypesProfileAndAddressResponse,
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

    async def named_types_deep_nested(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NamedTypesDeepNestedResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NamedTypesDeepNestedResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "namedTypes.deepNested",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamedTypesDeepNestedResponse,
                    parse_obj_as(
                        type_=NamedTypesDeepNestedResponse,
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
