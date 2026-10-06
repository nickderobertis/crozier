

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.conflict_error import ConflictError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.refresh_token_response import RefreshTokenResponse
from ..types.tokens_response import TokensResponse
from ..types.update_login_user_response import UpdateLoginUserResponse
from ..types.verify_status import VerifyStatus
from .types.update_login_user_request_password import UpdateLoginUserRequestPassword
from .types.update_login_user_request_user_email import UpdateLoginUserRequestUserEmail
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def user_registration(
        self, *, username: str, password: str, user_email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TokensResponse]:
        """
        Регистрация пользователя

        Parameters
        ----------
        username : str
            Никнейм пользователя

        password : str
            Пароль пользователя

        user_email : str
            Почта пользователя

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokensResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth/registration",
            method="POST",
            json={
                "username": username,
                "password": password,
                "user_email": user_email,
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
                    TokensResponse,
                    parse_obj_as(
                        type_=TokensResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def user_login(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TokensResponse]:
        """
        Вход пользователя и выдача токенов

        Parameters
        ----------
        username : str
            Никнейм пользователя

        password : str
            Пароль пользователя

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokensResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth/login",
            method="POST",
            json={
                "username": username,
                "password": password,
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
                    TokensResponse,
                    parse_obj_as(
                        type_=TokensResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def token_verify(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VerifyStatus]:
        """
        Проверка токена

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VerifyStatus]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth/verify",
            method="GET",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VerifyStatus,
                    parse_obj_as(
                        type_=VerifyStatus,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def token_refresh(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RefreshTokenResponse]:
        """
        Обновление токена

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RefreshTokenResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth/refresh",
            method="GET",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RefreshTokenResponse,
                    parse_obj_as(
                        type_=RefreshTokenResponse,
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

    def update_user_data_auth_users_update_user_patch(
        self,
        *,
        authorization: str,
        password: typing.Optional[UpdateLoginUserRequestPassword] = OMIT,
        user_email: typing.Optional[UpdateLoginUserRequestUserEmail] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateLoginUserResponse]:
        """
        Обнавление данных пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        password : typing.Optional[UpdateLoginUserRequestPassword]

        user_email : typing.Optional[UpdateLoginUserRequestUserEmail]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateLoginUserResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "auth/update_login_data",
            method="PATCH",
            json={
                "password": convert_and_respect_annotation_metadata(
                    object_=password, annotation=UpdateLoginUserRequestPassword, direction="write"
                ),
                "user_email": convert_and_respect_annotation_metadata(
                    object_=user_email, annotation=UpdateLoginUserRequestUserEmail, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateLoginUserResponse,
                    parse_obj_as(
                        type_=UpdateLoginUserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def user_registration(
        self, *, username: str, password: str, user_email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TokensResponse]:
        """
        Регистрация пользователя

        Parameters
        ----------
        username : str
            Никнейм пользователя

        password : str
            Пароль пользователя

        user_email : str
            Почта пользователя

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokensResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth/registration",
            method="POST",
            json={
                "username": username,
                "password": password,
                "user_email": user_email,
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
                    TokensResponse,
                    parse_obj_as(
                        type_=TokensResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def user_login(
        self, *, username: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TokensResponse]:
        """
        Вход пользователя и выдача токенов

        Parameters
        ----------
        username : str
            Никнейм пользователя

        password : str
            Пароль пользователя

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokensResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth/login",
            method="POST",
            json={
                "username": username,
                "password": password,
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
                    TokensResponse,
                    parse_obj_as(
                        type_=TokensResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def token_verify(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VerifyStatus]:
        """
        Проверка токена

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VerifyStatus]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth/verify",
            method="GET",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VerifyStatus,
                    parse_obj_as(
                        type_=VerifyStatus,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def token_refresh(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RefreshTokenResponse]:
        """
        Обновление токена

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RefreshTokenResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth/refresh",
            method="GET",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RefreshTokenResponse,
                    parse_obj_as(
                        type_=RefreshTokenResponse,
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

    async def update_user_data_auth_users_update_user_patch(
        self,
        *,
        authorization: str,
        password: typing.Optional[UpdateLoginUserRequestPassword] = OMIT,
        user_email: typing.Optional[UpdateLoginUserRequestUserEmail] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateLoginUserResponse]:
        """
        Обнавление данных пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        password : typing.Optional[UpdateLoginUserRequestPassword]

        user_email : typing.Optional[UpdateLoginUserRequestUserEmail]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateLoginUserResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "auth/update_login_data",
            method="PATCH",
            json={
                "password": convert_and_respect_annotation_metadata(
                    object_=password, annotation=UpdateLoginUserRequestPassword, direction="write"
                ),
                "user_email": convert_and_respect_annotation_metadata(
                    object_=user_email, annotation=UpdateLoginUserRequestUserEmail, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateLoginUserResponse,
                    parse_obj_as(
                        type_=UpdateLoginUserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
