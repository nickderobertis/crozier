

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawXsltResourceClient, RawXsltResourceClient


class XsltResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawXsltResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawXsltResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawXsltResourceClient
        """
        return self._raw_client

    def post_kbv_transform(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
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
            base_url="https://yourhost.com/path/to/api",
        )
        client.xslt_resource.post_kbv_transform()
        """
        _response = self._raw_client.post_kbv_transform(request_options=request_options)
        return _response.data


class AsyncXsltResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawXsltResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawXsltResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawXsltResourceClient
        """
        return self._raw_client

    async def post_kbv_transform(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.xslt_resource.post_kbv_transform()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_kbv_transform(request_options=request_options)
        return _response.data
