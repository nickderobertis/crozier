

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.element_spent_response import ElementSpentResponse
from ..types.hash256 import Hash256
from ..types.siacoin_element import SiacoinElement
from ..types.siafund_element import SiafundElement
from pydantic import ValidationError


class RawOutputsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_siacoin_output(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SiacoinElement]:
        """
        Parameters
        ----------
        id : Hash256
            Siacoin output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SiacoinElement]
            Siacoin element details.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"outputs/siacoin/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SiacoinElement,
                    parse_obj_as(
                        type_=SiacoinElement,
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

    def get_siacoin_output_spent(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ElementSpentResponse]:
        """
        Parameters
        ----------
        id : Hash256
            Siacoin output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ElementSpentResponse]
            Spent status and optional spend event.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"outputs/siacoin/{encode_path_param(id)}/spent",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ElementSpentResponse,
                    parse_obj_as(
                        type_=ElementSpentResponse,
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

    def get_siafund_output(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SiafundElement]:
        """
        Parameters
        ----------
        id : Hash256
            Siafund output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SiafundElement]
            Siafund element details.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"outputs/siafund/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SiafundElement,
                    parse_obj_as(
                        type_=SiafundElement,
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

    def get_siafund_output_spent(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ElementSpentResponse]:
        """
        Parameters
        ----------
        id : Hash256
            Siafund output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ElementSpentResponse]
            Spent status and optional spend event.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"outputs/siafund/{encode_path_param(id)}/spent",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ElementSpentResponse,
                    parse_obj_as(
                        type_=ElementSpentResponse,
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


class AsyncRawOutputsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_siacoin_output(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SiacoinElement]:
        """
        Parameters
        ----------
        id : Hash256
            Siacoin output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SiacoinElement]
            Siacoin element details.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"outputs/siacoin/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SiacoinElement,
                    parse_obj_as(
                        type_=SiacoinElement,
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

    async def get_siacoin_output_spent(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ElementSpentResponse]:
        """
        Parameters
        ----------
        id : Hash256
            Siacoin output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ElementSpentResponse]
            Spent status and optional spend event.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"outputs/siacoin/{encode_path_param(id)}/spent",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ElementSpentResponse,
                    parse_obj_as(
                        type_=ElementSpentResponse,
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

    async def get_siafund_output(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SiafundElement]:
        """
        Parameters
        ----------
        id : Hash256
            Siafund output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SiafundElement]
            Siafund element details.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"outputs/siafund/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SiafundElement,
                    parse_obj_as(
                        type_=SiafundElement,
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

    async def get_siafund_output_spent(
        self, id: Hash256, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ElementSpentResponse]:
        """
        Parameters
        ----------
        id : Hash256
            Siafund output ID (hex).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ElementSpentResponse]
            Spent status and optional spend event.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"outputs/siafund/{encode_path_param(id)}/spent",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ElementSpentResponse,
                    parse_obj_as(
                        type_=ElementSpentResponse,
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
