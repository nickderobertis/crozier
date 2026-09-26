

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.tic_response import TicResponse
from .types.get_tic_data_request_format import GetTicDataRequestFormat
from pydantic import ValidationError


class RawDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_tic_data(
        self,
        *,
        format: typing.Optional[GetTicDataRequestFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TicResponse]:
        """
        Returns Taxability Information Code (TIC) data

        Parameters
        ----------
        format : typing.Optional[GetTicDataRequestFormat]
            Serialization format of the response body: 'json' (default) or 'xml'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TicResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "data/tic",
            method="GET",
            params={
                "format": format,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TicResponse,
                    parse_obj_as(
                        type_=TicResponse,
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


class AsyncRawDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_tic_data(
        self,
        *,
        format: typing.Optional[GetTicDataRequestFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TicResponse]:
        """
        Returns Taxability Information Code (TIC) data

        Parameters
        ----------
        format : typing.Optional[GetTicDataRequestFormat]
            Serialization format of the response body: 'json' (default) or 'xml'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TicResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "data/tic",
            method="GET",
            params={
                "format": format,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TicResponse,
                    parse_obj_as(
                        type_=TicResponse,
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
