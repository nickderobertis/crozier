

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.hull import Hull
from pydantic import ValidationError


class RawVesselsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_vessels(
        self,
        *,
        owners: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        hulls: typing.Optional[typing.Union[Hull, typing.Sequence[Hull]]] = None,
        flags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        port: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        owners : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        hulls : typing.Optional[typing.Union[Hull, typing.Sequence[Hull]]]

        flags : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        port : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Vessels
        """
        _response = self._client_wrapper.httpx_client.request(
            "vessels",
            method="GET",
            params={
                "owners[]": owners,
                "hulls[]": hulls,
                "flags": flags,
                "port": port,
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


class AsyncRawVesselsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_vessels(
        self,
        *,
        owners: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        hulls: typing.Optional[typing.Union[Hull, typing.Sequence[Hull]]] = None,
        flags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        port: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        owners : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        hulls : typing.Optional[typing.Union[Hull, typing.Sequence[Hull]]]

        flags : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        port : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Vessels
        """
        _response = await self._client_wrapper.httpx_client.request(
            "vessels",
            method="GET",
            params={
                "owners[]": owners,
                "hulls[]": hulls,
                "flags": flags,
                "port": port,
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
