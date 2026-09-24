

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.version import Version
from .raw_client import AsyncRawVersionClient, RawVersionClient


class VersionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVersionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVersionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVersionClient
        """
        return self._raw_client

    def get_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> Version:
        """
        Get application version information

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Version
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.version.get_version()
        """
        _response = self._raw_client.get_version(request_options=request_options)
        return _response.data


class AsyncVersionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVersionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVersionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVersionClient
        """
        return self._raw_client

    async def get_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> Version:
        """
        Get application version information

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Version
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.version.get_version()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_version(request_options=request_options)
        return _response.data
