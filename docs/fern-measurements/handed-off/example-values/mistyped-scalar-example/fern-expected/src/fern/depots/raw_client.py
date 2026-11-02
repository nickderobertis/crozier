

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.compare_depots_response import CompareDepotsResponse
from .types.create_depot_response import CreateDepotResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDepotsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_depot(
        self,
        *,
        postcode: str,
        capacity: int,
        code: str,
        aliases: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateDepotResponse]:
        """
        Parameters
        ----------
        postcode : str

        capacity : int

        code : str

        aliases : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateDepotResponse]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "depots",
            method="POST",
            json={
                "postcode": postcode,
                "capacity": capacity,
                "code": code,
                "aliases": aliases,
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
                    CreateDepotResponse,
                    parse_obj_as(
                        type_=CreateDepotResponse,
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

    def compare_depots(
        self, *, left: str, right: str, level: float, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CompareDepotsResponse]:
        """
        Parameters
        ----------
        left : str

        right : str

        level : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CompareDepotsResponse]
            Compared
        """
        _response = self._client_wrapper.httpx_client.request(
            "depots/compare",
            method="POST",
            json={
                "left": left,
                "right": right,
                "level": level,
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
                    CompareDepotsResponse,
                    parse_obj_as(
                        type_=CompareDepotsResponse,
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

    def purge_depots(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "depots/purge",
            method="DELETE",
            json=request,
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


class AsyncRawDepotsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_depot(
        self,
        *,
        postcode: str,
        capacity: int,
        code: str,
        aliases: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateDepotResponse]:
        """
        Parameters
        ----------
        postcode : str

        capacity : int

        code : str

        aliases : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateDepotResponse]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "depots",
            method="POST",
            json={
                "postcode": postcode,
                "capacity": capacity,
                "code": code,
                "aliases": aliases,
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
                    CreateDepotResponse,
                    parse_obj_as(
                        type_=CreateDepotResponse,
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

    async def compare_depots(
        self, *, left: str, right: str, level: float, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CompareDepotsResponse]:
        """
        Parameters
        ----------
        left : str

        right : str

        level : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CompareDepotsResponse]
            Compared
        """
        _response = await self._client_wrapper.httpx_client.request(
            "depots/compare",
            method="POST",
            json={
                "left": left,
                "right": right,
                "level": level,
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
                    CompareDepotsResponse,
                    parse_obj_as(
                        type_=CompareDepotsResponse,
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

    async def purge_depots(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "depots/purge",
            method="DELETE",
            json=request,
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
