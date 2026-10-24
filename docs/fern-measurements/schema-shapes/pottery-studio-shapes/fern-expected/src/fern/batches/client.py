

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBatchesClient, RawBatchesClient
from .types.mix_batch_request import MixBatchRequest


OMIT = typing.cast(typing.Any, ...)


class BatchesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBatchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBatchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBatchesClient
        """
        return self._raw_client

    def mix_batch(self, *, request: MixBatchRequest, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : MixBatchRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.batches import MixBatchRequest_Recipe

        from fern import FernApi

        client = FernApi()
        client.batches.mix_batch(
            request=MixBatchRequest_Recipe(
                recipe="recipe",
            ),
        )
        """
        _response = self._raw_client.mix_batch(request=request, request_options=request_options)
        return _response.data


class AsyncBatchesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBatchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBatchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBatchesClient
        """
        return self._raw_client

    async def mix_batch(
        self, *, request: MixBatchRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : MixBatchRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.batches import MixBatchRequest_Recipe

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.batches.mix_batch(
                request=MixBatchRequest_Recipe(
                    recipe="recipe",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mix_batch(request=request, request_options=request_options)
        return _response.data
