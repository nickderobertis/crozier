

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.settings_dto import SettingsDto
from ..types.validation_error_response import ValidationErrorResponse
from .types.settings_update_dto_thumbnail_size import SettingsUpdateDtoThumbnailSize
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawServerSettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_server_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SettingsDto]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SettingsDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SettingsDto,
                    parse_obj_as(
                        type_=SettingsDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    def update_server_settings(
        self,
        *,
        delete_empty_collections: typing.Optional[bool] = OMIT,
        delete_empty_read_lists: typing.Optional[bool] = OMIT,
        kepubify_path: typing.Optional[str] = OMIT,
        kobo_port: typing.Optional[int] = OMIT,
        kobo_proxy: typing.Optional[bool] = OMIT,
        remember_me_duration_days: typing.Optional[int] = OMIT,
        renew_remember_me_key: typing.Optional[bool] = OMIT,
        server_context_path: typing.Optional[str] = OMIT,
        server_port: typing.Optional[int] = OMIT,
        task_pool_size: typing.Optional[int] = OMIT,
        thumbnail_size: typing.Optional[SettingsUpdateDtoThumbnailSize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        You can omit fields you don't want to update

        Required role: **ADMIN**

        Parameters
        ----------
        delete_empty_collections : typing.Optional[bool]

        delete_empty_read_lists : typing.Optional[bool]

        kepubify_path : typing.Optional[str]
            Will be removed in a future version

        kobo_port : typing.Optional[int]

        kobo_proxy : typing.Optional[bool]

        remember_me_duration_days : typing.Optional[int]

        renew_remember_me_key : typing.Optional[bool]

        server_context_path : typing.Optional[str]

        server_port : typing.Optional[int]

        task_pool_size : typing.Optional[int]

        thumbnail_size : typing.Optional[SettingsUpdateDtoThumbnailSize]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/settings",
            method="PATCH",
            json={
                "deleteEmptyCollections": delete_empty_collections,
                "deleteEmptyReadLists": delete_empty_read_lists,
                "kepubifyPath": kepubify_path,
                "koboPort": kobo_port,
                "koboProxy": kobo_proxy,
                "rememberMeDurationDays": remember_me_duration_days,
                "renewRememberMeKey": renew_remember_me_key,
                "serverContextPath": server_context_path,
                "serverPort": server_port,
                "taskPoolSize": task_pool_size,
                "thumbnailSize": thumbnail_size,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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


class AsyncRawServerSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_server_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SettingsDto]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SettingsDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SettingsDto,
                    parse_obj_as(
                        type_=SettingsDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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

    async def update_server_settings(
        self,
        *,
        delete_empty_collections: typing.Optional[bool] = OMIT,
        delete_empty_read_lists: typing.Optional[bool] = OMIT,
        kepubify_path: typing.Optional[str] = OMIT,
        kobo_port: typing.Optional[int] = OMIT,
        kobo_proxy: typing.Optional[bool] = OMIT,
        remember_me_duration_days: typing.Optional[int] = OMIT,
        renew_remember_me_key: typing.Optional[bool] = OMIT,
        server_context_path: typing.Optional[str] = OMIT,
        server_port: typing.Optional[int] = OMIT,
        task_pool_size: typing.Optional[int] = OMIT,
        thumbnail_size: typing.Optional[SettingsUpdateDtoThumbnailSize] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        You can omit fields you don't want to update

        Required role: **ADMIN**

        Parameters
        ----------
        delete_empty_collections : typing.Optional[bool]

        delete_empty_read_lists : typing.Optional[bool]

        kepubify_path : typing.Optional[str]
            Will be removed in a future version

        kobo_port : typing.Optional[int]

        kobo_proxy : typing.Optional[bool]

        remember_me_duration_days : typing.Optional[int]

        renew_remember_me_key : typing.Optional[bool]

        server_context_path : typing.Optional[str]

        server_port : typing.Optional[int]

        task_pool_size : typing.Optional[int]

        thumbnail_size : typing.Optional[SettingsUpdateDtoThumbnailSize]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/settings",
            method="PATCH",
            json={
                "deleteEmptyCollections": delete_empty_collections,
                "deleteEmptyReadLists": delete_empty_read_lists,
                "kepubifyPath": kepubify_path,
                "koboPort": kobo_port,
                "koboProxy": kobo_proxy,
                "rememberMeDurationDays": remember_me_duration_days,
                "renewRememberMeKey": renew_remember_me_key,
                "serverContextPath": server_context_path,
                "serverPort": server_port,
                "taskPoolSize": task_pool_size,
                "thumbnailSize": thumbnail_size,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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
