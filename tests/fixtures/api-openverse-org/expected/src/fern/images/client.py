

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.image import Image
from ..types.paginated_image_results import PaginatedImageResults
from ..types.report_request_reason import ReportRequestReason
from ..types.source_stats import SourceStats
from .raw_client import AsyncRawImagesClient, RawImagesClient
from .types.get_image_oembed_response import GetImageOembedResponse
from .types.search_images_request_aspect_ratio import SearchImagesRequestAspectRatio
from .types.search_images_request_category import SearchImagesRequestCategory
from .types.search_images_request_size import SearchImagesRequestSize


OMIT = typing.cast(typing.Any, ...)


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

    def search_images(
        self,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        license: typing.Optional[str] = None,
        license_type: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        excluded_source: typing.Optional[str] = None,
        creator: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        mature: typing.Optional[bool] = None,
        filter_dead: typing.Optional[bool] = None,
        aspect_ratio: typing.Optional[SearchImagesRequestAspectRatio] = None,
        size: typing.Optional[SearchImagesRequestSize] = None,
        category: typing.Optional[SearchImagesRequestCategory] = None,
        extension: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedImageResults:
        """
        Search for openly-licensed images with extensive filtering options.

        Parameters
        ----------
        q : typing.Optional[str]
            Full-text search query (max 200 characters)

        page : typing.Optional[int]
            Page number for pagination

        page_size : typing.Optional[int]
            Number of results per page

        license : typing.Optional[str]
            Filter by license type (comma-separated)

        license_type : typing.Optional[str]
            Filter by license category (commercial, modification)

        source : typing.Optional[str]
            Filter by content source

        excluded_source : typing.Optional[str]
            Exclude content from specific sources

        creator : typing.Optional[str]
            Filter by creator name

        tags : typing.Optional[str]
            Filter by tags

        title : typing.Optional[str]
            Filter by title

        mature : typing.Optional[bool]
            Include mature/sensitive content

        filter_dead : typing.Optional[bool]
            Filter out dead/broken links

        aspect_ratio : typing.Optional[SearchImagesRequestAspectRatio]
            Filter by aspect ratio

        size : typing.Optional[SearchImagesRequestSize]
            Filter by image size

        category : typing.Optional[SearchImagesRequestCategory]
            Filter by image category

        extension : typing.Optional[str]
            Filter by file extension

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedImageResults
            Successful image search results

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.images.search_images()
        """
        _response = self._raw_client.search_images(
            q=q,
            page=page,
            page_size=page_size,
            license=license,
            license_type=license_type,
            source=source,
            excluded_source=excluded_source,
            creator=creator,
            tags=tags,
            title=title,
            mature=mature,
            filter_dead=filter_dead,
            aspect_ratio=aspect_ratio,
            size=size,
            category=category,
            extension=extension,
            request_options=request_options,
        )
        return _response.data

    def get_image(self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None) -> Image:
        """
        Retrieve detailed information about a specific image by its UUID.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Image
            Image details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.images.get_image(
            identifier="identifier",
        )
        """
        _response = self._raw_client.get_image(identifier, request_options=request_options)
        return _response.data

    def get_related_images(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaginatedImageResults:
        """
        Find images related to a specified image.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedImageResults
            Related images

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.images.get_related_images(
            identifier="identifier",
        )
        """
        _response = self._raw_client.get_related_images(identifier, request_options=request_options)
        return _response.data

    def report_image(
        self,
        identifier: str,
        *,
        reason: ReportRequestReason,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Report an image for issues such as DMCA violations, mature content, or other concerns.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        reason : ReportRequestReason
            Reason for the report

        description : typing.Optional[str]
            Additional details about the report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, ReportRequestReason

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.images.report_image(
            identifier="identifier",
            reason=ReportRequestReason.MATURE,
        )
        """
        _response = self._raw_client.report_image(
            identifier, reason=reason, description=description, request_options=request_options
        )
        return _response.data

    def get_image_thumbnail(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Retrieve a thumbnail proxy for the specified image.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Thumbnail image

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.images.get_image_thumbnail(
            identifier="identifier",
        )
        """
        with self._raw_client.get_image_thumbnail(identifier, request_options=request_options) as r:
            yield from r.data

    def get_image_oembed(
        self, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetImageOembedResponse:
        """
        Retrieve oEmbed structured data for embedding an image.

        Parameters
        ----------
        url : str
            The URL of the image to retrieve oEmbed data for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetImageOembedResponse
            oEmbed response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.images.get_image_oembed(
            url="url",
        )
        """
        _response = self._raw_client.get_image_oembed(url=url, request_options=request_options)
        return _response.data

    def get_image_stats(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[SourceStats]:
        """
        List all content sources for images and their media counts.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SourceStats]
            Image source statistics

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.images.get_image_stats()
        """
        _response = self._raw_client.get_image_stats(request_options=request_options)
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

    async def search_images(
        self,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        license: typing.Optional[str] = None,
        license_type: typing.Optional[str] = None,
        source: typing.Optional[str] = None,
        excluded_source: typing.Optional[str] = None,
        creator: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        mature: typing.Optional[bool] = None,
        filter_dead: typing.Optional[bool] = None,
        aspect_ratio: typing.Optional[SearchImagesRequestAspectRatio] = None,
        size: typing.Optional[SearchImagesRequestSize] = None,
        category: typing.Optional[SearchImagesRequestCategory] = None,
        extension: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedImageResults:
        """
        Search for openly-licensed images with extensive filtering options.

        Parameters
        ----------
        q : typing.Optional[str]
            Full-text search query (max 200 characters)

        page : typing.Optional[int]
            Page number for pagination

        page_size : typing.Optional[int]
            Number of results per page

        license : typing.Optional[str]
            Filter by license type (comma-separated)

        license_type : typing.Optional[str]
            Filter by license category (commercial, modification)

        source : typing.Optional[str]
            Filter by content source

        excluded_source : typing.Optional[str]
            Exclude content from specific sources

        creator : typing.Optional[str]
            Filter by creator name

        tags : typing.Optional[str]
            Filter by tags

        title : typing.Optional[str]
            Filter by title

        mature : typing.Optional[bool]
            Include mature/sensitive content

        filter_dead : typing.Optional[bool]
            Filter out dead/broken links

        aspect_ratio : typing.Optional[SearchImagesRequestAspectRatio]
            Filter by aspect ratio

        size : typing.Optional[SearchImagesRequestSize]
            Filter by image size

        category : typing.Optional[SearchImagesRequestCategory]
            Filter by image category

        extension : typing.Optional[str]
            Filter by file extension

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedImageResults
            Successful image search results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.images.search_images()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_images(
            q=q,
            page=page,
            page_size=page_size,
            license=license,
            license_type=license_type,
            source=source,
            excluded_source=excluded_source,
            creator=creator,
            tags=tags,
            title=title,
            mature=mature,
            filter_dead=filter_dead,
            aspect_ratio=aspect_ratio,
            size=size,
            category=category,
            extension=extension,
            request_options=request_options,
        )
        return _response.data

    async def get_image(self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None) -> Image:
        """
        Retrieve detailed information about a specific image by its UUID.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Image
            Image details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.images.get_image(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image(identifier, request_options=request_options)
        return _response.data

    async def get_related_images(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaginatedImageResults:
        """
        Find images related to a specified image.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedImageResults
            Related images

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.images.get_related_images(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_related_images(identifier, request_options=request_options)
        return _response.data

    async def report_image(
        self,
        identifier: str,
        *,
        reason: ReportRequestReason,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Report an image for issues such as DMCA violations, mature content, or other concerns.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        reason : ReportRequestReason
            Reason for the report

        description : typing.Optional[str]
            Additional details about the report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ReportRequestReason

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.images.report_image(
                identifier="identifier",
                reason=ReportRequestReason.MATURE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.report_image(
            identifier, reason=reason, description=description, request_options=request_options
        )
        return _response.data

    async def get_image_thumbnail(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Retrieve a thumbnail proxy for the specified image.

        Parameters
        ----------
        identifier : str
            Unique media identifier (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Thumbnail image

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.images.get_image_thumbnail(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_image_thumbnail(identifier, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_image_oembed(
        self, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetImageOembedResponse:
        """
        Retrieve oEmbed structured data for embedding an image.

        Parameters
        ----------
        url : str
            The URL of the image to retrieve oEmbed data for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetImageOembedResponse
            oEmbed response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.images.get_image_oembed(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_oembed(url=url, request_options=request_options)
        return _response.data

    async def get_image_stats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SourceStats]:
        """
        List all content sources for images and their media counts.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SourceStats]
            Image source statistics

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.images.get_image_stats()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_stats(request_options=request_options)
        return _response.data
