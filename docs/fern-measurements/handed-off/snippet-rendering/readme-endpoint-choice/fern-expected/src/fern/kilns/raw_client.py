

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.firing import Firing
from ..types.kiln import Kiln
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawKilnsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_kilns(
        self, *, site: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Kiln]]:
        """
        Parameters
        ----------
        site : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Kiln]]
            The kilns at the site.
        """
        _response = self._client_wrapper.httpx_client.request(
            "kilns",
            method="GET",
            params={
                "site": site,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Kiln],
                    parse_obj_as(
                        type_=typing.List[Kiln],
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

    def record_firing(
        self, *, controller_log: core.File, kiln: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Firing]:
        """
        Parameters
        ----------
        controller_log : core.File
            See core.File for more documentation

        kiln : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Firing]
            The recorded firing.
        """
        _response = self._client_wrapper.httpx_client.request(
            "kilns/firings",
            method="POST",
            data={
                "kiln": kiln,
            },
            files={
                "controller_log": controller_log,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Firing,
                    parse_obj_as(
                        type_=Firing,
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

    def add_glaze(
        self, *, name: str, cone: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Firing]:
        """
        Parameters
        ----------
        name : str

        cone : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Firing]
            The added glaze.
        """
        _response = self._client_wrapper.httpx_client.request(
            "kilns/glazes",
            method="POST",
            json={
                "name": name,
                "cone": cone,
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
                    Firing,
                    parse_obj_as(
                        type_=Firing,
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


class AsyncRawKilnsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_kilns(
        self, *, site: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Kiln]]:
        """
        Parameters
        ----------
        site : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Kiln]]
            The kilns at the site.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "kilns",
            method="GET",
            params={
                "site": site,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Kiln],
                    parse_obj_as(
                        type_=typing.List[Kiln],
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

    async def record_firing(
        self, *, controller_log: core.File, kiln: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Firing]:
        """
        Parameters
        ----------
        controller_log : core.File
            See core.File for more documentation

        kiln : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Firing]
            The recorded firing.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "kilns/firings",
            method="POST",
            data={
                "kiln": kiln,
            },
            files={
                "controller_log": controller_log,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Firing,
                    parse_obj_as(
                        type_=Firing,
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

    async def add_glaze(
        self, *, name: str, cone: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Firing]:
        """
        Parameters
        ----------
        name : str

        cone : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Firing]
            The added glaze.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "kilns/glazes",
            method="POST",
            json={
                "name": name,
                "cone": cone,
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
                    Firing,
                    parse_obj_as(
                        type_=Firing,
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
