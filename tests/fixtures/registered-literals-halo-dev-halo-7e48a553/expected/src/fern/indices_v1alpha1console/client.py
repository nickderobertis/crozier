

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIndicesV1Alpha1ConsoleClient, RawIndicesV1Alpha1ConsoleClient


class IndicesV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIndicesV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIndicesV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIndicesV1Alpha1ConsoleClient
        """
        return self._raw_client

    def rebuild_all_indices(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Submit a request to rebuild all search indices.

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.indices_v1alpha1console.rebuild_all_indices()
        """
        _response = self._raw_client.rebuild_all_indices(request_options=request_options)
        return _response.data


class AsyncIndicesV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIndicesV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIndicesV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIndicesV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def rebuild_all_indices(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Submit a request to rebuild all search indices.

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.indices_v1alpha1console.rebuild_all_indices()


        asyncio.run(main())
        """
        _response = await self._raw_client.rebuild_all_indices(request_options=request_options)
        return _response.data
