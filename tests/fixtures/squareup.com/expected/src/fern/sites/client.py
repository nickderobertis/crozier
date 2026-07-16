

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_sites_response import ListSitesResponse
from .raw_client import AsyncRawSitesClient, RawSitesClient


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

    def list_sites(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListSitesResponse:
        """
        Lists the Square Online sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSitesResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.sites.list_sites()
        """
        _response = self._raw_client.list_sites(request_options=request_options)
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

    async def list_sites(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListSitesResponse:
        """
        Lists the Square Online sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSitesResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.list_sites()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sites(request_options=request_options)
        return _response.data
