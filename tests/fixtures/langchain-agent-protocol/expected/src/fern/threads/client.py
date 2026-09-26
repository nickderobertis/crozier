

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.message import Message
from ..types.thread import Thread
from ..types.thread_checkpoint import ThreadCheckpoint
from ..types.thread_state import ThreadState
from ..types.thread_status import ThreadStatus
from .raw_client import AsyncRawThreadsClient, RawThreadsClient
from .types.thread_create_if_exists import ThreadCreateIfExists


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
            thread_id=thread_id, metadata=metadata, if_exists=if_exists, request_options=request_options
        )
        return _response.data

    def search_threads(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[ThreadStatus] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Thread]:
        """
        Search for threads.

        This endpoint also functions as the endpoint to list all threads.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Thread metadata to filter on.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            State values to filter on.

        status : typing.Optional[ThreadStatus]
            Thread status to filter on.

        limit : typing.Optional[int]
            Maximum number to return.

        offset : typing.Optional[int]
            Offset to start from.

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
            metadata=metadata, values=values, status=status, limit=limit, offset=offset, request_options=request_options
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

    def copy_thread(self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Thread:
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
        client.threads.copy_thread(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.copy_thread(thread_id, request_options=request_options)
        return _response.data

    def get_thread(self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Thread:
        """
        Get a thread by ID.

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
        client.threads.get_thread(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.get_thread(thread_id, request_options=request_options)
        return _response.data

    def delete_thread(self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        None

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
        checkpoint: typing.Optional[ThreadCheckpoint] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        messages: typing.Optional[typing.Sequence[Message]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Thread:
        """
        Update a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        checkpoint : typing.Optional[ThreadCheckpoint]
            The identifier of the checkpoint to branch from. Ignored for metadata-only patches. If not provided, defaults to the latest checkpoint.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing thread metadata.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            Values to merge with existing thread values.

        messages : typing.Optional[typing.Sequence[Message]]
            Messages to combine with current thread messages.

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
            thread_id,
            checkpoint=checkpoint,
            metadata=metadata,
            values=values,
            messages=messages,
            request_options=request_options,
        )
        return _response.data


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
            thread_id=thread_id, metadata=metadata, if_exists=if_exists, request_options=request_options
        )
        return _response.data

    async def search_threads(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[ThreadStatus] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Thread]:
        """
        Search for threads.

        This endpoint also functions as the endpoint to list all threads.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Thread metadata to filter on.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            State values to filter on.

        status : typing.Optional[ThreadStatus]
            Thread status to filter on.

        limit : typing.Optional[int]
            Maximum number to return.

        offset : typing.Optional[int]
            Offset to start from.

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
            metadata=metadata, values=values, status=status, limit=limit, offset=offset, request_options=request_options
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

    async def copy_thread(self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Thread:
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
            await client.threads.copy_thread(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.copy_thread(thread_id, request_options=request_options)
        return _response.data

    async def get_thread(self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Thread:
        """
        Get a thread by ID.

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
            await client.threads.get_thread(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_thread(thread_id, request_options=request_options)
        return _response.data

    async def delete_thread(self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        None

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
        checkpoint: typing.Optional[ThreadCheckpoint] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        messages: typing.Optional[typing.Sequence[Message]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Thread:
        """
        Update a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        checkpoint : typing.Optional[ThreadCheckpoint]
            The identifier of the checkpoint to branch from. Ignored for metadata-only patches. If not provided, defaults to the latest checkpoint.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing thread metadata.

        values : typing.Optional[typing.Dict[str, typing.Any]]
            Values to merge with existing thread values.

        messages : typing.Optional[typing.Sequence[Message]]
            Messages to combine with current thread messages.

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
            thread_id,
            checkpoint=checkpoint,
            metadata=metadata,
            values=values,
            messages=messages,
            request_options=request_options,
        )
        return _response.data
