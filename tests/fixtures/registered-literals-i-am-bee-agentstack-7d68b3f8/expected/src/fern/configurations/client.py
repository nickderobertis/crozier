

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output6 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput6,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output7 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput7,
)
from .raw_client import AsyncRawConfigurationsClient, RawConfigurationsClient


OMIT = typing.cast(typing.Any, ...)


class ConfigurationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConfigurationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConfigurationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConfigurationsClient
        """
        return self._raw_client

    def get_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput6:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput6
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.configurations.get_configuration()
        """
        _response = self._raw_client.get_configuration(request_options=request_options)
        return _response.data

    def update_configuration(
        self,
        *,
        default_llm_model: typing.Optional[str] = OMIT,
        default_embedding_model: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput7:
        """
        Parameters
        ----------
        default_llm_model : typing.Optional[str]

        default_embedding_model : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput7
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.configurations.update_configuration()
        """
        _response = self._raw_client.update_configuration(
            default_llm_model=default_llm_model,
            default_embedding_model=default_embedding_model,
            request_options=request_options,
        )
        return _response.data


class AsyncConfigurationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConfigurationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConfigurationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConfigurationsClient
        """
        return self._raw_client

    async def get_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput6:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput6
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
            await client.configurations.get_configuration()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_configuration(request_options=request_options)
        return _response.data

    async def update_configuration(
        self,
        *,
        default_llm_model: typing.Optional[str] = OMIT,
        default_embedding_model: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput7:
        """
        Parameters
        ----------
        default_llm_model : typing.Optional[str]

        default_embedding_model : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput7
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
            await client.configurations.update_configuration()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_configuration(
            default_llm_model=default_llm_model,
            default_embedding_model=default_embedding_model,
            request_options=request_options,
        )
        return _response.data
