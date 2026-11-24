

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_zones_of_type(
        self,
        type_path_param: str,
        *,
        type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        type_path_param : str
            The zone type.

        type : typing.Optional[str]
            A product code filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            The zones.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"zones/{encode_path_param(type_path_param)}",
            method="GET",
            params={
                "type": type,
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

    async def list_zones_of_type(
        self,
        type_path_param: str,
        *,
        type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        type_path_param : str
            The zone type.

        type : typing.Optional[str]
            A product code filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            The zones.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"zones/{encode_path_param(type_path_param)}",
            method="GET",
            params={
                "type": type,
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
