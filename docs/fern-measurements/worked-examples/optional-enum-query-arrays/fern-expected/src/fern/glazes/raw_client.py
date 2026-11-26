

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.finish import Finish
from .types.list_glazes_request_firing_item import ListGlazesRequestFiringItem
from pydantic import ValidationError


class RawGlazesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_glazes(
        self,
        *,
        finish: typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]] = None,
        firing: typing.Optional[
            typing.Union[ListGlazesRequestFiringItem, typing.Sequence[ListGlazesRequestFiringItem]]
        ] = None,
        palette: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        finish : typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]]

        firing : typing.Optional[typing.Union[ListGlazesRequestFiringItem, typing.Sequence[ListGlazesRequestFiringItem]]]

        palette : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            The glazes.
        """
        _response = self._client_wrapper.httpx_client.request(
            "glazes",
            method="GET",
            params={
                "finish": finish,
                "firing": firing,
                "palette": palette,
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

    def list_required_glazes(
        self,
        *,
        finish: typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        finish : typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            The glazes.
        """
        _response = self._client_wrapper.httpx_client.request(
            "glazes/required",
            method="GET",
            params={
                "finish": finish,
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


class AsyncRawGlazesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_glazes(
        self,
        *,
        finish: typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]] = None,
        firing: typing.Optional[
            typing.Union[ListGlazesRequestFiringItem, typing.Sequence[ListGlazesRequestFiringItem]]
        ] = None,
        palette: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        finish : typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]]

        firing : typing.Optional[typing.Union[ListGlazesRequestFiringItem, typing.Sequence[ListGlazesRequestFiringItem]]]

        palette : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            The glazes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "glazes",
            method="GET",
            params={
                "finish": finish,
                "firing": firing,
                "palette": palette,
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

    async def list_required_glazes(
        self,
        *,
        finish: typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        finish : typing.Optional[typing.Union[Finish, typing.Sequence[Finish]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            The glazes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "glazes/required",
            method="GET",
            params={
                "finish": finish,
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
