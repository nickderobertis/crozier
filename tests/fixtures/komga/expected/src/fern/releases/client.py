

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.release_dto import ReleaseDto
from .raw_client import AsyncRawReleasesClient, RawReleasesClient


class ReleasesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReleasesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReleasesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReleasesClient
        """
        return self._raw_client

    def get_releases(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[ReleaseDto]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReleaseDto]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.releases.get_releases()
        """
        _response = self._raw_client.get_releases(request_options=request_options)
        return _response.data


class AsyncReleasesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReleasesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReleasesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReleasesClient
        """
        return self._raw_client

    async def get_releases(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[ReleaseDto]:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReleaseDto]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.releases.get_releases()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_releases(request_options=request_options)
        return _response.data
