

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dag_run import DagRun
from ..types.dag_run_collection import DagRunCollection
from ..types.dag_run_run_type import DagRunRunType
from ..types.dag_state import DagState
from ..types.dataset_event_collection import DatasetEventCollection
from .raw_client import AsyncRawDagRunClient, RawDagRunClient
from .types.update_dag_run_state_state import UpdateDagRunStateState


OMIT = typing.cast(typing.Any, ...)


class DagRunClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDagRunClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDagRunClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDagRunClient
        """
        return self._raw_client

    def get_dag_runs(
        self,
        dag_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        execution_date_gte: typing.Optional[dt.datetime] = None,
        execution_date_lte: typing.Optional[dt.datetime] = None,
        start_date_gte: typing.Optional[dt.datetime] = None,
        start_date_lte: typing.Optional[dt.datetime] = None,
        end_date_gte: typing.Optional[dt.datetime] = None,
        end_date_lte: typing.Optional[dt.datetime] = None,
        state: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagRunCollection:
        """
        This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

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

        state : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagRunCollection
            List of DAG runs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag_run.get_dag_runs(
            dag_id="dag_id",
        )
        """
        _response = self._raw_client.get_dag_runs(
            dag_id,
            limit=limit,
            offset=offset,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            state=state,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def post_dag_run(
        self,
        dag_id_: str,
        *,
        conf: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        dag_id: typing.Optional[str] = OMIT,
        dag_run_id: typing.Optional[str] = OMIT,
        data_interval_end: typing.Optional[dt.datetime] = OMIT,
        data_interval_start: typing.Optional[dt.datetime] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        execution_date: typing.Optional[dt.datetime] = OMIT,
        external_trigger: typing.Optional[bool] = OMIT,
        last_scheduling_decision: typing.Optional[dt.datetime] = OMIT,
        logical_date: typing.Optional[dt.datetime] = OMIT,
        note: typing.Optional[str] = OMIT,
        run_type: typing.Optional[DagRunRunType] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        state: typing.Optional[DagState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagRun:
        """
        Parameters
        ----------
        dag_id_ : str
            The DAG ID.

        conf : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            JSON object describing additional configuration parameters.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

        dag_id : typing.Optional[str]

        dag_run_id : typing.Optional[str]
            Run ID.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

            If not provided, a value will be generated based on execution_date.

            If the specified dag_run_id is in use, the creation request fails with an ALREADY_EXISTS error.

            This together with DAG_ID are a unique key.

        data_interval_end : typing.Optional[dt.datetime]

        data_interval_start : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        execution_date : typing.Optional[dt.datetime]
            The execution date. This is the same as logical_date, kept for backwards compatibility.
            If both this field and logical_date are provided but with different values, the request
            will fail with an BAD_REQUEST error.

            *Changed in version 2.2.0*&#58; Field becomes nullable.

            *Deprecated since version 2.2.0*&#58; Use 'logical_date' instead.

        external_trigger : typing.Optional[bool]

        last_scheduling_decision : typing.Optional[dt.datetime]

        logical_date : typing.Optional[dt.datetime]
            The logical date (previously called execution date). This is the time or interval covered by
            this DAG run, according to the DAG definition.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

            This together with DAG_ID are a unique key.

            *New in version 2.2.0*

        note : typing.Optional[str]
            Contains manually entered notes by the user about the DagRun.

            *New in version 2.5.0*

        run_type : typing.Optional[DagRunRunType]

        start_date : typing.Optional[dt.datetime]
            The start time. The time when DAG run was actually created.

            *Changed in version 2.1.3*&#58; Field becomes nullable.

        state : typing.Optional[DagState]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagRun
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag_run.post_dag_run(
            dag_id_="dag_id",
        )
        """
        _response = self._raw_client.post_dag_run(
            dag_id_,
            conf=conf,
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            data_interval_end=data_interval_end,
            data_interval_start=data_interval_start,
            end_date=end_date,
            execution_date=execution_date,
            external_trigger=external_trigger,
            last_scheduling_decision=last_scheduling_decision,
            logical_date=logical_date,
            note=note,
            run_type=run_type,
            start_date=start_date,
            state=state,
            request_options=request_options,
        )
        return _response.data

    def get_dag_run(
        self, dag_id: str, dag_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DagRun:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagRun
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag_run.get_dag_run(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
        )
        """
        _response = self._raw_client.get_dag_run(dag_id, dag_run_id, request_options=request_options)
        return _response.data

    def delete_dag_run(
        self, dag_id: str, dag_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

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
        client.dag_run.delete_dag_run(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
        )
        """
        _response = self._raw_client.delete_dag_run(dag_id, dag_run_id, request_options=request_options)
        return _response.data

    def update_dag_run_state(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        state: typing.Optional[UpdateDagRunStateState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagRun:
        """
        Modify a DAG run.

        *New in version 2.2.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        state : typing.Optional[UpdateDagRunStateState]
            The state to set this DagRun

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagRun
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag_run.update_dag_run_state(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
        )
        """
        _response = self._raw_client.update_dag_run_state(
            dag_id, dag_run_id, state=state, request_options=request_options
        )
        return _response.data

    def clear_dag_run(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagRun:
        """
        Clear a DAG run.

        *New in version 2.4.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain a list of task instances
            planned to be cleaned, but not modified in any way.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagRun
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag_run.clear_dag_run(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
        )
        """
        _response = self._raw_client.clear_dag_run(dag_id, dag_run_id, dry_run=dry_run, request_options=request_options)
        return _response.data

    def set_dag_run_note(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagRun:
        """
        Update the manual user note of a DagRun.

        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        note : typing.Optional[str]
            Custom notes left by users for this Dag Run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagRun
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag_run.set_dag_run_note(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
        )
        """
        _response = self._raw_client.set_dag_run_note(dag_id, dag_run_id, note=note, request_options=request_options)
        return _response.data

    def get_upstream_dataset_events(
        self, dag_id: str, dag_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetEventCollection:
        """
        Get datasets for a dag run.

        *New in version 2.4.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetEventCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag_run.get_upstream_dataset_events(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
        )
        """
        _response = self._raw_client.get_upstream_dataset_events(dag_id, dag_run_id, request_options=request_options)
        return _response.data

    def get_dag_runs_batch(
        self,
        *,
        dag_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        end_date_gte: typing.Optional[dt.datetime] = OMIT,
        end_date_lte: typing.Optional[dt.datetime] = OMIT,
        execution_date_gte: typing.Optional[dt.datetime] = OMIT,
        execution_date_lte: typing.Optional[dt.datetime] = OMIT,
        order_by: typing.Optional[str] = OMIT,
        page_limit: typing.Optional[int] = OMIT,
        page_offset: typing.Optional[int] = OMIT,
        start_date_gte: typing.Optional[dt.datetime] = OMIT,
        start_date_lte: typing.Optional[dt.datetime] = OMIT,
        states: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagRunCollection:
        """
        This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limit.

        Parameters
        ----------
        dag_ids : typing.Optional[typing.Sequence[str]]
            Return objects with specific DAG IDs.
            The value can be repeated to retrieve multiple matching values (OR condition).

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with end_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with end_date_gte parameter to receive only the selected period.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte key to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte key to receive only the selected period.

        order_by : typing.Optional[str]
            The name of the field to order the results by. Prefix a field name
            with `-` to reverse the sort order.

            *New in version 2.1.0*

        page_limit : typing.Optional[int]
            The numbers of items to return.

        page_offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte key to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period

        states : typing.Optional[typing.Sequence[str]]
            Return objects with specific states.
            The value can be repeated to retrieve multiple matching values (OR condition).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagRunCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag_run.get_dag_runs_batch()
        """
        _response = self._raw_client.get_dag_runs_batch(
            dag_ids=dag_ids,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            order_by=order_by,
            page_limit=page_limit,
            page_offset=page_offset,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            states=states,
            request_options=request_options,
        )
        return _response.data


class AsyncDagRunClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDagRunClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDagRunClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDagRunClient
        """
        return self._raw_client

    async def get_dag_runs(
        self,
        dag_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        execution_date_gte: typing.Optional[dt.datetime] = None,
        execution_date_lte: typing.Optional[dt.datetime] = None,
        start_date_gte: typing.Optional[dt.datetime] = None,
        start_date_lte: typing.Optional[dt.datetime] = None,
        end_date_gte: typing.Optional[dt.datetime] = None,
        end_date_lte: typing.Optional[dt.datetime] = None,
        state: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagRunCollection:
        """
        This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

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

        state : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The value can be repeated to retrieve multiple matching values (OR condition).

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagRunCollection
            List of DAG runs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dag_run.get_dag_runs(
                dag_id="dag_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dag_runs(
            dag_id,
            limit=limit,
            offset=offset,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            state=state,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def post_dag_run(
        self,
        dag_id_: str,
        *,
        conf: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        dag_id: typing.Optional[str] = OMIT,
        dag_run_id: typing.Optional[str] = OMIT,
        data_interval_end: typing.Optional[dt.datetime] = OMIT,
        data_interval_start: typing.Optional[dt.datetime] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        execution_date: typing.Optional[dt.datetime] = OMIT,
        external_trigger: typing.Optional[bool] = OMIT,
        last_scheduling_decision: typing.Optional[dt.datetime] = OMIT,
        logical_date: typing.Optional[dt.datetime] = OMIT,
        note: typing.Optional[str] = OMIT,
        run_type: typing.Optional[DagRunRunType] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        state: typing.Optional[DagState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagRun:
        """
        Parameters
        ----------
        dag_id_ : str
            The DAG ID.

        conf : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            JSON object describing additional configuration parameters.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

        dag_id : typing.Optional[str]

        dag_run_id : typing.Optional[str]
            Run ID.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

            If not provided, a value will be generated based on execution_date.

            If the specified dag_run_id is in use, the creation request fails with an ALREADY_EXISTS error.

            This together with DAG_ID are a unique key.

        data_interval_end : typing.Optional[dt.datetime]

        data_interval_start : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        execution_date : typing.Optional[dt.datetime]
            The execution date. This is the same as logical_date, kept for backwards compatibility.
            If both this field and logical_date are provided but with different values, the request
            will fail with an BAD_REQUEST error.

            *Changed in version 2.2.0*&#58; Field becomes nullable.

            *Deprecated since version 2.2.0*&#58; Use 'logical_date' instead.

        external_trigger : typing.Optional[bool]

        last_scheduling_decision : typing.Optional[dt.datetime]

        logical_date : typing.Optional[dt.datetime]
            The logical date (previously called execution date). This is the time or interval covered by
            this DAG run, according to the DAG definition.

            The value of this field can be set only when creating the object. If you try to modify the
            field of an existing object, the request fails with an BAD_REQUEST error.

            This together with DAG_ID are a unique key.

            *New in version 2.2.0*

        note : typing.Optional[str]
            Contains manually entered notes by the user about the DagRun.

            *New in version 2.5.0*

        run_type : typing.Optional[DagRunRunType]

        start_date : typing.Optional[dt.datetime]
            The start time. The time when DAG run was actually created.

            *Changed in version 2.1.3*&#58; Field becomes nullable.

        state : typing.Optional[DagState]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagRun
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
            await client.dag_run.post_dag_run(
                dag_id_="dag_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_dag_run(
            dag_id_,
            conf=conf,
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            data_interval_end=data_interval_end,
            data_interval_start=data_interval_start,
            end_date=end_date,
            execution_date=execution_date,
            external_trigger=external_trigger,
            last_scheduling_decision=last_scheduling_decision,
            logical_date=logical_date,
            note=note,
            run_type=run_type,
            start_date=start_date,
            state=state,
            request_options=request_options,
        )
        return _response.data

    async def get_dag_run(
        self, dag_id: str, dag_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DagRun:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagRun
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
            await client.dag_run.get_dag_run(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dag_run(dag_id, dag_run_id, request_options=request_options)
        return _response.data

    async def delete_dag_run(
        self, dag_id: str, dag_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

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
            await client.dag_run.delete_dag_run(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_dag_run(dag_id, dag_run_id, request_options=request_options)
        return _response.data

    async def update_dag_run_state(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        state: typing.Optional[UpdateDagRunStateState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagRun:
        """
        Modify a DAG run.

        *New in version 2.2.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        state : typing.Optional[UpdateDagRunStateState]
            The state to set this DagRun

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagRun
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
            await client.dag_run.update_dag_run_state(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_dag_run_state(
            dag_id, dag_run_id, state=state, request_options=request_options
        )
        return _response.data

    async def clear_dag_run(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagRun:
        """
        Clear a DAG run.

        *New in version 2.4.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        dry_run : typing.Optional[bool]
            If set, don't actually run this operation. The response will contain a list of task instances
            planned to be cleaned, but not modified in any way.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagRun
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
            await client.dag_run.clear_dag_run(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clear_dag_run(
            dag_id, dag_run_id, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    async def set_dag_run_note(
        self,
        dag_id: str,
        dag_run_id: str,
        *,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagRun:
        """
        Update the manual user note of a DagRun.

        *New in version 2.5.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        note : typing.Optional[str]
            Custom notes left by users for this Dag Run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagRun
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
            await client.dag_run.set_dag_run_note(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_dag_run_note(
            dag_id, dag_run_id, note=note, request_options=request_options
        )
        return _response.data

    async def get_upstream_dataset_events(
        self, dag_id: str, dag_run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetEventCollection:
        """
        Get datasets for a dag run.

        *New in version 2.4.0*

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetEventCollection
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
            await client.dag_run.get_upstream_dataset_events(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_upstream_dataset_events(
            dag_id, dag_run_id, request_options=request_options
        )
        return _response.data

    async def get_dag_runs_batch(
        self,
        *,
        dag_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        end_date_gte: typing.Optional[dt.datetime] = OMIT,
        end_date_lte: typing.Optional[dt.datetime] = OMIT,
        execution_date_gte: typing.Optional[dt.datetime] = OMIT,
        execution_date_lte: typing.Optional[dt.datetime] = OMIT,
        order_by: typing.Optional[str] = OMIT,
        page_limit: typing.Optional[int] = OMIT,
        page_offset: typing.Optional[int] = OMIT,
        start_date_gte: typing.Optional[dt.datetime] = OMIT,
        start_date_lte: typing.Optional[dt.datetime] = OMIT,
        states: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagRunCollection:
        """
        This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limit.

        Parameters
        ----------
        dag_ids : typing.Optional[typing.Sequence[str]]
            Return objects with specific DAG IDs.
            The value can be repeated to retrieve multiple matching values (OR condition).

        end_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with end_date_lte parameter to receive only the selected period.

        end_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with end_date_gte parameter to receive only the selected period.

        execution_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal to the specified date.

            This can be combined with execution_date_lte key to receive only the selected period.

        execution_date_lte : typing.Optional[dt.datetime]
            Returns objects less than or equal to the specified date.

            This can be combined with execution_date_gte key to receive only the selected period.

        order_by : typing.Optional[str]
            The name of the field to order the results by. Prefix a field name
            with `-` to reverse the sort order.

            *New in version 2.1.0*

        page_limit : typing.Optional[int]
            The numbers of items to return.

        page_offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        start_date_gte : typing.Optional[dt.datetime]
            Returns objects greater or equal the specified date.

            This can be combined with start_date_lte key to receive only the selected period.

        start_date_lte : typing.Optional[dt.datetime]
            Returns objects less or equal the specified date.

            This can be combined with start_date_gte parameter to receive only the selected period

        states : typing.Optional[typing.Sequence[str]]
            Return objects with specific states.
            The value can be repeated to retrieve multiple matching values (OR condition).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagRunCollection
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
            await client.dag_run.get_dag_runs_batch()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dag_runs_batch(
            dag_ids=dag_ids,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            order_by=order_by,
            page_limit=page_limit,
            page_offset=page_offset,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            states=states,
            request_options=request_options,
        )
        return _response.data
