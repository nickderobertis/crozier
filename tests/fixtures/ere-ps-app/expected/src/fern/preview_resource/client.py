

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPreviewResourceClient, RawPreviewResourceClient


class PreviewResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPreviewResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPreviewResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPreviewResourceClient
        """
        return self._raw_client

    def post_preview_generate(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.preview_resource.post_preview_generate()
        """
        _response = self._raw_client.post_preview_generate(request_options=request_options)
        return _response.data


class AsyncPreviewResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPreviewResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPreviewResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPreviewResourceClient
        """
        return self._raw_client

    async def post_preview_generate(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.preview_resource.post_preview_generate()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_preview_generate(request_options=request_options)
        return _response.data
