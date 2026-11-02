

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from pydantic import ValidationError


class RawKeepersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_keeper_shifts(
        self,
        keeper_id: str,
        *,
        season: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        rostered_on: typing.Optional[dt.datetime] = None,
        rostered_after: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        keeper_id : str

        season : typing.Optional[str]

        page : typing.Optional[int]

        q : typing.Optional[str]

        rostered_on : typing.Optional[dt.datetime]

        rostered_after : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Shifts
        """
        _response = self._client_wrapper.httpx_client.request(
            f"keepers/{encode_path_param(keeper_id)}/shifts",
            method="GET",
            params={
                "season": season,
                "page": page,
                "q": q,
                "rosteredOn": serialize_datetime(rostered_on) if rostered_on is not None else None,
                "rosteredAfter": serialize_datetime(rostered_after) if rostered_after is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def list_keeper_callbacks(
        self, *, since: typing.Optional[dt.datetime] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        since : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Callbacks
        """
        _response = self._client_wrapper.httpx_client.request(
            "keepers/callbacks",
            method="GET",
            params={
                "since": serialize_datetime(since) if since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def search_keepers(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        q : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Keepers
        """
        _response = self._client_wrapper.httpx_client.request(
            "keepers/search",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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


class AsyncRawKeepersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_keeper_shifts(
        self,
        keeper_id: str,
        *,
        season: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        rostered_on: typing.Optional[dt.datetime] = None,
        rostered_after: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        keeper_id : str

        season : typing.Optional[str]

        page : typing.Optional[int]

        q : typing.Optional[str]

        rostered_on : typing.Optional[dt.datetime]

        rostered_after : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Shifts
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"keepers/{encode_path_param(keeper_id)}/shifts",
            method="GET",
            params={
                "season": season,
                "page": page,
                "q": q,
                "rosteredOn": serialize_datetime(rostered_on) if rostered_on is not None else None,
                "rosteredAfter": serialize_datetime(rostered_after) if rostered_after is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def list_keeper_callbacks(
        self, *, since: typing.Optional[dt.datetime] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        since : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Callbacks
        """
        _response = await self._client_wrapper.httpx_client.request(
            "keepers/callbacks",
            method="GET",
            params={
                "since": serialize_datetime(since) if since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def search_keepers(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        q : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Keepers
        """
        _response = await self._client_wrapper.httpx_client.request(
            "keepers/search",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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
