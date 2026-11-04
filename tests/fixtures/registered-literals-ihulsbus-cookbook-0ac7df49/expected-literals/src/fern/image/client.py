

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paginated_image_response import PaginatedImageResponse
from .raw_client import AsyncRawImageClient, RawImageClient
from .types.create_image_request_entity_type import CreateImageRequestEntityType
from .types.image_data import ImageData


OMIT = typing.cast(typing.Any, ...)


class ImageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImageClient
        """
        return self._raw_client

    def get_all_images(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedImageResponse:
        """
        Returns images stored in the API in a paginated format

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (1-indexed)

        limit : typing.Optional[int]
            Number of items per page (max 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedImageResponse
            Returned on a succesful query

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.image.get_all_images()
        """
        _response = self._raw_client.get_all_images(page=page, limit=limit, request_options=request_options)
        return _response.data

    def get_image(self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ImageData:
        """
        Get information of an image based on the imageID

        Parameters
        ----------
        image_id : str
            ID of an image

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageData
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.image.get_image(
            image_id="ImageID",
        )
        """
        _response = self._raw_client.get_image(image_id, request_options=request_options)
        return _response.data

    def update_image(
        self,
        image_id: str,
        *,
        image: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageData:
        """
        Update an image. Image can either be JPEG or PNG. The dimensions must be between 300x300 and 1000x1000.
        Max file size is 5MB

        Parameters
        ----------
        image_id : str
            ID of an image

        image : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageData
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.image.update_image(
            image_id="ImageID",
        )
        """
        _response = self._raw_client.update_image(image_id, image=image, request_options=request_options)
        return _response.data

    def delete_images(self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes an image and it's associated file in the CDN

        Parameters
        ----------
        image_id : str
            ID of an image

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
        client.image.delete_images(
            image_id="ImageID",
        )
        """
        _response = self._raw_client.delete_images(image_id, request_options=request_options)
        return _response.data

    def create_image(
        self,
        entity_type: CreateImageRequestEntityType,
        entity_id: str,
        *,
        image: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageData:
        """
        Endpoint to create an image. Image can either be JPEG or PNG. The dimensions must be between 300x300 and 1000x1000.
        Max file size is 5MB

        Parameters
        ----------
        entity_type : CreateImageRequestEntityType
            Type of the entity queried

        entity_id : str
            UUID of a entity

        image : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageData
            Image created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.image.create_image(
            entity_type="recipe",
            entity_id="EntityID",
        )
        """
        _response = self._raw_client.create_image(entity_type, entity_id, image=image, request_options=request_options)
        return _response.data

    def search_image(
        self,
        *,
        entity_type: str,
        id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageData:
        """
        Search for images based on their associated EntityType and EntityID

        Parameters
        ----------
        entity_type : str
            Type of the entity queried. E.g.: recipe

        id : typing.Optional[str]
            UUID of the entity referencing in the search

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageData
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.image.search_image(
            entity_type="entityType",
        )
        """
        _response = self._raw_client.search_image(entity_type=entity_type, id=id, request_options=request_options)
        return _response.data


class AsyncImageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImageClient
        """
        return self._raw_client

    async def get_all_images(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedImageResponse:
        """
        Returns images stored in the API in a paginated format

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (1-indexed)

        limit : typing.Optional[int]
            Number of items per page (max 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedImageResponse
            Returned on a succesful query

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.image.get_all_images()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_images(page=page, limit=limit, request_options=request_options)
        return _response.data

    async def get_image(self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ImageData:
        """
        Get information of an image based on the imageID

        Parameters
        ----------
        image_id : str
            ID of an image

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageData
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.image.get_image(
                image_id="ImageID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image(image_id, request_options=request_options)
        return _response.data

    async def update_image(
        self,
        image_id: str,
        *,
        image: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageData:
        """
        Update an image. Image can either be JPEG or PNG. The dimensions must be between 300x300 and 1000x1000.
        Max file size is 5MB

        Parameters
        ----------
        image_id : str
            ID of an image

        image : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageData
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.image.update_image(
                image_id="ImageID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_image(image_id, image=image, request_options=request_options)
        return _response.data

    async def delete_images(self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes an image and it's associated file in the CDN

        Parameters
        ----------
        image_id : str
            ID of an image

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
            await client.image.delete_images(
                image_id="ImageID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_images(image_id, request_options=request_options)
        return _response.data

    async def create_image(
        self,
        entity_type: CreateImageRequestEntityType,
        entity_id: str,
        *,
        image: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageData:
        """
        Endpoint to create an image. Image can either be JPEG or PNG. The dimensions must be between 300x300 and 1000x1000.
        Max file size is 5MB

        Parameters
        ----------
        entity_type : CreateImageRequestEntityType
            Type of the entity queried

        entity_id : str
            UUID of a entity

        image : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageData
            Image created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.image.create_image(
                entity_type="recipe",
                entity_id="EntityID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_image(
            entity_type, entity_id, image=image, request_options=request_options
        )
        return _response.data

    async def search_image(
        self,
        *,
        entity_type: str,
        id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageData:
        """
        Search for images based on their associated EntityType and EntityID

        Parameters
        ----------
        entity_type : str
            Type of the entity queried. E.g.: recipe

        id : typing.Optional[str]
            UUID of the entity referencing in the search

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageData
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.image.search_image(
                entity_type="entityType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_image(entity_type=entity_type, id=id, request_options=request_options)
        return _response.data
