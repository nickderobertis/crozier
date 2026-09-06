

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_global_resources_shared_models_global_image import (
    ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage,
)
from ..types.global_resources_shared_models_global_image import GlobalResourcesSharedModelsGlobalImage
from ..types.global_resources_shared_models_global_image_category import GlobalResourcesSharedModelsGlobalImageCategory
from ..types.global_resources_shared_models_global_image_state import GlobalResourcesSharedModelsGlobalImageState
from ..types.system_object import SystemObject
from .raw_client import AsyncRawGlobalimagesClient, RawGlobalimagesClient


OMIT = typing.cast(typing.Any, ...)


class GlobalimagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGlobalimagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGlobalimagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGlobalimagesClient
        """
        return self._raw_client

    def getglobalimages(
        self,
        *,
        search: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        publisher: typing.Optional[str] = None,
        include_deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage:
        """
        No Documentation Found.

        Parameters
        ----------
        search : typing.Optional[str]
            Optional. Searches for matching global images with the matching Category Name, Publisher or Description

        category_id : typing.Optional[str]


        publisher : typing.Optional[str]


        include_deleted : typing.Optional[bool]
            Indicates whether to include GlobalImages marked as removed.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.globalimages.getglobalimages()
        """
        _response = self._raw_client.getglobalimages(
            search=search,
            category_id=category_id,
            publisher=publisher,
            include_deleted=include_deleted,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def postglobalimage(
        self,
        *,
        crc: str,
        description: str,
        height: int,
        name: str,
        state: GlobalResourcesSharedModelsGlobalImageState,
        thumbnail_crc: str,
        width: int,
        override_publisher_or_date: typing.Optional[bool] = None,
        categories: typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]] = OMIT,
        date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[str] = OMIT,
        publisher: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        thumbnail_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        crc : str
            The Hash of the file (SHA256, HEX-encoded).

        description : str
            The description of the file.

        height : int
            The height of the file.

        name : str
            The name of the file when downloaded.

        state : GlobalResourcesSharedModelsGlobalImageState
            Indicates the state of this file. Must be 'Created' when created. Read Only.

        thumbnail_crc : str
            The Hash of the thumbnail file (SHA256, HEX-encoded).

        width : int
            The width of the file.

        override_publisher_or_date : typing.Optional[bool]
            Whether to set the publisher and date to the provided values.

        categories : typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]]
            The category of the file.

        date : typing.Optional[dt.datetime]
            The date of the file.

        id : typing.Optional[str]
            The Id of the GlobalImage Metadata.

        publisher : typing.Optional[str]
            The Publisher of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        thumbnail_size : typing.Optional[int]
            The size of the thumbnail file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi, GlobalResourcesSharedModelsGlobalImageState

        client = FernApi()
        client.globalimages.postglobalimage(
            crc="CRC",
            description="Description",
            height=1,
            name="Name",
            state=GlobalResourcesSharedModelsGlobalImageState.CREATED,
            thumbnail_crc="ThumbnailCRC",
            width=1,
        )
        """
        _response = self._raw_client.postglobalimage(
            crc=crc,
            description=description,
            height=height,
            name=name,
            state=state,
            thumbnail_crc=thumbnail_crc,
            width=width,
            override_publisher_or_date=override_publisher_or_date,
            categories=categories,
            date=date,
            id=id,
            publisher=publisher,
            size=size,
            thumbnail_size=thumbnail_size,
            request_options=request_options,
        )
        return _response.data

    def getglobalimage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalResourcesSharedModelsGlobalImage:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The GlobalImage's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsGlobalImage
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.globalimages.getglobalimage(
            id="ID",
        )
        """
        _response = self._raw_client.getglobalimage(id, request_options=request_options)
        return _response.data

    def putglobalimage(
        self,
        id_: str,
        *,
        crc: str,
        description: str,
        height: int,
        name: str,
        state: GlobalResourcesSharedModelsGlobalImageState,
        thumbnail_crc: str,
        width: int,
        override_publisher_or_date: typing.Optional[bool] = None,
        categories: typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]] = OMIT,
        date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[str] = OMIT,
        publisher: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        thumbnail_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the metadata for an image. Size may not be modified by the client.
                        Set status to 'Available' to publish an image. Both the image and thumbnail must be uploaded.
                        Set status to 'Created' to reset an image's contents and re-upload.
                        A file may only be 'Removed' by the DELETE method.

        Parameters
        ----------
        id_ : str
            The GlobalImage's id.

        crc : str
            The Hash of the file (SHA256, HEX-encoded).

        description : str
            The description of the file.

        height : int
            The height of the file.

        name : str
            The name of the file when downloaded.

        state : GlobalResourcesSharedModelsGlobalImageState
            Indicates the state of this file. Must be 'Created' when created. Read Only.

        thumbnail_crc : str
            The Hash of the thumbnail file (SHA256, HEX-encoded).

        width : int
            The width of the file.

        override_publisher_or_date : typing.Optional[bool]
            Whether to set the publisher and date to the provided values.

        categories : typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]]
            The category of the file.

        date : typing.Optional[dt.datetime]
            The date of the file.

        id : typing.Optional[str]
            The Id of the GlobalImage Metadata.

        publisher : typing.Optional[str]
            The Publisher of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        thumbnail_size : typing.Optional[int]
            The size of the thumbnail file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, GlobalResourcesSharedModelsGlobalImageState

        client = FernApi()
        client.globalimages.putglobalimage(
            id_="ID",
            crc="CRC",
            description="Description",
            height=1,
            name="Name",
            state=GlobalResourcesSharedModelsGlobalImageState.CREATED,
            thumbnail_crc="ThumbnailCRC",
            width=1,
        )
        """
        _response = self._raw_client.putglobalimage(
            id_,
            crc=crc,
            description=description,
            height=height,
            name=name,
            state=state,
            thumbnail_crc=thumbnail_crc,
            width=width,
            override_publisher_or_date=override_publisher_or_date,
            categories=categories,
            date=date,
            id=id,
            publisher=publisher,
            size=size,
            thumbnail_size=thumbnail_size,
            request_options=request_options,
        )
        return _response.data

    def deletefile(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The GlobalImage's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.globalimages.deletefile(
            id="ID",
        )
        """
        _response = self._raw_client.deletefile(id, request_options=request_options)
        return _response.data

    def getglobalimagecontents(
        self,
        id: str,
        *,
        is_full_image: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SystemObject:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The global image metadata id.

        is_full_image : typing.Optional[bool]
            Indicated whether to download the full image or the thumbnail. Defaults to 'true'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.globalimages.getglobalimagecontents(
            id="ID",
        )
        """
        _response = self._raw_client.getglobalimagecontents(
            id, is_full_image=is_full_image, request_options=request_options
        )
        return _response.data

    def putglobalimagecontents(
        self,
        id: str,
        *,
        is_full_image: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SystemObject:
        """
        Both the image and thumbnail must be uploaded.
                        Set isFullImage = 'True' for Full Image, isFullImage = 'False' for Thumbnail

        Parameters
        ----------
        id : str
            The global image metadata id.

        is_full_image : typing.Optional[bool]
            Indicated whether this is the full image or the thumbnail. Defaults to 'true'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.globalimages.putglobalimagecontents(
            id="ID",
        )
        """
        _response = self._raw_client.putglobalimagecontents(
            id, is_full_image=is_full_image, request_options=request_options
        )
        return _response.data


class AsyncGlobalimagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGlobalimagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGlobalimagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGlobalimagesClient
        """
        return self._raw_client

    async def getglobalimages(
        self,
        *,
        search: typing.Optional[str] = None,
        category_id: typing.Optional[str] = None,
        publisher: typing.Optional[str] = None,
        include_deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage:
        """
        No Documentation Found.

        Parameters
        ----------
        search : typing.Optional[str]
            Optional. Searches for matching global images with the matching Category Name, Publisher or Description

        category_id : typing.Optional[str]


        publisher : typing.Optional[str]


        include_deleted : typing.Optional[bool]
            Indicates whether to include GlobalImages marked as removed.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsGlobalImage
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.globalimages.getglobalimages()


        asyncio.run(main())
        """
        _response = await self._raw_client.getglobalimages(
            search=search,
            category_id=category_id,
            publisher=publisher,
            include_deleted=include_deleted,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def postglobalimage(
        self,
        *,
        crc: str,
        description: str,
        height: int,
        name: str,
        state: GlobalResourcesSharedModelsGlobalImageState,
        thumbnail_crc: str,
        width: int,
        override_publisher_or_date: typing.Optional[bool] = None,
        categories: typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]] = OMIT,
        date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[str] = OMIT,
        publisher: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        thumbnail_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        crc : str
            The Hash of the file (SHA256, HEX-encoded).

        description : str
            The description of the file.

        height : int
            The height of the file.

        name : str
            The name of the file when downloaded.

        state : GlobalResourcesSharedModelsGlobalImageState
            Indicates the state of this file. Must be 'Created' when created. Read Only.

        thumbnail_crc : str
            The Hash of the thumbnail file (SHA256, HEX-encoded).

        width : int
            The width of the file.

        override_publisher_or_date : typing.Optional[bool]
            Whether to set the publisher and date to the provided values.

        categories : typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]]
            The category of the file.

        date : typing.Optional[dt.datetime]
            The date of the file.

        id : typing.Optional[str]
            The Id of the GlobalImage Metadata.

        publisher : typing.Optional[str]
            The Publisher of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        thumbnail_size : typing.Optional[int]
            The size of the thumbnail file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GlobalResourcesSharedModelsGlobalImageState

        client = AsyncFernApi()


        async def main() -> None:
            await client.globalimages.postglobalimage(
                crc="CRC",
                description="Description",
                height=1,
                name="Name",
                state=GlobalResourcesSharedModelsGlobalImageState.CREATED,
                thumbnail_crc="ThumbnailCRC",
                width=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postglobalimage(
            crc=crc,
            description=description,
            height=height,
            name=name,
            state=state,
            thumbnail_crc=thumbnail_crc,
            width=width,
            override_publisher_or_date=override_publisher_or_date,
            categories=categories,
            date=date,
            id=id,
            publisher=publisher,
            size=size,
            thumbnail_size=thumbnail_size,
            request_options=request_options,
        )
        return _response.data

    async def getglobalimage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalResourcesSharedModelsGlobalImage:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The GlobalImage's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsGlobalImage
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.globalimages.getglobalimage(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getglobalimage(id, request_options=request_options)
        return _response.data

    async def putglobalimage(
        self,
        id_: str,
        *,
        crc: str,
        description: str,
        height: int,
        name: str,
        state: GlobalResourcesSharedModelsGlobalImageState,
        thumbnail_crc: str,
        width: int,
        override_publisher_or_date: typing.Optional[bool] = None,
        categories: typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]] = OMIT,
        date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[str] = OMIT,
        publisher: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        thumbnail_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the metadata for an image. Size may not be modified by the client.
                        Set status to 'Available' to publish an image. Both the image and thumbnail must be uploaded.
                        Set status to 'Created' to reset an image's contents and re-upload.
                        A file may only be 'Removed' by the DELETE method.

        Parameters
        ----------
        id_ : str
            The GlobalImage's id.

        crc : str
            The Hash of the file (SHA256, HEX-encoded).

        description : str
            The description of the file.

        height : int
            The height of the file.

        name : str
            The name of the file when downloaded.

        state : GlobalResourcesSharedModelsGlobalImageState
            Indicates the state of this file. Must be 'Created' when created. Read Only.

        thumbnail_crc : str
            The Hash of the thumbnail file (SHA256, HEX-encoded).

        width : int
            The width of the file.

        override_publisher_or_date : typing.Optional[bool]
            Whether to set the publisher and date to the provided values.

        categories : typing.Optional[typing.Sequence[GlobalResourcesSharedModelsGlobalImageCategory]]
            The category of the file.

        date : typing.Optional[dt.datetime]
            The date of the file.

        id : typing.Optional[str]
            The Id of the GlobalImage Metadata.

        publisher : typing.Optional[str]
            The Publisher of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        thumbnail_size : typing.Optional[int]
            The size of the thumbnail file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GlobalResourcesSharedModelsGlobalImageState

        client = AsyncFernApi()


        async def main() -> None:
            await client.globalimages.putglobalimage(
                id_="ID",
                crc="CRC",
                description="Description",
                height=1,
                name="Name",
                state=GlobalResourcesSharedModelsGlobalImageState.CREATED,
                thumbnail_crc="ThumbnailCRC",
                width=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putglobalimage(
            id_,
            crc=crc,
            description=description,
            height=height,
            name=name,
            state=state,
            thumbnail_crc=thumbnail_crc,
            width=width,
            override_publisher_or_date=override_publisher_or_date,
            categories=categories,
            date=date,
            id=id,
            publisher=publisher,
            size=size,
            thumbnail_size=thumbnail_size,
            request_options=request_options,
        )
        return _response.data

    async def deletefile(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The GlobalImage's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.globalimages.deletefile(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletefile(id, request_options=request_options)
        return _response.data

    async def getglobalimagecontents(
        self,
        id: str,
        *,
        is_full_image: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SystemObject:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The global image metadata id.

        is_full_image : typing.Optional[bool]
            Indicated whether to download the full image or the thumbnail. Defaults to 'true'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.globalimages.getglobalimagecontents(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getglobalimagecontents(
            id, is_full_image=is_full_image, request_options=request_options
        )
        return _response.data

    async def putglobalimagecontents(
        self,
        id: str,
        *,
        is_full_image: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SystemObject:
        """
        Both the image and thumbnail must be uploaded.
                        Set isFullImage = 'True' for Full Image, isFullImage = 'False' for Thumbnail

        Parameters
        ----------
        id : str
            The global image metadata id.

        is_full_image : typing.Optional[bool]
            Indicated whether this is the full image or the thumbnail. Defaults to 'true'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.globalimages.putglobalimagecontents(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putglobalimagecontents(
            id, is_full_image=is_full_image, request_options=request_options
        )
        return _response.data
