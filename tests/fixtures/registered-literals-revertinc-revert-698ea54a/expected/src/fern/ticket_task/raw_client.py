

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
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.common_base_error import CommonBaseError
from ..types.common_ticket_priority import CommonTicketPriority
from ..types.common_ticket_status import CommonTicketStatus
from ..types.ticket_create_or_update_task_response import TicketCreateOrUpdateTaskResponse
from ..types.ticket_get_task_response import TicketGetTaskResponse
from ..types.ticket_get_tasks_response import TicketGetTasksResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTicketTaskClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def ticket_task_get_task(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TicketGetTaskResponse]:
        """
        Get details of a task

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TicketGetTaskResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ticket/tasks/{encode_path_param(id)}",
            method="GET",
            params={
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TicketGetTaskResponse,
                    parse_obj_as(
                        type_=TicketGetTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    def ticket_task_update_task(
        self,
        id: str,
        *,
        name: str,
        assignees: typing.Sequence[str],
        description: str,
        status: CommonTicketStatus,
        priority: CommonTicketPriority,
        creator_id: str,
        due_date: str,
        completed_date: str,
        parent_id: str,
        list_id: str,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TicketCreateOrUpdateTaskResponse]:
        """
        Update a task

        Parameters
        ----------
        id : str

        name : str
            Name of the task.

        assignees : typing.Sequence[str]
            collection of IDs belonging to assignees.

        description : str
            Description of the task.

        status : CommonTicketStatus
            Current status of the task.

        priority : CommonTicketPriority
            Priority of the task.

        creator_id : str
            ID of the task creator.

        due_date : str
            Due date for the given task.

        completed_date : str
            Date at which task was completed.

        parent_id : str
            Id of the parent task.

        list_id : str
            Id of the list

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TicketCreateOrUpdateTaskResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ticket/tasks/{encode_path_param(id)}",
            method="PATCH",
            params={
                "fields": fields,
            },
            json={
                "name": name,
                "assignees": assignees,
                "description": description,
                "status": status,
                "priority": priority,
                "creatorId": creator_id,
                "dueDate": due_date,
                "completedDate": completed_date,
                "parentId": parent_id,
                "listId": list_id,
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
                    TicketCreateOrUpdateTaskResponse,
                    parse_obj_as(
                        type_=TicketCreateOrUpdateTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    def ticket_task_get_tasks(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TicketGetTasksResponse]:
        """
        Get all the tasks

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TicketGetTasksResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ticket/tasks",
            method="GET",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TicketGetTasksResponse,
                    parse_obj_as(
                        type_=TicketGetTasksResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    def ticket_task_create_task(
        self,
        *,
        name: str,
        assignees: typing.Sequence[str],
        description: str,
        status: CommonTicketStatus,
        priority: CommonTicketPriority,
        creator_id: str,
        due_date: str,
        completed_date: str,
        parent_id: str,
        list_id: str,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TicketCreateOrUpdateTaskResponse]:
        """
        Parameters
        ----------
        name : str
            Name of the task.

        assignees : typing.Sequence[str]
            collection of IDs belonging to assignees.

        description : str
            Description of the task.

        status : CommonTicketStatus
            Current status of the task.

        priority : CommonTicketPriority
            Priority of the task.

        creator_id : str
            ID of the task creator.

        due_date : str
            Due date for the given task.

        completed_date : str
            Date at which task was completed.

        parent_id : str
            Id of the parent task.

        list_id : str
            Id of the list

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TicketCreateOrUpdateTaskResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ticket/tasks",
            method="POST",
            params={
                "fields": fields,
            },
            json={
                "name": name,
                "assignees": assignees,
                "description": description,
                "status": status,
                "priority": priority,
                "creatorId": creator_id,
                "dueDate": due_date,
                "completedDate": completed_date,
                "parentId": parent_id,
                "listId": list_id,
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
                    TicketCreateOrUpdateTaskResponse,
                    parse_obj_as(
                        type_=TicketCreateOrUpdateTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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


class AsyncRawTicketTaskClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def ticket_task_get_task(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TicketGetTaskResponse]:
        """
        Get details of a task

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TicketGetTaskResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ticket/tasks/{encode_path_param(id)}",
            method="GET",
            params={
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TicketGetTaskResponse,
                    parse_obj_as(
                        type_=TicketGetTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    async def ticket_task_update_task(
        self,
        id: str,
        *,
        name: str,
        assignees: typing.Sequence[str],
        description: str,
        status: CommonTicketStatus,
        priority: CommonTicketPriority,
        creator_id: str,
        due_date: str,
        completed_date: str,
        parent_id: str,
        list_id: str,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TicketCreateOrUpdateTaskResponse]:
        """
        Update a task

        Parameters
        ----------
        id : str

        name : str
            Name of the task.

        assignees : typing.Sequence[str]
            collection of IDs belonging to assignees.

        description : str
            Description of the task.

        status : CommonTicketStatus
            Current status of the task.

        priority : CommonTicketPriority
            Priority of the task.

        creator_id : str
            ID of the task creator.

        due_date : str
            Due date for the given task.

        completed_date : str
            Date at which task was completed.

        parent_id : str
            Id of the parent task.

        list_id : str
            Id of the list

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TicketCreateOrUpdateTaskResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ticket/tasks/{encode_path_param(id)}",
            method="PATCH",
            params={
                "fields": fields,
            },
            json={
                "name": name,
                "assignees": assignees,
                "description": description,
                "status": status,
                "priority": priority,
                "creatorId": creator_id,
                "dueDate": due_date,
                "completedDate": completed_date,
                "parentId": parent_id,
                "listId": list_id,
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
                    TicketCreateOrUpdateTaskResponse,
                    parse_obj_as(
                        type_=TicketCreateOrUpdateTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    async def ticket_task_get_tasks(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TicketGetTasksResponse]:
        """
        Get all the tasks

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TicketGetTasksResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ticket/tasks",
            method="GET",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TicketGetTasksResponse,
                    parse_obj_as(
                        type_=TicketGetTasksResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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

    async def ticket_task_create_task(
        self,
        *,
        name: str,
        assignees: typing.Sequence[str],
        description: str,
        status: CommonTicketStatus,
        priority: CommonTicketPriority,
        creator_id: str,
        due_date: str,
        completed_date: str,
        parent_id: str,
        list_id: str,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TicketCreateOrUpdateTaskResponse]:
        """
        Parameters
        ----------
        name : str
            Name of the task.

        assignees : typing.Sequence[str]
            collection of IDs belonging to assignees.

        description : str
            Description of the task.

        status : CommonTicketStatus
            Current status of the task.

        priority : CommonTicketPriority
            Priority of the task.

        creator_id : str
            ID of the task creator.

        due_date : str
            Due date for the given task.

        completed_date : str
            Date at which task was completed.

        parent_id : str
            Id of the parent task.

        list_id : str
            Id of the list

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TicketCreateOrUpdateTaskResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ticket/tasks",
            method="POST",
            params={
                "fields": fields,
            },
            json={
                "name": name,
                "assignees": assignees,
                "description": description,
                "status": status,
                "priority": priority,
                "creatorId": creator_id,
                "dueDate": due_date,
                "completedDate": completed_date,
                "parentId": parent_id,
                "listId": list_id,
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
                    TicketCreateOrUpdateTaskResponse,
                    parse_obj_as(
                        type_=TicketCreateOrUpdateTaskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
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
