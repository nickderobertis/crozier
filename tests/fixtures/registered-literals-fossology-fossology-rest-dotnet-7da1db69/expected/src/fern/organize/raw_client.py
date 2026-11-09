

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..types.info import Info
from .types.move_folder_by_id_request_action import MoveFolderByIdRequestAction
from pydantic import ValidationError


class RawOrganizeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_folder(
        self,
        *,
        parent_folder: int,
        folder_name: str,
        group_name: typing.Optional[str] = None,
        folder_description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Create a new child folder with optional description

        Parameters
        ----------
        parent_folder : int
            Parent folder for the new folder

        folder_name : str
            Name of the new folder

        group_name : typing.Optional[str]
            The group name to chose while accessing folders

        folder_description : typing.Optional[str]
            Description of the new folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            Folder with the same name already exists under the same parent
        """
        _response = self._client_wrapper.httpx_client.request(
            "folders",
            method="POST",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "parentFolder": str(parent_folder) if parent_folder is not None else None,
                "folderName": str(folder_name) if folder_name is not None else None,
                "folderDescription": str(folder_description) if folder_description is not None else None,
            },
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

    def move_folder_by_id(
        self,
        id: int,
        *,
        parent: int,
        action: MoveFolderByIdRequestAction,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Copy or move a folder by id

        Parameters
        ----------
        id : int
            ID of the folder

        parent : int
            New parent folder id

        action : MoveFolderByIdRequestAction
            Action to be performed

        group_name : typing.Optional[str]
            The group name to chose while accessing the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            Folder will be copied/moved
        """
        _response = self._client_wrapper.httpx_client.request(
            f"folders/{encode_path_param(id)}",
            method="PUT",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "parent": str(parent) if parent is not None else None,
                "action": action.value if action is not None else None,
            },
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

    def delete_folder_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Schedule a folder deletion

        Parameters
        ----------
        id : int
            ID of the folder

        group_name : typing.Optional[str]
            The group name to chose while accessing the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            Folder scheduled to be deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"folders/{encode_path_param(id)}",
            method="DELETE",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
            },
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

    def patch_folder_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Change a folder's name and/or description

        Parameters
        ----------
        id : int
            ID of the folder

        group_name : typing.Optional[str]
            The group name to chose while accessing the folder

        name : typing.Optional[str]
            New name of the folder

        description : typing.Optional[str]
            New description of the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            Folder is updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"folders/{encode_path_param(id)}",
            method="PATCH",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "name": str(name) if name is not None else None,
                "description": str(description) if description is not None else None,
            },
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

    def create_group(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Info]:
        """
        Create a new user group

        Parameters
        ----------
        name : str
            Name of the new group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            Group has been added
        """
        _response = self._client_wrapper.httpx_client.request(
            "groups",
            method="POST",
            headers={
                "name": str(name) if name is not None else None,
            },
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


class AsyncRawOrganizeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_folder(
        self,
        *,
        parent_folder: int,
        folder_name: str,
        group_name: typing.Optional[str] = None,
        folder_description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Create a new child folder with optional description

        Parameters
        ----------
        parent_folder : int
            Parent folder for the new folder

        folder_name : str
            Name of the new folder

        group_name : typing.Optional[str]
            The group name to chose while accessing folders

        folder_description : typing.Optional[str]
            Description of the new folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            Folder with the same name already exists under the same parent
        """
        _response = await self._client_wrapper.httpx_client.request(
            "folders",
            method="POST",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "parentFolder": str(parent_folder) if parent_folder is not None else None,
                "folderName": str(folder_name) if folder_name is not None else None,
                "folderDescription": str(folder_description) if folder_description is not None else None,
            },
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

    async def move_folder_by_id(
        self,
        id: int,
        *,
        parent: int,
        action: MoveFolderByIdRequestAction,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Copy or move a folder by id

        Parameters
        ----------
        id : int
            ID of the folder

        parent : int
            New parent folder id

        action : MoveFolderByIdRequestAction
            Action to be performed

        group_name : typing.Optional[str]
            The group name to chose while accessing the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            Folder will be copied/moved
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"folders/{encode_path_param(id)}",
            method="PUT",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "parent": str(parent) if parent is not None else None,
                "action": action.value if action is not None else None,
            },
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

    async def delete_folder_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Schedule a folder deletion

        Parameters
        ----------
        id : int
            ID of the folder

        group_name : typing.Optional[str]
            The group name to chose while accessing the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            Folder scheduled to be deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"folders/{encode_path_param(id)}",
            method="DELETE",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
            },
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

    async def patch_folder_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Change a folder's name and/or description

        Parameters
        ----------
        id : int
            ID of the folder

        group_name : typing.Optional[str]
            The group name to chose while accessing the folder

        name : typing.Optional[str]
            New name of the folder

        description : typing.Optional[str]
            New description of the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            Folder is updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"folders/{encode_path_param(id)}",
            method="PATCH",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "name": str(name) if name is not None else None,
                "description": str(description) if description is not None else None,
            },
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

    async def create_group(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Create a new user group

        Parameters
        ----------
        name : str
            Name of the new group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            Group has been added
        """
        _response = await self._client_wrapper.httpx_client.request(
            "groups",
            method="POST",
            headers={
                "name": str(name) if name is not None else None,
            },
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
