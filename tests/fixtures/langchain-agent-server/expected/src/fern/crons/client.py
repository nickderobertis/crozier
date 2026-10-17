

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cron import Cron
from .raw_client import AsyncRawCronsClient, RawCronsClient
from .types.cron_create_config import CronCreateConfig
from .types.cron_create_durability import CronCreateDurability
from .types.cron_create_input import CronCreateInput
from .types.cron_create_interrupt_after import CronCreateInterruptAfter
from .types.cron_create_interrupt_before import CronCreateInterruptBefore
from .types.cron_create_on_run_completed import CronCreateOnRunCompleted
from .types.cron_create_stream_mode import CronCreateStreamMode
from .types.cron_patch_config import CronPatchConfig
from .types.cron_patch_durability import CronPatchDurability
from .types.cron_patch_input import CronPatchInput
from .types.cron_patch_interrupt_after import CronPatchInterruptAfter
from .types.cron_patch_interrupt_before import CronPatchInterruptBefore
from .types.cron_patch_on_run_completed import CronPatchOnRunCompleted
from .types.cron_patch_stream_mode import CronPatchStreamMode
from .types.cron_search_select_item import CronSearchSelectItem
from .types.cron_search_sort_by import CronSearchSortBy
from .types.cron_search_sort_order import CronSearchSortOrder
from .types.thread_cron_create_config import ThreadCronCreateConfig
from .types.thread_cron_create_durability import ThreadCronCreateDurability
from .types.thread_cron_create_input import ThreadCronCreateInput
from .types.thread_cron_create_interrupt_after import ThreadCronCreateInterruptAfter
from .types.thread_cron_create_interrupt_before import ThreadCronCreateInterruptBefore
from .types.thread_cron_create_multitask_strategy import ThreadCronCreateMultitaskStrategy
from .types.thread_cron_create_stream_mode import ThreadCronCreateStreamMode


OMIT = typing.cast(typing.Any, ...)


class CronsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCronsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCronsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCronsClient
        """
        return self._raw_client

    def create_thread_cron(
        self,
        thread_id: str,
        *,
        schedule: str,
        assistant_id: str,
        timezone: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[ThreadCronCreateInput] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[ThreadCronCreateConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[ThreadCronCreateInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[ThreadCronCreateInterruptAfter] = OMIT,
        multitask_strategy: typing.Optional[ThreadCronCreateMultitaskStrategy] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stream_mode: typing.Optional[ThreadCronCreateStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        durability: typing.Optional[ThreadCronCreateDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cron:
        """
        Create a cron to schedule runs on a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        schedule : str
            The cron schedule to execute this job on.

        assistant_id : str

        timezone : typing.Optional[str]
            IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.

        end_time : typing.Optional[dt.datetime]
            The end date to stop running the cron.

        input : typing.Optional[ThreadCronCreateInput]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the cron job runs.

        config : typing.Optional[ThreadCronCreateConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[ThreadCronCreateInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[ThreadCronCreateInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        multitask_strategy : typing.Optional[ThreadCronCreateMultitaskStrategy]
            Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

        enabled : typing.Optional[bool]
            Whether the cron job should be enabled. Disabled crons are not executed.

        stream_mode : typing.Optional[ThreadCronCreateStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        durability : typing.Optional[ThreadCronCreateDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cron
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.crons.create_thread_cron(
            thread_id="thread_id",
            schedule="schedule",
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.create_thread_cron(
            thread_id,
            schedule=schedule,
            assistant_id=assistant_id,
            timezone=timezone,
            end_time=end_time,
            input=input,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            interrupt_before=interrupt_before,
            interrupt_after=interrupt_after,
            multitask_strategy=multitask_strategy,
            enabled=enabled,
            stream_mode=stream_mode,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            durability=durability,
            request_options=request_options,
        )
        return _response.data

    def create_cron(
        self,
        *,
        schedule: str,
        assistant_id: str,
        timezone: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[CronCreateInput] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[CronCreateConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[CronCreateInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[CronCreateInterruptAfter] = OMIT,
        on_run_completed: typing.Optional[CronCreateOnRunCompleted] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stream_mode: typing.Optional[CronCreateStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        durability: typing.Optional[CronCreateDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cron:
        """
        Create a cron to schedule runs on new threads.

        Parameters
        ----------
        schedule : str
            The cron schedule to execute this job on.

        assistant_id : str

        timezone : typing.Optional[str]
            IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.

        end_time : typing.Optional[dt.datetime]
            The end date to stop running the cron.

        input : typing.Optional[CronCreateInput]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the cron job runs.

        config : typing.Optional[CronCreateConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[CronCreateInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[CronCreateInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        on_run_completed : typing.Optional[CronCreateOnRunCompleted]
            What to do with the thread after the run completes. 'delete' removes the thread after execution. 'keep' creates a new thread for each execution but does not clean them up.

        enabled : typing.Optional[bool]
            Whether the cron job should be enabled. Disabled crons are not executed.

        stream_mode : typing.Optional[CronCreateStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        durability : typing.Optional[CronCreateDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cron
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.crons.create_cron(
            schedule="schedule",
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.create_cron(
            schedule=schedule,
            assistant_id=assistant_id,
            timezone=timezone,
            end_time=end_time,
            input=input,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            interrupt_before=interrupt_before,
            interrupt_after=interrupt_after,
            on_run_completed=on_run_completed,
            enabled=enabled,
            stream_mode=stream_mode,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            durability=durability,
            request_options=request_options,
        )
        return _response.data

    def search_crons_runs_crons_post(
        self,
        *,
        assistant_id: typing.Optional[str] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[CronSearchSortBy] = OMIT,
        sort_order: typing.Optional[CronSearchSortOrder] = OMIT,
        select: typing.Optional[typing.Sequence[CronSearchSelectItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Cron]:
        """
        Search all active crons

        Parameters
        ----------
        assistant_id : typing.Optional[str]
            The assistant ID or graph name to filter by using exact match.

        thread_id : typing.Optional[str]
            The thread ID to search for.

        enabled : typing.Optional[bool]
            Filter by enabled status. If not provided, returns both enabled and disabled crons.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        limit : typing.Optional[int]
            The maximum number of results to return.

        offset : typing.Optional[int]
            The number of results to skip.

        sort_by : typing.Optional[CronSearchSortBy]
            The field to sort by.

        sort_order : typing.Optional[CronSearchSortOrder]
            The order to sort by.

        select : typing.Optional[typing.Sequence[CronSearchSelectItem]]
            Specify which fields to return. If not provided, all fields are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Cron]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.crons.search_crons_runs_crons_post()
        """
        _response = self._raw_client.search_crons_runs_crons_post(
            assistant_id=assistant_id,
            thread_id=thread_id,
            enabled=enabled,
            metadata=metadata,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order,
            select=select,
            request_options=request_options,
        )
        return _response.data

    def count_crons(
        self,
        *,
        assistant_id: typing.Optional[str] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Get the count of crons matching the specified criteria.

        Parameters
        ----------
        assistant_id : typing.Optional[str]
            The assistant ID or graph name to search for.

        thread_id : typing.Optional[str]
            The thread ID to search for.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.crons.count_crons()
        """
        _response = self._raw_client.count_crons(
            assistant_id=assistant_id, thread_id=thread_id, metadata=metadata, request_options=request_options
        )
        return _response.data

    def get_cron(self, cron_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Cron:
        """
        Get a cron by ID.

        Parameters
        ----------
        cron_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cron
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.crons.get_cron(
            cron_id="cron_id",
        )
        """
        _response = self._raw_client.get_cron(cron_id, request_options=request_options)
        return _response.data

    def delete_cron(self, cron_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Delete a cron by ID.

        Parameters
        ----------
        cron_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.crons.delete_cron(
            cron_id="cron_id",
        )
        """
        _response = self._raw_client.delete_cron(cron_id, request_options=request_options)
        return _response.data

    def patch_cron(
        self,
        cron_id: str,
        *,
        schedule: typing.Optional[str] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[CronPatchInput] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[CronPatchConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[CronPatchInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[CronPatchInterruptAfter] = OMIT,
        on_run_completed: typing.Optional[CronPatchOnRunCompleted] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stream_mode: typing.Optional[CronPatchStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        durability: typing.Optional[CronPatchDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cron:
        """
        Update a cron job by ID.

        Parameters
        ----------
        cron_id : str

        schedule : typing.Optional[str]
            The cron schedule to execute this job on.

        timezone : typing.Optional[str]
            IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.

        end_time : typing.Optional[dt.datetime]
            The end date to stop running the cron. Send null to clear a previously set end time; omit this field to leave the existing value unchanged.

        input : typing.Optional[CronPatchInput]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing cron job metadata.

        config : typing.Optional[CronPatchConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[CronPatchInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[CronPatchInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        on_run_completed : typing.Optional[CronPatchOnRunCompleted]
            What to do with the thread after the run completes. 'delete' removes the thread after execution. 'keep' creates a new thread for each execution but does not clean them up.

        enabled : typing.Optional[bool]
            Enable or disable the cron job.

        stream_mode : typing.Optional[CronPatchStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        durability : typing.Optional[CronPatchDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cron
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.crons.patch_cron(
            cron_id="cron_id",
        )
        """
        _response = self._raw_client.patch_cron(
            cron_id,
            schedule=schedule,
            timezone=timezone,
            end_time=end_time,
            input=input,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            interrupt_before=interrupt_before,
            interrupt_after=interrupt_after,
            on_run_completed=on_run_completed,
            enabled=enabled,
            stream_mode=stream_mode,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            durability=durability,
            request_options=request_options,
        )
        return _response.data


class AsyncCronsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCronsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCronsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCronsClient
        """
        return self._raw_client

    async def create_thread_cron(
        self,
        thread_id: str,
        *,
        schedule: str,
        assistant_id: str,
        timezone: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[ThreadCronCreateInput] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[ThreadCronCreateConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[ThreadCronCreateInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[ThreadCronCreateInterruptAfter] = OMIT,
        multitask_strategy: typing.Optional[ThreadCronCreateMultitaskStrategy] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stream_mode: typing.Optional[ThreadCronCreateStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        durability: typing.Optional[ThreadCronCreateDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cron:
        """
        Create a cron to schedule runs on a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        schedule : str
            The cron schedule to execute this job on.

        assistant_id : str

        timezone : typing.Optional[str]
            IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.

        end_time : typing.Optional[dt.datetime]
            The end date to stop running the cron.

        input : typing.Optional[ThreadCronCreateInput]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the cron job runs.

        config : typing.Optional[ThreadCronCreateConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[ThreadCronCreateInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[ThreadCronCreateInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        multitask_strategy : typing.Optional[ThreadCronCreateMultitaskStrategy]
            Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

        enabled : typing.Optional[bool]
            Whether the cron job should be enabled. Disabled crons are not executed.

        stream_mode : typing.Optional[ThreadCronCreateStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        durability : typing.Optional[ThreadCronCreateDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cron
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.crons.create_thread_cron(
                thread_id="thread_id",
                schedule="schedule",
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_thread_cron(
            thread_id,
            schedule=schedule,
            assistant_id=assistant_id,
            timezone=timezone,
            end_time=end_time,
            input=input,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            interrupt_before=interrupt_before,
            interrupt_after=interrupt_after,
            multitask_strategy=multitask_strategy,
            enabled=enabled,
            stream_mode=stream_mode,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            durability=durability,
            request_options=request_options,
        )
        return _response.data

    async def create_cron(
        self,
        *,
        schedule: str,
        assistant_id: str,
        timezone: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[CronCreateInput] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[CronCreateConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[CronCreateInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[CronCreateInterruptAfter] = OMIT,
        on_run_completed: typing.Optional[CronCreateOnRunCompleted] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stream_mode: typing.Optional[CronCreateStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        durability: typing.Optional[CronCreateDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cron:
        """
        Create a cron to schedule runs on new threads.

        Parameters
        ----------
        schedule : str
            The cron schedule to execute this job on.

        assistant_id : str

        timezone : typing.Optional[str]
            IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.

        end_time : typing.Optional[dt.datetime]
            The end date to stop running the cron.

        input : typing.Optional[CronCreateInput]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the cron job runs.

        config : typing.Optional[CronCreateConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[CronCreateInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[CronCreateInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        on_run_completed : typing.Optional[CronCreateOnRunCompleted]
            What to do with the thread after the run completes. 'delete' removes the thread after execution. 'keep' creates a new thread for each execution but does not clean them up.

        enabled : typing.Optional[bool]
            Whether the cron job should be enabled. Disabled crons are not executed.

        stream_mode : typing.Optional[CronCreateStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        durability : typing.Optional[CronCreateDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cron
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.crons.create_cron(
                schedule="schedule",
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_cron(
            schedule=schedule,
            assistant_id=assistant_id,
            timezone=timezone,
            end_time=end_time,
            input=input,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            interrupt_before=interrupt_before,
            interrupt_after=interrupt_after,
            on_run_completed=on_run_completed,
            enabled=enabled,
            stream_mode=stream_mode,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            durability=durability,
            request_options=request_options,
        )
        return _response.data

    async def search_crons_runs_crons_post(
        self,
        *,
        assistant_id: typing.Optional[str] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[CronSearchSortBy] = OMIT,
        sort_order: typing.Optional[CronSearchSortOrder] = OMIT,
        select: typing.Optional[typing.Sequence[CronSearchSelectItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Cron]:
        """
        Search all active crons

        Parameters
        ----------
        assistant_id : typing.Optional[str]
            The assistant ID or graph name to filter by using exact match.

        thread_id : typing.Optional[str]
            The thread ID to search for.

        enabled : typing.Optional[bool]
            Filter by enabled status. If not provided, returns both enabled and disabled crons.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        limit : typing.Optional[int]
            The maximum number of results to return.

        offset : typing.Optional[int]
            The number of results to skip.

        sort_by : typing.Optional[CronSearchSortBy]
            The field to sort by.

        sort_order : typing.Optional[CronSearchSortOrder]
            The order to sort by.

        select : typing.Optional[typing.Sequence[CronSearchSelectItem]]
            Specify which fields to return. If not provided, all fields are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Cron]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.crons.search_crons_runs_crons_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_crons_runs_crons_post(
            assistant_id=assistant_id,
            thread_id=thread_id,
            enabled=enabled,
            metadata=metadata,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order,
            select=select,
            request_options=request_options,
        )
        return _response.data

    async def count_crons(
        self,
        *,
        assistant_id: typing.Optional[str] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Get the count of crons matching the specified criteria.

        Parameters
        ----------
        assistant_id : typing.Optional[str]
            The assistant ID or graph name to search for.

        thread_id : typing.Optional[str]
            The thread ID to search for.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.crons.count_crons()


        asyncio.run(main())
        """
        _response = await self._raw_client.count_crons(
            assistant_id=assistant_id, thread_id=thread_id, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def get_cron(self, cron_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Cron:
        """
        Get a cron by ID.

        Parameters
        ----------
        cron_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cron
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.crons.get_cron(
                cron_id="cron_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cron(cron_id, request_options=request_options)
        return _response.data

    async def delete_cron(self, cron_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Delete a cron by ID.

        Parameters
        ----------
        cron_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.crons.delete_cron(
                cron_id="cron_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_cron(cron_id, request_options=request_options)
        return _response.data

    async def patch_cron(
        self,
        cron_id: str,
        *,
        schedule: typing.Optional[str] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        end_time: typing.Optional[dt.datetime] = OMIT,
        input: typing.Optional[CronPatchInput] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[CronPatchConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[CronPatchInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[CronPatchInterruptAfter] = OMIT,
        on_run_completed: typing.Optional[CronPatchOnRunCompleted] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stream_mode: typing.Optional[CronPatchStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        durability: typing.Optional[CronPatchDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cron:
        """
        Update a cron job by ID.

        Parameters
        ----------
        cron_id : str

        schedule : typing.Optional[str]
            The cron schedule to execute this job on.

        timezone : typing.Optional[str]
            IANA timezone for the cron schedule (e.g. 'America/New_York'). Defaults to null, which is treated as UTC.

        end_time : typing.Optional[dt.datetime]
            The end date to stop running the cron. Send null to clear a previously set end time; omit this field to leave the existing value unchanged.

        input : typing.Optional[CronPatchInput]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing cron job metadata.

        config : typing.Optional[CronPatchConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[CronPatchInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[CronPatchInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        on_run_completed : typing.Optional[CronPatchOnRunCompleted]
            What to do with the thread after the run completes. 'delete' removes the thread after execution. 'keep' creates a new thread for each execution but does not clean them up.

        enabled : typing.Optional[bool]
            Enable or disable the cron job.

        stream_mode : typing.Optional[CronPatchStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        durability : typing.Optional[CronPatchDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cron
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.crons.patch_cron(
                cron_id="cron_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_cron(
            cron_id,
            schedule=schedule,
            timezone=timezone,
            end_time=end_time,
            input=input,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            interrupt_before=interrupt_before,
            interrupt_after=interrupt_after,
            on_run_completed=on_run_completed,
            enabled=enabled,
            stream_mode=stream_mode,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            durability=durability,
            request_options=request_options,
        )
        return _response.data
