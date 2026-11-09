

import datetime as dt
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
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.analysis import Analysis
from ..types.info import Info
from ..types.token_request_token_scope import TokenRequestTokenScope
from ..types.user import User
from ..types.user_access_level import UserAccessLevel
from .types.create_rest_api_token_response import CreateRestApiTokenResponse
from .types.create_user_request_default_visibility import CreateUserRequestDefaultVisibility
from .types.get_self_response import GetSelfResponse
from .types.get_tokens_by_type_request_type import GetTokensByTypeRequestType
from .types.get_tokens_by_type_response import GetTokensByTypeResponse
from .types.modify_user_by_id_request_default_visibility import ModifyUserByIdRequestDefaultVisibility
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_users(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.List[User]]:
        """
        Get the registered users

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[User]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[User],
                    parse_obj_as(
                        type_=typing.List[User],
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
        name: str,
        id: int,
        user_pass: typing.Optional[str] = OMIT,
        default_visibility: typing.Optional[CreateUserRequestDefaultVisibility] = OMIT,
        description: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        access_level: typing.Optional[UserAccessLevel] = OMIT,
        root_folder_id: typing.Optional[float] = OMIT,
        email_notification: typing.Optional[bool] = OMIT,
        default_group: typing.Optional[int] = OMIT,
        agents: typing.Optional[Analysis] = OMIT,
        default_bucketpool: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Create a new user

        Parameters
        ----------
        name : str
            Unique username

        id : int
            ID of the user

        user_pass : typing.Optional[str]

        default_visibility : typing.Optional[CreateUserRequestDefaultVisibility]

        description : typing.Optional[str]
            Description of the user

        email : typing.Optional[str]
            Email of the user, needs to be unique and is required

        access_level : typing.Optional[UserAccessLevel]

        root_folder_id : typing.Optional[float]
            root folder id of the user

        email_notification : typing.Optional[bool]
            enable email notification when upload scan completes

        default_group : typing.Optional[int]
            Default group id of the user

        agents : typing.Optional[Analysis]

        default_bucketpool : typing.Optional[int]
            Default bucket pool id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            User created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="POST",
            json={
                "name": name,
                "user_pass": user_pass,
                "defaultVisibility": default_visibility,
                "id": id,
                "description": description,
                "email": email,
                "accessLevel": access_level,
                "rootFolderId": root_folder_id,
                "emailNotification": email_notification,
                "defaultGroup": default_group,
                "agents": convert_and_respect_annotation_metadata(
                    object_=agents, annotation=Analysis, direction="write"
                ),
                "defaultBucketpool": default_bucketpool,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_user_by_id(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[User]:
        """
        Get one single user by id

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            User with the given id
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id)}",
            method="GET",
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

    def modify_user_by_id(
        self,
        id_path_param: int,
        *,
        id: int,
        user_pass: typing.Optional[str] = OMIT,
        default_folder_id: typing.Optional[int] = OMIT,
        default_visibility: typing.Optional[ModifyUserByIdRequestDefaultVisibility] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        access_level: typing.Optional[UserAccessLevel] = OMIT,
        root_folder_id: typing.Optional[float] = OMIT,
        email_notification: typing.Optional[bool] = OMIT,
        default_group: typing.Optional[int] = OMIT,
        agents: typing.Optional[Analysis] = OMIT,
        default_bucketpool: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Edit user details by id

        Parameters
        ----------
        id_path_param : int

        id : int
            ID of the user

        user_pass : typing.Optional[str]

        default_folder_id : typing.Optional[int]

        default_visibility : typing.Optional[ModifyUserByIdRequestDefaultVisibility]

        name : typing.Optional[str]
            Unique username

        description : typing.Optional[str]
            Description of the user

        email : typing.Optional[str]
            Email of the user, needs to be unique and is required

        access_level : typing.Optional[UserAccessLevel]

        root_folder_id : typing.Optional[float]
            root folder id of the user

        email_notification : typing.Optional[bool]
            enable email notification when upload scan completes

        default_group : typing.Optional[int]
            Default group id of the user

        agents : typing.Optional[Analysis]

        default_bucketpool : typing.Optional[int]
            Default bucket pool id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            User updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id_path_param)}",
            method="PUT",
            json={
                "user_pass": user_pass,
                "defaultFolderId": default_folder_id,
                "defaultVisibility": default_visibility,
                "id": id,
                "name": name,
                "description": description,
                "email": email,
                "accessLevel": access_level,
                "rootFolderId": root_folder_id,
                "emailNotification": email_notification,
                "defaultGroup": default_group,
                "agents": convert_and_respect_annotation_metadata(
                    object_=agents, annotation=Analysis, direction="write"
                ),
                "defaultBucketpool": default_bucketpool,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def delete_user_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Delete a single user by id

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            User will be deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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

    def get_self(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[GetSelfResponse]:
        """
        Get the information about logged in user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSelfResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/self",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSelfResponse,
                    parse_obj_as(
                        type_=GetSelfResponse,
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

    def create_rest_api_token(
        self,
        *,
        token_name: str,
        token_scope: TokenRequestTokenScope,
        token_expire: dt.date,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateRestApiTokenResponse]:
        """
        Create a new REST API Token

        Parameters
        ----------
        token_name : str
            Friendly name of the token

        token_scope : TokenRequestTokenScope
            The scope of the token.

        token_expire : dt.date
            Date when the token must expire (default max 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateRestApiTokenResponse]
            Token created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/tokens",
            method="POST",
            data={
                "token_name": token_name,
                "token_scope": token_scope,
                "token_expire": token_expire,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateRestApiTokenResponse,
                    parse_obj_as(
                        type_=CreateRestApiTokenResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_tokens_by_type(
        self, type: GetTokensByTypeRequestType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetTokensByTypeResponse]:
        """
        Get all the REST API tokens (active | expired)

        Parameters
        ----------
        type : GetTokensByTypeRequestType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTokensByTypeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/tokens/{encode_path_param(type)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTokensByTypeResponse,
                    parse_obj_as(
                        type_=GetTokensByTypeResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_permission_by_group_id_and_user_id(
        self,
        id: int,
        user_id: int,
        *,
        perm: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Update User's permission in group.

        Parameters
        ----------
        id : int
            Id of the group

        user_id : int
            user id of the member

        perm : typing.Optional[int]
            New user permission in the group.
            0: User
            1: Admin
            2: Advisor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            User's permission will be updated.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/user/{encode_path_param(user_id)}",
            method="PUT",
            json={
                "perm": perm,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[User]]:
        """
        Get the registered users

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[User]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[User],
                    parse_obj_as(
                        type_=typing.List[User],
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
        name: str,
        id: int,
        user_pass: typing.Optional[str] = OMIT,
        default_visibility: typing.Optional[CreateUserRequestDefaultVisibility] = OMIT,
        description: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        access_level: typing.Optional[UserAccessLevel] = OMIT,
        root_folder_id: typing.Optional[float] = OMIT,
        email_notification: typing.Optional[bool] = OMIT,
        default_group: typing.Optional[int] = OMIT,
        agents: typing.Optional[Analysis] = OMIT,
        default_bucketpool: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Create a new user

        Parameters
        ----------
        name : str
            Unique username

        id : int
            ID of the user

        user_pass : typing.Optional[str]

        default_visibility : typing.Optional[CreateUserRequestDefaultVisibility]

        description : typing.Optional[str]
            Description of the user

        email : typing.Optional[str]
            Email of the user, needs to be unique and is required

        access_level : typing.Optional[UserAccessLevel]

        root_folder_id : typing.Optional[float]
            root folder id of the user

        email_notification : typing.Optional[bool]
            enable email notification when upload scan completes

        default_group : typing.Optional[int]
            Default group id of the user

        agents : typing.Optional[Analysis]

        default_bucketpool : typing.Optional[int]
            Default bucket pool id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            User created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="POST",
            json={
                "name": name,
                "user_pass": user_pass,
                "defaultVisibility": default_visibility,
                "id": id,
                "description": description,
                "email": email,
                "accessLevel": access_level,
                "rootFolderId": root_folder_id,
                "emailNotification": email_notification,
                "defaultGroup": default_group,
                "agents": convert_and_respect_annotation_metadata(
                    object_=agents, annotation=Analysis, direction="write"
                ),
                "defaultBucketpool": default_bucketpool,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_user_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[User]:
        """
        Get one single user by id

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            User with the given id
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id)}",
            method="GET",
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

    async def modify_user_by_id(
        self,
        id_path_param: int,
        *,
        id: int,
        user_pass: typing.Optional[str] = OMIT,
        default_folder_id: typing.Optional[int] = OMIT,
        default_visibility: typing.Optional[ModifyUserByIdRequestDefaultVisibility] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        access_level: typing.Optional[UserAccessLevel] = OMIT,
        root_folder_id: typing.Optional[float] = OMIT,
        email_notification: typing.Optional[bool] = OMIT,
        default_group: typing.Optional[int] = OMIT,
        agents: typing.Optional[Analysis] = OMIT,
        default_bucketpool: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Edit user details by id

        Parameters
        ----------
        id_path_param : int

        id : int
            ID of the user

        user_pass : typing.Optional[str]

        default_folder_id : typing.Optional[int]

        default_visibility : typing.Optional[ModifyUserByIdRequestDefaultVisibility]

        name : typing.Optional[str]
            Unique username

        description : typing.Optional[str]
            Description of the user

        email : typing.Optional[str]
            Email of the user, needs to be unique and is required

        access_level : typing.Optional[UserAccessLevel]

        root_folder_id : typing.Optional[float]
            root folder id of the user

        email_notification : typing.Optional[bool]
            enable email notification when upload scan completes

        default_group : typing.Optional[int]
            Default group id of the user

        agents : typing.Optional[Analysis]

        default_bucketpool : typing.Optional[int]
            Default bucket pool id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            User updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id_path_param)}",
            method="PUT",
            json={
                "user_pass": user_pass,
                "defaultFolderId": default_folder_id,
                "defaultVisibility": default_visibility,
                "id": id,
                "name": name,
                "description": description,
                "email": email,
                "accessLevel": access_level,
                "rootFolderId": root_folder_id,
                "emailNotification": email_notification,
                "defaultGroup": default_group,
                "agents": convert_and_respect_annotation_metadata(
                    object_=agents, annotation=Analysis, direction="write"
                ),
                "defaultBucketpool": default_bucketpool,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def delete_user_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Delete a single user by id

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            User will be deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
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

    async def get_self(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSelfResponse]:
        """
        Get the information about logged in user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSelfResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/self",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSelfResponse,
                    parse_obj_as(
                        type_=GetSelfResponse,
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

    async def create_rest_api_token(
        self,
        *,
        token_name: str,
        token_scope: TokenRequestTokenScope,
        token_expire: dt.date,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateRestApiTokenResponse]:
        """
        Create a new REST API Token

        Parameters
        ----------
        token_name : str
            Friendly name of the token

        token_scope : TokenRequestTokenScope
            The scope of the token.

        token_expire : dt.date
            Date when the token must expire (default max 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateRestApiTokenResponse]
            Token created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/tokens",
            method="POST",
            data={
                "token_name": token_name,
                "token_scope": token_scope,
                "token_expire": token_expire,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateRestApiTokenResponse,
                    parse_obj_as(
                        type_=CreateRestApiTokenResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_tokens_by_type(
        self, type: GetTokensByTypeRequestType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetTokensByTypeResponse]:
        """
        Get all the REST API tokens (active | expired)

        Parameters
        ----------
        type : GetTokensByTypeRequestType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTokensByTypeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/tokens/{encode_path_param(type)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTokensByTypeResponse,
                    parse_obj_as(
                        type_=GetTokensByTypeResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_permission_by_group_id_and_user_id(
        self,
        id: int,
        user_id: int,
        *,
        perm: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Update User's permission in group.

        Parameters
        ----------
        id : int
            Id of the group

        user_id : int
            user id of the member

        perm : typing.Optional[int]
            New user permission in the group.
            0: User
            1: Admin
            2: Advisor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            User's permission will be updated.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(id)}/user/{encode_path_param(user_id)}",
            method="PUT",
            json={
                "perm": perm,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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
