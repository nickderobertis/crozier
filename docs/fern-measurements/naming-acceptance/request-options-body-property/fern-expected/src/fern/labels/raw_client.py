

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.dispatch import Dispatch
from pydantic import ValidationError


class RawLabelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_label(
        self, request_options_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dispatch]:
        """
        Parameters
        ----------
        request_options_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dispatch]
            the label
        """
        _response = self._client_wrapper.httpx_client.request(
            f"labels/{encode_path_param(request_options_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dispatch,
                    parse_obj_as(
                        type_=Dispatch,
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

    def list_labels(
        self, *, request_options: typing.Optional[str] = None, _request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Dispatch]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[str]

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Dispatch]]
            every label
        """
        _response = self._client_wrapper.httpx_client.request(
            "labels",
            method="GET",
            headers={
                "Request-Options": str(request_options) if request_options is not None else None,
            },
            request_options=_request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Dispatch],
                    parse_obj_as(
                        type_=typing.List[Dispatch],
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


class AsyncRawLabelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_label(
        self, request_options_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dispatch]:
        """
        Parameters
        ----------
        request_options_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dispatch]
            the label
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"labels/{encode_path_param(request_options_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dispatch,
                    parse_obj_as(
                        type_=Dispatch,
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

    async def list_labels(
        self, *, request_options: typing.Optional[str] = None, _request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Dispatch]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[str]

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Dispatch]]
            every label
        """
        _response = await self._client_wrapper.httpx_client.request(
            "labels",
            method="GET",
            headers={
                "Request-Options": str(request_options) if request_options is not None else None,
            },
            request_options=_request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Dispatch],
                    parse_obj_as(
                        type_=typing.List[Dispatch],
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
