

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.module_federation_dto import ModuleFederationDto
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawModuleFederationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_manifest_for_client_app(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, ModuleFederationDto]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, ModuleFederationDto]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/module-federation/get-manifest",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, ModuleFederationDto],
                    parse_obj_as(
                        type_=typing.Dict[str, ModuleFederationDto],
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

    def registry_module(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        remote_entry: typing.Optional[str] = OMIT,
        base_url: typing.Optional[str] = OMIT,
        export_module: typing.Optional[ModuleFederationDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            See 'name' in webpack.config.js

        remote_entry : typing.Optional[str]
            Remote entry

        base_url : typing.Optional[str]
            Base Url

        export_module : typing.Optional[ModuleFederationDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/module-federation/register-module",
            method="POST",
            json={
                "name": name,
                "remoteEntry": remote_entry,
                "baseUrl": base_url,
                "exportModule": convert_and_respect_annotation_metadata(
                    object_=export_module, annotation=ModuleFederationDto, direction="write"
                ),
            },
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


class AsyncRawModuleFederationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_manifest_for_client_app(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, ModuleFederationDto]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, ModuleFederationDto]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/module-federation/get-manifest",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, ModuleFederationDto],
                    parse_obj_as(
                        type_=typing.Dict[str, ModuleFederationDto],
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

    async def registry_module(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        remote_entry: typing.Optional[str] = OMIT,
        base_url: typing.Optional[str] = OMIT,
        export_module: typing.Optional[ModuleFederationDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            See 'name' in webpack.config.js

        remote_entry : typing.Optional[str]
            Remote entry

        base_url : typing.Optional[str]
            Base Url

        export_module : typing.Optional[ModuleFederationDto]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/module-federation/register-module",
            method="POST",
            json={
                "name": name,
                "remoteEntry": remote_entry,
                "baseUrl": base_url,
                "exportModule": convert_and_respect_annotation_metadata(
                    object_=export_module, annotation=ModuleFederationDto, direction="write"
                ),
            },
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
