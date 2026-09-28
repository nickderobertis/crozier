

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.embeddings_migrate_post_response import EmbeddingsMigratePostResponse
from .raw_client import AsyncRawEmbeddingsClient, RawEmbeddingsClient


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

    def migrate_embedding_vectors_when_switching_between_embedding_providers_re_embeds_all_data_using_the_current_provider(
        self, *, collection: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> EmbeddingsMigratePostResponse:
        """
        Migrate embedding vectors when switching between embedding providers. Re-embeds all data using the current provider.

        Parameters
        ----------
        collection : typing.Optional[str]
            Collection name to migrate. If omitted, migrates all collections.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmbeddingsMigratePostResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.embeddings.migrate_embedding_vectors_when_switching_between_embedding_providers_re_embeds_all_data_using_the_current_provider()
        """
        _response = self._raw_client.migrate_embedding_vectors_when_switching_between_embedding_providers_re_embeds_all_data_using_the_current_provider(
            collection=collection, request_options=request_options
        )
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

    async def migrate_embedding_vectors_when_switching_between_embedding_providers_re_embeds_all_data_using_the_current_provider(
        self, *, collection: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> EmbeddingsMigratePostResponse:
        """
        Migrate embedding vectors when switching between embedding providers. Re-embeds all data using the current provider.

        Parameters
        ----------
        collection : typing.Optional[str]
            Collection name to migrate. If omitted, migrates all collections.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmbeddingsMigratePostResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.embeddings.migrate_embedding_vectors_when_switching_between_embedding_providers_re_embeds_all_data_using_the_current_provider()


        asyncio.run(main())
        """
        _response = await self._raw_client.migrate_embedding_vectors_when_switching_between_embedding_providers_re_embeds_all_data_using_the_current_provider(
            collection=collection, request_options=request_options
        )
        return _response.data
