

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.media import Media
from .raw_client import AsyncRawMediaClient, RawMediaClient


OMIT = typing.cast(typing.Any, ...)


class MediaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMediaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMediaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMediaClient
        """
        return self._raw_client

    def submit_a_new_media_file(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Media:
        """
        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Media
            Media created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.media.submit_a_new_media_file(
            request="string",
        )
        """
        _response = self._raw_client.submit_a_new_media_file(request=request, request_options=request_options)
        return _response.data


class AsyncMediaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMediaClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMediaClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMediaClient
        """
        return self._raw_client

    async def submit_a_new_media_file(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Media:
        """
        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Media
            Media created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.media.submit_a_new_media_file(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_a_new_media_file(request=request, request_options=request_options)
        return _response.data
