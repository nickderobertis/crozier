

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dag import Dag
from ..types.dag_collection import DagCollection
from ..types.dag_detail import DagDetail
from ..types.schedule_interval import ScheduleInterval
from ..types.tag import Tag
from ..types.task import Task
from ..types.task_collection import TaskCollection
from ..types.task_instance_reference_collection import TaskInstanceReferenceCollection
from .raw_client import AsyncRawDagClient, RawDagClient
from .types.get_dag_source_response import GetDagSourceResponse
from .types.update_task_instances_state_new_state import UpdateTaskInstancesStateNewState


OMIT = typing.cast(typing.Any, ...)


class DagClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDagClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDagClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDagClient
        """
        return self._raw_client

    def get_dag_source(
        self, file_token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDagSourceResponse:
        """
        Get a source code using file token.

        Parameters
        ----------
        file_token : str
            The key containing the encrypted path to the file. Encryption and decryption take place only on
            the server. This prevents the client from reading an non-DAG file. This also ensures API
            extensibility, because the format of encrypted data may change.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDagSourceResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag.get_dag_source(
            file_token="file_token",
        )
        """
        _response = self._raw_client.get_dag_source(file_token, request_options=request_options)
        return _response.data

    def get_dags(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        only_active: typing.Optional[bool] = None,
        dag_id_pattern: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagCollection:
        """
        List DAGs in the database.
        `dag_id_pattern` can be set to match dags of a specific pattern

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of tags to filter results.

            *New in version 2.2.0*

        only_active : typing.Optional[bool]
            Only filter active DAGs.

            *New in version 2.1.1*

        dag_id_pattern : typing.Optional[str]
            If set, only return DAGs with dag_ids matching this pattern.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag.get_dags()
        """
        _response = self._raw_client.get_dags(
            limit=limit,
            offset=offset,
            order_by=order_by,
            tags=tags,
            only_active=only_active,
            dag_id_pattern=dag_id_pattern,
            request_options=request_options,
        )
        return _response.data

    def patch_dags(
        self,
        *,
        dag_id_pattern: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        only_active: typing.Optional[bool] = None,
        dag_id: typing.Optional[str] = OMIT,
        default_view: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        file_token: typing.Optional[str] = OMIT,
        fileloc: typing.Optional[str] = OMIT,
        has_import_errors: typing.Optional[bool] = OMIT,
        has_task_concurrency_limits: typing.Optional[bool] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_paused: typing.Optional[bool] = OMIT,
        is_subdag: typing.Optional[bool] = OMIT,
        last_expired: typing.Optional[dt.datetime] = OMIT,
        last_parsed_time: typing.Optional[dt.datetime] = OMIT,
        last_pickled: typing.Optional[dt.datetime] = OMIT,
        max_active_runs: typing.Optional[int] = OMIT,
        max_active_tasks: typing.Optional[int] = OMIT,
        next_dagrun: typing.Optional[dt.datetime] = OMIT,
        next_dagrun_create_after: typing.Optional[dt.datetime] = OMIT,
        next_dagrun_data_interval_end: typing.Optional[dt.datetime] = OMIT,
        next_dagrun_data_interval_start: typing.Optional[dt.datetime] = OMIT,
        owners: typing.Optional[typing.Sequence[str]] = OMIT,
        pickle_id: typing.Optional[str] = OMIT,
        root_dag_id: typing.Optional[str] = OMIT,
        schedule_interval: typing.Optional[ScheduleInterval] = OMIT,
        scheduler_lock: typing.Optional[bool] = OMIT,
        dag_tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        timetable_description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagCollection:
        """
        Update DAGs of a given dag_id_pattern using UpdateMask.
        This endpoint allows specifying `~` as the dag_id_pattern to update all DAGs.
        *New in version 2.3.0*

        Parameters
        ----------
        dag_id_pattern : str
            If set, only update DAGs with dag_ids matching this pattern.

        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of tags to filter results.

            *New in version 2.2.0*

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        only_active : typing.Optional[bool]
            Only filter active DAGs.

            *New in version 2.1.1*

        dag_id : typing.Optional[str]
            The ID of the DAG.

        default_view : typing.Optional[str]
            Default view of the DAG inside the webserver

            *New in version 2.3.0*

        description : typing.Optional[str]
            User-provided DAG description, which can consist of several sentences or paragraphs that describe DAG contents.

        file_token : typing.Optional[str]
            The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change.

        fileloc : typing.Optional[str]
            The absolute path to the file.

        has_import_errors : typing.Optional[bool]
            Whether the DAG has import errors

            *New in version 2.3.0*

        has_task_concurrency_limits : typing.Optional[bool]
            Whether the DAG has task concurrency limits

            *New in version 2.3.0*

        is_active : typing.Optional[bool]
            Whether the DAG is currently seen by the scheduler(s).

            *New in version 2.1.1*

            *Changed in version 2.2.0*&#58; Field is read-only.

        is_paused : typing.Optional[bool]
            Whether the DAG is paused.

        is_subdag : typing.Optional[bool]
            Whether the DAG is SubDAG.

        last_expired : typing.Optional[dt.datetime]
            Time when the DAG last received a refresh signal
            (e.g. the DAG's "refresh" button was clicked in the web UI)

            *New in version 2.3.0*

        last_parsed_time : typing.Optional[dt.datetime]
            The last time the DAG was parsed.

            *New in version 2.3.0*

        last_pickled : typing.Optional[dt.datetime]
            The last time the DAG was pickled.

            *New in version 2.3.0*

        max_active_runs : typing.Optional[int]
            Maximum number of active DAG runs for the DAG

            *New in version 2.3.0*

        max_active_tasks : typing.Optional[int]
            Maximum number of active tasks that can be run on the DAG

            *New in version 2.3.0*

        next_dagrun : typing.Optional[dt.datetime]
            The logical date of the next dag run.

            *New in version 2.3.0*

        next_dagrun_create_after : typing.Optional[dt.datetime]
            Earliest time at which this ``next_dagrun`` can be created.

            *New in version 2.3.0*

        next_dagrun_data_interval_end : typing.Optional[dt.datetime]
            The end of the interval of the next dag run.

            *New in version 2.3.0*

        next_dagrun_data_interval_start : typing.Optional[dt.datetime]
            The start of the interval of the next dag run.

            *New in version 2.3.0*

        owners : typing.Optional[typing.Sequence[str]]

        pickle_id : typing.Optional[str]
            Foreign key to the latest pickle_id

            *New in version 2.3.0*

        root_dag_id : typing.Optional[str]
            If the DAG is SubDAG then it is the top level DAG identifier. Otherwise, null.

        schedule_interval : typing.Optional[ScheduleInterval]

        scheduler_lock : typing.Optional[bool]
            Whether (one of) the scheduler is scheduling this DAG at the moment

            *New in version 2.3.0*

        dag_tags : typing.Optional[typing.Sequence[Tag]]
            List of tags.

        timetable_description : typing.Optional[str]
            Timetable/Schedule Interval description.

            *New in version 2.3.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag.patch_dags(
            dag_id_pattern="dag_id_pattern",
            is_paused=True,
        )
        """
        _response = self._raw_client.patch_dags(
            dag_id_pattern=dag_id_pattern,
            limit=limit,
            offset=offset,
            tags=tags,
            update_mask=update_mask,
            only_active=only_active,
            dag_id=dag_id,
            default_view=default_view,
            description=description,
            file_token=file_token,
            fileloc=fileloc,
            has_import_errors=has_import_errors,
            has_task_concurrency_limits=has_task_concurrency_limits,
            is_active=is_active,
            is_paused=is_paused,
            is_subdag=is_subdag,
            last_expired=last_expired,
            last_parsed_time=last_parsed_time,
            last_pickled=last_pickled,
            max_active_runs=max_active_runs,
            max_active_tasks=max_active_tasks,
            next_dagrun=next_dagrun,
            next_dagrun_create_after=next_dagrun_create_after,
            next_dagrun_data_interval_end=next_dagrun_data_interval_end,
            next_dagrun_data_interval_start=next_dagrun_data_interval_start,
            owners=owners,
            pickle_id=pickle_id,
            root_dag_id=root_dag_id,
            schedule_interval=schedule_interval,
            scheduler_lock=scheduler_lock,
            dag_tags=dag_tags,
            timetable_description=timetable_description,
            request_options=request_options,
        )
        return _response.data

    def get_dag(self, dag_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Dag:
        """
        Presents only information available in database (DAGModel).
        If you need detailed information, consider using GET /dags/{dag_id}/details.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dag
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag.get_dag(
            dag_id="dag_id",
        )
        """
        _response = self._raw_client.get_dag(dag_id, request_options=request_options)
        return _response.data

    def delete_dag(self, dag_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes all metadata related to the DAG, including finished DAG Runs and Tasks.
        Logs are not deleted. This action cannot be undone.

        *New in version 2.2.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag.delete_dag(
            dag_id="dag_id",
        )
        """
        _response = self._raw_client.delete_dag(dag_id, request_options=request_options)
        return _response.data

    def patch_dag(
        self,
        dag_id_: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        dag_id: typing.Optional[str] = OMIT,
        default_view: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        file_token: typing.Optional[str] = OMIT,
        fileloc: typing.Optional[str] = OMIT,
        has_import_errors: typing.Optional[bool] = OMIT,
        has_task_concurrency_limits: typing.Optional[bool] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_paused: typing.Optional[bool] = OMIT,
        is_subdag: typing.Optional[bool] = OMIT,
        last_expired: typing.Optional[dt.datetime] = OMIT,
        last_parsed_time: typing.Optional[dt.datetime] = OMIT,
        last_pickled: typing.Optional[dt.datetime] = OMIT,
        max_active_runs: typing.Optional[int] = OMIT,
        max_active_tasks: typing.Optional[int] = OMIT,
        next_dagrun: typing.Optional[dt.datetime] = OMIT,
        next_dagrun_create_after: typing.Optional[dt.datetime] = OMIT,
        next_dagrun_data_interval_end: typing.Optional[dt.datetime] = OMIT,
        next_dagrun_data_interval_start: typing.Optional[dt.datetime] = OMIT,
        owners: typing.Optional[typing.Sequence[str]] = OMIT,
        pickle_id: typing.Optional[str] = OMIT,
        root_dag_id: typing.Optional[str] = OMIT,
        schedule_interval: typing.Optional[ScheduleInterval] = OMIT,
        scheduler_lock: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        timetable_description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dag:
        """
        Parameters
        ----------
        dag_id_ : str
            The DAG ID.

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        dag_id : typing.Optional[str]
            The ID of the DAG.

        default_view : typing.Optional[str]
            Default view of the DAG inside the webserver

            *New in version 2.3.0*

        description : typing.Optional[str]
            User-provided DAG description, which can consist of several sentences or paragraphs that describe DAG contents.

        file_token : typing.Optional[str]
            The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change.

        fileloc : typing.Optional[str]
            The absolute path to the file.

        has_import_errors : typing.Optional[bool]
            Whether the DAG has import errors

            *New in version 2.3.0*

        has_task_concurrency_limits : typing.Optional[bool]
            Whether the DAG has task concurrency limits

            *New in version 2.3.0*

        is_active : typing.Optional[bool]
            Whether the DAG is currently seen by the scheduler(s).

            *New in version 2.1.1*

            *Changed in version 2.2.0*&#58; Field is read-only.

        is_paused : typing.Optional[bool]
            Whether the DAG is paused.

        is_subdag : typing.Optional[bool]
            Whether the DAG is SubDAG.

        last_expired : typing.Optional[dt.datetime]
            Time when the DAG last received a refresh signal
            (e.g. the DAG's "refresh" button was clicked in the web UI)

            *New in version 2.3.0*

        last_parsed_time : typing.Optional[dt.datetime]
            The last time the DAG was parsed.

            *New in version 2.3.0*

        last_pickled : typing.Optional[dt.datetime]
            The last time the DAG was pickled.

            *New in version 2.3.0*

        max_active_runs : typing.Optional[int]
            Maximum number of active DAG runs for the DAG

            *New in version 2.3.0*

        max_active_tasks : typing.Optional[int]
            Maximum number of active tasks that can be run on the DAG

            *New in version 2.3.0*

        next_dagrun : typing.Optional[dt.datetime]
            The logical date of the next dag run.

            *New in version 2.3.0*

        next_dagrun_create_after : typing.Optional[dt.datetime]
            Earliest time at which this ``next_dagrun`` can be created.

            *New in version 2.3.0*

        next_dagrun_data_interval_end : typing.Optional[dt.datetime]
            The end of the interval of the next dag run.

            *New in version 2.3.0*

        next_dagrun_data_interval_start : typing.Optional[dt.datetime]
            The start of the interval of the next dag run.

            *New in version 2.3.0*

        owners : typing.Optional[typing.Sequence[str]]

        pickle_id : typing.Optional[str]
            Foreign key to the latest pickle_id

            *New in version 2.3.0*

        root_dag_id : typing.Optional[str]
            If the DAG is SubDAG then it is the top level DAG identifier. Otherwise, null.

        schedule_interval : typing.Optional[ScheduleInterval]

        scheduler_lock : typing.Optional[bool]
            Whether (one of) the scheduler is scheduling this DAG at the moment

            *New in version 2.3.0*

        tags : typing.Optional[typing.Sequence[Tag]]
            List of tags.

        timetable_description : typing.Optional[str]
            Timetable/Schedule Interval description.

            *New in version 2.3.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dag
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag.patch_dag(
            dag_id_="dag_id",
            is_paused=True,
        )
        """
        _response = self._raw_client.patch_dag(
            dag_id_,
            update_mask=update_mask,
            dag_id=dag_id,
            default_view=default_view,
            description=description,
            file_token=file_token,
            fileloc=fileloc,
            has_import_errors=has_import_errors,
            has_task_concurrency_limits=has_task_concurrency_limits,
            is_active=is_active,
            is_paused=is_paused,
            is_subdag=is_subdag,
            last_expired=last_expired,
            last_parsed_time=last_parsed_time,
            last_pickled=last_pickled,
            max_active_runs=max_active_runs,
            max_active_tasks=max_active_tasks,
            next_dagrun=next_dagrun,
            next_dagrun_create_after=next_dagrun_create_after,
            next_dagrun_data_interval_end=next_dagrun_data_interval_end,
            next_dagrun_data_interval_start=next_dagrun_data_interval_start,
            owners=owners,
            pickle_id=pickle_id,
            root_dag_id=root_dag_id,
            schedule_interval=schedule_interval,
            scheduler_lock=scheduler_lock,
            tags=tags,
            timetable_description=timetable_description,
            request_options=request_options,
        )
        return _response.data

    def post_clear_task_instances(
        self,
        dag_id: str,
        *,
        dag_run_id: typing.Optional[str] = OMIT,
        dry_run: typing.Optional[bool] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        include_downstream: typing.Optional[bool] = OMIT,
        include_future: typing.Optional[bool] = OMIT,
        include_parentdag: typing.Optional[bool] = OMIT,
        include_past: typing.Optional[bool] = OMIT,
        include_subdags: typing.Optional[bool] = OMIT,
        include_upstream: typing.Optional[bool] = OMIT,
        only_failed: typing.Optional[bool] = OMIT,
        only_running: typing.Optional[bool] = OMIT,
        reset_dag_runs: typing.Optional[bool] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        task_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstanceReferenceCollection:
        """
        Clears a set of task instances associated with the DAG for a specified date range.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : typing.Optional[str]
            The DagRun ID for this task instance

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain a list of task instances
            planned to be cleaned, but not modified in any way.

        end_date : typing.Optional[str]
            The maximum execution date to clear.

        include_downstream : typing.Optional[bool]
            If set to true, downstream tasks are also affected.

        include_future : typing.Optional[bool]
            If set to True, also tasks from future DAG Runs are affected.

        include_parentdag : typing.Optional[bool]
            Clear tasks in the parent dag of the subdag.

        include_past : typing.Optional[bool]
            If set to True, also tasks from past DAG Runs are affected.

        include_subdags : typing.Optional[bool]
            Clear tasks in subdags and clear external tasks indicated by ExternalTaskMarker.

        include_upstream : typing.Optional[bool]
            If set to true, upstream tasks are also affected.

        only_failed : typing.Optional[bool]
            Only clear failed tasks.

        only_running : typing.Optional[bool]
            Only clear running tasks.

        reset_dag_runs : typing.Optional[bool]
            Set state of DAG runs to RUNNING.

        start_date : typing.Optional[str]
            The minimum execution date to clear.

        task_ids : typing.Optional[typing.Sequence[str]]
            A list of task ids to clear.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstanceReferenceCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag.post_clear_task_instances(
            dag_id="dag_id",
        )
        """
        _response = self._raw_client.post_clear_task_instances(
            dag_id,
            dag_run_id=dag_run_id,
            dry_run=dry_run,
            end_date=end_date,
            include_downstream=include_downstream,
            include_future=include_future,
            include_parentdag=include_parentdag,
            include_past=include_past,
            include_subdags=include_subdags,
            include_upstream=include_upstream,
            only_failed=only_failed,
            only_running=only_running,
            reset_dag_runs=reset_dag_runs,
            start_date=start_date,
            task_ids=task_ids,
            request_options=request_options,
        )
        return _response.data

    def get_dag_details(self, dag_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DagDetail:
        """
        The response contains many DAG attributes, so the response can be large. If possible, consider using GET /dags/{dag_id}.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagDetail
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag.get_dag_details(
            dag_id="dag_id",
        )
        """
        _response = self._raw_client.get_dag_details(dag_id, request_options=request_options)
        return _response.data

    def get_tasks(
        self,
        dag_id: str,
        *,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskCollection:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag.get_tasks(
            dag_id="dag_id",
        )
        """
        _response = self._raw_client.get_tasks(dag_id, order_by=order_by, request_options=request_options)
        return _response.data

    def get_task(self, dag_id: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Task:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        task_id : str
            The task ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag.get_task(
            dag_id="dag_id",
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_task(dag_id, task_id, request_options=request_options)
        return _response.data

    def post_set_task_instances_state(
        self,
        dag_id: str,
        *,
        dag_run_id: typing.Optional[str] = OMIT,
        dry_run: typing.Optional[bool] = OMIT,
        execution_date: typing.Optional[str] = OMIT,
        include_downstream: typing.Optional[bool] = OMIT,
        include_future: typing.Optional[bool] = OMIT,
        include_past: typing.Optional[bool] = OMIT,
        include_upstream: typing.Optional[bool] = OMIT,
        new_state: typing.Optional[UpdateTaskInstancesStateNewState] = OMIT,
        task_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstanceReferenceCollection:
        """
        Updates the state for multiple task instances simultaneously.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : typing.Optional[str]
            The task instance's DAG run ID. Either set this or execution_date but not both.

            *New in version 2.3.0*

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain a list of task instances
            planned to be affected, but won't be modified in any way.

        execution_date : typing.Optional[str]
            The execution date. Either set this or dag_run_id but not both.

        include_downstream : typing.Optional[bool]
            If set to true, downstream tasks are also affected.

        include_future : typing.Optional[bool]
            If set to True, also tasks from future DAG Runs are affected.

        include_past : typing.Optional[bool]
            If set to True, also tasks from past DAG Runs are affected.

        include_upstream : typing.Optional[bool]
            If set to true, upstream tasks are also affected.

        new_state : typing.Optional[UpdateTaskInstancesStateNewState]
            Expected new state.

        task_id : typing.Optional[str]
            The task ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstanceReferenceCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag.post_set_task_instances_state(
            dag_id="dag_id",
        )
        """
        _response = self._raw_client.post_set_task_instances_state(
            dag_id,
            dag_run_id=dag_run_id,
            dry_run=dry_run,
            execution_date=execution_date,
            include_downstream=include_downstream,
            include_future=include_future,
            include_past=include_past,
            include_upstream=include_upstream,
            new_state=new_state,
            task_id=task_id,
            request_options=request_options,
        )
        return _response.data


class AsyncDagClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDagClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDagClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDagClient
        """
        return self._raw_client

    async def get_dag_source(
        self, file_token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDagSourceResponse:
        """
        Get a source code using file token.

        Parameters
        ----------
        file_token : str
            The key containing the encrypted path to the file. Encryption and decryption take place only on
            the server. This prevents the client from reading an non-DAG file. This also ensures API
            extensibility, because the format of encrypted data may change.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDagSourceResponse
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dag.get_dag_source(
                file_token="file_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dag_source(file_token, request_options=request_options)
        return _response.data

    async def get_dags(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        only_active: typing.Optional[bool] = None,
        dag_id_pattern: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagCollection:
        """
        List DAGs in the database.
        `dag_id_pattern` can be set to match dags of a specific pattern

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of tags to filter results.

            *New in version 2.2.0*

        only_active : typing.Optional[bool]
            Only filter active DAGs.

            *New in version 2.1.1*

        dag_id_pattern : typing.Optional[str]
            If set, only return DAGs with dag_ids matching this pattern.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagCollection
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dag.get_dags()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dags(
            limit=limit,
            offset=offset,
            order_by=order_by,
            tags=tags,
            only_active=only_active,
            dag_id_pattern=dag_id_pattern,
            request_options=request_options,
        )
        return _response.data

    async def patch_dags(
        self,
        *,
        dag_id_pattern: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        only_active: typing.Optional[bool] = None,
        dag_id: typing.Optional[str] = OMIT,
        default_view: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        file_token: typing.Optional[str] = OMIT,
        fileloc: typing.Optional[str] = OMIT,
        has_import_errors: typing.Optional[bool] = OMIT,
        has_task_concurrency_limits: typing.Optional[bool] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_paused: typing.Optional[bool] = OMIT,
        is_subdag: typing.Optional[bool] = OMIT,
        last_expired: typing.Optional[dt.datetime] = OMIT,
        last_parsed_time: typing.Optional[dt.datetime] = OMIT,
        last_pickled: typing.Optional[dt.datetime] = OMIT,
        max_active_runs: typing.Optional[int] = OMIT,
        max_active_tasks: typing.Optional[int] = OMIT,
        next_dagrun: typing.Optional[dt.datetime] = OMIT,
        next_dagrun_create_after: typing.Optional[dt.datetime] = OMIT,
        next_dagrun_data_interval_end: typing.Optional[dt.datetime] = OMIT,
        next_dagrun_data_interval_start: typing.Optional[dt.datetime] = OMIT,
        owners: typing.Optional[typing.Sequence[str]] = OMIT,
        pickle_id: typing.Optional[str] = OMIT,
        root_dag_id: typing.Optional[str] = OMIT,
        schedule_interval: typing.Optional[ScheduleInterval] = OMIT,
        scheduler_lock: typing.Optional[bool] = OMIT,
        dag_tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        timetable_description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagCollection:
        """
        Update DAGs of a given dag_id_pattern using UpdateMask.
        This endpoint allows specifying `~` as the dag_id_pattern to update all DAGs.
        *New in version 2.3.0*

        Parameters
        ----------
        dag_id_pattern : str
            If set, only update DAGs with dag_ids matching this pattern.

        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of tags to filter results.

            *New in version 2.2.0*

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        only_active : typing.Optional[bool]
            Only filter active DAGs.

            *New in version 2.1.1*

        dag_id : typing.Optional[str]
            The ID of the DAG.

        default_view : typing.Optional[str]
            Default view of the DAG inside the webserver

            *New in version 2.3.0*

        description : typing.Optional[str]
            User-provided DAG description, which can consist of several sentences or paragraphs that describe DAG contents.

        file_token : typing.Optional[str]
            The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change.

        fileloc : typing.Optional[str]
            The absolute path to the file.

        has_import_errors : typing.Optional[bool]
            Whether the DAG has import errors

            *New in version 2.3.0*

        has_task_concurrency_limits : typing.Optional[bool]
            Whether the DAG has task concurrency limits

            *New in version 2.3.0*

        is_active : typing.Optional[bool]
            Whether the DAG is currently seen by the scheduler(s).

            *New in version 2.1.1*

            *Changed in version 2.2.0*&#58; Field is read-only.

        is_paused : typing.Optional[bool]
            Whether the DAG is paused.

        is_subdag : typing.Optional[bool]
            Whether the DAG is SubDAG.

        last_expired : typing.Optional[dt.datetime]
            Time when the DAG last received a refresh signal
            (e.g. the DAG's "refresh" button was clicked in the web UI)

            *New in version 2.3.0*

        last_parsed_time : typing.Optional[dt.datetime]
            The last time the DAG was parsed.

            *New in version 2.3.0*

        last_pickled : typing.Optional[dt.datetime]
            The last time the DAG was pickled.

            *New in version 2.3.0*

        max_active_runs : typing.Optional[int]
            Maximum number of active DAG runs for the DAG

            *New in version 2.3.0*

        max_active_tasks : typing.Optional[int]
            Maximum number of active tasks that can be run on the DAG

            *New in version 2.3.0*

        next_dagrun : typing.Optional[dt.datetime]
            The logical date of the next dag run.

            *New in version 2.3.0*

        next_dagrun_create_after : typing.Optional[dt.datetime]
            Earliest time at which this ``next_dagrun`` can be created.

            *New in version 2.3.0*

        next_dagrun_data_interval_end : typing.Optional[dt.datetime]
            The end of the interval of the next dag run.

            *New in version 2.3.0*

        next_dagrun_data_interval_start : typing.Optional[dt.datetime]
            The start of the interval of the next dag run.

            *New in version 2.3.0*

        owners : typing.Optional[typing.Sequence[str]]

        pickle_id : typing.Optional[str]
            Foreign key to the latest pickle_id

            *New in version 2.3.0*

        root_dag_id : typing.Optional[str]
            If the DAG is SubDAG then it is the top level DAG identifier. Otherwise, null.

        schedule_interval : typing.Optional[ScheduleInterval]

        scheduler_lock : typing.Optional[bool]
            Whether (one of) the scheduler is scheduling this DAG at the moment

            *New in version 2.3.0*

        dag_tags : typing.Optional[typing.Sequence[Tag]]
            List of tags.

        timetable_description : typing.Optional[str]
            Timetable/Schedule Interval description.

            *New in version 2.3.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagCollection
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dag.patch_dags(
                dag_id_pattern="dag_id_pattern",
                is_paused=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_dags(
            dag_id_pattern=dag_id_pattern,
            limit=limit,
            offset=offset,
            tags=tags,
            update_mask=update_mask,
            only_active=only_active,
            dag_id=dag_id,
            default_view=default_view,
            description=description,
            file_token=file_token,
            fileloc=fileloc,
            has_import_errors=has_import_errors,
            has_task_concurrency_limits=has_task_concurrency_limits,
            is_active=is_active,
            is_paused=is_paused,
            is_subdag=is_subdag,
            last_expired=last_expired,
            last_parsed_time=last_parsed_time,
            last_pickled=last_pickled,
            max_active_runs=max_active_runs,
            max_active_tasks=max_active_tasks,
            next_dagrun=next_dagrun,
            next_dagrun_create_after=next_dagrun_create_after,
            next_dagrun_data_interval_end=next_dagrun_data_interval_end,
            next_dagrun_data_interval_start=next_dagrun_data_interval_start,
            owners=owners,
            pickle_id=pickle_id,
            root_dag_id=root_dag_id,
            schedule_interval=schedule_interval,
            scheduler_lock=scheduler_lock,
            dag_tags=dag_tags,
            timetable_description=timetable_description,
            request_options=request_options,
        )
        return _response.data

    async def get_dag(self, dag_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Dag:
        """
        Presents only information available in database (DAGModel).
        If you need detailed information, consider using GET /dags/{dag_id}/details.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dag
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dag.get_dag(
                dag_id="dag_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dag(dag_id, request_options=request_options)
        return _response.data

    async def delete_dag(self, dag_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes all metadata related to the DAG, including finished DAG Runs and Tasks.
        Logs are not deleted. This action cannot be undone.

        *New in version 2.2.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dag.delete_dag(
                dag_id="dag_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_dag(dag_id, request_options=request_options)
        return _response.data

    async def patch_dag(
        self,
        dag_id_: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        dag_id: typing.Optional[str] = OMIT,
        default_view: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        file_token: typing.Optional[str] = OMIT,
        fileloc: typing.Optional[str] = OMIT,
        has_import_errors: typing.Optional[bool] = OMIT,
        has_task_concurrency_limits: typing.Optional[bool] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        is_paused: typing.Optional[bool] = OMIT,
        is_subdag: typing.Optional[bool] = OMIT,
        last_expired: typing.Optional[dt.datetime] = OMIT,
        last_parsed_time: typing.Optional[dt.datetime] = OMIT,
        last_pickled: typing.Optional[dt.datetime] = OMIT,
        max_active_runs: typing.Optional[int] = OMIT,
        max_active_tasks: typing.Optional[int] = OMIT,
        next_dagrun: typing.Optional[dt.datetime] = OMIT,
        next_dagrun_create_after: typing.Optional[dt.datetime] = OMIT,
        next_dagrun_data_interval_end: typing.Optional[dt.datetime] = OMIT,
        next_dagrun_data_interval_start: typing.Optional[dt.datetime] = OMIT,
        owners: typing.Optional[typing.Sequence[str]] = OMIT,
        pickle_id: typing.Optional[str] = OMIT,
        root_dag_id: typing.Optional[str] = OMIT,
        schedule_interval: typing.Optional[ScheduleInterval] = OMIT,
        scheduler_lock: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        timetable_description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dag:
        """
        Parameters
        ----------
        dag_id_ : str
            The DAG ID.

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        dag_id : typing.Optional[str]
            The ID of the DAG.

        default_view : typing.Optional[str]
            Default view of the DAG inside the webserver

            *New in version 2.3.0*

        description : typing.Optional[str]
            User-provided DAG description, which can consist of several sentences or paragraphs that describe DAG contents.

        file_token : typing.Optional[str]
            The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change.

        fileloc : typing.Optional[str]
            The absolute path to the file.

        has_import_errors : typing.Optional[bool]
            Whether the DAG has import errors

            *New in version 2.3.0*

        has_task_concurrency_limits : typing.Optional[bool]
            Whether the DAG has task concurrency limits

            *New in version 2.3.0*

        is_active : typing.Optional[bool]
            Whether the DAG is currently seen by the scheduler(s).

            *New in version 2.1.1*

            *Changed in version 2.2.0*&#58; Field is read-only.

        is_paused : typing.Optional[bool]
            Whether the DAG is paused.

        is_subdag : typing.Optional[bool]
            Whether the DAG is SubDAG.

        last_expired : typing.Optional[dt.datetime]
            Time when the DAG last received a refresh signal
            (e.g. the DAG's "refresh" button was clicked in the web UI)

            *New in version 2.3.0*

        last_parsed_time : typing.Optional[dt.datetime]
            The last time the DAG was parsed.

            *New in version 2.3.0*

        last_pickled : typing.Optional[dt.datetime]
            The last time the DAG was pickled.

            *New in version 2.3.0*

        max_active_runs : typing.Optional[int]
            Maximum number of active DAG runs for the DAG

            *New in version 2.3.0*

        max_active_tasks : typing.Optional[int]
            Maximum number of active tasks that can be run on the DAG

            *New in version 2.3.0*

        next_dagrun : typing.Optional[dt.datetime]
            The logical date of the next dag run.

            *New in version 2.3.0*

        next_dagrun_create_after : typing.Optional[dt.datetime]
            Earliest time at which this ``next_dagrun`` can be created.

            *New in version 2.3.0*

        next_dagrun_data_interval_end : typing.Optional[dt.datetime]
            The end of the interval of the next dag run.

            *New in version 2.3.0*

        next_dagrun_data_interval_start : typing.Optional[dt.datetime]
            The start of the interval of the next dag run.

            *New in version 2.3.0*

        owners : typing.Optional[typing.Sequence[str]]

        pickle_id : typing.Optional[str]
            Foreign key to the latest pickle_id

            *New in version 2.3.0*

        root_dag_id : typing.Optional[str]
            If the DAG is SubDAG then it is the top level DAG identifier. Otherwise, null.

        schedule_interval : typing.Optional[ScheduleInterval]

        scheduler_lock : typing.Optional[bool]
            Whether (one of) the scheduler is scheduling this DAG at the moment

            *New in version 2.3.0*

        tags : typing.Optional[typing.Sequence[Tag]]
            List of tags.

        timetable_description : typing.Optional[str]
            Timetable/Schedule Interval description.

            *New in version 2.3.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dag
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dag.patch_dag(
                dag_id_="dag_id",
                is_paused=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_dag(
            dag_id_,
            update_mask=update_mask,
            dag_id=dag_id,
            default_view=default_view,
            description=description,
            file_token=file_token,
            fileloc=fileloc,
            has_import_errors=has_import_errors,
            has_task_concurrency_limits=has_task_concurrency_limits,
            is_active=is_active,
            is_paused=is_paused,
            is_subdag=is_subdag,
            last_expired=last_expired,
            last_parsed_time=last_parsed_time,
            last_pickled=last_pickled,
            max_active_runs=max_active_runs,
            max_active_tasks=max_active_tasks,
            next_dagrun=next_dagrun,
            next_dagrun_create_after=next_dagrun_create_after,
            next_dagrun_data_interval_end=next_dagrun_data_interval_end,
            next_dagrun_data_interval_start=next_dagrun_data_interval_start,
            owners=owners,
            pickle_id=pickle_id,
            root_dag_id=root_dag_id,
            schedule_interval=schedule_interval,
            scheduler_lock=scheduler_lock,
            tags=tags,
            timetable_description=timetable_description,
            request_options=request_options,
        )
        return _response.data

    async def post_clear_task_instances(
        self,
        dag_id: str,
        *,
        dag_run_id: typing.Optional[str] = OMIT,
        dry_run: typing.Optional[bool] = OMIT,
        end_date: typing.Optional[str] = OMIT,
        include_downstream: typing.Optional[bool] = OMIT,
        include_future: typing.Optional[bool] = OMIT,
        include_parentdag: typing.Optional[bool] = OMIT,
        include_past: typing.Optional[bool] = OMIT,
        include_subdags: typing.Optional[bool] = OMIT,
        include_upstream: typing.Optional[bool] = OMIT,
        only_failed: typing.Optional[bool] = OMIT,
        only_running: typing.Optional[bool] = OMIT,
        reset_dag_runs: typing.Optional[bool] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        task_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstanceReferenceCollection:
        """
        Clears a set of task instances associated with the DAG for a specified date range.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : typing.Optional[str]
            The DagRun ID for this task instance

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain a list of task instances
            planned to be cleaned, but not modified in any way.

        end_date : typing.Optional[str]
            The maximum execution date to clear.

        include_downstream : typing.Optional[bool]
            If set to true, downstream tasks are also affected.

        include_future : typing.Optional[bool]
            If set to True, also tasks from future DAG Runs are affected.

        include_parentdag : typing.Optional[bool]
            Clear tasks in the parent dag of the subdag.

        include_past : typing.Optional[bool]
            If set to True, also tasks from past DAG Runs are affected.

        include_subdags : typing.Optional[bool]
            Clear tasks in subdags and clear external tasks indicated by ExternalTaskMarker.

        include_upstream : typing.Optional[bool]
            If set to true, upstream tasks are also affected.

        only_failed : typing.Optional[bool]
            Only clear failed tasks.

        only_running : typing.Optional[bool]
            Only clear running tasks.

        reset_dag_runs : typing.Optional[bool]
            Set state of DAG runs to RUNNING.

        start_date : typing.Optional[str]
            The minimum execution date to clear.

        task_ids : typing.Optional[typing.Sequence[str]]
            A list of task ids to clear.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstanceReferenceCollection
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dag.post_clear_task_instances(
                dag_id="dag_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_clear_task_instances(
            dag_id,
            dag_run_id=dag_run_id,
            dry_run=dry_run,
            end_date=end_date,
            include_downstream=include_downstream,
            include_future=include_future,
            include_parentdag=include_parentdag,
            include_past=include_past,
            include_subdags=include_subdags,
            include_upstream=include_upstream,
            only_failed=only_failed,
            only_running=only_running,
            reset_dag_runs=reset_dag_runs,
            start_date=start_date,
            task_ids=task_ids,
            request_options=request_options,
        )
        return _response.data

    async def get_dag_details(
        self, dag_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DagDetail:
        """
        The response contains many DAG attributes, so the response can be large. If possible, consider using GET /dags/{dag_id}.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagDetail
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dag.get_dag_details(
                dag_id="dag_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dag_details(dag_id, request_options=request_options)
        return _response.data

    async def get_tasks(
        self,
        dag_id: str,
        *,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskCollection:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskCollection
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dag.get_tasks(
                dag_id="dag_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tasks(dag_id, order_by=order_by, request_options=request_options)
        return _response.data

    async def get_task(
        self, dag_id: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        task_id : str
            The task ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dag.get_task(
                dag_id="dag_id",
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_task(dag_id, task_id, request_options=request_options)
        return _response.data

    async def post_set_task_instances_state(
        self,
        dag_id: str,
        *,
        dag_run_id: typing.Optional[str] = OMIT,
        dry_run: typing.Optional[bool] = OMIT,
        execution_date: typing.Optional[str] = OMIT,
        include_downstream: typing.Optional[bool] = OMIT,
        include_future: typing.Optional[bool] = OMIT,
        include_past: typing.Optional[bool] = OMIT,
        include_upstream: typing.Optional[bool] = OMIT,
        new_state: typing.Optional[UpdateTaskInstancesStateNewState] = OMIT,
        task_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstanceReferenceCollection:
        """
        Updates the state for multiple task instances simultaneously.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : typing.Optional[str]
            The task instance's DAG run ID. Either set this or execution_date but not both.

            *New in version 2.3.0*

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain a list of task instances
            planned to be affected, but won't be modified in any way.

        execution_date : typing.Optional[str]
            The execution date. Either set this or dag_run_id but not both.

        include_downstream : typing.Optional[bool]
            If set to true, downstream tasks are also affected.

        include_future : typing.Optional[bool]
            If set to True, also tasks from future DAG Runs are affected.

        include_past : typing.Optional[bool]
            If set to True, also tasks from past DAG Runs are affected.

        include_upstream : typing.Optional[bool]
            If set to true, upstream tasks are also affected.

        new_state : typing.Optional[UpdateTaskInstancesStateNewState]
            Expected new state.

        task_id : typing.Optional[str]
            The task ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstanceReferenceCollection
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dag.post_set_task_instances_state(
                dag_id="dag_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_set_task_instances_state(
            dag_id,
            dag_run_id=dag_run_id,
            dry_run=dry_run,
            execution_date=execution_date,
            include_downstream=include_downstream,
            include_future=include_future,
            include_past=include_past,
            include_upstream=include_upstream,
            new_state=new_state,
            task_id=task_id,
            request_options=request_options,
        )
        return _response.data
