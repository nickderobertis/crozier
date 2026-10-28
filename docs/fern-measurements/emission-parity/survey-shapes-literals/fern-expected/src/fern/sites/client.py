

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.site import Site
from .raw_client import AsyncRawSitesClient, RawSitesClient
from .types.site_search_within import SiteSearchWithin


OMIT = typing.cast(typing.Any, ...)


class SitesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSitesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSitesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSitesClient
        """
        return self._raw_client

    def list_sites(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Site]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Site]
            Every surveyed site.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.sites.list_sites()
        """
        _response = self._raw_client.list_sites(request_options=request_options)
        return _response.data

    def search_sites(
        self,
        *,
        within: typing.Optional[SiteSearchWithin] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Site]:
        """
        Parameters
        ----------
        within : typing.Optional[SiteSearchWithin]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Site]
            The sites inside the outline.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.sites.search_sites()
        """
        _response = self._raw_client.search_sites(within=within, request_options=request_options)
        return _response.data


class AsyncSitesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSitesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSitesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSitesClient
        """
        return self._raw_client

    async def list_sites(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Site]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Site]
            Every surveyed site.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.sites.list_sites()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sites(request_options=request_options)
        return _response.data

    async def search_sites(
        self,
        *,
        within: typing.Optional[SiteSearchWithin] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Site]:
        """
        Parameters
        ----------
        within : typing.Optional[SiteSearchWithin]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Site]
            The sites inside the outline.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.sites.search_sites()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_sites(within=within, request_options=request_options)
        return _response.data
