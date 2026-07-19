

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.duplicate_file_handling import DuplicateFileHandling
from ..types.embedding_config import EmbeddingConfig
from ..types.file_metadata import FileMetadata
from ..types.folder import Folder
from ..types.organization_sources_stats import OrganizationSourcesStats
from ..types.passage import Passage
from .raw_client import AsyncRawFoldersClient, RawFoldersClient
from .types.list_agents_for_folder_request_order import ListAgentsForFolderRequestOrder
from .types.list_agents_for_folder_request_order_by import ListAgentsForFolderRequestOrderBy
from .types.list_files_for_folder_request_order import ListFilesForFolderRequestOrder
from .types.list_files_for_folder_request_order_by import ListFilesForFolderRequestOrderBy
from .types.list_folder_passages_request_order import ListFolderPassagesRequestOrder
from .types.list_folder_passages_request_order_by import ListFolderPassagesRequestOrderBy
from .types.list_folders_request_order import ListFoldersRequestOrder
from .types.list_folders_request_order_by import ListFoldersRequestOrderBy


OMIT = typing.cast(typing.Any, ...)


class FoldersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFoldersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFoldersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFoldersClient
        """
        return self._raw_client

    def count_folders(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Count all data folders created by a user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.count_folders()
        """
        _response = self._raw_client.count_folders(request_options=request_options)
        return _response.data

    def retrieve_folder(self, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Folder:
        """
        Get a folder by ID

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Folder
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.retrieve_folder(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.retrieve_folder(folder_id, request_options=request_options)
        return _response.data

    def delete_folder(self, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Delete a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

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
            token="YOUR_TOKEN",
        )
        client.folders.delete_folder(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.delete_folder(folder_id, request_options=request_options)
        return _response.data

    def modify_folder(
        self,
        folder_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Folder:
        """
        Update the name or documentation of an existing data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        name : typing.Optional[str]
            The name of the source.

        description : typing.Optional[str]
            The description of the source.

        instructions : typing.Optional[str]
            Instructions for how to use the source.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata associated with the source.

        embedding_config : typing.Optional[EmbeddingConfig]
            The embedding configuration used by the source.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Folder
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.modify_folder(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.modify_folder(
            folder_id,
            name=name,
            description=description,
            instructions=instructions,
            metadata=metadata,
            embedding_config=embedding_config,
            request_options=request_options,
        )
        return _response.data

    def get_folder_by_name(self, folder_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        **Deprecated**: Please use the list endpoint `GET /v1/folders?name=` instead.


        Get a folder by name.

        Parameters
        ----------
        folder_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.get_folder_by_name(
            folder_name="folder_name",
        )
        """
        _response = self._raw_client.get_folder_by_name(folder_name, request_options=request_options)
        return _response.data

    def retrieve_metadata(
        self,
        *,
        include_detailed_per_source_metadata: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationSourcesStats:
        """
        Get aggregated metadata for all folders in an organization.

        Returns structured metadata including:
        - Total number of folders
        - Total number of files across all folders
        - Total size of all files
        - Per-source breakdown with file details (file_name, file_size per file) if include_detailed_per_source_metadata is True

        Parameters
        ----------
        include_detailed_per_source_metadata : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationSourcesStats
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.retrieve_metadata()
        """
        _response = self._raw_client.retrieve_metadata(
            include_detailed_per_source_metadata=include_detailed_per_source_metadata, request_options=request_options
        )
        return _response.data

    def list_folders(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFoldersRequestOrder] = None,
        order_by: typing.Optional[ListFoldersRequestOrderBy] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Folder]:
        """
        List all data folders created by a user.

        Parameters
        ----------
        before : typing.Optional[str]
            Folder ID cursor for pagination. Returns folders that come before this folder ID in the specified sort order

        after : typing.Optional[str]
            Folder ID cursor for pagination. Returns folders that come after this folder ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of folders to return

        order : typing.Optional[ListFoldersRequestOrder]
            Sort order for folders by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFoldersRequestOrderBy]
            Field to sort by

        name : typing.Optional[str]
            Folder name to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Folder]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.list_folders()
        """
        _response = self._raw_client.list_folders(
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            name=name,
            request_options=request_options,
        )
        return _response.data

    def create_folder(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        embedding: typing.Optional[str] = OMIT,
        embedding_chunk_size: typing.Optional[int] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Folder:
        """
        Create a new data folder.

        Parameters
        ----------
        name : str
            The name of the source.

        description : typing.Optional[str]
            The description of the source.

        instructions : typing.Optional[str]
            Instructions for how to use the source.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata associated with the source.

        embedding : typing.Optional[str]
            The handle for the embedding config used by the source.

        embedding_chunk_size : typing.Optional[int]
            The chunk size of the embedding.

        embedding_config : typing.Optional[EmbeddingConfig]
            (Legacy) The embedding configuration used by the source.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Folder
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.create_folder(
            name="name",
        )
        """
        _response = self._raw_client.create_folder(
            name=name,
            description=description,
            instructions=instructions,
            metadata=metadata,
            embedding=embedding,
            embedding_chunk_size=embedding_chunk_size,
            embedding_config=embedding_config,
            request_options=request_options,
        )
        return _response.data

    def upload_file_to_folder(
        self,
        folder_id: str,
        *,
        file: core.File,
        duplicate_handling: typing.Optional[DuplicateFileHandling] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileMetadata:
        """
        Upload a file to a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        file : core.File
            See core.File for more documentation

        duplicate_handling : typing.Optional[DuplicateFileHandling]
            How to handle duplicate filenames

        name : typing.Optional[str]
            Optional custom name to override the uploaded file's name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileMetadata
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.upload_file_to_folder(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.upload_file_to_folder(
            folder_id, file=file, duplicate_handling=duplicate_handling, name=name, request_options=request_options
        )
        return _response.data

    def list_agents_for_folder(
        self,
        folder_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForFolderRequestOrder] = None,
        order_by: typing.Optional[ListAgentsForFolderRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Get all agent IDs that have the specified folder attached.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForFolderRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentsForFolderRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.list_agents_for_folder(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.list_agents_for_folder(
            folder_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def list_folder_passages(
        self,
        folder_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFolderPassagesRequestOrder] = None,
        order_by: typing.Optional[ListFolderPassagesRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Passage]:
        """
        List all passages associated with a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        before : typing.Optional[str]
            Passage ID cursor for pagination. Returns passages that come before this passage ID in the specified sort order

        after : typing.Optional[str]
            Passage ID cursor for pagination. Returns passages that come after this passage ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of passages to return

        order : typing.Optional[ListFolderPassagesRequestOrder]
            Sort order for passages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFolderPassagesRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Passage]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.list_folder_passages(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.list_folder_passages(
            folder_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def list_files_for_folder(
        self,
        folder_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFilesForFolderRequestOrder] = None,
        order_by: typing.Optional[ListFilesForFolderRequestOrderBy] = None,
        include_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FileMetadata]:
        """
        List paginated files associated with a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        before : typing.Optional[str]
            File ID cursor for pagination. Returns files that come before this file ID in the specified sort order

        after : typing.Optional[str]
            File ID cursor for pagination. Returns files that come after this file ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of files to return

        order : typing.Optional[ListFilesForFolderRequestOrder]
            Sort order for files by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFilesForFolderRequestOrderBy]
            Field to sort by

        include_content : typing.Optional[bool]
            Whether to include full file content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FileMetadata]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.list_files_for_folder(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.list_files_for_folder(
            folder_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            include_content=include_content,
            request_options=request_options,
        )
        return _response.data

    def retrieve_file(
        self,
        folder_id: str,
        file_id: str,
        *,
        include_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileMetadata:
        """
        Retrieve a file from a folder by ID.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        file_id : str
            The ID of the file in the format 'file-<uuid4>'

        include_content : typing.Optional[bool]
            Whether to include full file content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileMetadata
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.folders.retrieve_file(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            file_id="file-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.retrieve_file(
            folder_id, file_id, include_content=include_content, request_options=request_options
        )
        return _response.data

    def delete_file_from_folder(
        self, folder_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a file from a folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        file_id : str
            The ID of the file in the format 'file-<uuid4>'

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
        client.folders.delete_file_from_folder(
            folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            file_id="file-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.delete_file_from_folder(folder_id, file_id, request_options=request_options)
        return _response.data


class AsyncFoldersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFoldersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFoldersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFoldersClient
        """
        return self._raw_client

    async def count_folders(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Count all data folders created by a user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.count_folders()


        asyncio.run(main())
        """
        _response = await self._raw_client.count_folders(request_options=request_options)
        return _response.data

    async def retrieve_folder(
        self, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Folder:
        """
        Get a folder by ID

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Folder
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.retrieve_folder(
                folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_folder(folder_id, request_options=request_options)
        return _response.data

    async def delete_folder(
        self, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.delete_folder(
                folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_folder(folder_id, request_options=request_options)
        return _response.data

    async def modify_folder(
        self,
        folder_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Folder:
        """
        Update the name or documentation of an existing data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        name : typing.Optional[str]
            The name of the source.

        description : typing.Optional[str]
            The description of the source.

        instructions : typing.Optional[str]
            Instructions for how to use the source.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata associated with the source.

        embedding_config : typing.Optional[EmbeddingConfig]
            The embedding configuration used by the source.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Folder
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.modify_folder(
                folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_folder(
            folder_id,
            name=name,
            description=description,
            instructions=instructions,
            metadata=metadata,
            embedding_config=embedding_config,
            request_options=request_options,
        )
        return _response.data

    async def get_folder_by_name(
        self, folder_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        **Deprecated**: Please use the list endpoint `GET /v1/folders?name=` instead.


        Get a folder by name.

        Parameters
        ----------
        folder_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.get_folder_by_name(
                folder_name="folder_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_folder_by_name(folder_name, request_options=request_options)
        return _response.data

    async def retrieve_metadata(
        self,
        *,
        include_detailed_per_source_metadata: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationSourcesStats:
        """
        Get aggregated metadata for all folders in an organization.

        Returns structured metadata including:
        - Total number of folders
        - Total number of files across all folders
        - Total size of all files
        - Per-source breakdown with file details (file_name, file_size per file) if include_detailed_per_source_metadata is True

        Parameters
        ----------
        include_detailed_per_source_metadata : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationSourcesStats
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.retrieve_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_metadata(
            include_detailed_per_source_metadata=include_detailed_per_source_metadata, request_options=request_options
        )
        return _response.data

    async def list_folders(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFoldersRequestOrder] = None,
        order_by: typing.Optional[ListFoldersRequestOrderBy] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Folder]:
        """
        List all data folders created by a user.

        Parameters
        ----------
        before : typing.Optional[str]
            Folder ID cursor for pagination. Returns folders that come before this folder ID in the specified sort order

        after : typing.Optional[str]
            Folder ID cursor for pagination. Returns folders that come after this folder ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of folders to return

        order : typing.Optional[ListFoldersRequestOrder]
            Sort order for folders by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFoldersRequestOrderBy]
            Field to sort by

        name : typing.Optional[str]
            Folder name to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Folder]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.list_folders()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_folders(
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            name=name,
            request_options=request_options,
        )
        return _response.data

    async def create_folder(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        embedding: typing.Optional[str] = OMIT,
        embedding_chunk_size: typing.Optional[int] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Folder:
        """
        Create a new data folder.

        Parameters
        ----------
        name : str
            The name of the source.

        description : typing.Optional[str]
            The description of the source.

        instructions : typing.Optional[str]
            Instructions for how to use the source.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata associated with the source.

        embedding : typing.Optional[str]
            The handle for the embedding config used by the source.

        embedding_chunk_size : typing.Optional[int]
            The chunk size of the embedding.

        embedding_config : typing.Optional[EmbeddingConfig]
            (Legacy) The embedding configuration used by the source.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Folder
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.create_folder(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_folder(
            name=name,
            description=description,
            instructions=instructions,
            metadata=metadata,
            embedding=embedding,
            embedding_chunk_size=embedding_chunk_size,
            embedding_config=embedding_config,
            request_options=request_options,
        )
        return _response.data

    async def upload_file_to_folder(
        self,
        folder_id: str,
        *,
        file: core.File,
        duplicate_handling: typing.Optional[DuplicateFileHandling] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileMetadata:
        """
        Upload a file to a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        file : core.File
            See core.File for more documentation

        duplicate_handling : typing.Optional[DuplicateFileHandling]
            How to handle duplicate filenames

        name : typing.Optional[str]
            Optional custom name to override the uploaded file's name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileMetadata
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.upload_file_to_folder(
                folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_file_to_folder(
            folder_id, file=file, duplicate_handling=duplicate_handling, name=name, request_options=request_options
        )
        return _response.data

    async def list_agents_for_folder(
        self,
        folder_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForFolderRequestOrder] = None,
        order_by: typing.Optional[ListAgentsForFolderRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Get all agent IDs that have the specified folder attached.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForFolderRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentsForFolderRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.list_agents_for_folder(
                folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_agents_for_folder(
            folder_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def list_folder_passages(
        self,
        folder_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFolderPassagesRequestOrder] = None,
        order_by: typing.Optional[ListFolderPassagesRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Passage]:
        """
        List all passages associated with a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        before : typing.Optional[str]
            Passage ID cursor for pagination. Returns passages that come before this passage ID in the specified sort order

        after : typing.Optional[str]
            Passage ID cursor for pagination. Returns passages that come after this passage ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of passages to return

        order : typing.Optional[ListFolderPassagesRequestOrder]
            Sort order for passages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFolderPassagesRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Passage]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.list_folder_passages(
                folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_folder_passages(
            folder_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def list_files_for_folder(
        self,
        folder_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListFilesForFolderRequestOrder] = None,
        order_by: typing.Optional[ListFilesForFolderRequestOrderBy] = None,
        include_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FileMetadata]:
        """
        List paginated files associated with a data folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        before : typing.Optional[str]
            File ID cursor for pagination. Returns files that come before this file ID in the specified sort order

        after : typing.Optional[str]
            File ID cursor for pagination. Returns files that come after this file ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of files to return

        order : typing.Optional[ListFilesForFolderRequestOrder]
            Sort order for files by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListFilesForFolderRequestOrderBy]
            Field to sort by

        include_content : typing.Optional[bool]
            Whether to include full file content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FileMetadata]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.list_files_for_folder(
                folder_id="source-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_files_for_folder(
            folder_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            include_content=include_content,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_file(
        self,
        folder_id: str,
        file_id: str,
        *,
        include_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileMetadata:
        """
        Retrieve a file from a folder by ID.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        file_id : str
            The ID of the file in the format 'file-<uuid4>'

        include_content : typing.Optional[bool]
            Whether to include full file content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileMetadata
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.folders.retrieve_file(
                folder_id="source-123e4567-e89b-42d3-8456-426614174000",
                file_id="file-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_file(
            folder_id, file_id, include_content=include_content, request_options=request_options
        )
        return _response.data

    async def delete_file_from_folder(
        self, folder_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a file from a folder.

        Parameters
        ----------
        folder_id : str
            The ID of the source in the format 'source-<uuid4>'

        file_id : str
            The ID of the file in the format 'file-<uuid4>'

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
            await client.folders.delete_file_from_folder(
                folder_id="source-123e4567-e89b-42d3-8456-426614174000",
                file_id="file-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_from_folder(folder_id, file_id, request_options=request_options)
        return _response.data
