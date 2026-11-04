

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.forbidden_error_body import ForbiddenErrorBody
from ..types.unauthorized_error_body import UnauthorizedErrorBody
from .types.workspace_api_ocs_add_user_as_workspace_manager_response import (
    WorkspaceApiOcsAddUserAsWorkspaceManagerResponse,
)
from .types.workspace_api_ocs_add_users_in_workspace_response import WorkspaceApiOcsAddUsersInWorkspaceResponse
from .types.workspace_api_ocs_add_users_to_group_response import WorkspaceApiOcsAddUsersToGroupResponse
from .types.workspace_api_ocs_find_users_by_id_response import WorkspaceApiOcsFindUsersByIdResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWorkspaceUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def workspace_api_ocs_find_users_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkspaceApiOcsFindUsersByIdResponse]:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkspaceApiOcsFindUsersByIdResponse]
            Users of the specified workspace returned successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/workspace/api/v1/spaces/{encode_path_param(id)}/users",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkspaceApiOcsFindUsersByIdResponse,
                    parse_obj_as(
                        type_=WorkspaceApiOcsFindUsersByIdResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def workspace_api_ocs_add_users_in_workspace(
        self, id: int, *, uids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkspaceApiOcsAddUsersInWorkspaceResponse]:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uids : typing.Sequence[str]
            Represents the user uids to add to the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkspaceApiOcsAddUsersInWorkspaceResponse]
            Confirmation message indicating that users have been added successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/workspace/api/v1/spaces/{encode_path_param(id)}/users",
            method="POST",
            json={
                "uids": uids,
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
                    WorkspaceApiOcsAddUsersInWorkspaceResponse,
                    parse_obj_as(
                        type_=WorkspaceApiOcsAddUsersInWorkspaceResponse,
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

    def workspace_api_ocs_remove_users_in_workspace(
        self,
        id: int,
        *,
        uids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Represents the user uids to remove to the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/workspace/api/v1/spaces/{encode_path_param(id)}/users",
            method="DELETE",
            params={
                "uids[]": uids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def workspace_api_ocs_add_user_as_workspace_manager(
        self, id: int, *, uid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkspaceApiOcsAddUserAsWorkspaceManagerResponse]:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uid : str
            Represents the user uid to add as a workspace manager

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkspaceApiOcsAddUserAsWorkspaceManagerResponse]
            Confirmation for users added to the workspace.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/workspace/api/v1/spaces/{encode_path_param(id)}/workspace-manager",
            method="POST",
            json={
                "uid": uid,
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
                    WorkspaceApiOcsAddUserAsWorkspaceManagerResponse,
                    parse_obj_as(
                        type_=WorkspaceApiOcsAddUserAsWorkspaceManagerResponse,
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

    def workspace_api_ocs_remove_user_as_workspace_manager(
        self, id: int, *, uid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uid : str
            Represents the user uid to remove as a workspace manager

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/workspace/api/v1/spaces/{encode_path_param(id)}/workspace-manager",
            method="DELETE",
            params={
                "uid": uid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def workspace_api_ocs_add_users_to_group(
        self, id: int, gid: str, *, uids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkspaceApiOcsAddUsersToGroupResponse]:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        gid : str
            The subgroup id

        uids : typing.Sequence[str]
            Represents the user uids to add to the subgroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkspaceApiOcsAddUsersToGroupResponse]
            Users added in subgroup successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/workspace/api/v1/spaces/{encode_path_param(id)}/groups/{encode_path_param(gid)}/users",
            method="POST",
            json={
                "uids": uids,
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
                    WorkspaceApiOcsAddUsersToGroupResponse,
                    parse_obj_as(
                        type_=WorkspaceApiOcsAddUsersToGroupResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
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

    def workspace_api_ocs_remove_users_from_group(
        self,
        id: int,
        gid: str,
        *,
        uids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        gid : str
            The subgroup id

        uids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Represents the user uids to remove from the subgroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/workspace/api/v1/spaces/{encode_path_param(id)}/groups/{encode_path_param(gid)}/users",
            method="DELETE",
            params={
                "uids[]": uids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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


class AsyncRawWorkspaceUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def workspace_api_ocs_find_users_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkspaceApiOcsFindUsersByIdResponse]:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkspaceApiOcsFindUsersByIdResponse]
            Users of the specified workspace returned successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/workspace/api/v1/spaces/{encode_path_param(id)}/users",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkspaceApiOcsFindUsersByIdResponse,
                    parse_obj_as(
                        type_=WorkspaceApiOcsFindUsersByIdResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def workspace_api_ocs_add_users_in_workspace(
        self, id: int, *, uids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkspaceApiOcsAddUsersInWorkspaceResponse]:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uids : typing.Sequence[str]
            Represents the user uids to add to the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkspaceApiOcsAddUsersInWorkspaceResponse]
            Confirmation message indicating that users have been added successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/workspace/api/v1/spaces/{encode_path_param(id)}/users",
            method="POST",
            json={
                "uids": uids,
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
                    WorkspaceApiOcsAddUsersInWorkspaceResponse,
                    parse_obj_as(
                        type_=WorkspaceApiOcsAddUsersInWorkspaceResponse,
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

    async def workspace_api_ocs_remove_users_in_workspace(
        self,
        id: int,
        *,
        uids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Represents the user uids to remove to the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/workspace/api/v1/spaces/{encode_path_param(id)}/users",
            method="DELETE",
            params={
                "uids[]": uids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def workspace_api_ocs_add_user_as_workspace_manager(
        self, id: int, *, uid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkspaceApiOcsAddUserAsWorkspaceManagerResponse]:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uid : str
            Represents the user uid to add as a workspace manager

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkspaceApiOcsAddUserAsWorkspaceManagerResponse]
            Confirmation for users added to the workspace.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/workspace/api/v1/spaces/{encode_path_param(id)}/workspace-manager",
            method="POST",
            json={
                "uid": uid,
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
                    WorkspaceApiOcsAddUserAsWorkspaceManagerResponse,
                    parse_obj_as(
                        type_=WorkspaceApiOcsAddUserAsWorkspaceManagerResponse,
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

    async def workspace_api_ocs_remove_user_as_workspace_manager(
        self, id: int, *, uid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        uid : str
            Represents the user uid to remove as a workspace manager

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/workspace/api/v1/spaces/{encode_path_param(id)}/workspace-manager",
            method="DELETE",
            params={
                "uid": uid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def workspace_api_ocs_add_users_to_group(
        self, id: int, gid: str, *, uids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkspaceApiOcsAddUsersToGroupResponse]:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        gid : str
            The subgroup id

        uids : typing.Sequence[str]
            Represents the user uids to add to the subgroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkspaceApiOcsAddUsersToGroupResponse]
            Users added in subgroup successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/workspace/api/v1/spaces/{encode_path_param(id)}/groups/{encode_path_param(gid)}/users",
            method="POST",
            json={
                "uids": uids,
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
                    WorkspaceApiOcsAddUsersToGroupResponse,
                    parse_obj_as(
                        type_=WorkspaceApiOcsAddUsersToGroupResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
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

    async def workspace_api_ocs_remove_users_from_group(
        self,
        id: int,
        gid: str,
        *,
        uids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Represents the ID of the workspace

        gid : str
            The subgroup id

        uids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Represents the user uids to remove from the subgroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/workspace/api/v1/spaces/{encode_path_param(id)}/groups/{encode_path_param(gid)}/users",
            method="DELETE",
            params={
                "uids[]": uids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
