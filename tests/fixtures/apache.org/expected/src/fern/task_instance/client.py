

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.extra_link_collection import ExtraLinkCollection
from ..types.task_instance import TaskInstance
from ..types.task_instance_collection import TaskInstanceCollection
from ..types.task_instance_reference import TaskInstanceReference
from ..types.task_state import TaskState
from ..types.update_task_instance_new_state import UpdateTaskInstanceNewState
from .raw_client import AsyncRawTaskInstanceClient, RawTaskInstanceClient
from .types.get_log_response import GetLogResponse


OMIT = typing.cast(typing.Any, ...)


class TaskInstanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTaskInstanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTaskInstanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTaskInstanceClient
        """
        return self._raw_client

    def get_task_instances(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        execution_date_gte: typing.Optional[dt.datetime] = None,
        execution_date_lte: typing.Optional[dt.datetime] = None,
        start_date_gte: typing.Optional[dt.datetime] = None,
        start_date_lte: typing.Optional[dt.datetime] = None,
        end_date_gte: typing.Optional[dt.datetime] = None,
        end_date_lte: typing.Optional[dt.datetime] = None,
        duration_gte: typing.Optional[float] = None,
        duration_lte: typing.Optional[float] = None,
        state: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pool: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        queue: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstanceCollection:
        """
        This endpoint allows specifying `~` as the dag_id, dag_run_id to retrieve DAG runs for all DAGs and DAG runs.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte parameter to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte parameter to receive only the selected period.

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        duration_gte : typing.Optional[float]
            Returns objects greater than or equal to the specified values.

            This can be combined with duration_lte parameter to receive only the selected period.

        duration_lte : typing.Optional[float]
            Returns objects less than or equal to the specified values.

            This can be combined with duration_gte parameter to receive only the selected range.

        state : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        pool : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        queue : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstanceCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.task_instance.get_task_instances(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
        )
        """
        _response = self._raw_client.get_task_instances(
            dag_id,
            dag_run_id,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            duration_gte=duration_gte,
            duration_lte=duration_lte,
            state=state,
            pool=pool,
            queue=queue,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def get_task_instance(
        self, dag_id: str, dag_run_id: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskInstance:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstance
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.task_instance.get_task_instance(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_task_instance(dag_id, dag_run_id, task_id, request_options=request_options)
        return _response.data

    def patch_task_instance(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        new_state: typing.Optional[UpdateTaskInstanceNewState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstanceReference:
        """
        Updates the state for single task instance.
        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain the task instance
            planned to be affected, but won't be modified in any way.

        new_state : typing.Optional[UpdateTaskInstanceNewState]
            Expected new state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstanceReference
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.task_instance.patch_task_instance(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
            task_id="task_id",
        )
        """
        _response = self._raw_client.patch_task_instance(
            dag_id, dag_run_id, task_id, dry_run=dry_run, new_state=new_state, request_options=request_options
        )
        return _response.data

    def get_extra_links(
        self, dag_id: str, dag_run_id: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtraLinkCollection:
        """
        List extra links for task instance.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtraLinkCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.task_instance.get_extra_links(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_extra_links(dag_id, dag_run_id, task_id, request_options=request_options)
        return _response.data

    def get_mapped_task_instances(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        execution_date_gte: typing.Optional[dt.datetime] = None,
        execution_date_lte: typing.Optional[dt.datetime] = None,
        start_date_gte: typing.Optional[dt.datetime] = None,
        start_date_lte: typing.Optional[dt.datetime] = None,
        end_date_gte: typing.Optional[dt.datetime] = None,
        end_date_lte: typing.Optional[dt.datetime] = None,
        duration_gte: typing.Optional[float] = None,
        duration_lte: typing.Optional[float] = None,
        state: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pool: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        queue: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstanceCollection:
        """
        Get details of all mapped task instances.

        *New in version 2.3.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte parameter to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte parameter to receive only the selected period.

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        duration_gte : typing.Optional[float]
            Returns objects greater than or equal to the specified values.

            This can be combined with duration_lte parameter to receive only the selected period.

        duration_lte : typing.Optional[float]
            Returns objects less than or equal to the specified values.

            This can be combined with duration_gte parameter to receive only the selected range.

        state : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        pool : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        queue : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstanceCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.task_instance.get_mapped_task_instances(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_mapped_task_instances(
            dag_id,
            dag_run_id,
            task_id,
            limit=limit,
            offset=offset,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            duration_gte=duration_gte,
            duration_lte=duration_lte,
            state=state,
            pool=pool,
            queue=queue,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def get_log(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        task_try_number: int,
        *,
        full_content: typing.Optional[bool] = None,
        map_index: typing.Optional[int] = None,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLogResponse:
        """
        Get logs for a specific task instance and its try number.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        task_try_number : int
            The task try number.

        full_content : typing.Optional[bool]
            A full content will be returned.
            By default, only the first fragment will be returned.

        map_index : typing.Optional[int]
            Filter on map index for mapped task.

        token : typing.Optional[str]
            A token that allows you to continue fetching logs.
            If passed, it will specify the location from which the download should be continued.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLogResponse
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.task_instance.get_log(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
            task_id="task_id",
            task_try_number=1,
        )
        """
        _response = self._raw_client.get_log(
            dag_id,
            dag_run_id,
            task_id,
            task_try_number,
            full_content=full_content,
            map_index=map_index,
            token=token,
            request_options=request_options,
        )
        return _response.data

    def set_task_instance_note(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        note: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstance:
        """
        Update the manual user note of a non-mapped Task Instance.

        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        note : str
            The custom note to set for this Task Instance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstance
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.task_instance.set_task_instance_note(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
            task_id="task_id",
            note="note",
        )
        """
        _response = self._raw_client.set_task_instance_note(
            dag_id, dag_run_id, task_id, note=note, request_options=request_options
        )
        return _response.data

    def get_mapped_task_instance(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstance:
        """
        Get details of a mapped task instance.

        *New in version 2.3.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        map_index : int
            The map index.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstance
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.task_instance.get_mapped_task_instance(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
            task_id="task_id",
            map_index=1,
        )
        """
        _response = self._raw_client.get_mapped_task_instance(
            dag_id, dag_run_id, task_id, map_index, request_options=request_options
        )
        return _response.data

    def patch_mapped_task_instance(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        new_state: typing.Optional[UpdateTaskInstanceNewState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstanceReference:
        """
        Updates the state for single mapped task instance.
        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        map_index : int
            The map index.

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain the task instance
            planned to be affected, but won't be modified in any way.

        new_state : typing.Optional[UpdateTaskInstanceNewState]
            Expected new state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstanceReference
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.task_instance.patch_mapped_task_instance(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
            task_id="task_id",
            map_index=1,
        )
        """
        _response = self._raw_client.patch_mapped_task_instance(
            dag_id,
            dag_run_id,
            task_id,
            map_index,
            dry_run=dry_run,
            new_state=new_state,
            request_options=request_options,
        )
        return _response.data

    def set_mapped_task_instance_note(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
        *,
        note: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstance:
        """
        Update the manual user note of a mapped Task Instance.

        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        map_index : int
            The map index.

        note : str
            The custom note to set for this Task Instance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstance
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.task_instance.set_mapped_task_instance_note(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
            task_id="task_id",
            map_index=1,
            note="note",
        )
        """
        _response = self._raw_client.set_mapped_task_instance_note(
            dag_id, dag_run_id, task_id, map_index, note=note, request_options=request_options
        )
        return _response.data

    def get_task_instances_batch(
        self,
        *,
        dag_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        duration_gte: typing.Optional[float] = OMIT,
        duration_lte: typing.Optional[float] = OMIT,
        end_date_gte: typing.Optional[dt.datetime] = OMIT,
        end_date_lte: typing.Optional[dt.datetime] = OMIT,
        execution_date_gte: typing.Optional[dt.datetime] = OMIT,
        execution_date_lte: typing.Optional[dt.datetime] = OMIT,
        pool: typing.Optional[typing.Sequence[str]] = OMIT,
        queue: typing.Optional[typing.Sequence[str]] = OMIT,
        start_date_gte: typing.Optional[dt.datetime] = OMIT,
        start_date_lte: typing.Optional[dt.datetime] = OMIT,
        state: typing.Optional[typing.Sequence[TaskState]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstanceCollection:
        """
        List task instances from all DAGs and DAG runs.
        This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limits.

        Parameters
        ----------
        dag_ids : typing.Optional[typing.Sequence[str]]
            Return objects with specific DAG IDs.
            The value can be repeated to retrieve multiple matching values (OR condition).

        duration_gte : typing.Optional[float]
            Returns objects greater than or equal to the specified values.

            This can be combined with duration_lte parameter to receive only the selected period.

        duration_lte : typing.Optional[float]
            Returns objects less than or equal to the specified values.

            This can be combined with duration_gte parameter to receive only the selected range.

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte parameter to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte parameter to receive only the selected period.

        pool : typing.Optional[typing.Sequence[str]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        queue : typing.Optional[typing.Sequence[str]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        state : typing.Optional[typing.Sequence[TaskState]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstanceCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.task_instance.get_task_instances_batch()
        """
        _response = self._raw_client.get_task_instances_batch(
            dag_ids=dag_ids,
            duration_gte=duration_gte,
            duration_lte=duration_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            pool=pool,
            queue=queue,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            state=state,
            request_options=request_options,
        )
        return _response.data


class AsyncTaskInstanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTaskInstanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTaskInstanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTaskInstanceClient
        """
        return self._raw_client

    async def get_task_instances(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        execution_date_gte: typing.Optional[dt.datetime] = None,
        execution_date_lte: typing.Optional[dt.datetime] = None,
        start_date_gte: typing.Optional[dt.datetime] = None,
        start_date_lte: typing.Optional[dt.datetime] = None,
        end_date_gte: typing.Optional[dt.datetime] = None,
        end_date_lte: typing.Optional[dt.datetime] = None,
        duration_gte: typing.Optional[float] = None,
        duration_lte: typing.Optional[float] = None,
        state: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pool: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        queue: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstanceCollection:
        """
        This endpoint allows specifying `~` as the dag_id, dag_run_id to retrieve DAG runs for all DAGs and DAG runs.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte parameter to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte parameter to receive only the selected period.

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        duration_gte : typing.Optional[float]
            Returns objects greater than or equal to the specified values.

            This can be combined with duration_lte parameter to receive only the selected period.

        duration_lte : typing.Optional[float]
            Returns objects less than or equal to the specified values.

            This can be combined with duration_gte parameter to receive only the selected range.

        state : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        pool : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        queue : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstanceCollection
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
            await client.task_instance.get_task_instances(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_task_instances(
            dag_id,
            dag_run_id,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            duration_gte=duration_gte,
            duration_lte=duration_lte,
            state=state,
            pool=pool,
            queue=queue,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def get_task_instance(
        self, dag_id: str, dag_run_id: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskInstance:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstance
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
            await client.task_instance.get_task_instance(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_task_instance(
            dag_id, dag_run_id, task_id, request_options=request_options
        )
        return _response.data

    async def patch_task_instance(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        new_state: typing.Optional[UpdateTaskInstanceNewState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstanceReference:
        """
        Updates the state for single task instance.
        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain the task instance
            planned to be affected, but won't be modified in any way.

        new_state : typing.Optional[UpdateTaskInstanceNewState]
            Expected new state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstanceReference
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
            await client.task_instance.patch_task_instance(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_task_instance(
            dag_id, dag_run_id, task_id, dry_run=dry_run, new_state=new_state, request_options=request_options
        )
        return _response.data

    async def get_extra_links(
        self, dag_id: str, dag_run_id: str, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtraLinkCollection:
        """
        List extra links for task instance.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtraLinkCollection
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
            await client.task_instance.get_extra_links(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_extra_links(dag_id, dag_run_id, task_id, request_options=request_options)
        return _response.data

    async def get_mapped_task_instances(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        execution_date_gte: typing.Optional[dt.datetime] = None,
        execution_date_lte: typing.Optional[dt.datetime] = None,
        start_date_gte: typing.Optional[dt.datetime] = None,
        start_date_lte: typing.Optional[dt.datetime] = None,
        end_date_gte: typing.Optional[dt.datetime] = None,
        end_date_lte: typing.Optional[dt.datetime] = None,
        duration_gte: typing.Optional[float] = None,
        duration_lte: typing.Optional[float] = None,
        state: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pool: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        queue: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstanceCollection:
        """
        Get details of all mapped task instances.

        *New in version 2.3.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte parameter to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte parameter to receive only the selected period.

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        duration_gte : typing.Optional[float]
            Returns objects greater than or equal to the specified values.

            This can be combined with duration_lte parameter to receive only the selected period.

        duration_lte : typing.Optional[float]
            Returns objects less than or equal to the specified values.

            This can be combined with duration_gte parameter to receive only the selected range.

        state : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        pool : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        queue : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstanceCollection
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
            await client.task_instance.get_mapped_task_instances(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mapped_task_instances(
            dag_id,
            dag_run_id,
            task_id,
            limit=limit,
            offset=offset,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            duration_gte=duration_gte,
            duration_lte=duration_lte,
            state=state,
            pool=pool,
            queue=queue,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def get_log(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        task_try_number: int,
        *,
        full_content: typing.Optional[bool] = None,
        map_index: typing.Optional[int] = None,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLogResponse:
        """
        Get logs for a specific task instance and its try number.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        task_try_number : int
            The task try number.

        full_content : typing.Optional[bool]
            A full content will be returned.
            By default, only the first fragment will be returned.

        map_index : typing.Optional[int]
            Filter on map index for mapped task.

        token : typing.Optional[str]
            A token that allows you to continue fetching logs.
            If passed, it will specify the location from which the download should be continued.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLogResponse
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
            await client.task_instance.get_log(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
                task_id="task_id",
                task_try_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_log(
            dag_id,
            dag_run_id,
            task_id,
            task_try_number,
            full_content=full_content,
            map_index=map_index,
            token=token,
            request_options=request_options,
        )
        return _response.data

    async def set_task_instance_note(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        note: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstance:
        """
        Update the manual user note of a non-mapped Task Instance.

        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        note : str
            The custom note to set for this Task Instance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstance
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
            await client.task_instance.set_task_instance_note(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
                task_id="task_id",
                note="note",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_task_instance_note(
            dag_id, dag_run_id, task_id, note=note, request_options=request_options
        )
        return _response.data

    async def get_mapped_task_instance(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstance:
        """
        Get details of a mapped task instance.

        *New in version 2.3.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        map_index : int
            The map index.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstance
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
            await client.task_instance.get_mapped_task_instance(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
                task_id="task_id",
                map_index=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mapped_task_instance(
            dag_id, dag_run_id, task_id, map_index, request_options=request_options
        )
        return _response.data

    async def patch_mapped_task_instance(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        new_state: typing.Optional[UpdateTaskInstanceNewState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstanceReference:
        """
        Updates the state for single mapped task instance.
        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        map_index : int
            The map index.

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain the task instance
            planned to be affected, but won't be modified in any way.

        new_state : typing.Optional[UpdateTaskInstanceNewState]
            Expected new state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstanceReference
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
            await client.task_instance.patch_mapped_task_instance(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
                task_id="task_id",
                map_index=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_mapped_task_instance(
            dag_id,
            dag_run_id,
            task_id,
            map_index,
            dry_run=dry_run,
            new_state=new_state,
            request_options=request_options,
        )
        return _response.data

    async def set_mapped_task_instance_note(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        map_index: int,
        *,
        note: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstance:
        """
        Update the manual user note of a mapped Task Instance.

        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        map_index : int
            The map index.

        note : str
            The custom note to set for this Task Instance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstance
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
            await client.task_instance.set_mapped_task_instance_note(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
                task_id="task_id",
                map_index=1,
                note="note",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_mapped_task_instance_note(
            dag_id, dag_run_id, task_id, map_index, note=note, request_options=request_options
        )
        return _response.data

    async def get_task_instances_batch(
        self,
        *,
        dag_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        duration_gte: typing.Optional[float] = OMIT,
        duration_lte: typing.Optional[float] = OMIT,
        end_date_gte: typing.Optional[dt.datetime] = OMIT,
        end_date_lte: typing.Optional[dt.datetime] = OMIT,
        execution_date_gte: typing.Optional[dt.datetime] = OMIT,
        execution_date_lte: typing.Optional[dt.datetime] = OMIT,
        pool: typing.Optional[typing.Sequence[str]] = OMIT,
        queue: typing.Optional[typing.Sequence[str]] = OMIT,
        start_date_gte: typing.Optional[dt.datetime] = OMIT,
        start_date_lte: typing.Optional[dt.datetime] = OMIT,
        state: typing.Optional[typing.Sequence[TaskState]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskInstanceCollection:
        """
        List task instances from all DAGs and DAG runs.
        This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limits.

        Parameters
        ----------
        dag_ids : typing.Optional[typing.Sequence[str]]
            Return objects with specific DAG IDs.
            The value can be repeated to retrieve multiple matching values (OR condition).

        duration_gte : typing.Optional[float]
            Returns objects greater than or equal to the specified values.

            This can be combined with duration_lte parameter to receive only the selected period.

        duration_lte : typing.Optional[float]
            Returns objects less than or equal to the specified values.

            This can be combined with duration_gte parameter to receive only the selected range.

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte parameter to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte parameter to receive only the selected period.

        pool : typing.Optional[typing.Sequence[str]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        queue : typing.Optional[typing.Sequence[str]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte parameter to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period.

        state : typing.Optional[typing.Sequence[TaskState]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskInstanceCollection
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
            await client.task_instance.get_task_instances_batch()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_task_instances_batch(
            dag_ids=dag_ids,
            duration_gte=duration_gte,
            duration_lte=duration_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            pool=pool,
            queue=queue,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            state=state,
            request_options=request_options,
        )
        return _response.data
