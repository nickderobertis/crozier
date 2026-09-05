

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cursor_page_type_var_customized_path_meta_data_get import CursorPageTypeVarCustomizedPathMetaDataGet
from ..types.envelope_file_upload_complete_future_response import EnvelopeFileUploadCompleteFutureResponse
from ..types.envelope_file_upload_complete_response import EnvelopeFileUploadCompleteResponse
from ..types.envelope_list_dataset_meta_data import EnvelopeListDatasetMetaData
from ..types.envelope_list_file_meta_data_get import EnvelopeListFileMetaDataGet
from ..types.envelope_presigned_link import EnvelopePresignedLink
from ..types.envelope_task_get import EnvelopeTaskGet
from ..types.file_location import FileLocation
from ..types.file_upload_completion_body import FileUploadCompletionBody
from ..types.link_type import LinkType
from ..types.search_filters import SearchFilters
from ..types.upload_file_request_file_size import UploadFileRequestFileSize
from .raw_client import AsyncRawStorageClient, RawStorageClient
from .types.get_file_metadata_response import GetFileMetadataResponse
from .types.upload_file_response import UploadFileResponse


OMIT = typing.cast(typing.Any, ...)


class StorageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStorageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStorageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStorageClient
        """
        return self._raw_client

    def list_storage_locations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FileLocation]:
        """
        Get available storage locations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FileLocation]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.list_storage_locations()
        """
        _response = self._raw_client.list_storage_locations(request_options=request_options)
        return _response.data

    def list_storage_paths(
        self,
        location_id: int,
        *,
        size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        file_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CursorPageTypeVarCustomizedPathMetaDataGet:
        """
        Lists the files/directories in WorkingDirectory

        Parameters
        ----------
        location_id : int

        size : typing.Optional[int]

        cursor : typing.Optional[str]

        file_filter : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CursorPageTypeVarCustomizedPathMetaDataGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.list_storage_paths(
            location_id=1,
        )
        """
        _response = self._raw_client.list_storage_paths(
            location_id, size=size, cursor=cursor, file_filter=file_filter, request_options=request_options
        )
        return _response.data

    def compute_path_size(
        self, location_id: int, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeTaskGet:
        """
        Compute the size of a path

        Parameters
        ----------
        location_id : int

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.compute_path_size(
            location_id=1,
            path="path",
        )
        """
        _response = self._raw_client.compute_path_size(location_id, path, request_options=request_options)
        return _response.data

    def batch_delete_paths(
        self,
        location_id: int,
        *,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTaskGet:
        """
        Deletes Paths

        Parameters
        ----------
        location_id : int

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.batch_delete_paths(
            location_id=1,
            request=["string"],
        )
        """
        _response = self._raw_client.batch_delete_paths(location_id, request=request, request_options=request_options)
        return _response.data

    def list_datasets_metadata(
        self, location_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListDatasetMetaData:
        """
        Get datasets metadata

        Parameters
        ----------
        location_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListDatasetMetaData
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.list_datasets_metadata(
            location_id=1,
        )
        """
        _response = self._raw_client.list_datasets_metadata(location_id, request_options=request_options)
        return _response.data

    def get_files_metadata(
        self,
        location_id: int,
        *,
        uuid_filter: typing.Optional[str] = None,
        expand_dirs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListDatasetMetaData:
        """
        Get datasets metadata

        Parameters
        ----------
        location_id : int

        uuid_filter : typing.Optional[str]

        expand_dirs : typing.Optional[bool]
            Automatic directory expansion. This will be replaced by pagination the future

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListDatasetMetaData
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.get_files_metadata(
            location_id=1,
        )
        """
        _response = self._raw_client.get_files_metadata(
            location_id, uuid_filter=uuid_filter, expand_dirs=expand_dirs, request_options=request_options
        )
        return _response.data

    def list_dataset_files_metadata(
        self,
        location_id: int,
        dataset_id: str,
        *,
        expand_dirs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListFileMetaDataGet:
        """
        Get Files Metadata

        Parameters
        ----------
        location_id : int

        dataset_id : str

        expand_dirs : typing.Optional[bool]
            Automatic directory expansion. This will be replaced by pagination the future

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListFileMetaDataGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.list_dataset_files_metadata(
            location_id=1,
            dataset_id="dataset_id",
        )
        """
        _response = self._raw_client.list_dataset_files_metadata(
            location_id, dataset_id, expand_dirs=expand_dirs, request_options=request_options
        )
        return _response.data

    def get_file_metadata(
        self, location_id: int, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFileMetadataResponse:
        """
        Get File Metadata

        Parameters
        ----------
        location_id : int

        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFileMetadataResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.get_file_metadata(
            location_id=1,
            file_id="file_id",
        )
        """
        _response = self._raw_client.get_file_metadata(location_id, file_id, request_options=request_options)
        return _response.data

    def download_file(
        self,
        location_id: int,
        file_id: str,
        *,
        link_type: typing.Optional[LinkType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopePresignedLink:
        """
        Returns download link for requested file

        Parameters
        ----------
        location_id : int

        file_id : str

        link_type : typing.Optional[LinkType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePresignedLink
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.download_file(
            location_id=1,
            file_id="file_id",
        )
        """
        _response = self._raw_client.download_file(
            location_id, file_id, link_type=link_type, request_options=request_options
        )
        return _response.data

    def upload_file(
        self,
        location_id: int,
        file_id: str,
        *,
        file_size: typing.Optional[UploadFileRequestFileSize] = None,
        link_type: typing.Optional[LinkType] = None,
        is_directory: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadFileResponse:
        """
        Returns upload link

        Parameters
        ----------
        location_id : int

        file_id : str

        file_size : typing.Optional[UploadFileRequestFileSize]

        link_type : typing.Optional[LinkType]

        is_directory : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadFileResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.upload_file(
            location_id=1,
            file_id="file_id",
            file_size="file_size",
        )
        """
        _response = self._raw_client.upload_file(
            location_id,
            file_id,
            file_size=file_size,
            link_type=link_type,
            is_directory=is_directory,
            request_options=request_options,
        )
        return _response.data

    def delete_file(
        self, location_id: int, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes File

        Parameters
        ----------
        location_id : int

        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.delete_file(
            location_id=1,
            file_id="file_id",
        )
        """
        _response = self._raw_client.delete_file(location_id, file_id, request_options=request_options)
        return _response.data

    def abort_upload_file(
        self, location_id: int, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        aborts an upload if user has the rights to, and reverts
        to the latest version if available, else will delete the file

        Parameters
        ----------
        location_id : int

        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.abort_upload_file(
            location_id=1,
            file_id="file_id",
        )
        """
        _response = self._raw_client.abort_upload_file(location_id, file_id, request_options=request_options)
        return _response.data

    def complete_upload_file(
        self,
        location_id: int,
        file_id: str,
        *,
        data: typing.Optional[FileUploadCompletionBody] = OMIT,
        error: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeFileUploadCompleteResponse:
        """
        completes an upload if the user has the rights to

        Parameters
        ----------
        location_id : int

        file_id : str

        data : typing.Optional[FileUploadCompletionBody]

        error : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeFileUploadCompleteResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.complete_upload_file(
            location_id=1,
            file_id="file_id",
        )
        """
        _response = self._raw_client.complete_upload_file(
            location_id, file_id, data=data, error=error, request_options=request_options
        )
        return _response.data

    def is_completed_upload_file(
        self, location_id: int, file_id: str, future_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeFileUploadCompleteFutureResponse:
        """
        Check for upload completion

        Parameters
        ----------
        location_id : int

        file_id : str

        future_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeFileUploadCompleteFutureResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.is_completed_upload_file(
            location_id=1,
            file_id="file_id",
            future_id="future_id",
        )
        """
        _response = self._raw_client.is_completed_upload_file(
            location_id, file_id, future_id, request_options=request_options
        )
        return _response.data

    def export_data(
        self, location_id: int, *, paths: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeTaskGet:
        """
        Export data

        Parameters
        ----------
        location_id : int

        paths : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.storage.export_data(
            location_id=1,
            paths=["paths"],
        )
        """
        _response = self._raw_client.export_data(location_id, paths=paths, request_options=request_options)
        return _response.data

    def search(
        self, location_id: int, *, filters: SearchFilters, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeTaskGet:
        """
        Starts a files/folders search

        Parameters
        ----------
        location_id : int

        filters : SearchFilters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        from fern import FernApi, SearchFilters

        client = FernApi()
        client.storage.search(
            location_id=1,
            filters=SearchFilters(
                name_pattern="namePattern",
            ),
        )
        """
        _response = self._raw_client.search(location_id, filters=filters, request_options=request_options)
        return _response.data


class AsyncStorageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStorageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStorageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStorageClient
        """
        return self._raw_client

    async def list_storage_locations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FileLocation]:
        """
        Get available storage locations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FileLocation]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.storage.list_storage_locations()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_storage_locations(request_options=request_options)
        return _response.data

    async def list_storage_paths(
        self,
        location_id: int,
        *,
        size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        file_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CursorPageTypeVarCustomizedPathMetaDataGet:
        """
        Lists the files/directories in WorkingDirectory

        Parameters
        ----------
        location_id : int

        size : typing.Optional[int]

        cursor : typing.Optional[str]

        file_filter : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CursorPageTypeVarCustomizedPathMetaDataGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.storage.list_storage_paths(
                location_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_storage_paths(
            location_id, size=size, cursor=cursor, file_filter=file_filter, request_options=request_options
        )
        return _response.data

    async def compute_path_size(
        self, location_id: int, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeTaskGet:
        """
        Compute the size of a path

        Parameters
        ----------
        location_id : int

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.storage.compute_path_size(
                location_id=1,
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.compute_path_size(location_id, path, request_options=request_options)
        return _response.data

    async def batch_delete_paths(
        self,
        location_id: int,
        *,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeTaskGet:
        """
        Deletes Paths

        Parameters
        ----------
        location_id : int

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.storage.batch_delete_paths(
                location_id=1,
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch_delete_paths(
            location_id, request=request, request_options=request_options
        )
        return _response.data

    async def list_datasets_metadata(
        self, location_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListDatasetMetaData:
        """
        Get datasets metadata

        Parameters
        ----------
        location_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListDatasetMetaData
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.storage.list_datasets_metadata(
                location_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_datasets_metadata(location_id, request_options=request_options)
        return _response.data

    async def get_files_metadata(
        self,
        location_id: int,
        *,
        uuid_filter: typing.Optional[str] = None,
        expand_dirs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListDatasetMetaData:
        """
        Get datasets metadata

        Parameters
        ----------
        location_id : int

        uuid_filter : typing.Optional[str]

        expand_dirs : typing.Optional[bool]
            Automatic directory expansion. This will be replaced by pagination the future

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListDatasetMetaData
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.storage.get_files_metadata(
                location_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_files_metadata(
            location_id, uuid_filter=uuid_filter, expand_dirs=expand_dirs, request_options=request_options
        )
        return _response.data

    async def list_dataset_files_metadata(
        self,
        location_id: int,
        dataset_id: str,
        *,
        expand_dirs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListFileMetaDataGet:
        """
        Get Files Metadata

        Parameters
        ----------
        location_id : int

        dataset_id : str

        expand_dirs : typing.Optional[bool]
            Automatic directory expansion. This will be replaced by pagination the future

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListFileMetaDataGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.storage.list_dataset_files_metadata(
                location_id=1,
                dataset_id="dataset_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_dataset_files_metadata(
            location_id, dataset_id, expand_dirs=expand_dirs, request_options=request_options
        )
        return _response.data

    async def get_file_metadata(
        self, location_id: int, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFileMetadataResponse:
        """
        Get File Metadata

        Parameters
        ----------
        location_id : int

        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFileMetadataResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.storage.get_file_metadata(
                location_id=1,
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_metadata(location_id, file_id, request_options=request_options)
        return _response.data

    async def download_file(
        self,
        location_id: int,
        file_id: str,
        *,
        link_type: typing.Optional[LinkType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopePresignedLink:
        """
        Returns download link for requested file

        Parameters
        ----------
        location_id : int

        file_id : str

        link_type : typing.Optional[LinkType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePresignedLink
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.storage.download_file(
                location_id=1,
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_file(
            location_id, file_id, link_type=link_type, request_options=request_options
        )
        return _response.data

    async def upload_file(
        self,
        location_id: int,
        file_id: str,
        *,
        file_size: typing.Optional[UploadFileRequestFileSize] = None,
        link_type: typing.Optional[LinkType] = None,
        is_directory: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadFileResponse:
        """
        Returns upload link

        Parameters
        ----------
        location_id : int

        file_id : str

        file_size : typing.Optional[UploadFileRequestFileSize]

        link_type : typing.Optional[LinkType]

        is_directory : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadFileResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.storage.upload_file(
                location_id=1,
                file_id="file_id",
                file_size="file_size",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_file(
            location_id,
            file_id,
            file_size=file_size,
            link_type=link_type,
            is_directory=is_directory,
            request_options=request_options,
        )
        return _response.data

    async def delete_file(
        self, location_id: int, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes File

        Parameters
        ----------
        location_id : int

        file_id : str

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
            await client.storage.delete_file(
                location_id=1,
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file(location_id, file_id, request_options=request_options)
        return _response.data

    async def abort_upload_file(
        self, location_id: int, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        aborts an upload if user has the rights to, and reverts
        to the latest version if available, else will delete the file

        Parameters
        ----------
        location_id : int

        file_id : str

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
            await client.storage.abort_upload_file(
                location_id=1,
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.abort_upload_file(location_id, file_id, request_options=request_options)
        return _response.data

    async def complete_upload_file(
        self,
        location_id: int,
        file_id: str,
        *,
        data: typing.Optional[FileUploadCompletionBody] = OMIT,
        error: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeFileUploadCompleteResponse:
        """
        completes an upload if the user has the rights to

        Parameters
        ----------
        location_id : int

        file_id : str

        data : typing.Optional[FileUploadCompletionBody]

        error : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeFileUploadCompleteResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.storage.complete_upload_file(
                location_id=1,
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_upload_file(
            location_id, file_id, data=data, error=error, request_options=request_options
        )
        return _response.data

    async def is_completed_upload_file(
        self, location_id: int, file_id: str, future_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeFileUploadCompleteFutureResponse:
        """
        Check for upload completion

        Parameters
        ----------
        location_id : int

        file_id : str

        future_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeFileUploadCompleteFutureResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.storage.is_completed_upload_file(
                location_id=1,
                file_id="file_id",
                future_id="future_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.is_completed_upload_file(
            location_id, file_id, future_id, request_options=request_options
        )
        return _response.data

    async def export_data(
        self, location_id: int, *, paths: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeTaskGet:
        """
        Export data

        Parameters
        ----------
        location_id : int

        paths : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.storage.export_data(
                location_id=1,
                paths=["paths"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export_data(location_id, paths=paths, request_options=request_options)
        return _response.data

    async def search(
        self, location_id: int, *, filters: SearchFilters, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeTaskGet:
        """
        Starts a files/folders search

        Parameters
        ----------
        location_id : int

        filters : SearchFilters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeTaskGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SearchFilters

        client = AsyncFernApi()


        async def main() -> None:
            await client.storage.search(
                location_id=1,
                filters=SearchFilters(
                    name_pattern="namePattern",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search(location_id, filters=filters, request_options=request_options)
        return _response.data
