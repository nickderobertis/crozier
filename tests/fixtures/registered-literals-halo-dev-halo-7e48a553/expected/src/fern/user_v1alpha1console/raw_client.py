

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.detailed_user import DetailedUser
from ..types.metadata import Metadata
from ..types.user import User
from ..types.user_endpoint_listed_user_list import UserEndpointListedUserList
from ..types.user_permission import UserPermission
from ..types.user_spec import UserSpec
from ..types.user_status import UserStatus
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUserV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_users(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        keyword: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UserEndpointListedUserList]:
        """
        List users

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        keyword : typing.Optional[str]
            Keyword to search

        role : typing.Optional[str]
            Role metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserEndpointListedUserList]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/users",
            method="GET",
            params={
                "page": page,
                "size": size,
                "labelSelector": label_selector,
                "fieldSelector": field_selector,
                "sort": sort,
                "keyword": keyword,
                "role": role,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserEndpointListedUserList,
                    parse_obj_as(
                        type_=UserEndpointListedUserList,
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

    def create_user(
        self,
        *,
        email: str,
        name: str,
        annotations: typing.Optional[typing.Dict[str, str]] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        bio: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[User]:
        """
        Creates a new user.

        Parameters
        ----------
        email : str
            email address of the user

        name : str
            user <code>metadata.name</code>, which also serves as the login name

        annotations : typing.Optional[typing.Dict[str, str]]
            metadata annotations to set on the user

        avatar : typing.Optional[str]
            avatar URL of the user

        bio : typing.Optional[str]
            biography or profile text of the user

        display_name : typing.Optional[str]
            display name shown in the console and theme

        password : typing.Optional[str]
            raw password to set for the user

        phone : typing.Optional[str]
            phone number of the user

        roles : typing.Optional[typing.Sequence[str]]
            role <code>metadata.name</code> values to grant to the user after creation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/users",
            method="POST",
            json={
                "annotations": annotations,
                "avatar": avatar,
                "bio": bio,
                "displayName": display_name,
                "email": email,
                "name": name,
                "password": password,
                "phone": phone,
                "roles": roles,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_current_user_detail(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DetailedUser]:
        """
        Get current user detail

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DetailedUser]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/users/-",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DetailedUser,
                    parse_obj_as(
                        type_=DetailedUser,
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

    def update_current_user(
        self,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: UserSpec,
        status: typing.Optional[UserStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[User]:
        """
        Update current user profile, but password.

        Parameters
        ----------
        api_version : str

        kind : str

        metadata : Metadata

        spec : UserSpec

        status : typing.Optional[UserStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/users/-",
            method="PUT",
            json={
                "apiVersion": api_version,
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=Metadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(object_=spec, annotation=UserSpec, direction="write"),
                "status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=UserStatus, direction="write"
                ),
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def change_own_password(
        self, *, old_password: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[User]:
        """
        Change own password of user.

        Parameters
        ----------
        old_password : str
            old password

        password : str
            new password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/users/-/password",
            method="PUT",
            json={
                "oldPassword": old_password,
                "password": password,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def send_email_verification_code(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Send email verification code for user

        Parameters
        ----------
        email : str
            email address to verify

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/users/-/send-email-verification-code",
            method="POST",
            json={
                "email": email,
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

    def verify_email(
        self, *, code: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Verify email for user by code.

        Parameters
        ----------
        code : str
            email verification code

        password : str
            current password of the authenticated user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/users/-/verify-email",
            method="POST",
            json={
                "code": code,
                "password": password,
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

    def get_user_detail(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DetailedUser]:
        """
        Get user detail by metadata.name

        Parameters
        ----------
        name : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DetailedUser]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/users/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DetailedUser,
                    parse_obj_as(
                        type_=DetailedUser,
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

    def upload_user_avatar(
        self, name: str, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[User]:
        """
        upload user avatar

        Parameters
        ----------
        name : str
            User metadata.name

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/users/{encode_path_param(name)}/avatar",
            method="POST",
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_user_avatar(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[User]:
        """
        delete user avatar

        Parameters
        ----------
        name : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/users/{encode_path_param(name)}/avatar",
            method="DELETE",
            request_options=request_options,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def change_anyone_password(
        self, name: str, *, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[User]:
        """
        Change anyone password of user for admin.

        Parameters
        ----------
        name : str
            User metadata.name. If the name is equal to '-', it will change the password of current user.

        password : str
            new password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/users/{encode_path_param(name)}/password",
            method="PUT",
            json={
                "password": password,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_permissions(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserPermission]:
        """
        Get permissions of user

        Parameters
        ----------
        name : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserPermission]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/users/{encode_path_param(name)}/permissions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserPermission,
                    parse_obj_as(
                        type_=UserPermission,
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

    def grant_permission(
        self, name: str, *, roles: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[User]:
        """
        Grant permissions to user

        Parameters
        ----------
        name : str
            User metadata.name

        roles : typing.Sequence[str]
            role <code>metadata.name</code> values to grant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/users/{encode_path_param(name)}/permissions",
            method="POST",
            json={
                "roles": roles,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def disable_user(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[User]:
        """
        Disable user by metadata.name

        Parameters
        ----------
        username : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            The user has been disabled.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/console.api.security.halo.run/v1alpha1/users/{encode_path_param(username)}/disable",
            method="POST",
            request_options=request_options,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def enable_user(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[User]:
        """
        Enable user by metadata.name

        Parameters
        ----------
        username : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            The user has been enabled.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/console.api.security.halo.run/v1alpha1/users/{encode_path_param(username)}/enable",
            method="POST",
            request_options=request_options,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawUserV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_users(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        keyword: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UserEndpointListedUserList]:
        """
        List users

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        keyword : typing.Optional[str]
            Keyword to search

        role : typing.Optional[str]
            Role metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserEndpointListedUserList]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/users",
            method="GET",
            params={
                "page": page,
                "size": size,
                "labelSelector": label_selector,
                "fieldSelector": field_selector,
                "sort": sort,
                "keyword": keyword,
                "role": role,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserEndpointListedUserList,
                    parse_obj_as(
                        type_=UserEndpointListedUserList,
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

    async def create_user(
        self,
        *,
        email: str,
        name: str,
        annotations: typing.Optional[typing.Dict[str, str]] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        bio: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        roles: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[User]:
        """
        Creates a new user.

        Parameters
        ----------
        email : str
            email address of the user

        name : str
            user <code>metadata.name</code>, which also serves as the login name

        annotations : typing.Optional[typing.Dict[str, str]]
            metadata annotations to set on the user

        avatar : typing.Optional[str]
            avatar URL of the user

        bio : typing.Optional[str]
            biography or profile text of the user

        display_name : typing.Optional[str]
            display name shown in the console and theme

        password : typing.Optional[str]
            raw password to set for the user

        phone : typing.Optional[str]
            phone number of the user

        roles : typing.Optional[typing.Sequence[str]]
            role <code>metadata.name</code> values to grant to the user after creation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/users",
            method="POST",
            json={
                "annotations": annotations,
                "avatar": avatar,
                "bio": bio,
                "displayName": display_name,
                "email": email,
                "name": name,
                "password": password,
                "phone": phone,
                "roles": roles,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_current_user_detail(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DetailedUser]:
        """
        Get current user detail

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DetailedUser]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/users/-",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DetailedUser,
                    parse_obj_as(
                        type_=DetailedUser,
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

    async def update_current_user(
        self,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: UserSpec,
        status: typing.Optional[UserStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[User]:
        """
        Update current user profile, but password.

        Parameters
        ----------
        api_version : str

        kind : str

        metadata : Metadata

        spec : UserSpec

        status : typing.Optional[UserStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/users/-",
            method="PUT",
            json={
                "apiVersion": api_version,
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=Metadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(object_=spec, annotation=UserSpec, direction="write"),
                "status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=UserStatus, direction="write"
                ),
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def change_own_password(
        self, *, old_password: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[User]:
        """
        Change own password of user.

        Parameters
        ----------
        old_password : str
            old password

        password : str
            new password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/users/-/password",
            method="PUT",
            json={
                "oldPassword": old_password,
                "password": password,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def send_email_verification_code(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Send email verification code for user

        Parameters
        ----------
        email : str
            email address to verify

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/users/-/send-email-verification-code",
            method="POST",
            json={
                "email": email,
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

    async def verify_email(
        self, *, code: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Verify email for user by code.

        Parameters
        ----------
        code : str
            email verification code

        password : str
            current password of the authenticated user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/users/-/verify-email",
            method="POST",
            json={
                "code": code,
                "password": password,
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

    async def get_user_detail(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DetailedUser]:
        """
        Get user detail by metadata.name

        Parameters
        ----------
        name : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DetailedUser]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/users/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DetailedUser,
                    parse_obj_as(
                        type_=DetailedUser,
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

    async def upload_user_avatar(
        self, name: str, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[User]:
        """
        upload user avatar

        Parameters
        ----------
        name : str
            User metadata.name

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/users/{encode_path_param(name)}/avatar",
            method="POST",
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_user_avatar(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[User]:
        """
        delete user avatar

        Parameters
        ----------
        name : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/users/{encode_path_param(name)}/avatar",
            method="DELETE",
            request_options=request_options,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def change_anyone_password(
        self, name: str, *, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[User]:
        """
        Change anyone password of user for admin.

        Parameters
        ----------
        name : str
            User metadata.name. If the name is equal to '-', it will change the password of current user.

        password : str
            new password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/users/{encode_path_param(name)}/password",
            method="PUT",
            json={
                "password": password,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_permissions(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserPermission]:
        """
        Get permissions of user

        Parameters
        ----------
        name : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserPermission]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/users/{encode_path_param(name)}/permissions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserPermission,
                    parse_obj_as(
                        type_=UserPermission,
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

    async def grant_permission(
        self, name: str, *, roles: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[User]:
        """
        Grant permissions to user

        Parameters
        ----------
        name : str
            User metadata.name

        roles : typing.Sequence[str]
            role <code>metadata.name</code> values to grant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/users/{encode_path_param(name)}/permissions",
            method="POST",
            json={
                "roles": roles,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def disable_user(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[User]:
        """
        Disable user by metadata.name

        Parameters
        ----------
        username : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            The user has been disabled.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/console.api.security.halo.run/v1alpha1/users/{encode_path_param(username)}/disable",
            method="POST",
            request_options=request_options,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def enable_user(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[User]:
        """
        Enable user by metadata.name

        Parameters
        ----------
        username : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            The user has been enabled.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/console.api.security.halo.run/v1alpha1/users/{encode_path_param(username)}/enable",
            method="POST",
            request_options=request_options,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
