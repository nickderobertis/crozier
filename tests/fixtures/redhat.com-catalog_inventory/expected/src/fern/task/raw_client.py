

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.id import Id
from ..types.task import Task
from ..types.task_state import TaskState
from ..types.task_status import TaskStatus
from ..types.tasks_collection import TasksCollection
from ..types.uuid_ import Uuid


OMIT = typing.cast(typing.Any, ...)


class RawTaskClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_tasks(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TasksCollection]:
        """
        Returns an array of Task objects

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TasksCollection]
            Tasks collection
        """
        _response = self._client_wrapper.httpx_client.request(
            "tasks",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "filter": filter,
                "sort_by": sort_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TasksCollection,
                    parse_obj_as(
                        type_=TasksCollection,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def show_task(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Task]:
        """
        Returns a Task object

        Parameters
        ----------
        id : str
            UUID of task

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Task]
            Task info
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tasks/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Task,
                    parse_obj_as(
                        type_=Task,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_task(
        self,
        id_: str,
        *,
        archived_at: typing.Optional[dt.datetime] = OMIT,
        child_task_id: typing.Optional[str] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        controller_message_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[Uuid] = OMIT,
        input: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        message: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        output: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        owner: typing.Optional[str] = OMIT,
        source_id: typing.Optional[Id] = OMIT,
        state: typing.Optional[TaskState] = OMIT,
        status: typing.Optional[TaskStatus] = OMIT,
        target_source_ref: typing.Optional[str] = OMIT,
        target_type: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates a Task object

        Parameters
        ----------
        id_ : str
            UUID of task

        archived_at : typing.Optional[dt.datetime]

        child_task_id : typing.Optional[str]

        completed_at : typing.Optional[dt.datetime]

        controller_message_id : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        id : typing.Optional[Uuid]

        input : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        message : typing.Optional[str]

        name : typing.Optional[str]

        output : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        owner : typing.Optional[str]

        source_id : typing.Optional[Id]

        state : typing.Optional[TaskState]

        status : typing.Optional[TaskStatus]

        target_source_ref : typing.Optional[str]

        target_type : typing.Optional[str]

        type : typing.Optional[str]

        updated_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tasks/{jsonable_encoder(id_)}",
            method="PATCH",
            json={
                "archived_at": archived_at,
                "child_task_id": child_task_id,
                "completed_at": completed_at,
                "controller_message_id": controller_message_id,
                "created_at": created_at,
                "id": id,
                "input": input,
                "message": message,
                "name": name,
                "output": output,
                "owner": owner,
                "source_id": source_id,
                "state": state,
                "status": status,
                "target_source_ref": target_source_ref,
                "target_type": target_type,
                "type": type,
                "updated_at": updated_at,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTaskClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_tasks(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TasksCollection]:
        """
        Returns an array of Task objects

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TasksCollection]
            Tasks collection
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tasks",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "filter": filter,
                "sort_by": sort_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TasksCollection,
                    parse_obj_as(
                        type_=TasksCollection,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def show_task(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Task]:
        """
        Returns a Task object

        Parameters
        ----------
        id : str
            UUID of task

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Task]
            Task info
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tasks/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Task,
                    parse_obj_as(
                        type_=Task,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_task(
        self,
        id_: str,
        *,
        archived_at: typing.Optional[dt.datetime] = OMIT,
        child_task_id: typing.Optional[str] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        controller_message_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[Uuid] = OMIT,
        input: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        message: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        output: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        owner: typing.Optional[str] = OMIT,
        source_id: typing.Optional[Id] = OMIT,
        state: typing.Optional[TaskState] = OMIT,
        status: typing.Optional[TaskStatus] = OMIT,
        target_source_ref: typing.Optional[str] = OMIT,
        target_type: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates a Task object

        Parameters
        ----------
        id_ : str
            UUID of task

        archived_at : typing.Optional[dt.datetime]

        child_task_id : typing.Optional[str]

        completed_at : typing.Optional[dt.datetime]

        controller_message_id : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        id : typing.Optional[Uuid]

        input : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        message : typing.Optional[str]

        name : typing.Optional[str]

        output : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        owner : typing.Optional[str]

        source_id : typing.Optional[Id]

        state : typing.Optional[TaskState]

        status : typing.Optional[TaskStatus]

        target_source_ref : typing.Optional[str]

        target_type : typing.Optional[str]

        type : typing.Optional[str]

        updated_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tasks/{jsonable_encoder(id_)}",
            method="PATCH",
            json={
                "archived_at": archived_at,
                "child_task_id": child_task_id,
                "completed_at": completed_at,
                "controller_message_id": controller_message_id,
                "created_at": created_at,
                "id": id,
                "input": input,
                "message": message,
                "name": name,
                "output": output,
                "owner": owner,
                "source_id": source_id,
                "state": state,
                "status": status,
                "target_source_ref": target_source_ref,
                "target_type": target_type,
                "type": type,
                "updated_at": updated_at,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
