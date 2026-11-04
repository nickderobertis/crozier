

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAddonsClient, RawAddonsClient
from .types.addons_list_response_item import AddonsListResponseItem


class AddonsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAddonsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAddonsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAddonsClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[AddonsListResponseItem]:
        """

        A paginated list of addons configurable with the OSF, for read purposes only.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 addons. Each resource in the array is a separate addon object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AddonsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.addons.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data


class AsyncAddonsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAddonsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAddonsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAddonsClient
        """
        return self._raw_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AddonsListResponseItem]:
        """

        A paginated list of addons configurable with the OSF, for read purposes only.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 addons. Each resource in the array is a separate addon object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AddonsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.addons.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data
