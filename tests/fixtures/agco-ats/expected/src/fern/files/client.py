

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_global_resources_shared_models_file_download import (
    ApiIPagedResponseGlobalResourcesSharedModelsFileDownload,
)
from ..types.global_resources_shared_models_file_download import GlobalResourcesSharedModelsFileDownload
from ..types.global_resources_shared_models_file_download_state import GlobalResourcesSharedModelsFileDownloadState
from ..types.system_object import SystemObject
from .raw_client import AsyncRawFilesClient, RawFilesClient


OMIT = typing.cast(typing.Any, ...)


class FilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFilesClient
        """
        return self._raw_client

    def getfiles(
        self,
        *,
        include_deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsFileDownload:
        """
        No Documentation Found.

        Parameters
        ----------
        include_deleted : typing.Optional[bool]
            Indicates whether to include files marked as removed.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsFileDownload
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.files.getfiles()
        """
        _response = self._raw_client.getfiles(
            include_deleted=include_deleted, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def postfile(
        self,
        *,
        crc: str,
        content_type: str,
        description: str,
        is_public: bool,
        name: str,
        path: str,
        state: GlobalResourcesSharedModelsFileDownloadState,
        id: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        crc : str
            The crc of the file (SHA256, HEX-encoded). Must be provided when creating a file.

        content_type : str
            The type of file; sent as the content-type header.

        description : str
            The description of the file.

        is_public : bool
            Indicates whether this file is available to the public for download.

        name : str
            The name of the file when downloaded.

        path : str
            The Path of the file.

        state : GlobalResourcesSharedModelsFileDownloadState
            Indicates the state of this file. Must be 'Created' when created.

        id : typing.Optional[str]
            The Id of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi, GlobalResourcesSharedModelsFileDownloadState

        client = FernApi()
        client.files.postfile(
            crc="CRC",
            content_type="ContentType",
            description="Description",
            is_public=True,
            name="Name",
            path="Path",
            state=GlobalResourcesSharedModelsFileDownloadState.CREATED,
        )
        """
        _response = self._raw_client.postfile(
            crc=crc,
            content_type=content_type,
            description=description,
            is_public=is_public,
            name=name,
            path=path,
            state=state,
            id=id,
            size=size,
            request_options=request_options,
        )
        return _response.data

    def getfile(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalResourcesSharedModelsFileDownload:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsFileDownload
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.files.getfile(
            id="ID",
        )
        """
        _response = self._raw_client.getfile(id, request_options=request_options)
        return _response.data

    def putfile(
        self,
        id_: str,
        *,
        crc: str,
        content_type: str,
        description: str,
        is_public: bool,
        name: str,
        path: str,
        state: GlobalResourcesSharedModelsFileDownloadState,
        id: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the metadata for a file. Size may not be modified by the client.
                        Set status to 'Available' to publish a file. The file must be uploaded.
                        Set status to 'Created' to reset a file's contents and re-upload.
                        A file may only be 'Removed' by the DELETE method.

        Parameters
        ----------
        id_ : str
            The file's id

        crc : str
            The crc of the file (SHA256, HEX-encoded). Must be provided when creating a file.

        content_type : str
            The type of file; sent as the content-type header.

        description : str
            The description of the file.

        is_public : bool
            Indicates whether this file is available to the public for download.

        name : str
            The name of the file when downloaded.

        path : str
            The Path of the file.

        state : GlobalResourcesSharedModelsFileDownloadState
            Indicates the state of this file. Must be 'Created' when created.

        id : typing.Optional[str]
            The Id of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, GlobalResourcesSharedModelsFileDownloadState

        client = FernApi()
        client.files.putfile(
            id_="ID",
            crc="CRC",
            content_type="ContentType",
            description="Description",
            is_public=True,
            name="Name",
            path="Path",
            state=GlobalResourcesSharedModelsFileDownloadState.CREATED,
        )
        """
        _response = self._raw_client.putfile(
            id_,
            crc=crc,
            content_type=content_type,
            description=description,
            is_public=is_public,
            name=name,
            path=path,
            state=state,
            id=id,
            size=size,
            request_options=request_options,
        )
        return _response.data

    def deletefile(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The file's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.files.deletefile(
            id="ID",
        )
        """
        _response = self._raw_client.deletefile(id, request_options=request_options)
        return _response.data

    def getfilecontents(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SystemObject:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The file's metadata.

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
        client.files.getfilecontents(
            id="ID",
        )
        """
        _response = self._raw_client.getfilecontents(id, request_options=request_options)
        return _response.data

    def putfilecontents(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SystemObject:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The file's metadata.

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
        client.files.putfilecontents(
            id="ID",
        )
        """
        _response = self._raw_client.putfilecontents(id, request_options=request_options)
        return _response.data


class AsyncFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFilesClient
        """
        return self._raw_client

    async def getfiles(
        self,
        *,
        include_deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiIPagedResponseGlobalResourcesSharedModelsFileDownload:
        """
        No Documentation Found.

        Parameters
        ----------
        include_deleted : typing.Optional[bool]
            Indicates whether to include files marked as removed.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiIPagedResponseGlobalResourcesSharedModelsFileDownload
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.files.getfiles()


        asyncio.run(main())
        """
        _response = await self._raw_client.getfiles(
            include_deleted=include_deleted, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def postfile(
        self,
        *,
        crc: str,
        content_type: str,
        description: str,
        is_public: bool,
        name: str,
        path: str,
        state: GlobalResourcesSharedModelsFileDownloadState,
        id: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        crc : str
            The crc of the file (SHA256, HEX-encoded). Must be provided when creating a file.

        content_type : str
            The type of file; sent as the content-type header.

        description : str
            The description of the file.

        is_public : bool
            Indicates whether this file is available to the public for download.

        name : str
            The name of the file when downloaded.

        path : str
            The Path of the file.

        state : GlobalResourcesSharedModelsFileDownloadState
            Indicates the state of this file. Must be 'Created' when created.

        id : typing.Optional[str]
            The Id of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GlobalResourcesSharedModelsFileDownloadState

        client = AsyncFernApi()


        async def main() -> None:
            await client.files.postfile(
                crc="CRC",
                content_type="ContentType",
                description="Description",
                is_public=True,
                name="Name",
                path="Path",
                state=GlobalResourcesSharedModelsFileDownloadState.CREATED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postfile(
            crc=crc,
            content_type=content_type,
            description=description,
            is_public=is_public,
            name=name,
            path=path,
            state=state,
            id=id,
            size=size,
            request_options=request_options,
        )
        return _response.data

    async def getfile(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalResourcesSharedModelsFileDownload:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalResourcesSharedModelsFileDownload
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.files.getfile(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getfile(id, request_options=request_options)
        return _response.data

    async def putfile(
        self,
        id_: str,
        *,
        crc: str,
        content_type: str,
        description: str,
        is_public: bool,
        name: str,
        path: str,
        state: GlobalResourcesSharedModelsFileDownloadState,
        id: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the metadata for a file. Size may not be modified by the client.
                        Set status to 'Available' to publish a file. The file must be uploaded.
                        Set status to 'Created' to reset a file's contents and re-upload.
                        A file may only be 'Removed' by the DELETE method.

        Parameters
        ----------
        id_ : str
            The file's id

        crc : str
            The crc of the file (SHA256, HEX-encoded). Must be provided when creating a file.

        content_type : str
            The type of file; sent as the content-type header.

        description : str
            The description of the file.

        is_public : bool
            Indicates whether this file is available to the public for download.

        name : str
            The name of the file when downloaded.

        path : str
            The Path of the file.

        state : GlobalResourcesSharedModelsFileDownloadState
            Indicates the state of this file. Must be 'Created' when created.

        id : typing.Optional[str]
            The Id of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GlobalResourcesSharedModelsFileDownloadState

        client = AsyncFernApi()


        async def main() -> None:
            await client.files.putfile(
                id_="ID",
                crc="CRC",
                content_type="ContentType",
                description="Description",
                is_public=True,
                name="Name",
                path="Path",
                state=GlobalResourcesSharedModelsFileDownloadState.CREATED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putfile(
            id_,
            crc=crc,
            content_type=content_type,
            description=description,
            is_public=is_public,
            name=name,
            path=path,
            state=state,
            id=id,
            size=size,
            request_options=request_options,
        )
        return _response.data

    async def deletefile(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The file's id.

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
            await client.files.deletefile(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletefile(id, request_options=request_options)
        return _response.data

    async def getfilecontents(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SystemObject:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The file's metadata.

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
            await client.files.getfilecontents(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getfilecontents(id, request_options=request_options)
        return _response.data

    async def putfilecontents(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SystemObject:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The file's metadata.

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
            await client.files.putfilecontents(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putfilecontents(id, request_options=request_options)
        return _response.data
