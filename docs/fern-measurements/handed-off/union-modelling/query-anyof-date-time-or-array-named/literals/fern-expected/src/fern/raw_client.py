

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.datetime_utils import serialize_datetime
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_parcels(
        self,
        *,
        shipped_at: typing.Optional[typing.Union[dt.datetime, typing.Sequence[dt.datetime]]] = None,
        weight: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        shipped_at : typing.Optional[typing.Union[dt.datetime, typing.Sequence[dt.datetime]]]
            When the parcel shipped, or any of several moments.

        weight : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            The parcels.
        """
        _response = self._client_wrapper.httpx_client.request(
            "parcels",
            method="GET",
            params={
                "shipped_at": serialize_datetime(shipped_at) if shipped_at is not None else None,
                "weight": weight,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_parcels(
        self,
        *,
        shipped_at: typing.Optional[typing.Union[dt.datetime, typing.Sequence[dt.datetime]]] = None,
        weight: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        shipped_at : typing.Optional[typing.Union[dt.datetime, typing.Sequence[dt.datetime]]]
            When the parcel shipped, or any of several moments.

        weight : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            The parcels.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "parcels",
            method="GET",
            params={
                "shipped_at": serialize_datetime(shipped_at) if shipped_at is not None else None,
                "weight": weight,
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
