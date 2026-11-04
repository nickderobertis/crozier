

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.taskforce_object_phase import TaskforceObjectPhase
from ..types.taskforce_object_phase_change_log_item import TaskforceObjectPhaseChangeLogItem
from ..types.taskforce_object_pilot_config import TaskforceObjectPilotConfig
from ..types.taskforce_object_submit_dict_value import TaskforceObjectSubmitDictValue
from ..types.taskforce_object_worker_config import TaskforceObjectWorkerConfig
from .raw_client import AsyncRawTmsInternalClient, RawTmsInternalClient
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


OMIT = typing.cast(typing.Any, ...)


class TmsInternalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTmsInternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTmsInternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTmsInternalClient
        """
        return self._raw_client

    def post_v1tms_condor_complete_taskforces_taskforce_uuid(
        self, taskforce_uuid: str, *, condor_complete_ts: int, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse:
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
        PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse
            The UUID of the updated taskforce object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tms_internal.post_v1tms_condor_complete_taskforces_taskforce_uuid(
            taskforce_uuid="taskforce_uuid",
            condor_complete_ts=1,
        )
        """
        _response = self._raw_client.post_v1tms_condor_complete_taskforces_taskforce_uuid(
            taskforce_uuid, condor_complete_ts=condor_complete_ts, request_options=request_options
        )
        return _response.data

    def post_v1tms_condor_rm_taskforces_taskforce_uuid(
        self, taskforce_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV1TmsCondorRmTaskforcesTaskforceUuidResponse:
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
        PostV1TmsCondorRmTaskforcesTaskforceUuidResponse
            The UUID of the updated taskforce object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tms_internal.post_v1tms_condor_rm_taskforces_taskforce_uuid(
            taskforce_uuid="taskforce_uuid",
        )
        """
        _response = self._raw_client.post_v1tms_condor_rm_taskforces_taskforce_uuid(
            taskforce_uuid, request_options=request_options
        )
        return _response.data

    def post_v1tms_condor_rm_taskforces_taskforce_uuid_failed(
        self,
        taskforce_uuid: str,
        *,
        error: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse:
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
        PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse
            The UUID of the updated taskforce object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tms_internal.post_v1tms_condor_rm_taskforces_taskforce_uuid_failed(
            taskforce_uuid="taskforce_uuid",
        )
        """
        _response = self._raw_client.post_v1tms_condor_rm_taskforces_taskforce_uuid_failed(
            taskforce_uuid, error=error, request_options=request_options
        )
        return _response.data

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
    ) -> PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse:
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
        PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse
            The UUID of the updated taskforce object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tms_internal.post_v1tms_condor_submit_taskforces_taskforce_uuid(
            taskforce_uuid_="taskforce_uuid",
        )
        """
        _response = self._raw_client.post_v1tms_condor_submit_taskforces_taskforce_uuid(
            taskforce_uuid_,
            taskforce_uuid=taskforce_uuid,
            task_id=task_id,
            workflow_id=workflow_id,
            timestamp=timestamp,
            priority=priority,
            collector=collector,
            schedd=schedd,
            n_workers=n_workers,
            pilot_config=pilot_config,
            worker_config=worker_config,
            cluster_id=cluster_id,
            submit_dict=submit_dict,
            job_event_log_fpath=job_event_log_fpath,
            phase=phase,
            phase_change_log=phase_change_log,
            compound_statuses=compound_statuses,
            top_task_errors=top_task_errors,
            request_options=request_options,
        )
        return _response.data

    def post_v1tms_condor_submit_taskforces_taskforce_uuid_failed(
        self,
        taskforce_uuid: str,
        *,
        error: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse:
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
        PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse
            The UUID of the updated taskforce object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tms_internal.post_v1tms_condor_submit_taskforces_taskforce_uuid_failed(
            taskforce_uuid="taskforce_uuid",
        )
        """
        _response = self._raw_client.post_v1tms_condor_submit_taskforces_taskforce_uuid_failed(
            taskforce_uuid, error=error, request_options=request_options
        )
        return _response.data

    def get_v1tms_pending_starter_taskforces(
        self,
        *,
        schedd: str,
        collector: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1TmsPendingStarterTaskforcesResponse:
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
        GetV1TmsPendingStarterTaskforcesResponse
            The next taskforce to start at the HTCondor location.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tms_internal.get_v1tms_pending_starter_taskforces(
            schedd="schedd",
        )
        """
        _response = self._raw_client.get_v1tms_pending_starter_taskforces(
            schedd=schedd, collector=collector, request_options=request_options
        )
        return _response.data

    def get_v1tms_pending_stopper_taskforces(
        self,
        *,
        schedd: str,
        collector: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1TmsPendingStopperTaskforcesResponse:
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
        GetV1TmsPendingStopperTaskforcesResponse
            The next taskforce to stop at the HTCondor location.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tms_internal.get_v1tms_pending_stopper_taskforces(
            schedd="schedd",
        )
        """
        _response = self._raw_client.get_v1tms_pending_stopper_taskforces(
            schedd=schedd, collector=collector, request_options=request_options
        )
        return _response.data

    def post_v1tms_statuses_taskforces(
        self,
        *,
        top_task_errors_by_taskforce: typing.Optional[typing.Dict[str, typing.Dict[str, int]]] = OMIT,
        compound_statuses_by_taskforce: typing.Optional[
            typing.Dict[str, typing.Dict[str, typing.Dict[str, int]]]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1TmsStatusesTaskforcesResponse:
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
        PostV1TmsStatusesTaskforcesResponse
            Individual update results for each UUID.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tms_internal.post_v1tms_statuses_taskforces()
        """
        _response = self._raw_client.post_v1tms_statuses_taskforces(
            top_task_errors_by_taskforce=top_task_errors_by_taskforce,
            compound_statuses_by_taskforce=compound_statuses_by_taskforce,
            request_options=request_options,
        )
        return _response.data


class AsyncTmsInternalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTmsInternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTmsInternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTmsInternalClient
        """
        return self._raw_client

    async def post_v1tms_condor_complete_taskforces_taskforce_uuid(
        self, taskforce_uuid: str, *, condor_complete_ts: int, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse:
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
        PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse
            The UUID of the updated taskforce object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tms_internal.post_v1tms_condor_complete_taskforces_taskforce_uuid(
                taskforce_uuid="taskforce_uuid",
                condor_complete_ts=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1tms_condor_complete_taskforces_taskforce_uuid(
            taskforce_uuid, condor_complete_ts=condor_complete_ts, request_options=request_options
        )
        return _response.data

    async def post_v1tms_condor_rm_taskforces_taskforce_uuid(
        self, taskforce_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV1TmsCondorRmTaskforcesTaskforceUuidResponse:
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
        PostV1TmsCondorRmTaskforcesTaskforceUuidResponse
            The UUID of the updated taskforce object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tms_internal.post_v1tms_condor_rm_taskforces_taskforce_uuid(
                taskforce_uuid="taskforce_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1tms_condor_rm_taskforces_taskforce_uuid(
            taskforce_uuid, request_options=request_options
        )
        return _response.data

    async def post_v1tms_condor_rm_taskforces_taskforce_uuid_failed(
        self,
        taskforce_uuid: str,
        *,
        error: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse:
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
        PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse
            The UUID of the updated taskforce object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tms_internal.post_v1tms_condor_rm_taskforces_taskforce_uuid_failed(
                taskforce_uuid="taskforce_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1tms_condor_rm_taskforces_taskforce_uuid_failed(
            taskforce_uuid, error=error, request_options=request_options
        )
        return _response.data

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
    ) -> PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse:
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
        PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse
            The UUID of the updated taskforce object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tms_internal.post_v1tms_condor_submit_taskforces_taskforce_uuid(
                taskforce_uuid_="taskforce_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1tms_condor_submit_taskforces_taskforce_uuid(
            taskforce_uuid_,
            taskforce_uuid=taskforce_uuid,
            task_id=task_id,
            workflow_id=workflow_id,
            timestamp=timestamp,
            priority=priority,
            collector=collector,
            schedd=schedd,
            n_workers=n_workers,
            pilot_config=pilot_config,
            worker_config=worker_config,
            cluster_id=cluster_id,
            submit_dict=submit_dict,
            job_event_log_fpath=job_event_log_fpath,
            phase=phase,
            phase_change_log=phase_change_log,
            compound_statuses=compound_statuses,
            top_task_errors=top_task_errors,
            request_options=request_options,
        )
        return _response.data

    async def post_v1tms_condor_submit_taskforces_taskforce_uuid_failed(
        self,
        taskforce_uuid: str,
        *,
        error: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse:
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
        PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse
            The UUID of the updated taskforce object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tms_internal.post_v1tms_condor_submit_taskforces_taskforce_uuid_failed(
                taskforce_uuid="taskforce_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1tms_condor_submit_taskforces_taskforce_uuid_failed(
            taskforce_uuid, error=error, request_options=request_options
        )
        return _response.data

    async def get_v1tms_pending_starter_taskforces(
        self,
        *,
        schedd: str,
        collector: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1TmsPendingStarterTaskforcesResponse:
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
        GetV1TmsPendingStarterTaskforcesResponse
            The next taskforce to start at the HTCondor location.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tms_internal.get_v1tms_pending_starter_taskforces(
                schedd="schedd",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1tms_pending_starter_taskforces(
            schedd=schedd, collector=collector, request_options=request_options
        )
        return _response.data

    async def get_v1tms_pending_stopper_taskforces(
        self,
        *,
        schedd: str,
        collector: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1TmsPendingStopperTaskforcesResponse:
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
        GetV1TmsPendingStopperTaskforcesResponse
            The next taskforce to stop at the HTCondor location.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tms_internal.get_v1tms_pending_stopper_taskforces(
                schedd="schedd",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1tms_pending_stopper_taskforces(
            schedd=schedd, collector=collector, request_options=request_options
        )
        return _response.data

    async def post_v1tms_statuses_taskforces(
        self,
        *,
        top_task_errors_by_taskforce: typing.Optional[typing.Dict[str, typing.Dict[str, int]]] = OMIT,
        compound_statuses_by_taskforce: typing.Optional[
            typing.Dict[str, typing.Dict[str, typing.Dict[str, int]]]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1TmsStatusesTaskforcesResponse:
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
        PostV1TmsStatusesTaskforcesResponse
            Individual update results for each UUID.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tms_internal.post_v1tms_statuses_taskforces()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1tms_statuses_taskforces(
            top_task_errors_by_taskforce=top_task_errors_by_taskforce,
            compound_statuses_by_taskforce=compound_statuses_by_taskforce,
            request_options=request_options,
        )
        return _response.data
