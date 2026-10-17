

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawGalleryLightingClient, RawGalleryLightingClient


class GalleryLightingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGalleryLightingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGalleryLightingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGalleryLightingClient
        """
        return self._raw_client

    def lighting_plan_show(self, gallery: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        gallery : str

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
        client.gallery_lighting.lighting_plan_show(
            gallery="gallery",
        )
        """
        _response = self._raw_client.lighting_plan_show(gallery, request_options=request_options)
        return _response.data


class AsyncGalleryLightingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGalleryLightingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGalleryLightingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGalleryLightingClient
        """
        return self._raw_client

    async def lighting_plan_show(
        self, gallery: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        gallery : str

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
            await client.gallery_lighting.lighting_plan_show(
                gallery="gallery",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lighting_plan_show(gallery, request_options=request_options)
        return _response.data
