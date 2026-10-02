

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.generation import Generation
from ..types.generation_target import GenerationTarget
from .raw_client import AsyncRawWorkflowsClient, RawWorkflowsClient


OMIT = typing.cast(typing.Any, ...)


class WorkflowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWorkflowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWorkflowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWorkflowsClient
        """
        return self._raw_client

    def create_generation(
        self, *, target: GenerationTarget, request_options: typing.Optional[RequestOptions] = None
    ) -> Generation:
        """
        Starts authenticated course, chapter, or lesson generation. Daily and monthly limits depend on the caller's entitlement. Chapter and lesson targets also require an active subscription when the free first-chapter rule does not apply.

        Parameters
        ----------
        target : GenerationTarget

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Generation
            Generation accepted

        Examples
        --------
        from fern import FernApi, GenerationTarget

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workflows.create_generation(
            target=GenerationTarget(
                id="id",
                type="coursePrompt",
            ),
        )
        """
        _response = self._raw_client.create_generation(target=target, request_options=request_options)
        return _response.data

    def get_generation(
        self, generation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Generation:
        """
        Parameters
        ----------
        generation_id : str
            Generation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Generation
            Current generation status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workflows.get_generation(
            generation_id="generationId",
        )
        """
        _response = self._raw_client.get_generation(generation_id, request_options=request_options)
        return _response.data

    def stream_generation_events(
        self,
        generation_id: str,
        *,
        start_index: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[str]:
        """
        Returns a resumable Server-Sent Events stream with generation step updates.

        Parameters
        ----------
        generation_id : str
            Generation ID

        start_index : typing.Optional[int]
            Zero-based event index to resume from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            Generation event stream

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        response = client.workflows.stream_generation_events(
            generation_id="generationId",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.stream_generation_events(
            generation_id, start_index=start_index, request_options=request_options
        ) as r:
            yield from r.data


class AsyncWorkflowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWorkflowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWorkflowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWorkflowsClient
        """
        return self._raw_client

    async def create_generation(
        self, *, target: GenerationTarget, request_options: typing.Optional[RequestOptions] = None
    ) -> Generation:
        """
        Starts authenticated course, chapter, or lesson generation. Daily and monthly limits depend on the caller's entitlement. Chapter and lesson targets also require an active subscription when the free first-chapter rule does not apply.

        Parameters
        ----------
        target : GenerationTarget

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Generation
            Generation accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GenerationTarget

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workflows.create_generation(
                target=GenerationTarget(
                    id="id",
                    type="coursePrompt",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_generation(target=target, request_options=request_options)
        return _response.data

    async def get_generation(
        self, generation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Generation:
        """
        Parameters
        ----------
        generation_id : str
            Generation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Generation
            Current generation status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workflows.get_generation(
                generation_id="generationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_generation(generation_id, request_options=request_options)
        return _response.data

    async def stream_generation_events(
        self,
        generation_id: str,
        *,
        start_index: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[str]:
        """
        Returns a resumable Server-Sent Events stream with generation step updates.

        Parameters
        ----------
        generation_id : str
            Generation ID

        start_index : typing.Optional[int]
            Zero-based event index to resume from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            Generation event stream

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.workflows.stream_generation_events(
                generation_id="generationId",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.stream_generation_events(
            generation_id, start_index=start_index, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk
