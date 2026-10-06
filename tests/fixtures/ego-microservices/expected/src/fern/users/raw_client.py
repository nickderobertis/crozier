

import datetime as dt
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
from ..errors.conflict_error import ConflictError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.deleted_user_response import DeletedUserResponse
from ..types.gender_value import GenderValue
from ..types.http_validation_error import HttpValidationError
from ..types.user_data_response import UserDataResponse
from .types.update_user_request_birthday import UpdateUserRequestBirthday
from .types.update_user_request_first_name import UpdateUserRequestFirstName
from .types.update_user_request_gender import UpdateUserRequestGender
from .types.update_user_request_last_name import UpdateUserRequestLastName
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_user(
        self, *, user_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserDataResponse]:
        """
        Получение данных о пользователе с помощью его id

        Parameters
        ----------
        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserDataResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/info",
            method="GET",
            params={
                "user_id": user_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserDataResponse,
                    parse_obj_as(
                        type_=UserDataResponse,
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

    def create_user(
        self,
        *,
        authorization: str,
        first_name: str,
        last_name: str,
        gender: GenderValue,
        birthday: dt.date,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UserDataResponse]:
        """
        Создание пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        first_name : str
            Имя пользователя

        last_name : str
            Фамилия пользователя

        gender : GenderValue
            Пол пользователя

        birthday : dt.date
            Дата рождения

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserDataResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/create_user",
            method="POST",
            json={
                "first_name": first_name,
                "last_name": last_name,
                "gender": gender,
                "birthday": birthday,
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
                    UserDataResponse,
                    parse_obj_as(
                        type_=UserDataResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def update_user_info(
        self,
        *,
        authorization: str,
        first_name: typing.Optional[UpdateUserRequestFirstName] = OMIT,
        last_name: typing.Optional[UpdateUserRequestLastName] = OMIT,
        gender: typing.Optional[UpdateUserRequestGender] = OMIT,
        birthday: typing.Optional[UpdateUserRequestBirthday] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UserDataResponse]:
        """
        Обновление данных пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        first_name : typing.Optional[UpdateUserRequestFirstName]
            Имя

        last_name : typing.Optional[UpdateUserRequestLastName]
            Фамилия

        gender : typing.Optional[UpdateUserRequestGender]
            Пол

        birthday : typing.Optional[UpdateUserRequestBirthday]
            Дата

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserDataResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/update_user_info",
            method="PATCH",
            json={
                "first_name": convert_and_respect_annotation_metadata(
                    object_=first_name, annotation=UpdateUserRequestFirstName, direction="write"
                ),
                "last_name": convert_and_respect_annotation_metadata(
                    object_=last_name, annotation=UpdateUserRequestLastName, direction="write"
                ),
                "gender": convert_and_respect_annotation_metadata(
                    object_=gender, annotation=UpdateUserRequestGender, direction="write"
                ),
                "birthday": convert_and_respect_annotation_metadata(
                    object_=birthday, annotation=UpdateUserRequestBirthday, direction="write"
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
                    UserDataResponse,
                    parse_obj_as(
                        type_=UserDataResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def delete_user(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeletedUserResponse]:
        """
        Удаление пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeletedUserResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/delete_user",
            method="DELETE",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletedUserResponse,
                    parse_obj_as(
                        type_=DeletedUserResponse,
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


class AsyncRawUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_user(
        self, *, user_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserDataResponse]:
        """
        Получение данных о пользователе с помощью его id

        Parameters
        ----------
        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserDataResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/info",
            method="GET",
            params={
                "user_id": user_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserDataResponse,
                    parse_obj_as(
                        type_=UserDataResponse,
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

    async def create_user(
        self,
        *,
        authorization: str,
        first_name: str,
        last_name: str,
        gender: GenderValue,
        birthday: dt.date,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UserDataResponse]:
        """
        Создание пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        first_name : str
            Имя пользователя

        last_name : str
            Фамилия пользователя

        gender : GenderValue
            Пол пользователя

        birthday : dt.date
            Дата рождения

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserDataResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/create_user",
            method="POST",
            json={
                "first_name": first_name,
                "last_name": last_name,
                "gender": gender,
                "birthday": birthday,
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
                    UserDataResponse,
                    parse_obj_as(
                        type_=UserDataResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def update_user_info(
        self,
        *,
        authorization: str,
        first_name: typing.Optional[UpdateUserRequestFirstName] = OMIT,
        last_name: typing.Optional[UpdateUserRequestLastName] = OMIT,
        gender: typing.Optional[UpdateUserRequestGender] = OMIT,
        birthday: typing.Optional[UpdateUserRequestBirthday] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UserDataResponse]:
        """
        Обновление данных пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        first_name : typing.Optional[UpdateUserRequestFirstName]
            Имя

        last_name : typing.Optional[UpdateUserRequestLastName]
            Фамилия

        gender : typing.Optional[UpdateUserRequestGender]
            Пол

        birthday : typing.Optional[UpdateUserRequestBirthday]
            Дата

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserDataResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/update_user_info",
            method="PATCH",
            json={
                "first_name": convert_and_respect_annotation_metadata(
                    object_=first_name, annotation=UpdateUserRequestFirstName, direction="write"
                ),
                "last_name": convert_and_respect_annotation_metadata(
                    object_=last_name, annotation=UpdateUserRequestLastName, direction="write"
                ),
                "gender": convert_and_respect_annotation_metadata(
                    object_=gender, annotation=UpdateUserRequestGender, direction="write"
                ),
                "birthday": convert_and_respect_annotation_metadata(
                    object_=birthday, annotation=UpdateUserRequestBirthday, direction="write"
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
                    UserDataResponse,
                    parse_obj_as(
                        type_=UserDataResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def delete_user(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeletedUserResponse]:
        """
        Удаление пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeletedUserResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/delete_user",
            method="DELETE",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletedUserResponse,
                    parse_obj_as(
                        type_=DeletedUserResponse,
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
