

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agent_card_output import AgentCardOutput
from .raw_client import AsyncRawA2AClient, RawA2AClient


class A2AClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawA2AClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawA2AClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawA2AClient
        """
        return self._raw_client

    def get_agent_card_api_v1a2a_provider_id_well_known_agent_card_json_get(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentCardOutput:
        """
        Parameters
        ----------
        provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentCardOutput
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.a2a.get_agent_card_api_v1a2a_provider_id_well_known_agent_card_json_get(
            provider_id="provider_id",
        )
        """
        _response = self._raw_client.get_agent_card_api_v1a2a_provider_id_well_known_agent_card_json_get(
            provider_id, request_options=request_options
        )
        return _response.data

    def a2a_proxy_jsonrpc_transport(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        provider_id : str

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
        client.a2a.a2a_proxy_jsonrpc_transport(
            provider_id="provider_id",
        )
        """
        _response = self._raw_client.a2a_proxy_jsonrpc_transport(provider_id, request_options=request_options)
        return _response.data

    def proxy_http_transport_api_v1a2a_provider_id_http_path_options(
        self, provider_id: str, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        provider_id : str

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.a2a.proxy_http_transport_api_v1a2a_provider_id_http_path_options(
            provider_id="provider_id",
            path="path",
        )
        """
        _response = self._raw_client.proxy_http_transport_api_v1a2a_provider_id_http_path_options(
            provider_id, path, request_options=request_options
        )
        return _response.headers

    def proxy_http_transport_api_v1a2a_provider_id_http_options(
        self,
        provider_id: str,
        *,
        path: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        provider_id : str

        path : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.a2a.proxy_http_transport_api_v1a2a_provider_id_http_options(
            provider_id="provider_id",
        )
        """
        _response = self._raw_client.proxy_http_transport_api_v1a2a_provider_id_http_options(
            provider_id, path=path, request_options=request_options
        )
        return _response.headers


class AsyncA2AClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawA2AClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawA2AClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawA2AClient
        """
        return self._raw_client

    async def get_agent_card_api_v1a2a_provider_id_well_known_agent_card_json_get(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AgentCardOutput:
        """
        Parameters
        ----------
        provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentCardOutput
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
            await client.a2a.get_agent_card_api_v1a2a_provider_id_well_known_agent_card_json_get(
                provider_id="provider_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agent_card_api_v1a2a_provider_id_well_known_agent_card_json_get(
            provider_id, request_options=request_options
        )
        return _response.data

    async def a2a_proxy_jsonrpc_transport(
        self, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        provider_id : str

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
            await client.a2a.a2a_proxy_jsonrpc_transport(
                provider_id="provider_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.a2a_proxy_jsonrpc_transport(provider_id, request_options=request_options)
        return _response.data

    async def proxy_http_transport_api_v1a2a_provider_id_http_path_options(
        self, provider_id: str, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        provider_id : str

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
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
            await client.a2a.proxy_http_transport_api_v1a2a_provider_id_http_path_options(
                provider_id="provider_id",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.proxy_http_transport_api_v1a2a_provider_id_http_path_options(
            provider_id, path, request_options=request_options
        )
        return _response.headers

    async def proxy_http_transport_api_v1a2a_provider_id_http_options(
        self,
        provider_id: str,
        *,
        path: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        provider_id : str

        path : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
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
            await client.a2a.proxy_http_transport_api_v1a2a_provider_id_http_options(
                provider_id="provider_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.proxy_http_transport_api_v1a2a_provider_id_http_options(
            provider_id, path=path, request_options=request_options
        )
        return _response.headers
