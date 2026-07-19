

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.embedding_model import EmbeddingModel
from ..types.model import Model
from ..types.provider_category import ProviderCategory
from ..types.provider_type import ProviderType
from .raw_client import AsyncRawModelsClient, RawModelsClient


class ModelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawModelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawModelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawModelsClient
        """
        return self._raw_client

    def list_models(
        self,
        *,
        provider_category: typing.Optional[typing.Sequence[ProviderCategory]] = None,
        provider_name: typing.Optional[str] = None,
        provider_type: typing.Optional[ProviderType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Model]:
        """
        List available LLM models using the asynchronous implementation for improved performance.

        Returns Model format which extends LLMConfig with additional metadata fields.
        Legacy LLMConfig fields are marked as deprecated but still available for backward compatibility.

        Parameters
        ----------
        provider_category : typing.Optional[typing.Sequence[ProviderCategory]]

        provider_name : typing.Optional[str]

        provider_type : typing.Optional[ProviderType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Model]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.models.list_models()
        """
        _response = self._raw_client.list_models(
            provider_category=provider_category,
            provider_name=provider_name,
            provider_type=provider_type,
            request_options=request_options,
        )
        return _response.data

    def list_embedding_models(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EmbeddingModel]:
        """
        List available embedding models using the asynchronous implementation for improved performance.

        Returns EmbeddingModel format which extends EmbeddingConfig with additional metadata fields.
        Legacy EmbeddingConfig fields are marked as deprecated but still available for backward compatibility.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EmbeddingModel]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.models.list_embedding_models()
        """
        _response = self._raw_client.list_embedding_models(request_options=request_options)
        return _response.data

    def listembeddingmodels(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.models.listembeddingmodels()
        """
        _response = self._raw_client.listembeddingmodels(request_options=request_options)
        return _response.data


class AsyncModelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawModelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawModelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawModelsClient
        """
        return self._raw_client

    async def list_models(
        self,
        *,
        provider_category: typing.Optional[typing.Sequence[ProviderCategory]] = None,
        provider_name: typing.Optional[str] = None,
        provider_type: typing.Optional[ProviderType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Model]:
        """
        List available LLM models using the asynchronous implementation for improved performance.

        Returns Model format which extends LLMConfig with additional metadata fields.
        Legacy LLMConfig fields are marked as deprecated but still available for backward compatibility.

        Parameters
        ----------
        provider_category : typing.Optional[typing.Sequence[ProviderCategory]]

        provider_name : typing.Optional[str]

        provider_type : typing.Optional[ProviderType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Model]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.models.list_models()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_models(
            provider_category=provider_category,
            provider_name=provider_name,
            provider_type=provider_type,
            request_options=request_options,
        )
        return _response.data

    async def list_embedding_models(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EmbeddingModel]:
        """
        List available embedding models using the asynchronous implementation for improved performance.

        Returns EmbeddingModel format which extends EmbeddingConfig with additional metadata fields.
        Legacy EmbeddingConfig fields are marked as deprecated but still available for backward compatibility.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EmbeddingModel]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.models.list_embedding_models()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_embedding_models(request_options=request_options)
        return _response.data

    async def listembeddingmodels(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.models.listembeddingmodels()


        asyncio.run(main())
        """
        _response = await self._raw_client.listembeddingmodels(request_options=request_options)
        return _response.data
