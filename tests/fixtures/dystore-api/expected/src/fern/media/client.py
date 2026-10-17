

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMediaClient, RawMediaClient


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

    def get_image(
        self, *, media_conversions: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get image

        Parameters
        ----------
        media_conversions : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.media.get_image(
            media_conversions="webp,large",
        )
        """
        _response = self._raw_client.get_image(media_conversions=media_conversions, request_options=request_options)
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

    async def get_image(
        self, *, media_conversions: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get image

        Parameters
        ----------
        media_conversions : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.media.get_image(
                media_conversions="webp,large",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image(
            media_conversions=media_conversions, request_options=request_options
        )
        return _response.data
