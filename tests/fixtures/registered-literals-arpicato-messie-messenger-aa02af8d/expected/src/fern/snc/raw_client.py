

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
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.not_implemented_error import NotImplementedError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.created_group import CreatedGroup
from ..types.internal_server_error_body import InternalServerErrorBody
from ..types.not_found_error_body import NotFoundErrorBody
from ..types.not_implemented_error_body import NotImplementedErrorBody
from ..types.resolved_identifier import ResolvedIdentifier
from ..types.unauthorized_error_body import UnauthorizedErrorBody
from ..types.user_login_id import UserLoginId
from .types.create_dm_response import CreateDmResponse
from .types.get_contacts_response import GetContactsResponse
from .types.group_create_params_avatar import GroupCreateParamsAvatar
from .types.group_create_params_disappear import GroupCreateParamsDisappear
from .types.group_create_params_name import GroupCreateParamsName
from .types.group_create_params_topic import GroupCreateParamsTopic
from .types.search_users_response import SearchUsersResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSncClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_contacts(
        self, *, login_id: typing.Optional[UserLoginId] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetContactsResponse]:
        """
        Parameters
        ----------
        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetContactsResponse]
            Contact list fetched successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/contacts",
            method="GET",
            params={
                "login_id": login_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetContactsResponse,
                    parse_obj_as(
                        type_=GetContactsResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotImplementedErrorBody,
                        parse_obj_as(
                            type_=NotImplementedErrorBody,
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

    def search_users(
        self,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchUsersResponse]:
        """
        Parameters
        ----------
        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        query : typing.Optional[str]
            The search query to send to the remote network

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchUsersResponse]
            Search completed successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/search_users",
            method="POST",
            params={
                "login_id": login_id,
            },
            json={
                "query": query,
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
                    SearchUsersResponse,
                    parse_obj_as(
                        type_=SearchUsersResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotImplementedErrorBody,
                        parse_obj_as(
                            type_=NotImplementedErrorBody,
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

    def resolve_identifier(
        self,
        identifier: str,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResolvedIdentifier]:
        """
        Parameters
        ----------
        identifier : str
            The identifier to resolve or start a chat with.

        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResolvedIdentifier]
            Identifier resolved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v3/resolve_identifier/{encode_path_param(identifier)}",
            method="GET",
            params={
                "login_id": login_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResolvedIdentifier,
                    parse_obj_as(
                        type_=ResolvedIdentifier,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotImplementedErrorBody,
                        parse_obj_as(
                            type_=NotImplementedErrorBody,
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

    def create_dm(
        self,
        identifier: str,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateDmResponse]:
        """
        Parameters
        ----------
        identifier : str
            The identifier to resolve or start a chat with.

        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateDmResponse]
            Identifier resolved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v3/create_dm/{encode_path_param(identifier)}",
            method="POST",
            params={
                "login_id": login_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDmResponse,
                    parse_obj_as(
                        type_=CreateDmResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotImplementedErrorBody,
                        parse_obj_as(
                            type_=NotImplementedErrorBody,
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

    def create_group(
        self,
        type_path_param: str,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        type: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        participants: typing.Optional[typing.Sequence[str]] = OMIT,
        parent: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[GroupCreateParamsName] = OMIT,
        avatar: typing.Optional[GroupCreateParamsAvatar] = OMIT,
        topic: typing.Optional[GroupCreateParamsTopic] = OMIT,
        disappear: typing.Optional[GroupCreateParamsDisappear] = OMIT,
        room_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreatedGroup]:
        """
        Parameters
        ----------
        type_path_param : str

        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        type : typing.Optional[str]
            The type of group to create.

        username : typing.Optional[str]
            The public username for the created group.

        participants : typing.Optional[typing.Sequence[str]]
            The users to add to the group initially.

        parent : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[GroupCreateParamsName]
            The `m.room.name` event content for the room.

        avatar : typing.Optional[GroupCreateParamsAvatar]
            The `m.room.avatar` event content for the room.

        topic : typing.Optional[GroupCreateParamsTopic]
            The `m.room.topic` event content for the room.

        disappear : typing.Optional[GroupCreateParamsDisappear]
            The `com.beeper.disappearing_timer` event content for the room.

        room_id : typing.Optional[str]
            An existing Matrix room ID to bridge to.
            The other parameters must be already in sync with the room state when using this parameter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreatedGroup]
            Identifier resolved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v3/create_group/{encode_path_param(type_path_param)}",
            method="POST",
            params={
                "login_id": login_id,
            },
            json={
                "type": type,
                "username": username,
                "participants": participants,
                "parent": parent,
                "name": convert_and_respect_annotation_metadata(
                    object_=name, annotation=GroupCreateParamsName, direction="write"
                ),
                "avatar": convert_and_respect_annotation_metadata(
                    object_=avatar, annotation=GroupCreateParamsAvatar, direction="write"
                ),
                "topic": convert_and_respect_annotation_metadata(
                    object_=topic, annotation=GroupCreateParamsTopic, direction="write"
                ),
                "disappear": convert_and_respect_annotation_metadata(
                    object_=disappear, annotation=GroupCreateParamsDisappear, direction="write"
                ),
                "room_id": room_id,
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
                    CreatedGroup,
                    parse_obj_as(
                        type_=CreatedGroup,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotImplementedErrorBody,
                        parse_obj_as(
                            type_=NotImplementedErrorBody,
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


class AsyncRawSncClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_contacts(
        self, *, login_id: typing.Optional[UserLoginId] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetContactsResponse]:
        """
        Parameters
        ----------
        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetContactsResponse]
            Contact list fetched successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/contacts",
            method="GET",
            params={
                "login_id": login_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetContactsResponse,
                    parse_obj_as(
                        type_=GetContactsResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotImplementedErrorBody,
                        parse_obj_as(
                            type_=NotImplementedErrorBody,
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

    async def search_users(
        self,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchUsersResponse]:
        """
        Parameters
        ----------
        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        query : typing.Optional[str]
            The search query to send to the remote network

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchUsersResponse]
            Search completed successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/search_users",
            method="POST",
            params={
                "login_id": login_id,
            },
            json={
                "query": query,
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
                    SearchUsersResponse,
                    parse_obj_as(
                        type_=SearchUsersResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotImplementedErrorBody,
                        parse_obj_as(
                            type_=NotImplementedErrorBody,
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

    async def resolve_identifier(
        self,
        identifier: str,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResolvedIdentifier]:
        """
        Parameters
        ----------
        identifier : str
            The identifier to resolve or start a chat with.

        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResolvedIdentifier]
            Identifier resolved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v3/resolve_identifier/{encode_path_param(identifier)}",
            method="GET",
            params={
                "login_id": login_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResolvedIdentifier,
                    parse_obj_as(
                        type_=ResolvedIdentifier,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotImplementedErrorBody,
                        parse_obj_as(
                            type_=NotImplementedErrorBody,
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

    async def create_dm(
        self,
        identifier: str,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateDmResponse]:
        """
        Parameters
        ----------
        identifier : str
            The identifier to resolve or start a chat with.

        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateDmResponse]
            Identifier resolved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v3/create_dm/{encode_path_param(identifier)}",
            method="POST",
            params={
                "login_id": login_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDmResponse,
                    parse_obj_as(
                        type_=CreateDmResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotImplementedErrorBody,
                        parse_obj_as(
                            type_=NotImplementedErrorBody,
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

    async def create_group(
        self,
        type_path_param: str,
        *,
        login_id: typing.Optional[UserLoginId] = None,
        type: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        participants: typing.Optional[typing.Sequence[str]] = OMIT,
        parent: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[GroupCreateParamsName] = OMIT,
        avatar: typing.Optional[GroupCreateParamsAvatar] = OMIT,
        topic: typing.Optional[GroupCreateParamsTopic] = OMIT,
        disappear: typing.Optional[GroupCreateParamsDisappear] = OMIT,
        room_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreatedGroup]:
        """
        Parameters
        ----------
        type_path_param : str

        login_id : typing.Optional[UserLoginId]
            An optional explicit login ID to do the action through.

        type : typing.Optional[str]
            The type of group to create.

        username : typing.Optional[str]
            The public username for the created group.

        participants : typing.Optional[typing.Sequence[str]]
            The users to add to the group initially.

        parent : typing.Optional[typing.Dict[str, typing.Any]]

        name : typing.Optional[GroupCreateParamsName]
            The `m.room.name` event content for the room.

        avatar : typing.Optional[GroupCreateParamsAvatar]
            The `m.room.avatar` event content for the room.

        topic : typing.Optional[GroupCreateParamsTopic]
            The `m.room.topic` event content for the room.

        disappear : typing.Optional[GroupCreateParamsDisappear]
            The `com.beeper.disappearing_timer` event content for the room.

        room_id : typing.Optional[str]
            An existing Matrix room ID to bridge to.
            The other parameters must be already in sync with the room state when using this parameter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreatedGroup]
            Identifier resolved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v3/create_group/{encode_path_param(type_path_param)}",
            method="POST",
            params={
                "login_id": login_id,
            },
            json={
                "type": type,
                "username": username,
                "participants": participants,
                "parent": parent,
                "name": convert_and_respect_annotation_metadata(
                    object_=name, annotation=GroupCreateParamsName, direction="write"
                ),
                "avatar": convert_and_respect_annotation_metadata(
                    object_=avatar, annotation=GroupCreateParamsAvatar, direction="write"
                ),
                "topic": convert_and_respect_annotation_metadata(
                    object_=topic, annotation=GroupCreateParamsTopic, direction="write"
                ),
                "disappear": convert_and_respect_annotation_metadata(
                    object_=disappear, annotation=GroupCreateParamsDisappear, direction="write"
                ),
                "room_id": room_id,
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
                    CreatedGroup,
                    parse_obj_as(
                        type_=CreatedGroup,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotImplementedErrorBody,
                        parse_obj_as(
                            type_=NotImplementedErrorBody,
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
