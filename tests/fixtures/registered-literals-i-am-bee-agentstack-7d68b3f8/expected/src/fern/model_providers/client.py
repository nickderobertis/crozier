

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output4 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output5 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5,
)
from ..types.model_capability import ModelCapability
from ..types.model_provider_type import ModelProviderType
from ..types.paginated_result_model_provider import PaginatedResultModelProvider
from ..types.paginated_result_model_with_score import PaginatedResultModelWithScore
from .raw_client import AsyncRawModelProvidersClient, RawModelProvidersClient


OMIT = typing.cast(typing.Any, ...)


class ModelProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawModelProvidersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawModelProvidersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawModelProvidersClient
        """
        return self._raw_client

    def list_model_providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaginatedResultModelProvider:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultModelProvider
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.model_providers.list_model_providers()
        """
        _response = self._raw_client.list_model_providers(request_options=request_options)
        return _response.data

    def create_model_provider(
        self,
        *,
        type: ModelProviderType,
        base_url: str,
        api_key: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        watsonx_project_id: typing.Optional[str] = OMIT,
        watsonx_space_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4:
        """
        Parameters
        ----------
        type : ModelProviderType

        base_url : str

        api_key : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        watsonx_project_id : typing.Optional[str]

        watsonx_space_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4
            Successful Response

        Examples
        --------
        from fern import FernApi, ModelProviderType

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.model_providers.create_model_provider(
            type=ModelProviderType.ANTHROPIC,
            base_url="base_url",
            api_key="api_key",
        )
        """
        _response = self._raw_client.create_model_provider(
            type=type,
            base_url=base_url,
            api_key=api_key,
            name=name,
            description=description,
            watsonx_project_id=watsonx_project_id,
            watsonx_space_id=watsonx_space_id,
            request_options=request_options,
        )
        return _response.data

    def get_model_provider(
        self, model_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5:
        """
        Parameters
        ----------
        model_provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.model_providers.get_model_provider(
            model_provider_id="model_provider_id",
        )
        """
        _response = self._raw_client.get_model_provider(model_provider_id, request_options=request_options)
        return _response.data

    def delete_model_provider(
        self, model_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        model_provider_id : str

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.model_providers.delete_model_provider(
            model_provider_id="model_provider_id",
        )
        """
        _response = self._raw_client.delete_model_provider(model_provider_id, request_options=request_options)
        return _response.data

    def match(
        self,
        *,
        capability: ModelCapability,
        suggested_models: typing.Optional[typing.Sequence[str]] = OMIT,
        score_cutoff: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultModelWithScore:
        """
        Parameters
        ----------
        capability : ModelCapability

        suggested_models : typing.Optional[typing.Sequence[str]]

        score_cutoff : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultModelWithScore
            Successful Response

        Examples
        --------
        from fern import FernApi, ModelCapability

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.model_providers.match(
            capability=ModelCapability.LLM,
        )
        """
        _response = self._raw_client.match(
            capability=capability,
            suggested_models=suggested_models,
            score_cutoff=score_cutoff,
            request_options=request_options,
        )
        return _response.data


class AsyncModelProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawModelProvidersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawModelProvidersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawModelProvidersClient
        """
        return self._raw_client

    async def list_model_providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaginatedResultModelProvider:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultModelProvider
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.model_providers.list_model_providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_model_providers(request_options=request_options)
        return _response.data

    async def create_model_provider(
        self,
        *,
        type: ModelProviderType,
        base_url: str,
        api_key: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        watsonx_project_id: typing.Optional[str] = OMIT,
        watsonx_space_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4:
        """
        Parameters
        ----------
        type : ModelProviderType

        base_url : str

        api_key : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        watsonx_project_id : typing.Optional[str]

        watsonx_space_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ModelProviderType

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.model_providers.create_model_provider(
                type=ModelProviderType.ANTHROPIC,
                base_url="base_url",
                api_key="api_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_model_provider(
            type=type,
            base_url=base_url,
            api_key=api_key,
            name=name,
            description=description,
            watsonx_project_id=watsonx_project_id,
            watsonx_space_id=watsonx_space_id,
            request_options=request_options,
        )
        return _response.data

    async def get_model_provider(
        self, model_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5:
        """
        Parameters
        ----------
        model_provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.model_providers.get_model_provider(
                model_provider_id="model_provider_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_model_provider(model_provider_id, request_options=request_options)
        return _response.data

    async def delete_model_provider(
        self, model_provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        model_provider_id : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.model_providers.delete_model_provider(
                model_provider_id="model_provider_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_model_provider(model_provider_id, request_options=request_options)
        return _response.data

    async def match(
        self,
        *,
        capability: ModelCapability,
        suggested_models: typing.Optional[typing.Sequence[str]] = OMIT,
        score_cutoff: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultModelWithScore:
        """
        Parameters
        ----------
        capability : ModelCapability

        suggested_models : typing.Optional[typing.Sequence[str]]

        score_cutoff : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultModelWithScore
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ModelCapability

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.model_providers.match(
                capability=ModelCapability.LLM,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.match(
            capability=capability,
            suggested_models=suggested_models,
            score_cutoff=score_cutoff,
            request_options=request_options,
        )
        return _response.data
