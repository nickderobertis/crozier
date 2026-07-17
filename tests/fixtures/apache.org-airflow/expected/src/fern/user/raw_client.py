

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
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.role import Role
from ..types.user import User
from ..types.user_collection import UserCollection
from ..types.user_collection_item import UserCollectionItem
from ..types.user_collection_item_roles_item import UserCollectionItemRolesItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_users(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UserCollection]:
        """
        Get a list of users.

        *New in version 2.1.0*

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserCollection]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserCollection,
                    parse_obj_as(
                        type_=UserCollection,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def post_user(
        self,
        *,
        password: typing.Optional[str] = OMIT,
        active: typing.Optional[bool] = OMIT,
        changed_on: typing.Optional[str] = OMIT,
        created_on: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        failed_login_count: typing.Optional[int] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_login: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[User]:
        """
        Create a new user with unique username and email.

        *New in version 2.2.0*

        Parameters
        ----------
        password : typing.Optional[str]

        active : typing.Optional[bool]
            Whether the user is active

        changed_on : typing.Optional[str]
            The date user was changed

        created_on : typing.Optional[str]
            The date user was created

        email : typing.Optional[str]
            The user's email.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        failed_login_count : typing.Optional[int]
            The number of times the login failed

        first_name : typing.Optional[str]
            The user's first name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        last_login : typing.Optional[str]
            The last user login

        last_name : typing.Optional[str]
            The user's last name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        login_count : typing.Optional[int]
            The login count

        roles : typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]]
            User roles.

            *Changed in version 2.2.0*&#58; Field is no longer read-only.

        username : typing.Optional[str]
            The username.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="POST",
            json={
                "password": password,
                "active": active,
                "changed_on": changed_on,
                "created_on": created_on,
                "email": email,
                "failed_login_count": failed_login_count,
                "first_name": first_name,
                "last_login": last_login,
                "last_name": last_name,
                "login_count": login_count,
                "roles": convert_and_respect_annotation_metadata(
                    object_=roles,
                    annotation=typing.Sequence[typing.Optional[UserCollectionItemRolesItem]],
                    direction="write",
                ),
                "username": username,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    User,
                    parse_obj_as(
                        type_=User,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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

    def get_user(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserCollectionItem]:
        """
        Get a user with a specific username.

        *New in version 2.1.0*

        Parameters
        ----------
        username : str
            The username of the user.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserCollectionItem]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(username)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserCollectionItem,
                    parse_obj_as(
                        type_=UserCollectionItem,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def delete_user(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a user with a specific username.

        *New in version 2.2.0*

        Parameters
        ----------
        username : str
            The username of the user.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(username)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def patch_user(
        self,
        username_: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        password: typing.Optional[str] = OMIT,
        active: typing.Optional[bool] = OMIT,
        changed_on: typing.Optional[str] = OMIT,
        created_on: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        failed_login_count: typing.Optional[int] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_login: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Role]:
        """
        Update fields for a user.

        *New in version 2.2.0*

        Parameters
        ----------
        username_ : str
            The username of the user.

            *New in version 2.1.0*

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        password : typing.Optional[str]

        active : typing.Optional[bool]
            Whether the user is active

        changed_on : typing.Optional[str]
            The date user was changed

        created_on : typing.Optional[str]
            The date user was created

        email : typing.Optional[str]
            The user's email.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        failed_login_count : typing.Optional[int]
            The number of times the login failed

        first_name : typing.Optional[str]
            The user's first name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        last_login : typing.Optional[str]
            The last user login

        last_name : typing.Optional[str]
            The user's last name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        login_count : typing.Optional[int]
            The login count

        roles : typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]]
            User roles.

            *Changed in version 2.2.0*&#58; Field is no longer read-only.

        username : typing.Optional[str]
            The username.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Role]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(username_)}",
            method="PATCH",
            params={
                "update_mask": ",".join(map(str, update_mask))
                if isinstance(update_mask, (list, tuple, set))
                else update_mask,
            },
            json={
                "password": password,
                "active": active,
                "changed_on": changed_on,
                "created_on": created_on,
                "email": email,
                "failed_login_count": failed_login_count,
                "first_name": first_name,
                "last_login": last_login,
                "last_name": last_name,
                "login_count": login_count,
                "roles": convert_and_respect_annotation_metadata(
                    object_=roles,
                    annotation=typing.Sequence[typing.Optional[UserCollectionItemRolesItem]],
                    direction="write",
                ),
                "username": username,
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
                    Role,
                    parse_obj_as(
                        type_=Role,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
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


class AsyncRawUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_users(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UserCollection]:
        """
        Get a list of users.

        *New in version 2.1.0*

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserCollection]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserCollection,
                    parse_obj_as(
                        type_=UserCollection,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def post_user(
        self,
        *,
        password: typing.Optional[str] = OMIT,
        active: typing.Optional[bool] = OMIT,
        changed_on: typing.Optional[str] = OMIT,
        created_on: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        failed_login_count: typing.Optional[int] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_login: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[User]:
        """
        Create a new user with unique username and email.

        *New in version 2.2.0*

        Parameters
        ----------
        password : typing.Optional[str]

        active : typing.Optional[bool]
            Whether the user is active

        changed_on : typing.Optional[str]
            The date user was changed

        created_on : typing.Optional[str]
            The date user was created

        email : typing.Optional[str]
            The user's email.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        failed_login_count : typing.Optional[int]
            The number of times the login failed

        first_name : typing.Optional[str]
            The user's first name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        last_login : typing.Optional[str]
            The last user login

        last_name : typing.Optional[str]
            The user's last name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        login_count : typing.Optional[int]
            The login count

        roles : typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]]
            User roles.

            *Changed in version 2.2.0*&#58; Field is no longer read-only.

        username : typing.Optional[str]
            The username.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="POST",
            json={
                "password": password,
                "active": active,
                "changed_on": changed_on,
                "created_on": created_on,
                "email": email,
                "failed_login_count": failed_login_count,
                "first_name": first_name,
                "last_login": last_login,
                "last_name": last_name,
                "login_count": login_count,
                "roles": convert_and_respect_annotation_metadata(
                    object_=roles,
                    annotation=typing.Sequence[typing.Optional[UserCollectionItemRolesItem]],
                    direction="write",
                ),
                "username": username,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    User,
                    parse_obj_as(
                        type_=User,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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

    async def get_user(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserCollectionItem]:
        """
        Get a user with a specific username.

        *New in version 2.1.0*

        Parameters
        ----------
        username : str
            The username of the user.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserCollectionItem]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(username)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserCollectionItem,
                    parse_obj_as(
                        type_=UserCollectionItem,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def delete_user(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a user with a specific username.

        *New in version 2.2.0*

        Parameters
        ----------
        username : str
            The username of the user.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(username)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def patch_user(
        self,
        username_: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        password: typing.Optional[str] = OMIT,
        active: typing.Optional[bool] = OMIT,
        changed_on: typing.Optional[str] = OMIT,
        created_on: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        failed_login_count: typing.Optional[int] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_login: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        login_count: typing.Optional[int] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Role]:
        """
        Update fields for a user.

        *New in version 2.2.0*

        Parameters
        ----------
        username_ : str
            The username of the user.

            *New in version 2.1.0*

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        password : typing.Optional[str]

        active : typing.Optional[bool]
            Whether the user is active

        changed_on : typing.Optional[str]
            The date user was changed

        created_on : typing.Optional[str]
            The date user was created

        email : typing.Optional[str]
            The user's email.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        failed_login_count : typing.Optional[int]
            The number of times the login failed

        first_name : typing.Optional[str]
            The user's first name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        last_login : typing.Optional[str]
            The last user login

        last_name : typing.Optional[str]
            The user's last name.

            *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed.

        login_count : typing.Optional[int]
            The login count

        roles : typing.Optional[typing.Sequence[typing.Optional[UserCollectionItemRolesItem]]]
            User roles.

            *Changed in version 2.2.0*&#58; Field is no longer read-only.

        username : typing.Optional[str]
            The username.

            *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Role]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(username_)}",
            method="PATCH",
            params={
                "update_mask": ",".join(map(str, update_mask))
                if isinstance(update_mask, (list, tuple, set))
                else update_mask,
            },
            json={
                "password": password,
                "active": active,
                "changed_on": changed_on,
                "created_on": created_on,
                "email": email,
                "failed_login_count": failed_login_count,
                "first_name": first_name,
                "last_login": last_login,
                "last_name": last_name,
                "login_count": login_count,
                "roles": convert_and_respect_annotation_metadata(
                    object_=roles,
                    annotation=typing.Sequence[typing.Optional[UserCollectionItemRolesItem]],
                    direction="write",
                ),
                "username": username,
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
                    Role,
                    parse_obj_as(
                        type_=Role,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
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
