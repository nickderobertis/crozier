

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSiteClient, RawSiteClient
from .types.get_site_response import GetSiteResponse


class SiteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSiteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSiteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSiteClient
        """
        return self._raw_client

    def get_site(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetSiteResponse:
        """
        Can be used to fetch all categories and subcategories

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSiteResponse
            success response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.site.get_site()
        """
        _response = self._raw_client.get_site(request_options=request_options)
        return _response.data


class AsyncSiteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSiteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSiteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSiteClient
        """
        return self._raw_client

    async def get_site(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetSiteResponse:
        """
        Can be used to fetch all categories and subcategories

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSiteResponse
            success response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.site.get_site()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_site(request_options=request_options)
        return _response.data
