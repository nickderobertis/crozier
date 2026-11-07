

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
from ..errors.not_found_error import NotFoundError
from ..types.error import Error
from ..types.users import Users
from ..types.users_upsert_confirmation import UsersUpsertConfirmation
from ..types.userss import Userss
from ..types.where import Where
from .types.delete_users_response import DeleteUsersResponse
from .types.patch_users_response import PatchUsersResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def find_paginated_users(
        self,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Userss]:
        """
        Find paginated Users

        Parameters
        ----------
        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Userss]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Userss,
                    parse_obj_as(
                        type_=Userss,
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

    def create_a_new_user(
        self,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        email: typing.Optional[str] = OMIT,
        reset_password_token: typing.Optional[str] = OMIT,
        reset_password_expiration: typing.Optional[str] = OMIT,
        salt: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        login_attempts: typing.Optional[float] = OMIT,
        lock_until: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UsersUpsertConfirmation]:
        """
        Create a new User

        Parameters
        ----------
        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        email : typing.Optional[str]

        reset_password_token : typing.Optional[str]

        reset_password_expiration : typing.Optional[str]

        salt : typing.Optional[str]

        hash : typing.Optional[str]

        login_attempts : typing.Optional[float]

        lock_until : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UsersUpsertConfirmation]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="POST",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            json={
                "id": id,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "email": email,
                "resetPasswordToken": reset_password_token,
                "resetPasswordExpiration": reset_password_expiration,
                "salt": salt,
                "hash": hash,
                "loginAttempts": login_attempts,
                "lockUntil": lock_until,
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
                    UsersUpsertConfirmation,
                    parse_obj_as(
                        type_=UsersUpsertConfirmation,
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

    def delete_multiple_users(
        self,
        *,
        where: Where,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteUsersResponse]:
        """
        Delete all Users matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteUsersResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="DELETE",
            params={
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteUsersResponse,
                    parse_obj_as(
                        type_=DeleteUsersResponse,
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

    def update_multiple_users(
        self,
        *,
        where: Where,
        id: str,
        updated_at: str,
        created_at: str,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        email: typing.Optional[str] = OMIT,
        reset_password_token: typing.Optional[str] = OMIT,
        reset_password_expiration: typing.Optional[str] = OMIT,
        salt: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        login_attempts: typing.Optional[float] = OMIT,
        lock_until: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PatchUsersResponse]:
        """
        Update all Users matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        id : str

        updated_at : str

        created_at : str

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        email : typing.Optional[str]

        reset_password_token : typing.Optional[str]

        reset_password_expiration : typing.Optional[str]

        salt : typing.Optional[str]

        hash : typing.Optional[str]

        login_attempts : typing.Optional[float]

        lock_until : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PatchUsersResponse]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="PATCH",
            params={
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            json={
                "id": id,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "email": email,
                "resetPasswordToken": reset_password_token,
                "resetPasswordExpiration": reset_password_expiration,
                "salt": salt,
                "hash": hash,
                "loginAttempts": login_attempts,
                "lockUntil": lock_until,
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
                    PatchUsersResponse,
                    parse_obj_as(
                        type_=PatchUsersResponse,
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

    def get_a_single_user_by_its_id(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Users]:
        """
        Get a single User by its id

        Parameters
        ----------
        id : str
            id of the User

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Users]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id)}",
            method="GET",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Users,
                    parse_obj_as(
                        type_=Users,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def deletes_an_existing_user(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UsersUpsertConfirmation]:
        """
        Deletes an existing User

        Parameters
        ----------
        id : str
            id of the User

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UsersUpsertConfirmation]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id)}",
            method="DELETE",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersUpsertConfirmation,
                    parse_obj_as(
                        type_=UsersUpsertConfirmation,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def updates_a_user(
        self,
        id_: str,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        email: typing.Optional[str] = OMIT,
        reset_password_token: typing.Optional[str] = OMIT,
        reset_password_expiration: typing.Optional[str] = OMIT,
        salt: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        login_attempts: typing.Optional[float] = OMIT,
        lock_until: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UsersUpsertConfirmation]:
        """
        Updates a User

        Parameters
        ----------
        id_ : str
            id of the User

        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        email : typing.Optional[str]

        reset_password_token : typing.Optional[str]

        reset_password_expiration : typing.Optional[str]

        salt : typing.Optional[str]

        hash : typing.Optional[str]

        login_attempts : typing.Optional[float]

        lock_until : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UsersUpsertConfirmation]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            json={
                "id": id,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "email": email,
                "resetPasswordToken": reset_password_token,
                "resetPasswordExpiration": reset_password_expiration,
                "salt": salt,
                "hash": hash,
                "loginAttempts": login_attempts,
                "lockUntil": lock_until,
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
                    UsersUpsertConfirmation,
                    parse_obj_as(
                        type_=UsersUpsertConfirmation,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def find_paginated_users(
        self,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Userss]:
        """
        Find paginated Users

        Parameters
        ----------
        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Userss]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Userss,
                    parse_obj_as(
                        type_=Userss,
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

    async def create_a_new_user(
        self,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        email: typing.Optional[str] = OMIT,
        reset_password_token: typing.Optional[str] = OMIT,
        reset_password_expiration: typing.Optional[str] = OMIT,
        salt: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        login_attempts: typing.Optional[float] = OMIT,
        lock_until: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UsersUpsertConfirmation]:
        """
        Create a new User

        Parameters
        ----------
        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        email : typing.Optional[str]

        reset_password_token : typing.Optional[str]

        reset_password_expiration : typing.Optional[str]

        salt : typing.Optional[str]

        hash : typing.Optional[str]

        login_attempts : typing.Optional[float]

        lock_until : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UsersUpsertConfirmation]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="POST",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            json={
                "id": id,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "email": email,
                "resetPasswordToken": reset_password_token,
                "resetPasswordExpiration": reset_password_expiration,
                "salt": salt,
                "hash": hash,
                "loginAttempts": login_attempts,
                "lockUntil": lock_until,
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
                    UsersUpsertConfirmation,
                    parse_obj_as(
                        type_=UsersUpsertConfirmation,
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

    async def delete_multiple_users(
        self,
        *,
        where: Where,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteUsersResponse]:
        """
        Delete all Users matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteUsersResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="DELETE",
            params={
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteUsersResponse,
                    parse_obj_as(
                        type_=DeleteUsersResponse,
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

    async def update_multiple_users(
        self,
        *,
        where: Where,
        id: str,
        updated_at: str,
        created_at: str,
        sort: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        email: typing.Optional[str] = OMIT,
        reset_password_token: typing.Optional[str] = OMIT,
        reset_password_expiration: typing.Optional[str] = OMIT,
        salt: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        login_attempts: typing.Optional[float] = OMIT,
        lock_until: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PatchUsersResponse]:
        """
        Update all Users matching the where query

        Parameters
        ----------
        where : Where
            pass a where query to constrain returned documents (complex type, see documentation)

        id : str

        updated_at : str

        created_at : str

        sort : typing.Optional[str]
            sort by field

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        email : typing.Optional[str]

        reset_password_token : typing.Optional[str]

        reset_password_expiration : typing.Optional[str]

        salt : typing.Optional[str]

        hash : typing.Optional[str]

        login_attempts : typing.Optional[float]

        lock_until : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PatchUsersResponse]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="PATCH",
            params={
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            json={
                "id": id,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "email": email,
                "resetPasswordToken": reset_password_token,
                "resetPasswordExpiration": reset_password_expiration,
                "salt": salt,
                "hash": hash,
                "loginAttempts": login_attempts,
                "lockUntil": lock_until,
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
                    PatchUsersResponse,
                    parse_obj_as(
                        type_=PatchUsersResponse,
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

    async def get_a_single_user_by_its_id(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        sort: typing.Optional[str] = None,
        where: typing.Optional[Where] = None,
        limit: typing.Optional[float] = None,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Users]:
        """
        Get a single User by its id

        Parameters
        ----------
        id : str
            id of the User

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        sort : typing.Optional[str]
            sort by field

        where : typing.Optional[Where]
            pass a where query to constrain returned documents (complex type, see documentation)

        limit : typing.Optional[float]
            limit the returned documents to a certain number

        page : typing.Optional[float]
            get a specific page of documents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Users]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id)}",
            method="GET",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
                "sort": sort,
                "where": convert_and_respect_annotation_metadata(object_=where, annotation=Where, direction="write"),
                "limit": limit,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Users,
                    parse_obj_as(
                        type_=Users,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def deletes_an_existing_user(
        self,
        id: str,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UsersUpsertConfirmation]:
        """
        Deletes an existing User

        Parameters
        ----------
        id : str
            id of the User

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UsersUpsertConfirmation]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id)}",
            method="DELETE",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersUpsertConfirmation,
                    parse_obj_as(
                        type_=UsersUpsertConfirmation,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def updates_a_user(
        self,
        id_: str,
        *,
        id: str,
        updated_at: str,
        created_at: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        email: typing.Optional[str] = OMIT,
        reset_password_token: typing.Optional[str] = OMIT,
        reset_password_expiration: typing.Optional[str] = OMIT,
        salt: typing.Optional[str] = OMIT,
        hash: typing.Optional[str] = OMIT,
        login_attempts: typing.Optional[float] = OMIT,
        lock_until: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UsersUpsertConfirmation]:
        """
        Updates a User

        Parameters
        ----------
        id_ : str
            id of the User

        id : str

        updated_at : str

        created_at : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        email : typing.Optional[str]

        reset_password_token : typing.Optional[str]

        reset_password_expiration : typing.Optional[str]

        salt : typing.Optional[str]

        hash : typing.Optional[str]

        login_attempts : typing.Optional[float]

        lock_until : typing.Optional[str]

        password : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UsersUpsertConfirmation]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            json={
                "id": id,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "email": email,
                "resetPasswordToken": reset_password_token,
                "resetPasswordExpiration": reset_password_expiration,
                "salt": salt,
                "hash": hash,
                "loginAttempts": login_attempts,
                "lockUntil": lock_until,
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
                    UsersUpsertConfirmation,
                    parse_obj_as(
                        type_=UsersUpsertConfirmation,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
