

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.attempt_number import AttemptNumber
from ..types.attempt_stats import AttemptStats
from ..types.attempt_stream_stats import AttemptStreamStats
from ..types.attempt_sync_config import AttemptSyncConfig
from ..types.internal_operation_result import InternalOperationResult
from ..types.job_id import JobId
from ..types.workflow_id import WorkflowId
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAttemptClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def save_stats(
        self,
        *,
        attempt_number: AttemptNumber,
        job_id: JobId,
        stats: AttemptStats,
        stream_stats: typing.Optional[typing.Sequence[AttemptStreamStats]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InternalOperationResult]:
        """
        Parameters
        ----------
        attempt_number : AttemptNumber

        job_id : JobId

        stats : AttemptStats

        stream_stats : typing.Optional[typing.Sequence[AttemptStreamStats]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InternalOperationResult]
            Successful Operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/attempt/save_stats",
            method="POST",
            json={
                "attemptNumber": attempt_number,
                "jobId": job_id,
                "stats": convert_and_respect_annotation_metadata(
                    object_=stats, annotation=AttemptStats, direction="write"
                ),
                "streamStats": convert_and_respect_annotation_metadata(
                    object_=stream_stats, annotation=typing.Sequence[AttemptStreamStats], direction="write"
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
                    InternalOperationResult,
                    parse_obj_as(
                        type_=InternalOperationResult,
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

    def save_sync_config(
        self,
        *,
        attempt_number: AttemptNumber,
        job_id: JobId,
        sync_config: AttemptSyncConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InternalOperationResult]:
        """
        Parameters
        ----------
        attempt_number : AttemptNumber

        job_id : JobId

        sync_config : AttemptSyncConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InternalOperationResult]
            Successful Operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/attempt/save_sync_config",
            method="POST",
            json={
                "attemptNumber": attempt_number,
                "jobId": job_id,
                "syncConfig": convert_and_respect_annotation_metadata(
                    object_=sync_config, annotation=AttemptSyncConfig, direction="write"
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
                    InternalOperationResult,
                    parse_obj_as(
                        type_=InternalOperationResult,
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

    def set_workflow_in_attempt(
        self,
        *,
        attempt_number: AttemptNumber,
        job_id: JobId,
        workflow_id: WorkflowId,
        processing_task_queue: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InternalOperationResult]:
        """
        Parameters
        ----------
        attempt_number : AttemptNumber

        job_id : JobId

        workflow_id : WorkflowId

        processing_task_queue : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InternalOperationResult]
            Successful Operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/attempt/set_workflow_in_attempt",
            method="POST",
            json={
                "attemptNumber": attempt_number,
                "jobId": job_id,
                "processingTaskQueue": processing_task_queue,
                "workflowId": workflow_id,
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
                    InternalOperationResult,
                    parse_obj_as(
                        type_=InternalOperationResult,
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


class AsyncRawAttemptClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def save_stats(
        self,
        *,
        attempt_number: AttemptNumber,
        job_id: JobId,
        stats: AttemptStats,
        stream_stats: typing.Optional[typing.Sequence[AttemptStreamStats]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InternalOperationResult]:
        """
        Parameters
        ----------
        attempt_number : AttemptNumber

        job_id : JobId

        stats : AttemptStats

        stream_stats : typing.Optional[typing.Sequence[AttemptStreamStats]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InternalOperationResult]
            Successful Operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/attempt/save_stats",
            method="POST",
            json={
                "attemptNumber": attempt_number,
                "jobId": job_id,
                "stats": convert_and_respect_annotation_metadata(
                    object_=stats, annotation=AttemptStats, direction="write"
                ),
                "streamStats": convert_and_respect_annotation_metadata(
                    object_=stream_stats, annotation=typing.Sequence[AttemptStreamStats], direction="write"
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
                    InternalOperationResult,
                    parse_obj_as(
                        type_=InternalOperationResult,
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

    async def save_sync_config(
        self,
        *,
        attempt_number: AttemptNumber,
        job_id: JobId,
        sync_config: AttemptSyncConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InternalOperationResult]:
        """
        Parameters
        ----------
        attempt_number : AttemptNumber

        job_id : JobId

        sync_config : AttemptSyncConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InternalOperationResult]
            Successful Operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/attempt/save_sync_config",
            method="POST",
            json={
                "attemptNumber": attempt_number,
                "jobId": job_id,
                "syncConfig": convert_and_respect_annotation_metadata(
                    object_=sync_config, annotation=AttemptSyncConfig, direction="write"
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
                    InternalOperationResult,
                    parse_obj_as(
                        type_=InternalOperationResult,
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

    async def set_workflow_in_attempt(
        self,
        *,
        attempt_number: AttemptNumber,
        job_id: JobId,
        workflow_id: WorkflowId,
        processing_task_queue: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InternalOperationResult]:
        """
        Parameters
        ----------
        attempt_number : AttemptNumber

        job_id : JobId

        workflow_id : WorkflowId

        processing_task_queue : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InternalOperationResult]
            Successful Operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/attempt/set_workflow_in_attempt",
            method="POST",
            json={
                "attemptNumber": attempt_number,
                "jobId": job_id,
                "processingTaskQueue": processing_task_queue,
                "workflowId": workflow_id,
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
                    InternalOperationResult,
                    parse_obj_as(
                        type_=InternalOperationResult,
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
