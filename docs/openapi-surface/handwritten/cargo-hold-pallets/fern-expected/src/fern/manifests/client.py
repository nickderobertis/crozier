

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawManifestsClient, RawManifestsClient


class ManifestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawManifestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawManifestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawManifestsClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Manifest ids.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.manifests.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data


class AsyncManifestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawManifestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawManifestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawManifestsClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Manifest ids.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.manifests.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data
