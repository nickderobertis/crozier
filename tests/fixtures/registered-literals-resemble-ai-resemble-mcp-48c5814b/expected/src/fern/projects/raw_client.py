

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.create_project_response import CreateProjectResponse
from .types.delete_project_response import DeleteProjectResponse
from .types.get_project_response import GetProjectResponse
from .types.list_projects_response import ListProjectsResponse
from .types.update_project_response import UpdateProjectResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_projects(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListProjectsResponse]:
        """
        List all projects

        Parameters
        ----------
        page : int

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListProjectsResponse]
            List of projects
        """
        _response = self._client_wrapper.httpx_client.request(
            "projects",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListProjectsResponse,
                    parse_obj_as(
                        type_=ListProjectsResponse,
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

    def create_project(
        self,
        *,
        name: str,
        description: str,
        is_collaborative: bool,
        is_archived: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateProjectResponse]:
        """
        Create a new project

        Parameters
        ----------
        name : str

        description : str

        is_collaborative : bool

        is_archived : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateProjectResponse]
            Project created
        """
        _response = self._client_wrapper.httpx_client.request(
            "projects",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "name": name,
                "description": description,
                "is_collaborative": is_collaborative,
                "is_archived": is_archived,
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
                    CreateProjectResponse,
                    parse_obj_as(
                        type_=CreateProjectResponse,
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

    def get_project(
        self, project_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetProjectResponse]:
        """
        Get project details

        Parameters
        ----------
        project_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetProjectResponse]
            Project details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"projects/{encode_path_param(project_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProjectResponse,
                    parse_obj_as(
                        type_=GetProjectResponse,
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

    def update_project(
        self,
        project_uuid: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        is_collaborative: typing.Optional[bool] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateProjectResponse]:
        """
        Update a project

        Parameters
        ----------
        project_uuid : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        is_collaborative : typing.Optional[bool]

        is_archived : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateProjectResponse]
            Project updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"projects/{encode_path_param(project_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PUT",
            json={
                "name": name,
                "description": description,
                "is_collaborative": is_collaborative,
                "is_archived": is_archived,
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
                    UpdateProjectResponse,
                    parse_obj_as(
                        type_=UpdateProjectResponse,
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

    def delete_project(
        self, project_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteProjectResponse]:
        """
        Delete a project

        Parameters
        ----------
        project_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteProjectResponse]
            Project deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"projects/{encode_path_param(project_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteProjectResponse,
                    parse_obj_as(
                        type_=DeleteProjectResponse,
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


class AsyncRawProjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_projects(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListProjectsResponse]:
        """
        List all projects

        Parameters
        ----------
        page : int

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListProjectsResponse]
            List of projects
        """
        _response = await self._client_wrapper.httpx_client.request(
            "projects",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListProjectsResponse,
                    parse_obj_as(
                        type_=ListProjectsResponse,
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

    async def create_project(
        self,
        *,
        name: str,
        description: str,
        is_collaborative: bool,
        is_archived: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateProjectResponse]:
        """
        Create a new project

        Parameters
        ----------
        name : str

        description : str

        is_collaborative : bool

        is_archived : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateProjectResponse]
            Project created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "projects",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "name": name,
                "description": description,
                "is_collaborative": is_collaborative,
                "is_archived": is_archived,
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
                    CreateProjectResponse,
                    parse_obj_as(
                        type_=CreateProjectResponse,
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

    async def get_project(
        self, project_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetProjectResponse]:
        """
        Get project details

        Parameters
        ----------
        project_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetProjectResponse]
            Project details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"projects/{encode_path_param(project_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProjectResponse,
                    parse_obj_as(
                        type_=GetProjectResponse,
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

    async def update_project(
        self,
        project_uuid: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        is_collaborative: typing.Optional[bool] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateProjectResponse]:
        """
        Update a project

        Parameters
        ----------
        project_uuid : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        is_collaborative : typing.Optional[bool]

        is_archived : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateProjectResponse]
            Project updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"projects/{encode_path_param(project_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PUT",
            json={
                "name": name,
                "description": description,
                "is_collaborative": is_collaborative,
                "is_archived": is_archived,
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
                    UpdateProjectResponse,
                    parse_obj_as(
                        type_=UpdateProjectResponse,
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

    async def delete_project(
        self, project_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteProjectResponse]:
        """
        Delete a project

        Parameters
        ----------
        project_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteProjectResponse]
            Project deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"projects/{encode_path_param(project_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteProjectResponse,
                    parse_obj_as(
                        type_=DeleteProjectResponse,
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
