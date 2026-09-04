

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...core.serialization import convert_and_respect_annotation_metadata
from ...errors.bad_request_error import BadRequestError
from ...errors.not_found_error import NotFoundError
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.get_sandbox_provider_response import GetSandboxProviderResponse
from ...types.request_error_response import RequestErrorResponse
from ...types.sandbox_provider_manifest import SandboxProviderManifest
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSandboxProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSandboxProviderResponse]:
        """
        The single configured sandbox provider for this tenant. `auth.api_key` is redacted.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSandboxProviderResponse]
            The configured sandbox provider.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/settings/sandbox-providers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSandboxProviderResponse,
                    parse_obj_as(
                        type_=GetSandboxProviderResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_or_update(
        self, *, manifest: SandboxProviderManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSandboxProviderResponse]:
        """
        Upserts the single sandbox provider for this tenant: creates it or replaces its entire configuration. `auth.api_key`: real value sets/rotates; redacted keeps existing (400 if none).

        Parameters
        ----------
        manifest : SandboxProviderManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSandboxProviderResponse]
            The saved sandbox provider.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/settings/sandbox-providers",
            method="PUT",
            json={
                "manifest": convert_and_respect_annotation_metadata(
                    object_=manifest, annotation=SandboxProviderManifest, direction="write"
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
                _data = typing.cast(
                    GetSandboxProviderResponse,
                    parse_obj_as(
                        type_=GetSandboxProviderResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSandboxProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSandboxProviderResponse]:
        """
        The single configured sandbox provider for this tenant. `auth.api_key` is redacted.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSandboxProviderResponse]
            The configured sandbox provider.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/settings/sandbox-providers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSandboxProviderResponse,
                    parse_obj_as(
                        type_=GetSandboxProviderResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_or_update(
        self, *, manifest: SandboxProviderManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSandboxProviderResponse]:
        """
        Upserts the single sandbox provider for this tenant: creates it or replaces its entire configuration. `auth.api_key`: real value sets/rotates; redacted keeps existing (400 if none).

        Parameters
        ----------
        manifest : SandboxProviderManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSandboxProviderResponse]
            The saved sandbox provider.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/settings/sandbox-providers",
            method="PUT",
            json={
                "manifest": convert_and_respect_annotation_metadata(
                    object_=manifest, annotation=SandboxProviderManifest, direction="write"
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
                _data = typing.cast(
                    GetSandboxProviderResponse,
                    parse_obj_as(
                        type_=GetSandboxProviderResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RequestErrorResponse,
                        parse_obj_as(
                            type_=RequestErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
