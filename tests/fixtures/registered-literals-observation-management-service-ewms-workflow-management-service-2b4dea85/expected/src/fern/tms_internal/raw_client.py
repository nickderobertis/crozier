

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
from ..types.error_response import ErrorResponse
from ..types.taskforce_object_phase import TaskforceObjectPhase
from ..types.taskforce_object_phase_change_log_item import TaskforceObjectPhaseChangeLogItem
from ..types.taskforce_object_pilot_config import TaskforceObjectPilotConfig
from ..types.taskforce_object_submit_dict_value import TaskforceObjectSubmitDictValue
from ..types.taskforce_object_worker_config import TaskforceObjectWorkerConfig
from .types.get_v1tms_pending_starter_taskforces_response import GetV1TmsPendingStarterTaskforcesResponse
from .types.get_v1tms_pending_stopper_taskforces_response import GetV1TmsPendingStopperTaskforcesResponse
from .types.post_v1tms_condor_complete_taskforces_taskforce_uuid_response import (
    PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse,
)
from .types.post_v1tms_condor_rm_taskforces_taskforce_uuid_failed_response import (
    PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse,
)
from .types.post_v1tms_condor_rm_taskforces_taskforce_uuid_response import (
    PostV1TmsCondorRmTaskforcesTaskforceUuidResponse,
)
from .types.post_v1tms_condor_submit_taskforces_taskforce_uuid_failed_response import (
    PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse,
)
from .types.post_v1tms_condor_submit_taskforces_taskforce_uuid_response import (
    PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse,
)
from .types.post_v1tms_statuses_taskforces_response import PostV1TmsStatusesTaskforcesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTmsInternalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_v1tms_condor_complete_taskforces_taskforce_uuid(
        self, taskforce_uuid: str, *, condor_complete_ts: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse]:
        """
        For internal use only (TMS): Updates the specified taskforce with the completion timestamp of the HTCondor cluster. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        taskforce_uuid : str
            UUID of the taskforce.

        condor_complete_ts : int
            The time when the taskforce's HTCondor cluster ended.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse]
            The UUID of the updated taskforce object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tms/condor-complete/taskforces/{encode_path_param(taskforce_uuid)}",
            method="POST",
            json={
                "condor_complete_ts": condor_complete_ts,
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
                    PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse,
                    parse_obj_as(
                        type_=PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse,
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

    def post_v1tms_condor_rm_taskforces_taskforce_uuid(
        self, taskforce_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV1TmsCondorRmTaskforcesTaskforceUuidResponse]:
        """
        For internal use only (TMS): Confirms that a taskforce has been removed on HTCondor. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        taskforce_uuid : str
            UUID of the taskforce.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1TmsCondorRmTaskforcesTaskforceUuidResponse]
            The UUID of the updated taskforce object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tms/condor-rm/taskforces/{encode_path_param(taskforce_uuid)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostV1TmsCondorRmTaskforcesTaskforceUuidResponse,
                    parse_obj_as(
                        type_=PostV1TmsCondorRmTaskforcesTaskforceUuidResponse,
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

    def post_v1tms_condor_rm_taskforces_taskforce_uuid_failed(
        self,
        taskforce_uuid: str,
        *,
        error: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse]:
        """
        For internal use only (TMS): Communicates that a taskforce failed to be removed on HTCondor. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        taskforce_uuid : str
            UUID of the taskforce.

        error : typing.Optional[str]
            A description of why the taskforce could not be removed from HTCondor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse]
            The UUID of the updated taskforce object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tms/condor-rm/taskforces/{encode_path_param(taskforce_uuid)}/failed",
            method="POST",
            json={
                "error": error,
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
                    PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse,
                    parse_obj_as(
                        type_=PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse,
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

    def post_v1tms_condor_submit_taskforces_taskforce_uuid(
        self,
        taskforce_uuid_: str,
        *,
        taskforce_uuid: typing.Optional[str] = OMIT,
        task_id: typing.Optional[str] = OMIT,
        workflow_id: typing.Optional[str] = OMIT,
        timestamp: typing.Optional[float] = OMIT,
        priority: typing.Optional[int] = OMIT,
        collector: typing.Optional[str] = OMIT,
        schedd: typing.Optional[str] = OMIT,
        n_workers: typing.Optional[int] = OMIT,
        pilot_config: typing.Optional[TaskforceObjectPilotConfig] = OMIT,
        worker_config: typing.Optional[TaskforceObjectWorkerConfig] = OMIT,
        cluster_id: typing.Optional[int] = OMIT,
        submit_dict: typing.Optional[typing.Dict[str, TaskforceObjectSubmitDictValue]] = OMIT,
        job_event_log_fpath: typing.Optional[str] = OMIT,
        phase: typing.Optional[TaskforceObjectPhase] = OMIT,
        phase_change_log: typing.Optional[typing.Sequence[TaskforceObjectPhaseChangeLogItem]] = OMIT,
        compound_statuses: typing.Optional[typing.Dict[str, typing.Dict[str, int]]] = OMIT,
        top_task_errors: typing.Optional[typing.Dict[str, int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse]:
        """
        For internal use only (TMS): Confirms that a taskforce has been submitted to HTCondor for execution. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        taskforce_uuid_ : str
            UUID of the taskforce.

        taskforce_uuid : typing.Optional[str]
            A unique identifier automatically generated for this taskforce.

        task_id : typing.Optional[str]
            The identifier of the associated task directive object (N taskforces : 1 task directive).

        workflow_id : typing.Optional[str]
            The identifier of the overarching workflow object (N*M taskforces : M task directives : 1 workflow).

        timestamp : typing.Optional[float]
            The epoch time when this taskforce was created.

        priority : typing.Optional[int]
            The priority level relative to other taskforces (usually, this value is inherited from the parent workflow object).

        collector : typing.Optional[str]
            Deprecated. Address of the HTCondor collector; no longer used.

        schedd : typing.Optional[str]
            The address of the HTCondor schedd.

        n_workers : typing.Optional[int]
            The number of workers in this taskforce's HTCondor cluster (immutable).

        pilot_config : typing.Optional[TaskforceObjectPilotConfig]
            Configuration settings for the EWMS pilot.

        worker_config : typing.Optional[TaskforceObjectWorkerConfig]
            Configuration settings for the HTCondor cluster submission.

        cluster_id : typing.Optional[int]
            The identifier for the associated HTCondor cluster.

        submit_dict : typing.Optional[typing.Dict[str, TaskforceObjectSubmitDictValue]]
            The actual HTCondor submit class ad.

        job_event_log_fpath : typing.Optional[str]
            The file path on the HTCondor AP containing job event logs.

        phase : typing.Optional[TaskforceObjectPhase]
            The current phase of the taskforce within the workflow's lifetime. Not all taskforces will enter every phase.

        phase_change_log : typing.Optional[typing.Sequence[TaskforceObjectPhaseChangeLogItem]]
            A record of all attempted phase changes, including both successful and unsuccessful ones.

        compound_statuses : typing.Optional[typing.Dict[str, typing.Dict[str, int]]]
            Aggregated status of the workers, represented as a nested dictionary mapping HTCondor states to EWMS pilot states and their counts.

        top_task_errors : typing.Optional[typing.Dict[str, int]]
            The most common errors encountered by workers, paired with their occurrence counts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse]
            The UUID of the updated taskforce object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tms/condor-submit/taskforces/{encode_path_param(taskforce_uuid_)}",
            method="POST",
            json={
                "taskforce_uuid": taskforce_uuid,
                "task_id": task_id,
                "workflow_id": workflow_id,
                "timestamp": timestamp,
                "priority": priority,
                "collector": collector,
                "schedd": schedd,
                "n_workers": n_workers,
                "pilot_config": convert_and_respect_annotation_metadata(
                    object_=pilot_config, annotation=TaskforceObjectPilotConfig, direction="write"
                ),
                "worker_config": convert_and_respect_annotation_metadata(
                    object_=worker_config, annotation=TaskforceObjectWorkerConfig, direction="write"
                ),
                "cluster_id": cluster_id,
                "submit_dict": convert_and_respect_annotation_metadata(
                    object_=submit_dict, annotation=typing.Dict[str, TaskforceObjectSubmitDictValue], direction="write"
                ),
                "job_event_log_fpath": job_event_log_fpath,
                "phase": phase,
                "phase_change_log": convert_and_respect_annotation_metadata(
                    object_=phase_change_log,
                    annotation=typing.Sequence[TaskforceObjectPhaseChangeLogItem],
                    direction="write",
                ),
                "compound_statuses": compound_statuses,
                "top_task_errors": top_task_errors,
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
                    PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse,
                    parse_obj_as(
                        type_=PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse,
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

    def post_v1tms_condor_submit_taskforces_taskforce_uuid_failed(
        self,
        taskforce_uuid: str,
        *,
        error: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse]:
        """
        For internal use only (TMS): Communicates that a taskforce failed to be submitted to HTCondor for execution. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        taskforce_uuid : str
            UUID of the taskforce.

        error : typing.Optional[str]
            A description of why the taskforce could not be submitted to HTCondor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse]
            The UUID of the updated taskforce object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/tms/condor-submit/taskforces/{encode_path_param(taskforce_uuid)}/failed",
            method="POST",
            json={
                "error": error,
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
                    PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse,
                    parse_obj_as(
                        type_=PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse,
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

    def get_v1tms_pending_starter_taskforces(
        self,
        *,
        schedd: str,
        collector: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetV1TmsPendingStarterTaskforcesResponse]:
        """
        For internal use only (TMS): Retrieves the next taskforce ready to start at the specified HTCondor location. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_, `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_, `MQProfileObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/mqs-objects.html#mqprofileobject>`_.

        Parameters
        ----------
        schedd : str
            Name of the HTCondor schedd.

        collector : typing.Optional[str]
            Deprecated. Name of the HTCondor collector; no longer used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetV1TmsPendingStarterTaskforcesResponse]
            The next taskforce to start at the HTCondor location.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tms/pending-starter/taskforces",
            method="GET",
            params={
                "collector": collector,
                "schedd": schedd,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1TmsPendingStarterTaskforcesResponse,
                    parse_obj_as(
                        type_=GetV1TmsPendingStarterTaskforcesResponse,
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

    def get_v1tms_pending_stopper_taskforces(
        self,
        *,
        schedd: str,
        collector: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetV1TmsPendingStopperTaskforcesResponse]:
        """
        For internal use only (TMS): Retrieves the next taskforce ready to stop at the specified HTCondor location. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        schedd : str
            Name of the HTCondor schedd.

        collector : typing.Optional[str]
            Deprecated. Name of the HTCondor collector; no longer used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetV1TmsPendingStopperTaskforcesResponse]
            The next taskforce to stop at the HTCondor location.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tms/pending-stopper/taskforces",
            method="GET",
            params={
                "collector": collector,
                "schedd": schedd,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1TmsPendingStopperTaskforcesResponse,
                    parse_obj_as(
                        type_=GetV1TmsPendingStopperTaskforcesResponse,
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

    def post_v1tms_statuses_taskforces(
        self,
        *,
        top_task_errors_by_taskforce: typing.Optional[typing.Dict[str, typing.Dict[str, int]]] = OMIT,
        compound_statuses_by_taskforce: typing.Optional[
            typing.Dict[str, typing.Dict[str, typing.Dict[str, int]]]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV1TmsStatusesTaskforcesResponse]:
        """
        For internal use only (TMS): Updates and returns the statuses and errors for the specified taskforces. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        top_task_errors_by_taskforce : typing.Optional[typing.Dict[str, typing.Dict[str, int]]]
            The top errors (paired with a count) for each indicated taskforce

        compound_statuses_by_taskforce : typing.Optional[typing.Dict[str, typing.Dict[str, typing.Dict[str, int]]]]
            The compound statuses (status -> state -> count) for the indicated taskforces

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1TmsStatusesTaskforcesResponse]
            Individual update results for each UUID.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/tms/statuses/taskforces",
            method="POST",
            json={
                "top_task_errors_by_taskforce": top_task_errors_by_taskforce,
                "compound_statuses_by_taskforce": compound_statuses_by_taskforce,
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
                    PostV1TmsStatusesTaskforcesResponse,
                    parse_obj_as(
                        type_=PostV1TmsStatusesTaskforcesResponse,
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


class AsyncRawTmsInternalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_v1tms_condor_complete_taskforces_taskforce_uuid(
        self, taskforce_uuid: str, *, condor_complete_ts: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse]:
        """
        For internal use only (TMS): Updates the specified taskforce with the completion timestamp of the HTCondor cluster. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        taskforce_uuid : str
            UUID of the taskforce.

        condor_complete_ts : int
            The time when the taskforce's HTCondor cluster ended.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse]
            The UUID of the updated taskforce object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tms/condor-complete/taskforces/{encode_path_param(taskforce_uuid)}",
            method="POST",
            json={
                "condor_complete_ts": condor_complete_ts,
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
                    PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse,
                    parse_obj_as(
                        type_=PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse,
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

    async def post_v1tms_condor_rm_taskforces_taskforce_uuid(
        self, taskforce_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV1TmsCondorRmTaskforcesTaskforceUuidResponse]:
        """
        For internal use only (TMS): Confirms that a taskforce has been removed on HTCondor. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        taskforce_uuid : str
            UUID of the taskforce.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1TmsCondorRmTaskforcesTaskforceUuidResponse]
            The UUID of the updated taskforce object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tms/condor-rm/taskforces/{encode_path_param(taskforce_uuid)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostV1TmsCondorRmTaskforcesTaskforceUuidResponse,
                    parse_obj_as(
                        type_=PostV1TmsCondorRmTaskforcesTaskforceUuidResponse,
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

    async def post_v1tms_condor_rm_taskforces_taskforce_uuid_failed(
        self,
        taskforce_uuid: str,
        *,
        error: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse]:
        """
        For internal use only (TMS): Communicates that a taskforce failed to be removed on HTCondor. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        taskforce_uuid : str
            UUID of the taskforce.

        error : typing.Optional[str]
            A description of why the taskforce could not be removed from HTCondor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse]
            The UUID of the updated taskforce object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tms/condor-rm/taskforces/{encode_path_param(taskforce_uuid)}/failed",
            method="POST",
            json={
                "error": error,
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
                    PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse,
                    parse_obj_as(
                        type_=PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse,
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

    async def post_v1tms_condor_submit_taskforces_taskforce_uuid(
        self,
        taskforce_uuid_: str,
        *,
        taskforce_uuid: typing.Optional[str] = OMIT,
        task_id: typing.Optional[str] = OMIT,
        workflow_id: typing.Optional[str] = OMIT,
        timestamp: typing.Optional[float] = OMIT,
        priority: typing.Optional[int] = OMIT,
        collector: typing.Optional[str] = OMIT,
        schedd: typing.Optional[str] = OMIT,
        n_workers: typing.Optional[int] = OMIT,
        pilot_config: typing.Optional[TaskforceObjectPilotConfig] = OMIT,
        worker_config: typing.Optional[TaskforceObjectWorkerConfig] = OMIT,
        cluster_id: typing.Optional[int] = OMIT,
        submit_dict: typing.Optional[typing.Dict[str, TaskforceObjectSubmitDictValue]] = OMIT,
        job_event_log_fpath: typing.Optional[str] = OMIT,
        phase: typing.Optional[TaskforceObjectPhase] = OMIT,
        phase_change_log: typing.Optional[typing.Sequence[TaskforceObjectPhaseChangeLogItem]] = OMIT,
        compound_statuses: typing.Optional[typing.Dict[str, typing.Dict[str, int]]] = OMIT,
        top_task_errors: typing.Optional[typing.Dict[str, int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse]:
        """
        For internal use only (TMS): Confirms that a taskforce has been submitted to HTCondor for execution. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        taskforce_uuid_ : str
            UUID of the taskforce.

        taskforce_uuid : typing.Optional[str]
            A unique identifier automatically generated for this taskforce.

        task_id : typing.Optional[str]
            The identifier of the associated task directive object (N taskforces : 1 task directive).

        workflow_id : typing.Optional[str]
            The identifier of the overarching workflow object (N*M taskforces : M task directives : 1 workflow).

        timestamp : typing.Optional[float]
            The epoch time when this taskforce was created.

        priority : typing.Optional[int]
            The priority level relative to other taskforces (usually, this value is inherited from the parent workflow object).

        collector : typing.Optional[str]
            Deprecated. Address of the HTCondor collector; no longer used.

        schedd : typing.Optional[str]
            The address of the HTCondor schedd.

        n_workers : typing.Optional[int]
            The number of workers in this taskforce's HTCondor cluster (immutable).

        pilot_config : typing.Optional[TaskforceObjectPilotConfig]
            Configuration settings for the EWMS pilot.

        worker_config : typing.Optional[TaskforceObjectWorkerConfig]
            Configuration settings for the HTCondor cluster submission.

        cluster_id : typing.Optional[int]
            The identifier for the associated HTCondor cluster.

        submit_dict : typing.Optional[typing.Dict[str, TaskforceObjectSubmitDictValue]]
            The actual HTCondor submit class ad.

        job_event_log_fpath : typing.Optional[str]
            The file path on the HTCondor AP containing job event logs.

        phase : typing.Optional[TaskforceObjectPhase]
            The current phase of the taskforce within the workflow's lifetime. Not all taskforces will enter every phase.

        phase_change_log : typing.Optional[typing.Sequence[TaskforceObjectPhaseChangeLogItem]]
            A record of all attempted phase changes, including both successful and unsuccessful ones.

        compound_statuses : typing.Optional[typing.Dict[str, typing.Dict[str, int]]]
            Aggregated status of the workers, represented as a nested dictionary mapping HTCondor states to EWMS pilot states and their counts.

        top_task_errors : typing.Optional[typing.Dict[str, int]]
            The most common errors encountered by workers, paired with their occurrence counts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse]
            The UUID of the updated taskforce object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tms/condor-submit/taskforces/{encode_path_param(taskforce_uuid_)}",
            method="POST",
            json={
                "taskforce_uuid": taskforce_uuid,
                "task_id": task_id,
                "workflow_id": workflow_id,
                "timestamp": timestamp,
                "priority": priority,
                "collector": collector,
                "schedd": schedd,
                "n_workers": n_workers,
                "pilot_config": convert_and_respect_annotation_metadata(
                    object_=pilot_config, annotation=TaskforceObjectPilotConfig, direction="write"
                ),
                "worker_config": convert_and_respect_annotation_metadata(
                    object_=worker_config, annotation=TaskforceObjectWorkerConfig, direction="write"
                ),
                "cluster_id": cluster_id,
                "submit_dict": convert_and_respect_annotation_metadata(
                    object_=submit_dict, annotation=typing.Dict[str, TaskforceObjectSubmitDictValue], direction="write"
                ),
                "job_event_log_fpath": job_event_log_fpath,
                "phase": phase,
                "phase_change_log": convert_and_respect_annotation_metadata(
                    object_=phase_change_log,
                    annotation=typing.Sequence[TaskforceObjectPhaseChangeLogItem],
                    direction="write",
                ),
                "compound_statuses": compound_statuses,
                "top_task_errors": top_task_errors,
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
                    PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse,
                    parse_obj_as(
                        type_=PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse,
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

    async def post_v1tms_condor_submit_taskforces_taskforce_uuid_failed(
        self,
        taskforce_uuid: str,
        *,
        error: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse]:
        """
        For internal use only (TMS): Communicates that a taskforce failed to be submitted to HTCondor for execution. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        taskforce_uuid : str
            UUID of the taskforce.

        error : typing.Optional[str]
            A description of why the taskforce could not be submitted to HTCondor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse]
            The UUID of the updated taskforce object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/tms/condor-submit/taskforces/{encode_path_param(taskforce_uuid)}/failed",
            method="POST",
            json={
                "error": error,
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
                    PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse,
                    parse_obj_as(
                        type_=PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse,
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

    async def get_v1tms_pending_starter_taskforces(
        self,
        *,
        schedd: str,
        collector: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetV1TmsPendingStarterTaskforcesResponse]:
        """
        For internal use only (TMS): Retrieves the next taskforce ready to start at the specified HTCondor location. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_, `TaskDirectiveObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskdirectiveobject>`_, `MQProfileObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/mqs-objects.html#mqprofileobject>`_.

        Parameters
        ----------
        schedd : str
            Name of the HTCondor schedd.

        collector : typing.Optional[str]
            Deprecated. Name of the HTCondor collector; no longer used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetV1TmsPendingStarterTaskforcesResponse]
            The next taskforce to start at the HTCondor location.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tms/pending-starter/taskforces",
            method="GET",
            params={
                "collector": collector,
                "schedd": schedd,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1TmsPendingStarterTaskforcesResponse,
                    parse_obj_as(
                        type_=GetV1TmsPendingStarterTaskforcesResponse,
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

    async def get_v1tms_pending_stopper_taskforces(
        self,
        *,
        schedd: str,
        collector: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetV1TmsPendingStopperTaskforcesResponse]:
        """
        For internal use only (TMS): Retrieves the next taskforce ready to stop at the specified HTCondor location. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        schedd : str
            Name of the HTCondor schedd.

        collector : typing.Optional[str]
            Deprecated. Name of the HTCondor collector; no longer used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetV1TmsPendingStopperTaskforcesResponse]
            The next taskforce to stop at the HTCondor location.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tms/pending-stopper/taskforces",
            method="GET",
            params={
                "collector": collector,
                "schedd": schedd,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1TmsPendingStopperTaskforcesResponse,
                    parse_obj_as(
                        type_=GetV1TmsPendingStopperTaskforcesResponse,
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

    async def post_v1tms_statuses_taskforces(
        self,
        *,
        top_task_errors_by_taskforce: typing.Optional[typing.Dict[str, typing.Dict[str, int]]] = OMIT,
        compound_statuses_by_taskforce: typing.Optional[
            typing.Dict[str, typing.Dict[str, typing.Dict[str, int]]]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV1TmsStatusesTaskforcesResponse]:
        """
        For internal use only (TMS): Updates and returns the statuses and errors for the specified taskforces. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        top_task_errors_by_taskforce : typing.Optional[typing.Dict[str, typing.Dict[str, int]]]
            The top errors (paired with a count) for each indicated taskforce

        compound_statuses_by_taskforce : typing.Optional[typing.Dict[str, typing.Dict[str, typing.Dict[str, int]]]]
            The compound statuses (status -> state -> count) for the indicated taskforces

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1TmsStatusesTaskforcesResponse]
            Individual update results for each UUID.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/tms/statuses/taskforces",
            method="POST",
            json={
                "top_task_errors_by_taskforce": top_task_errors_by_taskforce,
                "compound_statuses_by_taskforce": compound_statuses_by_taskforce,
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
                    PostV1TmsStatusesTaskforcesResponse,
                    parse_obj_as(
                        type_=PostV1TmsStatusesTaskforcesResponse,
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
