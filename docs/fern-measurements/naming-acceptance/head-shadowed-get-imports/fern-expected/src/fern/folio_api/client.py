

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.page import Page
from .raw_client import AsyncRawFolioApiClient, RawFolioApiClient


class FolioApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFolioApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFolioApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFolioApiClient
        """
        return self._raw_client

    def get_site(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            The site's headers.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.folio_api.get_site()
        """
        _response = self._raw_client.get_site(request_options=request_options)
        return _response.headers

    def list_pages(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Page]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Page]
            The pages.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.folio_api.list_pages()
        """
        _response = self._raw_client.list_pages(request_options=request_options)
        return _response.data


class AsyncFolioApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFolioApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFolioApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFolioApiClient
        """
        return self._raw_client

    async def get_site(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            The site's headers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.folio_api.get_site()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_site(request_options=request_options)
        return _response.headers

    async def list_pages(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Page]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Page]
            The pages.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.folio_api.list_pages()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_pages(request_options=request_options)
        return _response.data
