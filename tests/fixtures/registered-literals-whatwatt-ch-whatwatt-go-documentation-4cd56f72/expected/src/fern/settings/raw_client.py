

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.bad_request_error_body import BadRequestErrorBody
from ..types.internal_server_error_body import InternalServerErrorBody
from ..types.unauthorized_error_body import UnauthorizedErrorBody
from .types.get_settings_response import GetSettingsResponse
from .types.replace_settings_request_services import ReplaceSettingsRequestServices
from .types.replace_settings_request_system import ReplaceSettingsRequestSystem
from .types.replace_settings_response import ReplaceSettingsResponse
from .types.update_settings_request_services import UpdateSettingsRequestServices
from .types.update_settings_request_system import UpdateSettingsRequestSystem
from .types.update_settings_response import UpdateSettingsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSettingsResponse]:
        """
        Reads the current configuration. Most settings apply dynamically without reboot.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSettingsResponse]
            Current settings
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSettingsResponse,
                    parse_obj_as(
                        type_=GetSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def replace_settings(
        self,
        *,
        system: typing.Optional[ReplaceSettingsRequestSystem] = OMIT,
        services: typing.Optional[ReplaceSettingsRequestServices] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ReplaceSettingsResponse]:
        """
        Replaces the entire configuration object. Values apply dynamically.

        Parameters
        ----------
        system : typing.Optional[ReplaceSettingsRequestSystem]

        services : typing.Optional[ReplaceSettingsRequestServices]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReplaceSettingsResponse]
            Replaced settings
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/settings",
            method="POST",
            json={
                "system": convert_and_respect_annotation_metadata(
                    object_=system, annotation=ReplaceSettingsRequestSystem, direction="write"
                ),
                "services": convert_and_respect_annotation_metadata(
                    object_=services, annotation=ReplaceSettingsRequestServices, direction="write"
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
                    ReplaceSettingsResponse,
                    parse_obj_as(
                        type_=ReplaceSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    def update_settings(
        self,
        *,
        system: typing.Optional[UpdateSettingsRequestSystem] = OMIT,
        services: typing.Optional[UpdateSettingsRequestServices] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateSettingsResponse]:
        """
        Partially updates the configuration object. Values apply dynamically.

        Parameters
        ----------
        system : typing.Optional[UpdateSettingsRequestSystem]

        services : typing.Optional[UpdateSettingsRequestServices]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSettingsResponse]
            Updated settings
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/settings",
            method="PUT",
            json={
                "system": convert_and_respect_annotation_metadata(
                    object_=system, annotation=UpdateSettingsRequestSystem, direction="write"
                ),
                "services": convert_and_respect_annotation_metadata(
                    object_=services, annotation=UpdateSettingsRequestServices, direction="write"
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
                    UpdateSettingsResponse,
                    parse_obj_as(
                        type_=UpdateSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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


class AsyncRawSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSettingsResponse]:
        """
        Reads the current configuration. Most settings apply dynamically without reboot.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSettingsResponse]
            Current settings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSettingsResponse,
                    parse_obj_as(
                        type_=GetSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def replace_settings(
        self,
        *,
        system: typing.Optional[ReplaceSettingsRequestSystem] = OMIT,
        services: typing.Optional[ReplaceSettingsRequestServices] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ReplaceSettingsResponse]:
        """
        Replaces the entire configuration object. Values apply dynamically.

        Parameters
        ----------
        system : typing.Optional[ReplaceSettingsRequestSystem]

        services : typing.Optional[ReplaceSettingsRequestServices]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReplaceSettingsResponse]
            Replaced settings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/settings",
            method="POST",
            json={
                "system": convert_and_respect_annotation_metadata(
                    object_=system, annotation=ReplaceSettingsRequestSystem, direction="write"
                ),
                "services": convert_and_respect_annotation_metadata(
                    object_=services, annotation=ReplaceSettingsRequestServices, direction="write"
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
                    ReplaceSettingsResponse,
                    parse_obj_as(
                        type_=ReplaceSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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

    async def update_settings(
        self,
        *,
        system: typing.Optional[UpdateSettingsRequestSystem] = OMIT,
        services: typing.Optional[UpdateSettingsRequestServices] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateSettingsResponse]:
        """
        Partially updates the configuration object. Values apply dynamically.

        Parameters
        ----------
        system : typing.Optional[UpdateSettingsRequestSystem]

        services : typing.Optional[UpdateSettingsRequestServices]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSettingsResponse]
            Updated settings
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/settings",
            method="PUT",
            json={
                "system": convert_and_respect_annotation_metadata(
                    object_=system, annotation=UpdateSettingsRequestSystem, direction="write"
                ),
                "services": convert_and_respect_annotation_metadata(
                    object_=services, annotation=UpdateSettingsRequestServices, direction="write"
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
                    UpdateSettingsResponse,
                    parse_obj_as(
                        type_=UpdateSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
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
