

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawImagesClient, RawImagesClient


class ImagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImagesClient
        """
        return self._raw_client

    def resolve_image_using_get(self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        image_id : str
            The id of the image to be resolved.

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
            api_key="YOUR_API_KEY",
        )
        client.images.resolve_image_using_get(
            image_id="imageID",
        )
        """
        _response = self._raw_client.resolve_image_using_get(image_id, request_options=request_options)
        return _response.data


class AsyncImagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImagesClient
        """
        return self._raw_client

    async def resolve_image_using_get(
        self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        image_id : str
            The id of the image to be resolved.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.images.resolve_image_using_get(
                image_id="imageID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resolve_image_using_get(image_id, request_options=request_options)
        return _response.data
