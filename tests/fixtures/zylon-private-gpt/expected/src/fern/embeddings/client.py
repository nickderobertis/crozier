

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.embeddings_response import EmbeddingsResponse
from .raw_client import AsyncRawEmbeddingsClient, RawEmbeddingsClient
from .types.embeddings_body_input import EmbeddingsBodyInput


OMIT = typing.cast(typing.Any, ...)


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

    def embeddings_generation(
        self, *, input: EmbeddingsBodyInput, request_options: typing.Optional[RequestOptions] = None
    ) -> EmbeddingsResponse:
        """
        Get a vector representation of a given input.

        That vector representation can be easily consumed
        by machine learning models and algorithms.

        Parameters
        ----------
        input : EmbeddingsBodyInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmbeddingsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.embeddings.embeddings_generation(
            input="input",
        )
        """
        _response = self._raw_client.embeddings_generation(input=input, request_options=request_options)
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

    async def embeddings_generation(
        self, *, input: EmbeddingsBodyInput, request_options: typing.Optional[RequestOptions] = None
    ) -> EmbeddingsResponse:
        """
        Get a vector representation of a given input.

        That vector representation can be easily consumed
        by machine learning models and algorithms.

        Parameters
        ----------
        input : EmbeddingsBodyInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmbeddingsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.embeddings.embeddings_generation(
                input="input",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.embeddings_generation(input=input, request_options=request_options)
        return _response.data
