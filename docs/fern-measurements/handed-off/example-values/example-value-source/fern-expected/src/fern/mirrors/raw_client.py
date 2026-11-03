

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.add_mirror_response import AddMirrorResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMirrorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_mirror(
        self, *, source: str, region: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AddMirrorResponse]:
        """
        A format uri and a pattern-only string.

        Parameters
        ----------
        source : str

        region : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddMirrorResponse]
            Added
        """
        _response = self._client_wrapper.httpx_client.request(
            "mirrors",
            method="POST",
            json={
                "source": source,
                "region": region,
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
                    AddMirrorResponse,
                    parse_obj_as(
                        type_=AddMirrorResponse,
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


class AsyncRawMirrorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_mirror(
        self, *, source: str, region: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AddMirrorResponse]:
        """
        A format uri and a pattern-only string.

        Parameters
        ----------
        source : str

        region : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddMirrorResponse]
            Added
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mirrors",
            method="POST",
            json={
                "source": source,
                "region": region,
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
                    AddMirrorResponse,
                    parse_obj_as(
                        type_=AddMirrorResponse,
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
