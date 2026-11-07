

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
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error_response import ErrorResponse
from ..types.task_directive_object import TaskDirectiveObject
from ..types.taskforce_object import TaskforceObject
from .types.post_v1query_task_directives_response import PostV1QueryTaskDirectivesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTaskDirectivesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_v1query_task_directives(
        self,
        *,
        query: typing.Dict[str, typing.Any],
        projection: typing.Optional[typing.Sequence[str]] = OMIT,
        after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1QueryTaskDirectivesResponse]:
        """
        Queries and returns a list of task directive objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_.

        Parameters
        ----------
        query : typing.Dict[str, typing.Any]
            The search criteria (MongoDB-filter syntax)

        projection : typing.Optional[typing.Sequence[str]]
            The fields to include in the response

        after : typing.Optional[str]
            The database '_id' to resume pagination from, taken from a previous response's 'next_after' field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1QueryTaskDirectivesResponse]
            Matching task directives and pagination metadata.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/query/task-directives",
            method="POST",
            json={
                "query": query,
                "projection": projection,
                "after": after,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostV1QueryTaskDirectivesResponse,
                    parse_obj_as(
                        type_=PostV1QueryTaskDirectivesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_v1task_directives_task_id(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TaskDirectiveObject]:
        """
        Retrieves the task directive that matches the specified task ID. See `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_.

        Parameters
        ----------
        task_id : str
            The ID of the task directive

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskDirectiveObject]
            The matching task directive
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/task-directives/{encode_path_param(task_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskDirectiveObject,
                    parse_obj_as(
                        type_=TaskDirectiveObject,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def post_v1task_directives_task_id_actions_add_workers(
        self,
        task_id: str,
        *,
        cluster_location: str,
        n_workers: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskforceObject]:
        """
        Creates a new taskforce (and associated workers) for an existing task directive. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        task_id : str
            The ID of the task directive to which the taskforce (and workers) will be added.

        cluster_location : str

        n_workers : typing.Optional[int]
            The number of workers in this taskforce's HTCondor cluster (immutable).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskforceObject]
            The created taskforce object with its details.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/task-directives/{encode_path_param(task_id)}/actions/add-workers",
            method="POST",
            json={
                "cluster_location": cluster_location,
                "n_workers": n_workers,
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
                    TaskforceObject,
                    parse_obj_as(
                        type_=TaskforceObject,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawTaskDirectivesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_v1query_task_directives(
        self,
        *,
        query: typing.Dict[str, typing.Any],
        projection: typing.Optional[typing.Sequence[str]] = OMIT,
        after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1QueryTaskDirectivesResponse]:
        """
        Queries and returns a list of task directive objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_.

        Parameters
        ----------
        query : typing.Dict[str, typing.Any]
            The search criteria (MongoDB-filter syntax)

        projection : typing.Optional[typing.Sequence[str]]
            The fields to include in the response

        after : typing.Optional[str]
            The database '_id' to resume pagination from, taken from a previous response's 'next_after' field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1QueryTaskDirectivesResponse]
            Matching task directives and pagination metadata.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/query/task-directives",
            method="POST",
            json={
                "query": query,
                "projection": projection,
                "after": after,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostV1QueryTaskDirectivesResponse,
                    parse_obj_as(
                        type_=PostV1QueryTaskDirectivesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_v1task_directives_task_id(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TaskDirectiveObject]:
        """
        Retrieves the task directive that matches the specified task ID. See `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_.

        Parameters
        ----------
        task_id : str
            The ID of the task directive

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskDirectiveObject]
            The matching task directive
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/task-directives/{encode_path_param(task_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskDirectiveObject,
                    parse_obj_as(
                        type_=TaskDirectiveObject,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def post_v1task_directives_task_id_actions_add_workers(
        self,
        task_id: str,
        *,
        cluster_location: str,
        n_workers: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskforceObject]:
        """
        Creates a new taskforce (and associated workers) for an existing task directive. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        task_id : str
            The ID of the task directive to which the taskforce (and workers) will be added.

        cluster_location : str

        n_workers : typing.Optional[int]
            The number of workers in this taskforce's HTCondor cluster (immutable).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskforceObject]
            The created taskforce object with its details.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/task-directives/{encode_path_param(task_id)}/actions/add-workers",
            method="POST",
            json={
                "cluster_location": cluster_location,
                "n_workers": n_workers,
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
                    TaskforceObject,
                    parse_obj_as(
                        type_=TaskforceObject,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
