

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawVersionsClient, RawVersionsClient
from .types.list_versions_request_channel import ListVersionsRequestChannel


class VersionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVersionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVersionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVersionsClient
        """
        return self._raw_client

    def list_versions(
        self,
        *,
        channel: typing.Optional[ListVersionsRequestChannel] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        channel : typing.Optional[ListVersionsRequestChannel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The versions.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.versions.list_versions()
        """
        _response = self._raw_client.list_versions(channel=channel, request_options=request_options)
        return _response.data


class AsyncVersionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVersionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVersionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVersionsClient
        """
        return self._raw_client

    async def list_versions(
        self,
        *,
        channel: typing.Optional[ListVersionsRequestChannel] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        channel : typing.Optional[ListVersionsRequestChannel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The versions.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.versions.list_versions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_versions(channel=channel, request_options=request_options)
        return _response.data
