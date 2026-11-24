

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAgentHostClient, RawAgentHostClient


class AgentHostClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAgentHostClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAgentHostClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAgentHostClient
        """
        return self._raw_client

    def pairing_create(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = FernApi()
        client.agent_host.pairing_create()
        """
        _response = self._raw_client.pairing_create(request_options=request_options)
        return _response.data

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The hosts.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.agent_host.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def harnesses_list(
        self, host_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        host_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The harnesses.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.agent_host.harnesses_list(
            host_id="host_id",
        )
        """
        _response = self._raw_client.harnesses_list(host_id, request_options=request_options)
        return _response.data


class AsyncAgentHostClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAgentHostClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAgentHostClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAgentHostClient
        """
        return self._raw_client

    async def pairing_create(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = AsyncFernApi()


        async def main() -> None:
            await client.agent_host.pairing_create()


        asyncio.run(main())
        """
        _response = await self._raw_client.pairing_create(request_options=request_options)
        return _response.data

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The hosts.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.agent_host.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def harnesses_list(
        self, host_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        host_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The harnesses.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.agent_host.harnesses_list(
                host_id="host_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.harnesses_list(host_id, request_options=request_options)
        return _response.data
