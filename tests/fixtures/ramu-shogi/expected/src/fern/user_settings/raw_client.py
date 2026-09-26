

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.conflict_error import ConflictError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.api_error_response import ApiErrorResponse
from ..types.get_user_settings_response import GetUserSettingsResponse
from ..types.json_value import JsonValue
from ..types.list_user_settings_response import ListUserSettingsResponse
from ..types.put_user_settings_response import PutUserSettingsResponse
from ..types.user_settings_document_key import UserSettingsDocumentKey
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUserSettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_user_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListUserSettingsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListUserSettingsResponse]
            List user settings documents
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/user/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListUserSettingsResponse,
                    parse_obj_as(
                        type_=ListUserSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    def get_user_settings(
        self, document_key: UserSettingsDocumentKey, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetUserSettingsResponse]:
        """
        Parameters
        ----------
        document_key : UserSettingsDocumentKey

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetUserSettingsResponse]
            Get a user settings document
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/user/settings/{encode_path_param(document_key)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserSettingsResponse,
                    parse_obj_as(
                        type_=GetUserSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    def put_user_settings(
        self,
        document_key: UserSettingsDocumentKey,
        *,
        value: typing.Optional[JsonValue] = OMIT,
        expected_version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutUserSettingsResponse]:
        """
        Parameters
        ----------
        document_key : UserSettingsDocumentKey

        value : typing.Optional[JsonValue]

        expected_version : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutUserSettingsResponse]
            Updated user settings document
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/user/settings/{encode_path_param(document_key)}",
            method="PUT",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=typing.Optional[JsonValue], direction="write"
                ),
                "expectedVersion": expected_version,
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
                    PutUserSettingsResponse,
                    parse_obj_as(
                        type_=PutUserSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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


class AsyncRawUserSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_user_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListUserSettingsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListUserSettingsResponse]
            List user settings documents
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/user/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListUserSettingsResponse,
                    parse_obj_as(
                        type_=ListUserSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    async def get_user_settings(
        self, document_key: UserSettingsDocumentKey, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetUserSettingsResponse]:
        """
        Parameters
        ----------
        document_key : UserSettingsDocumentKey

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetUserSettingsResponse]
            Get a user settings document
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/user/settings/{encode_path_param(document_key)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetUserSettingsResponse,
                    parse_obj_as(
                        type_=GetUserSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    async def put_user_settings(
        self,
        document_key: UserSettingsDocumentKey,
        *,
        value: typing.Optional[JsonValue] = OMIT,
        expected_version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutUserSettingsResponse]:
        """
        Parameters
        ----------
        document_key : UserSettingsDocumentKey

        value : typing.Optional[JsonValue]

        expected_version : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutUserSettingsResponse]
            Updated user settings document
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/user/settings/{encode_path_param(document_key)}",
            method="PUT",
            json={
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=typing.Optional[JsonValue], direction="write"
                ),
                "expectedVersion": expected_version,
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
                    PutUserSettingsResponse,
                    parse_obj_as(
                        type_=PutUserSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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
