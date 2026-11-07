

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
from ..errors.not_found_error import NotFoundError
from ..types.deactivated_workflow_response_object import DeactivatedWorkflowResponseObject
from ..types.error_response import ErrorResponse
from ..types.workflow_object import WorkflowObject
from .types.post_v1query_workflows_response import PostV1QueryWorkflowsResponse
from .types.post_v1workflows_request_tasks_item import PostV1WorkflowsRequestTasksItem
from .types.post_v1workflows_response import PostV1WorkflowsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWorkflowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_v1query_workflows(
        self,
        *,
        query: typing.Dict[str, typing.Any],
        projection: typing.Optional[typing.Sequence[str]] = OMIT,
        after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1QueryWorkflowsResponse]:
        """
        Queries and returns a list of workflow objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_.

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
        HttpResponse[PostV1QueryWorkflowsResponse]
            Matching workflows and pagination metadata.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/query/workflows",
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
                    PostV1QueryWorkflowsResponse,
                    parse_obj_as(
                        type_=PostV1QueryWorkflowsResponse,
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

    def post_v1workflows(
        self,
        *,
        tasks: typing.Sequence[PostV1WorkflowsRequestTasksItem],
        public_queue_aliases: typing.Sequence[str],
        priority: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1WorkflowsResponse]:
        """
        Creates a new workflow along with its associated task directives and taskforces. See `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_, `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_, `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        tasks : typing.Sequence[PostV1WorkflowsRequestTasksItem]

        public_queue_aliases : typing.Sequence[str]
            User-defined aliases for queues listed in 'input_queue_aliases' and 'output_queue_aliases' that will be used externally. The actual IDs will be generated after submission.

        priority : typing.Optional[int]
            The workflow's priority level relative to other workflows.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1WorkflowsResponse]
            The created workflow, task directives, and taskforces.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/workflows",
            method="POST",
            json={
                "tasks": convert_and_respect_annotation_metadata(
                    object_=tasks, annotation=typing.Sequence[PostV1WorkflowsRequestTasksItem], direction="write"
                ),
                "public_queue_aliases": public_queue_aliases,
                "priority": priority,
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
                    PostV1WorkflowsResponse,
                    parse_obj_as(
                        type_=PostV1WorkflowsResponse,
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

    def get_v1workflows_workflow_id(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkflowObject]:
        """
        Retrieves the workflow object that matches the specified workflow ID. See `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_.

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowObject]
            The matching workflow object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/workflows/{encode_path_param(workflow_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowObject,
                    parse_obj_as(
                        type_=WorkflowObject,
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

    def post_v1workflows_workflow_id_actions_abort(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeactivatedWorkflowResponseObject]:
        """
        Aborts the specified workflow, marks it as deactivated, and sends stop commands to the associated taskforces. See `DeactivatedWorkflowResponseObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#deactivatedworkflowresponseobject>`_.

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeactivatedWorkflowResponseObject]
            Summary of the deactivated workflow.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/workflows/{encode_path_param(workflow_id)}/actions/abort",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeactivatedWorkflowResponseObject,
                    parse_obj_as(
                        type_=DeactivatedWorkflowResponseObject,
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

    def post_v1workflows_workflow_id_actions_finished(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeactivatedWorkflowResponseObject]:
        """
        Marks the specified workflow as finished, marks it as deactivated, and sends stop commands to the associated taskforces. See `DeactivatedWorkflowResponseObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#deactivatedworkflowresponseobject>`_.

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeactivatedWorkflowResponseObject]
            Summary of the deactivated workflow.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/workflows/{encode_path_param(workflow_id)}/actions/finished",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeactivatedWorkflowResponseObject,
                    parse_obj_as(
                        type_=DeactivatedWorkflowResponseObject,
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


class AsyncRawWorkflowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_v1query_workflows(
        self,
        *,
        query: typing.Dict[str, typing.Any],
        projection: typing.Optional[typing.Sequence[str]] = OMIT,
        after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1QueryWorkflowsResponse]:
        """
        Queries and returns a list of workflow objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_.

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
        AsyncHttpResponse[PostV1QueryWorkflowsResponse]
            Matching workflows and pagination metadata.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/query/workflows",
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
                    PostV1QueryWorkflowsResponse,
                    parse_obj_as(
                        type_=PostV1QueryWorkflowsResponse,
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

    async def post_v1workflows(
        self,
        *,
        tasks: typing.Sequence[PostV1WorkflowsRequestTasksItem],
        public_queue_aliases: typing.Sequence[str],
        priority: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1WorkflowsResponse]:
        """
        Creates a new workflow along with its associated task directives and taskforces. See `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_, `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_, `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        tasks : typing.Sequence[PostV1WorkflowsRequestTasksItem]

        public_queue_aliases : typing.Sequence[str]
            User-defined aliases for queues listed in 'input_queue_aliases' and 'output_queue_aliases' that will be used externally. The actual IDs will be generated after submission.

        priority : typing.Optional[int]
            The workflow's priority level relative to other workflows.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1WorkflowsResponse]
            The created workflow, task directives, and taskforces.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/workflows",
            method="POST",
            json={
                "tasks": convert_and_respect_annotation_metadata(
                    object_=tasks, annotation=typing.Sequence[PostV1WorkflowsRequestTasksItem], direction="write"
                ),
                "public_queue_aliases": public_queue_aliases,
                "priority": priority,
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
                    PostV1WorkflowsResponse,
                    parse_obj_as(
                        type_=PostV1WorkflowsResponse,
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

    async def get_v1workflows_workflow_id(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkflowObject]:
        """
        Retrieves the workflow object that matches the specified workflow ID. See `WorkflowObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#workflowobject>`_.

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowObject]
            The matching workflow object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/workflows/{encode_path_param(workflow_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowObject,
                    parse_obj_as(
                        type_=WorkflowObject,
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

    async def post_v1workflows_workflow_id_actions_abort(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeactivatedWorkflowResponseObject]:
        """
        Aborts the specified workflow, marks it as deactivated, and sends stop commands to the associated taskforces. See `DeactivatedWorkflowResponseObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#deactivatedworkflowresponseobject>`_.

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeactivatedWorkflowResponseObject]
            Summary of the deactivated workflow.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/workflows/{encode_path_param(workflow_id)}/actions/abort",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeactivatedWorkflowResponseObject,
                    parse_obj_as(
                        type_=DeactivatedWorkflowResponseObject,
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

    async def post_v1workflows_workflow_id_actions_finished(
        self, workflow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeactivatedWorkflowResponseObject]:
        """
        Marks the specified workflow as finished, marks it as deactivated, and sends stop commands to the associated taskforces. See `DeactivatedWorkflowResponseObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#deactivatedworkflowresponseobject>`_.

        Parameters
        ----------
        workflow_id : str
            The ID of the workflow object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeactivatedWorkflowResponseObject]
            Summary of the deactivated workflow.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/workflows/{encode_path_param(workflow_id)}/actions/finished",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeactivatedWorkflowResponseObject,
                    parse_obj_as(
                        type_=DeactivatedWorkflowResponseObject,
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
