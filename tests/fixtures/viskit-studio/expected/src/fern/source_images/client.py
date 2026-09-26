

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.source_image_import_out import SourceImageImportOut
from ..types.source_image_out import SourceImageOut
from .raw_client import AsyncRawSourceImagesClient, RawSourceImagesClient


OMIT = typing.cast(typing.Any, ...)


class SourceImagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSourceImagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSourceImagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSourceImagesClient
        """
        return self._raw_client

    def create_source_image(self, *, request_options: typing.Optional[RequestOptions] = None) -> SourceImageOut:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceImageOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.source_images.create_source_image()
        """
        _response = self._raw_client.create_source_image(request_options=request_options)
        return _response.data

    def create_source_image_from_existing(
        self, *, image_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceImageImportOut:
        """
        Parameters
        ----------
        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceImageImportOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.source_images.create_source_image_from_existing(
            image_id="image_id",
        )
        """
        _response = self._raw_client.create_source_image_from_existing(
            image_id=image_id, request_options=request_options
        )
        return _response.data

    def get_source_image(
        self, source_image_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        source_image_ref : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.source_images.get_source_image(
            source_image_ref="source_image_ref",
        )
        """
        _response = self._raw_client.get_source_image(source_image_ref, request_options=request_options)
        return _response.data


class AsyncSourceImagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSourceImagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSourceImagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSourceImagesClient
        """
        return self._raw_client

    async def create_source_image(self, *, request_options: typing.Optional[RequestOptions] = None) -> SourceImageOut:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceImageOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.source_images.create_source_image()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_source_image(request_options=request_options)
        return _response.data

    async def create_source_image_from_existing(
        self, *, image_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceImageImportOut:
        """
        Parameters
        ----------
        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceImageImportOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.source_images.create_source_image_from_existing(
                image_id="image_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_source_image_from_existing(
            image_id=image_id, request_options=request_options
        )
        return _response.data

    async def get_source_image(
        self, source_image_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        source_image_ref : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.source_images.get_source_image(
                source_image_ref="source_image_ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_source_image(source_image_ref, request_options=request_options)
        return _response.data
