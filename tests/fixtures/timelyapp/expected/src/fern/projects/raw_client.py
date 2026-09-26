

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
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.v1project import V1Project
from .types.list_projects_request_filter import ListProjectsRequestFilter
from .types.list_projects_request_relation import ListProjectsRequestRelation
from .types.list_projects_request_state import ListProjectsRequestState
from .types.v1projects_create_project import V1ProjectsCreateProject
from .types.v1projects_update_project import V1ProjectsUpdateProject
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_projects(
        self,
        account_id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        filter: typing.Optional[ListProjectsRequestFilter] = None,
        state: typing.Optional[ListProjectsRequestState] = None,
        relation: typing.Optional[ListProjectsRequestRelation] = None,
        updated_after: typing.Optional[str] = None,
        project_ids: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        external_ids: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1Project]]:
        """
        List all projects in the Timely account. The projects will be returned in a paginated format.

        Parameters
        ----------
        account_id : int
            Account ID for the clients you want to retrieve

        offset : typing.Optional[int]
            Retrieve projects from offset

        limit : typing.Optional[int]
            Retrieve number of projects

        order : typing.Optional[str]
            Sorting order - desc, asc (Default desc)

        filter : typing.Optional[ListProjectsRequestFilter]
            Deprecated: Filter projects - mine, active, archived, all (Default mine, ignored if state or relation parameter present)

        state : typing.Optional[ListProjectsRequestState]
            Filter projects - active, archived, all

        relation : typing.Optional[ListProjectsRequestRelation]
            Filter projects - assigned, created, all

        updated_after : typing.Optional[str]
            Retrieve records updated after a certain timestamp

        project_ids : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            Retrieve specific projects

        external_ids : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            Retrieve specific projects by external ID reference

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1Project]]
            Project Details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/projects",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
                "order": order,
                "filter": filter,
                "state": state,
                "relation": relation,
                "updated_after": updated_after,
                "project_ids": project_ids,
                "external_ids": external_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Project],
                    parse_obj_as(
                        type_=typing.List[V1Project],
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
        account_id: int,
        *,
        project: V1ProjectsCreateProject,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Project]:
        """
        Create a new project in the Timely account. The project will be created with the provided details.

        Parameters
        ----------
        account_id : int
            Workspace id

        project : V1ProjectsCreateProject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Project]
            project created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/projects",
            method="POST",
            json={
                "project": convert_and_respect_annotation_metadata(
                    object_=project, annotation=V1ProjectsCreateProject, direction="write"
                ),
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
                    V1Project,
                    parse_obj_as(
                        type_=V1Project,
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

    def show_project(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Project]:
        """
        Retrieve details for a specific project.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Project]
            Project details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/projects/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Project,
                    parse_obj_as(
                        type_=V1Project,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
        account_id: int,
        id: int,
        *,
        project: V1ProjectsUpdateProject,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Project]:
        """
        Update an existing project. Only the provided fields will be updated.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Project ID

        project : V1ProjectsUpdateProject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Project]
            Project updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/projects/{encode_path_param(id)}",
            method="PUT",
            json={
                "project": convert_and_respect_annotation_metadata(
                    object_=project, annotation=V1ProjectsUpdateProject, direction="write"
                ),
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
                    V1Project,
                    parse_obj_as(
                        type_=V1Project,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def delete_project(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete a project. This will permanently remove the project from the account.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Project deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/projects/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
        account_id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        filter: typing.Optional[ListProjectsRequestFilter] = None,
        state: typing.Optional[ListProjectsRequestState] = None,
        relation: typing.Optional[ListProjectsRequestRelation] = None,
        updated_after: typing.Optional[str] = None,
        project_ids: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        external_ids: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1Project]]:
        """
        List all projects in the Timely account. The projects will be returned in a paginated format.

        Parameters
        ----------
        account_id : int
            Account ID for the clients you want to retrieve

        offset : typing.Optional[int]
            Retrieve projects from offset

        limit : typing.Optional[int]
            Retrieve number of projects

        order : typing.Optional[str]
            Sorting order - desc, asc (Default desc)

        filter : typing.Optional[ListProjectsRequestFilter]
            Deprecated: Filter projects - mine, active, archived, all (Default mine, ignored if state or relation parameter present)

        state : typing.Optional[ListProjectsRequestState]
            Filter projects - active, archived, all

        relation : typing.Optional[ListProjectsRequestRelation]
            Filter projects - assigned, created, all

        updated_after : typing.Optional[str]
            Retrieve records updated after a certain timestamp

        project_ids : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            Retrieve specific projects

        external_ids : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            Retrieve specific projects by external ID reference

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1Project]]
            Project Details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/projects",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
                "order": order,
                "filter": filter,
                "state": state,
                "relation": relation,
                "updated_after": updated_after,
                "project_ids": project_ids,
                "external_ids": external_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Project],
                    parse_obj_as(
                        type_=typing.List[V1Project],
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
        account_id: int,
        *,
        project: V1ProjectsCreateProject,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Project]:
        """
        Create a new project in the Timely account. The project will be created with the provided details.

        Parameters
        ----------
        account_id : int
            Workspace id

        project : V1ProjectsCreateProject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Project]
            project created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/projects",
            method="POST",
            json={
                "project": convert_and_respect_annotation_metadata(
                    object_=project, annotation=V1ProjectsCreateProject, direction="write"
                ),
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
                    V1Project,
                    parse_obj_as(
                        type_=V1Project,
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

    async def show_project(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Project]:
        """
        Retrieve details for a specific project.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Project]
            Project details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/projects/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Project,
                    parse_obj_as(
                        type_=V1Project,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
        account_id: int,
        id: int,
        *,
        project: V1ProjectsUpdateProject,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Project]:
        """
        Update an existing project. Only the provided fields will be updated.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Project ID

        project : V1ProjectsUpdateProject

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Project]
            Project updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/projects/{encode_path_param(id)}",
            method="PUT",
            json={
                "project": convert_and_respect_annotation_metadata(
                    object_=project, annotation=V1ProjectsUpdateProject, direction="write"
                ),
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
                    V1Project,
                    parse_obj_as(
                        type_=V1Project,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def delete_project(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Delete a project. This will permanently remove the project from the account.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Project deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/projects/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
