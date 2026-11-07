

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.check_addresses_response import CheckAddressesResponse
from ..types.state_response import StateResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMiscClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[StateResponse]:
        """
        Returns build metadata and runtime information about the walletd instance.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StateResponse]
            Current daemon state.
        """
        _response = self._client_wrapper.httpx_client.request(
            "state",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StateResponse,
                    parse_obj_as(
                        type_=StateResponse,
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

    def get_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.Dict[str, typing.Any]]]:
        """
        Returns 200 when walletd is healthy.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Dict[str, typing.Any]]]
            Walletd is healthy.
        """
        _response = self._client_wrapper.httpx_client.request(
            "health",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Dict[str, typing.Any]],
                    parse_obj_as(
                        type_=typing.Optional[typing.Dict[str, typing.Any]],
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

    def post_check_addresses(
        self, *, addresses: typing.Sequence[Address], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CheckAddressesResponse]:
        """
        Returns whether any supplied addresses are currently tracked by walletd. In personal indexing mode, only registered wallet addresses are recognized.

        Parameters
        ----------
        addresses : typing.Sequence[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckAddressesResponse]
            Address membership check result.
        """
        _response = self._client_wrapper.httpx_client.request(
            "check/addresses",
            method="POST",
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
                    CheckAddressesResponse,
                    parse_obj_as(
                        type_=CheckAddressesResponse,
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


class AsyncRawMiscClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_state(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StateResponse]:
        """
        Returns build metadata and runtime information about the walletd instance.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StateResponse]
            Current daemon state.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "state",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StateResponse,
                    parse_obj_as(
                        type_=StateResponse,
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

    async def get_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.Dict[str, typing.Any]]]:
        """
        Returns 200 when walletd is healthy.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Dict[str, typing.Any]]]
            Walletd is healthy.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "health",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Dict[str, typing.Any]],
                    parse_obj_as(
                        type_=typing.Optional[typing.Dict[str, typing.Any]],
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

    async def post_check_addresses(
        self, *, addresses: typing.Sequence[Address], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CheckAddressesResponse]:
        """
        Returns whether any supplied addresses are currently tracked by walletd. In personal indexing mode, only registered wallet addresses are recognized.

        Parameters
        ----------
        addresses : typing.Sequence[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckAddressesResponse]
            Address membership check result.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "check/addresses",
            method="POST",
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
                    CheckAddressesResponse,
                    parse_obj_as(
                        type_=CheckAddressesResponse,
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
