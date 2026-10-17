

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.plaque import Plaque
from .raw_client import AsyncRawGalleryplaqueClient, RawGalleryplaqueClient


class GalleryplaqueClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGalleryplaqueClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGalleryplaqueClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGalleryplaqueClient
        """
        return self._raw_client

    def show(self, gallery: str, *, request_options: typing.Optional[RequestOptions] = None) -> Plaque:
        """
        Parameters
        ----------
        gallery : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plaque
            The gallery's plaque.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.galleryplaque.show(
            gallery="gallery",
        )
        """
        _response = self._raw_client.show(gallery, request_options=request_options)
        return _response.data

    def destroy(self, gallery: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.galleryplaque.destroy(
            gallery="gallery",
        )
        """
        _response = self._raw_client.destroy(gallery, request_options=request_options)
        return _response.data


class AsyncGalleryplaqueClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGalleryplaqueClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGalleryplaqueClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGalleryplaqueClient
        """
        return self._raw_client

    async def show(self, gallery: str, *, request_options: typing.Optional[RequestOptions] = None) -> Plaque:
        """
        Parameters
        ----------
        gallery : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Plaque
            The gallery's plaque.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.galleryplaque.show(
                gallery="gallery",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show(gallery, request_options=request_options)
        return _response.data

    async def destroy(self, gallery: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.galleryplaque.destroy(
                gallery="gallery",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.destroy(gallery, request_options=request_options)
        return _response.data
