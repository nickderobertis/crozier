

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agent_card_input import AgentCardInput
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output2 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output3 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3,
)
from ..types.create_provider_request_location import CreateProviderRequestLocation
from ..types.list_variables_schema import ListVariablesSchema
from ..types.paginated_result_model_output import PaginatedResultModelOutput
from ..types.provider_with_state import ProviderWithState
from .raw_client import AsyncRawProvidersClient, RawProvidersClient
from .types.patch_provider_request_location import PatchProviderRequestLocation


OMIT = typing.cast(typing.Any, ...)


class ProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProvidersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProvidersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProvidersClient
        """
        return self._raw_client

    def list_providers(
        self,
        *,
        user_owned: typing.Optional[bool] = None,
        origin: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultModelOutput:
        """
        Parameters
        ----------
        user_owned : typing.Optional[bool]

        origin : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultModelOutput
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.list_providers()
        """
        _response = self._raw_client.list_providers(
            user_owned=user_owned, origin=origin, request_options=request_options
        )
        return _response.data

    def create_provider(
        self,
        *,
        location: CreateProviderRequestLocation,
        agent_card: typing.Optional[AgentCardInput] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        origin: typing.Optional[str] = OMIT,
        auto_stop_timeout_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderWithState:
        """
        Parameters
        ----------
        location : CreateProviderRequestLocation

        agent_card : typing.Optional[AgentCardInput]

        variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        origin : typing.Optional[str]
            A unique origin of the provider: most often a docker or github repository url (without tag). This is used to determine multiple versions of the same agent.

        auto_stop_timeout_sec : typing.Optional[int]
            Timeout after which the agent provider will be automatically downscaled if unused.Contact administrator if you need to increase this value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderWithState
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.create_provider(
            location="location",
        )
        """
        _response = self._raw_client.create_provider(
            location=location,
            agent_card=agent_card,
            variables=variables,
            origin=origin,
            auto_stop_timeout_sec=auto_stop_timeout_sec,
            request_options=request_options,
        )
        return _response.data

    def get_provider(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.get_provider(
            id="id",
        )
        """
        _response = self._raw_client.get_provider(id, request_options=request_options)
        return _response.data

    def delete_provider(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
        client.providers.delete_provider(
            id="id",
        )
        """
        _response = self._raw_client.delete_provider(id, request_options=request_options)
        return _response.data

    def patch_provider(
        self,
        id: str,
        *,
        location: typing.Optional[PatchProviderRequestLocation] = OMIT,
        agent_card: typing.Optional[AgentCardInput] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        origin: typing.Optional[str] = OMIT,
        auto_stop_timeout_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderWithState:
        """
        Parameters
        ----------
        id : str

        location : typing.Optional[PatchProviderRequestLocation]

        agent_card : typing.Optional[AgentCardInput]

        variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        origin : typing.Optional[str]
            A unique origin of the provider: most often a docker or github repository url (without tag). This is used to determine multiple versions of the same agent. None means that origin will be recomputed from location. To preserve original value, set it explicitly.

        auto_stop_timeout_sec : typing.Optional[int]
            Timeout after which the agent provider will be automatically downscaled if unused.Contact administrator if you need to increase this value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderWithState
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.patch_provider(
            id="id",
        )
        """
        _response = self._raw_client.patch_provider(
            id,
            location=location,
            agent_card=agent_card,
            variables=variables,
            origin=origin,
            auto_stop_timeout_sec=auto_stop_timeout_sec,
            request_options=request_options,
        )
        return _response.data

    def preview_provider(
        self,
        *,
        location: CreateProviderRequestLocation,
        agent_card: typing.Optional[AgentCardInput] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        origin: typing.Optional[str] = OMIT,
        auto_stop_timeout_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderWithState:
        """
        Parameters
        ----------
        location : CreateProviderRequestLocation

        agent_card : typing.Optional[AgentCardInput]

        variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        origin : typing.Optional[str]
            A unique origin of the provider: most often a docker or github repository url (without tag). This is used to determine multiple versions of the same agent.

        auto_stop_timeout_sec : typing.Optional[int]
            Timeout after which the agent provider will be automatically downscaled if unused.Contact administrator if you need to increase this value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderWithState
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.preview_provider(
            location="location",
        )
        """
        _response = self._raw_client.preview_provider(
            location=location,
            agent_card=agent_card,
            variables=variables,
            origin=origin,
            auto_stop_timeout_sec=auto_stop_timeout_sec,
            request_options=request_options,
        )
        return _response.data

    def get_provider_by_location(
        self, location: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3:
        """
        Parameters
        ----------
        location : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.get_provider_by_location(
            location="location",
        )
        """
        _response = self._raw_client.get_provider_by_location(location, request_options=request_options)
        return _response.data

    def stream_logs(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.stream_logs(
            id="id",
        )
        """
        _response = self._raw_client.stream_logs(id, request_options=request_options)
        return _response.data

    def list_provider_variables(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListVariablesSchema:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListVariablesSchema
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.list_provider_variables(
            id="id",
        )
        """
        _response = self._raw_client.list_provider_variables(id, request_options=request_options)
        return _response.data

    def update_provider_variables(
        self,
        id: str,
        *,
        variables: typing.Dict[str, typing.Optional[str]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        id : str

        variables : typing.Dict[str, typing.Optional[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.update_provider_variables(
            id="id",
            variables={},
        )
        """
        _response = self._raw_client.update_provider_variables(id, variables=variables, request_options=request_options)
        return _response.data


class AsyncProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProvidersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProvidersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProvidersClient
        """
        return self._raw_client

    async def list_providers(
        self,
        *,
        user_owned: typing.Optional[bool] = None,
        origin: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResultModelOutput:
        """
        Parameters
        ----------
        user_owned : typing.Optional[bool]

        origin : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultModelOutput
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
            await client.providers.list_providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_providers(
            user_owned=user_owned, origin=origin, request_options=request_options
        )
        return _response.data

    async def create_provider(
        self,
        *,
        location: CreateProviderRequestLocation,
        agent_card: typing.Optional[AgentCardInput] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        origin: typing.Optional[str] = OMIT,
        auto_stop_timeout_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderWithState:
        """
        Parameters
        ----------
        location : CreateProviderRequestLocation

        agent_card : typing.Optional[AgentCardInput]

        variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        origin : typing.Optional[str]
            A unique origin of the provider: most often a docker or github repository url (without tag). This is used to determine multiple versions of the same agent.

        auto_stop_timeout_sec : typing.Optional[int]
            Timeout after which the agent provider will be automatically downscaled if unused.Contact administrator if you need to increase this value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderWithState
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
            await client.providers.create_provider(
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_provider(
            location=location,
            agent_card=agent_card,
            variables=variables,
            origin=origin,
            auto_stop_timeout_sec=auto_stop_timeout_sec,
            request_options=request_options,
        )
        return _response.data

    async def get_provider(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2
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
            await client.providers.get_provider(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_provider(id, request_options=request_options)
        return _response.data

    async def delete_provider(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            await client.providers.delete_provider(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_provider(id, request_options=request_options)
        return _response.data

    async def patch_provider(
        self,
        id: str,
        *,
        location: typing.Optional[PatchProviderRequestLocation] = OMIT,
        agent_card: typing.Optional[AgentCardInput] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        origin: typing.Optional[str] = OMIT,
        auto_stop_timeout_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderWithState:
        """
        Parameters
        ----------
        id : str

        location : typing.Optional[PatchProviderRequestLocation]

        agent_card : typing.Optional[AgentCardInput]

        variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        origin : typing.Optional[str]
            A unique origin of the provider: most often a docker or github repository url (without tag). This is used to determine multiple versions of the same agent. None means that origin will be recomputed from location. To preserve original value, set it explicitly.

        auto_stop_timeout_sec : typing.Optional[int]
            Timeout after which the agent provider will be automatically downscaled if unused.Contact administrator if you need to increase this value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderWithState
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
            await client.providers.patch_provider(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_provider(
            id,
            location=location,
            agent_card=agent_card,
            variables=variables,
            origin=origin,
            auto_stop_timeout_sec=auto_stop_timeout_sec,
            request_options=request_options,
        )
        return _response.data

    async def preview_provider(
        self,
        *,
        location: CreateProviderRequestLocation,
        agent_card: typing.Optional[AgentCardInput] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        origin: typing.Optional[str] = OMIT,
        auto_stop_timeout_sec: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderWithState:
        """
        Parameters
        ----------
        location : CreateProviderRequestLocation

        agent_card : typing.Optional[AgentCardInput]

        variables : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        origin : typing.Optional[str]
            A unique origin of the provider: most often a docker or github repository url (without tag). This is used to determine multiple versions of the same agent.

        auto_stop_timeout_sec : typing.Optional[int]
            Timeout after which the agent provider will be automatically downscaled if unused.Contact administrator if you need to increase this value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderWithState
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
            await client.providers.preview_provider(
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_provider(
            location=location,
            agent_card=agent_card,
            variables=variables,
            origin=origin,
            auto_stop_timeout_sec=auto_stop_timeout_sec,
            request_options=request_options,
        )
        return _response.data

    async def get_provider_by_location(
        self, location: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3:
        """
        Parameters
        ----------
        location : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3
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
            await client.providers.get_provider_by_location(
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_provider_by_location(location, request_options=request_options)
        return _response.data

    async def stream_logs(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
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
            await client.providers.stream_logs(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stream_logs(id, request_options=request_options)
        return _response.data

    async def list_provider_variables(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListVariablesSchema:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListVariablesSchema
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
            await client.providers.list_provider_variables(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_provider_variables(id, request_options=request_options)
        return _response.data

    async def update_provider_variables(
        self,
        id: str,
        *,
        variables: typing.Dict[str, typing.Optional[str]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        id : str

        variables : typing.Dict[str, typing.Optional[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
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
            await client.providers.update_provider_variables(
                id="id",
                variables={},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_provider_variables(
            id, variables=variables, request_options=request_options
        )
        return _response.data
