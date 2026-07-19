

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEmbeddingsClient, RawEmbeddingsClient


class EmbeddingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEmbeddingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEmbeddingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEmbeddingsClient
        """
        return self._raw_client

    def get_total_storage_size(self, *, request_options: typing.Optional[RequestOptions] = None) -> float:
        """
        Get the total size of all embeddings in the database for a user in the storage unit given.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.embeddings.get_total_storage_size()
        """
        _response = self._raw_client.get_total_storage_size(request_options=request_options)
        return _response.data


class AsyncEmbeddingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEmbeddingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEmbeddingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEmbeddingsClient
        """
        return self._raw_client

    async def get_total_storage_size(self, *, request_options: typing.Optional[RequestOptions] = None) -> float:
        """
        Get the total size of all embeddings in the database for a user in the storage unit given.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.embeddings.get_total_storage_size()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_total_storage_size(request_options=request_options)
        return _response.data
