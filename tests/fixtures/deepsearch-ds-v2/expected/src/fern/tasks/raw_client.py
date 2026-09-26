

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.task_context import TaskContext
from ..types.task_result import TaskResult
from .types.list_project_tasks_request_sort_order import ListProjectTasksRequestSortOrder
from pydantic import ValidationError


class RawTasksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_project_celery_task(
        self,
        proj_key: str,
        task_id: str,
        *,
        wait: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskResult]:
        """
        Get a celery task for a project.

        Parameters
        ----------
        proj_key : str

        task_id : str

        wait : typing.Optional[float]
            Optionally block this method call for a few seconds to wait for the result instead of polling through multiple calls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/celery_tasks/{encode_path_param(task_id)}",
            method="GET",
            params={
                "wait": wait,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskResult,
                    parse_obj_as(
                        type_=TaskResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def list_project_tasks(
        self,
        proj_key: str,
        *,
        task_type: typing.Optional[str] = None,
        skip: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[ListProjectTasksRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[TaskContext]]:
        """
        List tasks for a project.

        Parameters
        ----------
        proj_key : str

        task_type : typing.Optional[str]

        skip : typing.Optional[int]

        limit : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_order : typing.Optional[ListProjectTasksRequestSortOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TaskContext]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/tasks",
            method="GET",
            params={
                "task_type": task_type,
                "skip": skip,
                "limit": limit,
                "sort_by": sort_by,
                "sort_order": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TaskContext],
                    parse_obj_as(
                        type_=typing.List[TaskContext],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_project_task(
        self, proj_key: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TaskContext]:
        """
        Get a task for a project.

        Parameters
        ----------
        proj_key : str

        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskContext]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/tasks/{encode_path_param(task_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskContext,
                    parse_obj_as(
                        type_=TaskContext,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def abort_project_task(
        self, proj_key: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Abort a task.

        Parameters
        ----------
        proj_key : str

        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/tasks/{encode_path_param(task_id)}/actions/abort",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawTasksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_project_celery_task(
        self,
        proj_key: str,
        task_id: str,
        *,
        wait: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskResult]:
        """
        Get a celery task for a project.

        Parameters
        ----------
        proj_key : str

        task_id : str

        wait : typing.Optional[float]
            Optionally block this method call for a few seconds to wait for the result instead of polling through multiple calls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/celery_tasks/{encode_path_param(task_id)}",
            method="GET",
            params={
                "wait": wait,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskResult,
                    parse_obj_as(
                        type_=TaskResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def list_project_tasks(
        self,
        proj_key: str,
        *,
        task_type: typing.Optional[str] = None,
        skip: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[ListProjectTasksRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[TaskContext]]:
        """
        List tasks for a project.

        Parameters
        ----------
        proj_key : str

        task_type : typing.Optional[str]

        skip : typing.Optional[int]

        limit : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_order : typing.Optional[ListProjectTasksRequestSortOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TaskContext]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/tasks",
            method="GET",
            params={
                "task_type": task_type,
                "skip": skip,
                "limit": limit,
                "sort_by": sort_by,
                "sort_order": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TaskContext],
                    parse_obj_as(
                        type_=typing.List[TaskContext],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_project_task(
        self, proj_key: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TaskContext]:
        """
        Get a task for a project.

        Parameters
        ----------
        proj_key : str

        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskContext]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/tasks/{encode_path_param(task_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskContext,
                    parse_obj_as(
                        type_=TaskContext,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def abort_project_task(
        self, proj_key: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Abort a task.

        Parameters
        ----------
        proj_key : str

        task_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/tasks/{encode_path_param(task_id)}/actions/abort",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
