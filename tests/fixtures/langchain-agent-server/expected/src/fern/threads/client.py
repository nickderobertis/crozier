

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.checkpoint_config import CheckpointConfig
from ..types.join_thread_stream_threads_thread_id_stream_get_request_stream_modes import (
    JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModes,
)
from ..types.thread import Thread
from ..types.thread_prune_response import ThreadPruneResponse
from ..types.thread_state import ThreadState
from ..types.thread_state_update_response import ThreadStateUpdateResponse
from ..types.thread_storage import ThreadStorage
from .raw_client import AsyncRawThreadsClient, RawThreadsClient
from .types.thread_count_request_status import ThreadCountRequestStatus
from .types.thread_create_if_exists import ThreadCreateIfExists
from .types.thread_create_supersteps_item import ThreadCreateSuperstepsItem
from .types.thread_create_ttl import ThreadCreateTtl
from .types.thread_patch_ttl import ThreadPatchTtl
from .types.thread_prune_request_strategy import ThreadPruneRequestStrategy
from .types.thread_search_request_select_item import ThreadSearchRequestSelectItem
from .types.thread_search_request_sort_by import ThreadSearchRequestSortBy
from .types.thread_search_request_sort_order import ThreadSearchRequestSortOrder
from .types.thread_search_request_status import ThreadSearchRequestStatus
from .types.thread_state_update_values import ThreadStateUpdateValues


OMIT = typing.cast(typing.Any, ...)


class ThreadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawThreadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawThreadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawThreadsClient
        """
        return self._raw_client

    def create_thread(
        self,
        *,
        thread_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        if_exists: typing.Optional[ThreadCreateIfExists] = OMIT,
        ttl: typing.Optional[ThreadCreateTtl] = OMIT,
        supersteps: typing.Optional[typing.Sequence[ThreadCreateSuperstepsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Thread:
        """
        Create a thread.

        Parameters
        ----------
        thread_id : typing.Optional[str]
            The ID of the thread. If not provided, a random UUID will be generated.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to add to thread.

        if_exists : typing.Optional[ThreadCreateIfExists]
            How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing thread).

        ttl : typing.Optional[ThreadCreateTtl]
            The time-to-live for the thread.

        supersteps : typing.Optional[typing.Sequence[ThreadCreateSuperstepsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Thread
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.threads.create_thread()
        """
        _response = self._raw_client.create_thread(
            thread_id=thread_id,
            metadata=metadata,
            if_exists=if_exists,
            ttl=ttl,
            supersteps=supersteps,
            request_options=request_options,
        )
        return _response.data

    def search_threads(
        self,
        *,
        ids: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[ThreadSearchRequestStatus] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[ThreadSearchRequestSortBy] = OMIT,
        sort_order: typing.Optional[ThreadSearchRequestSortOrder] = OMIT,
        select: typing.Optional[typing.Sequence[ThreadSearchRequestSelectItem]] = OMIT,
        extract: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Thread]:
        """
        Search for threads.

        This endpoint also functions as the endpoint to list all threads.

        Parameters
        ----------
        ids : typing.Optional[typing.Sequence[str]]
            List of thread IDs to include. Others are excluded.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Thread metadata to filter on.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            State values to filter on.

        status : typing.Optional[ThreadSearchRequestStatus]
            Thread status to filter on.

        limit : typing.Optional[int]
            Maximum number to return.

        offset : typing.Optional[int]
            Offset to start from.

        sort_by : typing.Optional[ThreadSearchRequestSortBy]
            Sort by field.

        sort_order : typing.Optional[ThreadSearchRequestSortOrder]
            Sort order.

        select : typing.Optional[typing.Sequence[ThreadSearchRequestSelectItem]]
            Specify which fields to return. If not provided, all fields are returned.

        extract : typing.Optional[typing.Dict[str, str]]
            Map of alias to JSONB path for extracting specific values. Paths must start with values, metadata, config, or interrupts. Example: {"last_msg": "values.messages[-1]"}.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Thread]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.threads.search_threads()
        """
        _response = self._raw_client.search_threads(
            ids=ids,
            metadata=metadata,
            values=values,
            status=status,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order,
            select=select,
            extract=extract,
            request_options=request_options,
        )
        return _response.data

    def count_threads(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[ThreadCountRequestStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Get the count of threads matching the specified criteria.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Thread metadata to filter on.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            State values to filter on.

        status : typing.Optional[ThreadCountRequestStatus]
            Thread status to filter on.

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
        client.threads.count_threads()
        """
        _response = self._raw_client.count_threads(
            metadata=metadata, values=values, status=status, request_options=request_options
        )
        return _response.data

    def prune_threads(
        self,
        *,
        thread_ids: typing.Sequence[str],
        strategy: typing.Optional[ThreadPruneRequestStrategy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadPruneResponse:
        """
        Prune threads by ID. The 'delete' strategy removes threads entirely. The 'keep_latest' strategy prunes old checkpoints but keeps threads and their latest state.

        Parameters
        ----------
        thread_ids : typing.Sequence[str]
            List of thread IDs to prune.

        strategy : typing.Optional[ThreadPruneRequestStrategy]
            The prune strategy. 'delete' removes threads entirely. 'keep_latest' prunes old checkpoints but keeps threads and their latest state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadPruneResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.threads.prune_threads(
            thread_ids=["thread_ids"],
        )
        """
        _response = self._raw_client.prune_threads(
            thread_ids=thread_ids, strategy=strategy, request_options=request_options
        )
        return _response.data

    def get_thread_storage(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ThreadStorage:
        """
        Bytes the thread's checkpoints occupy in the built-in checkpointer, as stored: checkpoints, channel values (per channel) and pending writes. Returns 501 when a custom checkpointer is configured.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadStorage
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.threads.get_thread_storage(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.get_thread_storage(thread_id, request_options=request_options)
        return _response.data

    def get_latest_thread_state(
        self,
        thread_id: str,
        *,
        subgraphs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadState:
        """
        Get state for a thread.

        The latest state of the thread (i.e. latest checkpoint) is returned.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        subgraphs : typing.Optional[bool]
            Whether to include subgraphs in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadState
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.threads.get_latest_thread_state(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.get_latest_thread_state(
            thread_id, subgraphs=subgraphs, request_options=request_options
        )
        return _response.data

    def update_thread_state(
        self,
        thread_id: str,
        *,
        values: typing.Optional[ThreadStateUpdateValues] = OMIT,
        checkpoint: typing.Optional[CheckpointConfig] = OMIT,
        as_node: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadStateUpdateResponse:
        """
        Add state to a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        values : typing.Optional[ThreadStateUpdateValues]
            The values to update the state with.

        checkpoint : typing.Optional[CheckpointConfig]
            The checkpoint to update the state of.

        as_node : typing.Optional[str]
            Update the state as if this node had just executed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadStateUpdateResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.threads.update_thread_state(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.update_thread_state(
            thread_id, values=values, checkpoint=checkpoint, as_node=as_node, request_options=request_options
        )
        return _response.data

    def get_thread_state_at_checkpoint(
        self,
        thread_id: str,
        checkpoint_id: str,
        *,
        subgraphs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadState:
        """
        Get state for a thread at a specific checkpoint.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        checkpoint_id : str
            The ID of the checkpoint.

        subgraphs : typing.Optional[bool]
            Whether to include subgraphs in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadState
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.threads.get_thread_state_at_checkpoint(
            thread_id="thread_id",
            checkpoint_id="checkpoint_id",
        )
        """
        _response = self._raw_client.get_thread_state_at_checkpoint(
            thread_id, checkpoint_id, subgraphs=subgraphs, request_options=request_options
        )
        return _response.data

    def post_thread_state_at_checkpoint_threads_thread_id_state_checkpoint_id_get(
        self,
        thread_id: str,
        *,
        checkpoint: CheckpointConfig,
        subgraphs: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadState:
        """
        Get state for a thread at a specific checkpoint.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        checkpoint : CheckpointConfig
            The checkpoint to get the state for.

        subgraphs : typing.Optional[bool]
            Include subgraph states.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadState
            Success

        Examples
        --------
        from fern import CheckpointConfig, FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.threads.post_thread_state_at_checkpoint_threads_thread_id_state_checkpoint_id_get(
            thread_id="thread_id",
            checkpoint=CheckpointConfig(),
        )
        """
        _response = self._raw_client.post_thread_state_at_checkpoint_threads_thread_id_state_checkpoint_id_get(
            thread_id, checkpoint=checkpoint, subgraphs=subgraphs, request_options=request_options
        )
        return _response.data

    def get_thread_history(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ThreadState]:
        """
        Get all past states for a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        limit : typing.Optional[int]

        before : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThreadState]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.threads.get_thread_history(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.get_thread_history(
            thread_id, limit=limit, before=before, request_options=request_options
        )
        return _response.data

    def get_thread_history_post(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = OMIT,
        before: typing.Optional[CheckpointConfig] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        checkpoint: typing.Optional[CheckpointConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ThreadState]:
        """
        Get all past states for a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        limit : typing.Optional[int]
            The maximum number of states to return.

        before : typing.Optional[CheckpointConfig]
            Return states before this checkpoint.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Filter states by metadata key-value pairs.

        checkpoint : typing.Optional[CheckpointConfig]
            Return states for this subgraph.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThreadState]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.threads.get_thread_history_post(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.get_thread_history_post(
            thread_id,
            limit=limit,
            before=before,
            metadata=metadata,
            checkpoint=checkpoint,
            request_options=request_options,
        )
        return _response.data

    def copy_thread_post(self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Thread:
        """
        Create a new thread with a copy of the state and checkpoints from an existing thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Thread
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.threads.copy_thread_post(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.copy_thread_post(thread_id, request_options=request_options)
        return _response.data

    def get_thread(
        self,
        thread_id: str,
        *,
        include: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Thread:
        """
        Get a thread by ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        include : typing.Optional[str]
            Comma-separated list of additional fields to include. Supported values: ttl

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Thread
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.threads.get_thread(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.get_thread(thread_id, include=include, request_options=request_options)
        return _response.data

    def delete_thread(self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Delete a thread by ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

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
        client.threads.delete_thread(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.delete_thread(thread_id, request_options=request_options)
        return _response.data

    def patch_thread(
        self,
        thread_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        ttl: typing.Optional[ThreadPatchTtl] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Thread:
        """
        Update a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing thread metadata.

        ttl : typing.Optional[ThreadPatchTtl]
            The time-to-live for the thread.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Thread
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.threads.patch_thread(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.patch_thread(
            thread_id, metadata=metadata, ttl=ttl, request_options=request_options
        )
        return _response.data

    def join_thread_stream(
        self,
        thread_id: str,
        *,
        stream_modes: typing.Optional[JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModes] = None,
        last_event_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[str]:
        """
        This endpoint streams output in real-time from a thread. The stream will include the output of each run executed sequentially on the thread and will remain open indefinitely. It is the responsibility of the calling client to close the connection.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        stream_modes : typing.Optional[JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModes]
            Stream modes to control which events are returned. 'lifecycle' returns only run start/end events, 'run_modes' returns all run events (default behavior), 'state_update' returns only state update events.

        last_event_id : typing.Optional[str]
            The ID of the last event received. Used to resume streaming from a specific point. Pass '-' to resume from the beginning.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.threads.join_thread_stream(
            thread_id="thread_id",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.join_thread_stream(
            thread_id, stream_modes=stream_modes, last_event_id=last_event_id, request_options=request_options
        ) as r:
            yield from r.data


class AsyncThreadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawThreadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawThreadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawThreadsClient
        """
        return self._raw_client

    async def create_thread(
        self,
        *,
        thread_id: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        if_exists: typing.Optional[ThreadCreateIfExists] = OMIT,
        ttl: typing.Optional[ThreadCreateTtl] = OMIT,
        supersteps: typing.Optional[typing.Sequence[ThreadCreateSuperstepsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Thread:
        """
        Create a thread.

        Parameters
        ----------
        thread_id : typing.Optional[str]
            The ID of the thread. If not provided, a random UUID will be generated.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to add to thread.

        if_exists : typing.Optional[ThreadCreateIfExists]
            How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing thread).

        ttl : typing.Optional[ThreadCreateTtl]
            The time-to-live for the thread.

        supersteps : typing.Optional[typing.Sequence[ThreadCreateSuperstepsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Thread
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.threads.create_thread()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_thread(
            thread_id=thread_id,
            metadata=metadata,
            if_exists=if_exists,
            ttl=ttl,
            supersteps=supersteps,
            request_options=request_options,
        )
        return _response.data

    async def search_threads(
        self,
        *,
        ids: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[ThreadSearchRequestStatus] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[ThreadSearchRequestSortBy] = OMIT,
        sort_order: typing.Optional[ThreadSearchRequestSortOrder] = OMIT,
        select: typing.Optional[typing.Sequence[ThreadSearchRequestSelectItem]] = OMIT,
        extract: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Thread]:
        """
        Search for threads.

        This endpoint also functions as the endpoint to list all threads.

        Parameters
        ----------
        ids : typing.Optional[typing.Sequence[str]]
            List of thread IDs to include. Others are excluded.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Thread metadata to filter on.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            State values to filter on.

        status : typing.Optional[ThreadSearchRequestStatus]
            Thread status to filter on.

        limit : typing.Optional[int]
            Maximum number to return.

        offset : typing.Optional[int]
            Offset to start from.

        sort_by : typing.Optional[ThreadSearchRequestSortBy]
            Sort by field.

        sort_order : typing.Optional[ThreadSearchRequestSortOrder]
            Sort order.

        select : typing.Optional[typing.Sequence[ThreadSearchRequestSelectItem]]
            Specify which fields to return. If not provided, all fields are returned.

        extract : typing.Optional[typing.Dict[str, str]]
            Map of alias to JSONB path for extracting specific values. Paths must start with values, metadata, config, or interrupts. Example: {"last_msg": "values.messages[-1]"}.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Thread]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.threads.search_threads()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_threads(
            ids=ids,
            metadata=metadata,
            values=values,
            status=status,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order,
            select=select,
            extract=extract,
            request_options=request_options,
        )
        return _response.data

    async def count_threads(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[ThreadCountRequestStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Get the count of threads matching the specified criteria.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Thread metadata to filter on.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            State values to filter on.

        status : typing.Optional[ThreadCountRequestStatus]
            Thread status to filter on.

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
            await client.threads.count_threads()


        asyncio.run(main())
        """
        _response = await self._raw_client.count_threads(
            metadata=metadata, values=values, status=status, request_options=request_options
        )
        return _response.data

    async def prune_threads(
        self,
        *,
        thread_ids: typing.Sequence[str],
        strategy: typing.Optional[ThreadPruneRequestStrategy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadPruneResponse:
        """
        Prune threads by ID. The 'delete' strategy removes threads entirely. The 'keep_latest' strategy prunes old checkpoints but keeps threads and their latest state.

        Parameters
        ----------
        thread_ids : typing.Sequence[str]
            List of thread IDs to prune.

        strategy : typing.Optional[ThreadPruneRequestStrategy]
            The prune strategy. 'delete' removes threads entirely. 'keep_latest' prunes old checkpoints but keeps threads and their latest state.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadPruneResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.threads.prune_threads(
                thread_ids=["thread_ids"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prune_threads(
            thread_ids=thread_ids, strategy=strategy, request_options=request_options
        )
        return _response.data

    async def get_thread_storage(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ThreadStorage:
        """
        Bytes the thread's checkpoints occupy in the built-in checkpointer, as stored: checkpoints, channel values (per channel) and pending writes. Returns 501 when a custom checkpointer is configured.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadStorage
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.threads.get_thread_storage(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_thread_storage(thread_id, request_options=request_options)
        return _response.data

    async def get_latest_thread_state(
        self,
        thread_id: str,
        *,
        subgraphs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadState:
        """
        Get state for a thread.

        The latest state of the thread (i.e. latest checkpoint) is returned.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        subgraphs : typing.Optional[bool]
            Whether to include subgraphs in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadState
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.threads.get_latest_thread_state(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_latest_thread_state(
            thread_id, subgraphs=subgraphs, request_options=request_options
        )
        return _response.data

    async def update_thread_state(
        self,
        thread_id: str,
        *,
        values: typing.Optional[ThreadStateUpdateValues] = OMIT,
        checkpoint: typing.Optional[CheckpointConfig] = OMIT,
        as_node: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadStateUpdateResponse:
        """
        Add state to a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        values : typing.Optional[ThreadStateUpdateValues]
            The values to update the state with.

        checkpoint : typing.Optional[CheckpointConfig]
            The checkpoint to update the state of.

        as_node : typing.Optional[str]
            Update the state as if this node had just executed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadStateUpdateResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.threads.update_thread_state(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_thread_state(
            thread_id, values=values, checkpoint=checkpoint, as_node=as_node, request_options=request_options
        )
        return _response.data

    async def get_thread_state_at_checkpoint(
        self,
        thread_id: str,
        checkpoint_id: str,
        *,
        subgraphs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadState:
        """
        Get state for a thread at a specific checkpoint.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        checkpoint_id : str
            The ID of the checkpoint.

        subgraphs : typing.Optional[bool]
            Whether to include subgraphs in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadState
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.threads.get_thread_state_at_checkpoint(
                thread_id="thread_id",
                checkpoint_id="checkpoint_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_thread_state_at_checkpoint(
            thread_id, checkpoint_id, subgraphs=subgraphs, request_options=request_options
        )
        return _response.data

    async def post_thread_state_at_checkpoint_threads_thread_id_state_checkpoint_id_get(
        self,
        thread_id: str,
        *,
        checkpoint: CheckpointConfig,
        subgraphs: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadState:
        """
        Get state for a thread at a specific checkpoint.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        checkpoint : CheckpointConfig
            The checkpoint to get the state for.

        subgraphs : typing.Optional[bool]
            Include subgraph states.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadState
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CheckpointConfig

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.threads.post_thread_state_at_checkpoint_threads_thread_id_state_checkpoint_id_get(
                thread_id="thread_id",
                checkpoint=CheckpointConfig(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_thread_state_at_checkpoint_threads_thread_id_state_checkpoint_id_get(
            thread_id, checkpoint=checkpoint, subgraphs=subgraphs, request_options=request_options
        )
        return _response.data

    async def get_thread_history(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ThreadState]:
        """
        Get all past states for a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        limit : typing.Optional[int]

        before : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThreadState]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.threads.get_thread_history(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_thread_history(
            thread_id, limit=limit, before=before, request_options=request_options
        )
        return _response.data

    async def get_thread_history_post(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = OMIT,
        before: typing.Optional[CheckpointConfig] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        checkpoint: typing.Optional[CheckpointConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ThreadState]:
        """
        Get all past states for a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        limit : typing.Optional[int]
            The maximum number of states to return.

        before : typing.Optional[CheckpointConfig]
            Return states before this checkpoint.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Filter states by metadata key-value pairs.

        checkpoint : typing.Optional[CheckpointConfig]
            Return states for this subgraph.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThreadState]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.threads.get_thread_history_post(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_thread_history_post(
            thread_id,
            limit=limit,
            before=before,
            metadata=metadata,
            checkpoint=checkpoint,
            request_options=request_options,
        )
        return _response.data

    async def copy_thread_post(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Thread:
        """
        Create a new thread with a copy of the state and checkpoints from an existing thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Thread
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.threads.copy_thread_post(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.copy_thread_post(thread_id, request_options=request_options)
        return _response.data

    async def get_thread(
        self,
        thread_id: str,
        *,
        include: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Thread:
        """
        Get a thread by ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        include : typing.Optional[str]
            Comma-separated list of additional fields to include. Supported values: ttl

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Thread
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.threads.get_thread(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_thread(thread_id, include=include, request_options=request_options)
        return _response.data

    async def delete_thread(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete a thread by ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

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
            await client.threads.delete_thread(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_thread(thread_id, request_options=request_options)
        return _response.data

    async def patch_thread(
        self,
        thread_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        ttl: typing.Optional[ThreadPatchTtl] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Thread:
        """
        Update a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing thread metadata.

        ttl : typing.Optional[ThreadPatchTtl]
            The time-to-live for the thread.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Thread
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.threads.patch_thread(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_thread(
            thread_id, metadata=metadata, ttl=ttl, request_options=request_options
        )
        return _response.data

    async def join_thread_stream(
        self,
        thread_id: str,
        *,
        stream_modes: typing.Optional[JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModes] = None,
        last_event_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[str]:
        """
        This endpoint streams output in real-time from a thread. The stream will include the output of each run executed sequentially on the thread and will remain open indefinitely. It is the responsibility of the calling client to close the connection.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        stream_modes : typing.Optional[JoinThreadStreamThreadsThreadIdStreamGetRequestStreamModes]
            Stream modes to control which events are returned. 'lifecycle' returns only run start/end events, 'run_modes' returns all run events (default behavior), 'state_update' returns only state update events.

        last_event_id : typing.Optional[str]
            The ID of the last event received. Used to resume streaming from a specific point. Pass '-' to resume from the beginning.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = client.threads.join_thread_stream(
                thread_id="thread_id",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.join_thread_stream(
            thread_id, stream_modes=stream_modes, last_event_id=last_event_id, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk
