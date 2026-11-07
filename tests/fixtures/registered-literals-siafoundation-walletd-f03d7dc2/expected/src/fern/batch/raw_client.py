

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.address_siacoin_elements_response import AddressSiacoinElementsResponse
from ..types.address_siafund_elements_response import AddressSiafundElementsResponse
from ..types.balance import Balance
from ..types.event import Event
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawBatchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_batch_addresses_balance(
        self, *, addresses: typing.Sequence[Address], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Balance]:
        """
        Returns the aggregate balance for all supplied addresses.

        Parameters
        ----------
        addresses : typing.Sequence[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Balance]
            Combined balance across addresses.
        """
        _response = self._client_wrapper.httpx_client.request(
            "batch/addresses/balance",
            method="POST",
            json={
                "addresses": addresses,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Balance,
                    parse_obj_as(
                        type_=Balance,
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

    def post_batch_addresses_events(
        self,
        *,
        addresses: typing.Sequence[Address],
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Event]]:
        """
        Parameters
        ----------
        addresses : typing.Sequence[Address]

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Event]]
            Events touching any of the supplied addresses.
        """
        _response = self._client_wrapper.httpx_client.request(
            "batch/addresses/events",
            method="POST",
            params={
                "offset": offset,
                "limit": limit,
            },
            json={
                "addresses": addresses,
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
                    typing.List[Event],
                    parse_obj_as(
                        type_=typing.List[Event],
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

    def post_batch_addresses_siacoin_outputs(
        self,
        *,
        addresses: typing.Sequence[Address],
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AddressSiacoinElementsResponse]:
        """
        Parameters
        ----------
        addresses : typing.Sequence[Address]

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddressSiacoinElementsResponse]
            Unspent siacoin outputs for the supplied addresses.
        """
        _response = self._client_wrapper.httpx_client.request(
            "batch/addresses/outputs/siacoin",
            method="POST",
            params={
                "offset": offset,
                "limit": limit,
            },
            json={
                "addresses": addresses,
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
                    AddressSiacoinElementsResponse,
                    parse_obj_as(
                        type_=AddressSiacoinElementsResponse,
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

    def post_batch_addresses_siafund_outputs(
        self,
        *,
        addresses: typing.Sequence[Address],
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AddressSiafundElementsResponse]:
        """
        Parameters
        ----------
        addresses : typing.Sequence[Address]

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddressSiafundElementsResponse]
            Unspent siafund outputs for the supplied addresses.
        """
        _response = self._client_wrapper.httpx_client.request(
            "batch/addresses/outputs/siafund",
            method="POST",
            params={
                "offset": offset,
                "limit": limit,
            },
            json={
                "addresses": addresses,
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
                    AddressSiafundElementsResponse,
                    parse_obj_as(
                        type_=AddressSiafundElementsResponse,
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


class AsyncRawBatchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_batch_addresses_balance(
        self, *, addresses: typing.Sequence[Address], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Balance]:
        """
        Returns the aggregate balance for all supplied addresses.

        Parameters
        ----------
        addresses : typing.Sequence[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Balance]
            Combined balance across addresses.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "batch/addresses/balance",
            method="POST",
            json={
                "addresses": addresses,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Balance,
                    parse_obj_as(
                        type_=Balance,
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

    async def post_batch_addresses_events(
        self,
        *,
        addresses: typing.Sequence[Address],
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Event]]:
        """
        Parameters
        ----------
        addresses : typing.Sequence[Address]

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Event]]
            Events touching any of the supplied addresses.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "batch/addresses/events",
            method="POST",
            params={
                "offset": offset,
                "limit": limit,
            },
            json={
                "addresses": addresses,
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
                    typing.List[Event],
                    parse_obj_as(
                        type_=typing.List[Event],
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

    async def post_batch_addresses_siacoin_outputs(
        self,
        *,
        addresses: typing.Sequence[Address],
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AddressSiacoinElementsResponse]:
        """
        Parameters
        ----------
        addresses : typing.Sequence[Address]

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddressSiacoinElementsResponse]
            Unspent siacoin outputs for the supplied addresses.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "batch/addresses/outputs/siacoin",
            method="POST",
            params={
                "offset": offset,
                "limit": limit,
            },
            json={
                "addresses": addresses,
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
                    AddressSiacoinElementsResponse,
                    parse_obj_as(
                        type_=AddressSiacoinElementsResponse,
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

    async def post_batch_addresses_siafund_outputs(
        self,
        *,
        addresses: typing.Sequence[Address],
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AddressSiafundElementsResponse]:
        """
        Parameters
        ----------
        addresses : typing.Sequence[Address]

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddressSiafundElementsResponse]
            Unspent siafund outputs for the supplied addresses.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "batch/addresses/outputs/siafund",
            method="POST",
            params={
                "offset": offset,
                "limit": limit,
            },
            json={
                "addresses": addresses,
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
                    AddressSiafundElementsResponse,
                    parse_obj_as(
                        type_=AddressSiafundElementsResponse,
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
