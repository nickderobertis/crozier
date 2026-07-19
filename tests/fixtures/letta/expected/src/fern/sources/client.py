

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.duplicate_file_handling import DuplicateFileHandling
from ..types.embedding_config import EmbeddingConfig
from ..types.file_metadata import FileMetadata
from ..types.organization_sources_stats import OrganizationSourcesStats
from ..types.passage import Passage
from ..types.source import Source
from .raw_client import AsyncRawSourcesClient, RawSourcesClient


OMIT = typing.cast(typing.Any, ...)


class SourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSourcesClient
        """
        return self._raw_client

    def count_sources(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Count all data sources created by a user.

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
        client.sources.count_sources()
        """
        _response = self._raw_client.count_sources(request_options=request_options)
        return _response.data

    def retrieve_source(self, source_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Source:
        """
        Get all sources

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Source
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sources.retrieve_source(
            source_id="source-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.retrieve_source(source_id, request_options=request_options)
        return _response.data

    def delete_source(self, source_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Delete a data source.

        Parameters
        ----------
        source_id : str
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
        client.sources.delete_source(
            source_id="source-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.delete_source(source_id, request_options=request_options)
        return _response.data

    def modify_source(
        self,
        source_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Source:
        """
        Update the name or documentation of an existing data source.

        Parameters
        ----------
        source_id : str
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
        Source
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sources.modify_source(
            source_id="source-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.modify_source(
            source_id,
            name=name,
            description=description,
            instructions=instructions,
            metadata=metadata,
            embedding_config=embedding_config,
            request_options=request_options,
        )
        return _response.data

    def get_source_id_by_name(
        self, source_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get a source by name

        Parameters
        ----------
        source_name : str

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
        client.sources.get_source_id_by_name(
            source_name="source_name",
        )
        """
        _response = self._raw_client.get_source_id_by_name(source_name, request_options=request_options)
        return _response.data

    def get_sources_metadata(
        self,
        *,
        include_detailed_per_source_metadata: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationSourcesStats:
        """
        Get aggregated metadata for all sources in an organization.

        Returns structured metadata including:
        - Total number of sources
        - Total number of files across all sources
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
        client.sources.get_sources_metadata()
        """
        _response = self._raw_client.get_sources_metadata(
            include_detailed_per_source_metadata=include_detailed_per_source_metadata, request_options=request_options
        )
        return _response.data

    def list_sources(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Source]:
        """
        List all data sources created by a user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Source]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sources.list_sources()
        """
        _response = self._raw_client.list_sources(request_options=request_options)
        return _response.data

    def create_source(
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
    ) -> Source:
        """
        Create a new data source.

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
        Source
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sources.create_source(
            name="name",
        )
        """
        _response = self._raw_client.create_source(
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

    def upload_file_to_source(
        self,
        source_id: str,
        *,
        file: core.File,
        duplicate_handling: typing.Optional[DuplicateFileHandling] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileMetadata:
        """
        Upload a file to a data source.

        Parameters
        ----------
        source_id : str
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
        client.sources.upload_file_to_source(
            source_id="source-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.upload_file_to_source(
            source_id, file=file, duplicate_handling=duplicate_handling, name=name, request_options=request_options
        )
        return _response.data

    def get_agents_for_source(
        self, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Get all agent IDs that have the specified source attached.

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

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
        client.sources.get_agents_for_source(
            source_id="source-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.get_agents_for_source(source_id, request_options=request_options)
        return _response.data

    def list_source_passages(
        self,
        source_id: str,
        *,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Passage]:
        """
        List all passages associated with a data source.

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        after : typing.Optional[str]
            Message after which to retrieve the returned messages.

        before : typing.Optional[str]
            Message before which to retrieve the returned messages.

        limit : typing.Optional[int]
            Maximum number of messages to retrieve.

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
        client.sources.list_source_passages(
            source_id="source-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.list_source_passages(
            source_id, after=after, before=before, limit=limit, request_options=request_options
        )
        return _response.data

    def list_source_files(
        self,
        source_id: str,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        include_content: typing.Optional[bool] = None,
        check_status_updates: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FileMetadata]:
        """
        List paginated files associated with a data source.

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        limit : typing.Optional[int]
            Number of files to return

        after : typing.Optional[str]
            Pagination cursor to fetch the next set of results

        include_content : typing.Optional[bool]
            Whether to include full file content

        check_status_updates : typing.Optional[bool]
            Whether to check and update file processing status (from the vector db service). If False, will not fetch and update the status, which may lead to performance gains.

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
        client.sources.list_source_files(
            source_id="source-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.list_source_files(
            source_id,
            limit=limit,
            after=after,
            include_content=include_content,
            check_status_updates=check_status_updates,
            request_options=request_options,
        )
        return _response.data

    def get_file_metadata(
        self,
        source_id: str,
        file_id: str,
        *,
        include_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileMetadata:
        """
        Retrieve metadata for a specific file by its ID.

        Parameters
        ----------
        source_id : str
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
        client.sources.get_file_metadata(
            source_id="source-123e4567-e89b-42d3-8456-426614174000",
            file_id="file-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.get_file_metadata(
            source_id, file_id, include_content=include_content, request_options=request_options
        )
        return _response.data

    def delete_file_from_source(
        self, source_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a data source.

        Parameters
        ----------
        source_id : str
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
        client.sources.delete_file_from_source(
            source_id="source-123e4567-e89b-42d3-8456-426614174000",
            file_id="file-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.delete_file_from_source(source_id, file_id, request_options=request_options)
        return _response.data


class AsyncSourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSourcesClient
        """
        return self._raw_client

    async def count_sources(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Count all data sources created by a user.

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
            await client.sources.count_sources()


        asyncio.run(main())
        """
        _response = await self._raw_client.count_sources(request_options=request_options)
        return _response.data

    async def retrieve_source(
        self, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Source:
        """
        Get all sources

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Source
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sources.retrieve_source(
                source_id="source-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_source(source_id, request_options=request_options)
        return _response.data

    async def delete_source(
        self, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete a data source.

        Parameters
        ----------
        source_id : str
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
            await client.sources.delete_source(
                source_id="source-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_source(source_id, request_options=request_options)
        return _response.data

    async def modify_source(
        self,
        source_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Source:
        """
        Update the name or documentation of an existing data source.

        Parameters
        ----------
        source_id : str
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
        Source
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sources.modify_source(
                source_id="source-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_source(
            source_id,
            name=name,
            description=description,
            instructions=instructions,
            metadata=metadata,
            embedding_config=embedding_config,
            request_options=request_options,
        )
        return _response.data

    async def get_source_id_by_name(
        self, source_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get a source by name

        Parameters
        ----------
        source_name : str

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
            await client.sources.get_source_id_by_name(
                source_name="source_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_source_id_by_name(source_name, request_options=request_options)
        return _response.data

    async def get_sources_metadata(
        self,
        *,
        include_detailed_per_source_metadata: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationSourcesStats:
        """
        Get aggregated metadata for all sources in an organization.

        Returns structured metadata including:
        - Total number of sources
        - Total number of files across all sources
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
            await client.sources.get_sources_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sources_metadata(
            include_detailed_per_source_metadata=include_detailed_per_source_metadata, request_options=request_options
        )
        return _response.data

    async def list_sources(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Source]:
        """
        List all data sources created by a user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Source]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sources.list_sources()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sources(request_options=request_options)
        return _response.data

    async def create_source(
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
    ) -> Source:
        """
        Create a new data source.

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
        Source
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sources.create_source(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_source(
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

    async def upload_file_to_source(
        self,
        source_id: str,
        *,
        file: core.File,
        duplicate_handling: typing.Optional[DuplicateFileHandling] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileMetadata:
        """
        Upload a file to a data source.

        Parameters
        ----------
        source_id : str
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
            await client.sources.upload_file_to_source(
                source_id="source-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_file_to_source(
            source_id, file=file, duplicate_handling=duplicate_handling, name=name, request_options=request_options
        )
        return _response.data

    async def get_agents_for_source(
        self, source_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Get all agent IDs that have the specified source attached.

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

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
            await client.sources.get_agents_for_source(
                source_id="source-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agents_for_source(source_id, request_options=request_options)
        return _response.data

    async def list_source_passages(
        self,
        source_id: str,
        *,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Passage]:
        """
        List all passages associated with a data source.

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        after : typing.Optional[str]
            Message after which to retrieve the returned messages.

        before : typing.Optional[str]
            Message before which to retrieve the returned messages.

        limit : typing.Optional[int]
            Maximum number of messages to retrieve.

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
            await client.sources.list_source_passages(
                source_id="source-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_source_passages(
            source_id, after=after, before=before, limit=limit, request_options=request_options
        )
        return _response.data

    async def list_source_files(
        self,
        source_id: str,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        include_content: typing.Optional[bool] = None,
        check_status_updates: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FileMetadata]:
        """
        List paginated files associated with a data source.

        Parameters
        ----------
        source_id : str
            The ID of the source in the format 'source-<uuid4>'

        limit : typing.Optional[int]
            Number of files to return

        after : typing.Optional[str]
            Pagination cursor to fetch the next set of results

        include_content : typing.Optional[bool]
            Whether to include full file content

        check_status_updates : typing.Optional[bool]
            Whether to check and update file processing status (from the vector db service). If False, will not fetch and update the status, which may lead to performance gains.

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
            await client.sources.list_source_files(
                source_id="source-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_source_files(
            source_id,
            limit=limit,
            after=after,
            include_content=include_content,
            check_status_updates=check_status_updates,
            request_options=request_options,
        )
        return _response.data

    async def get_file_metadata(
        self,
        source_id: str,
        file_id: str,
        *,
        include_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileMetadata:
        """
        Retrieve metadata for a specific file by its ID.

        Parameters
        ----------
        source_id : str
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
            await client.sources.get_file_metadata(
                source_id="source-123e4567-e89b-42d3-8456-426614174000",
                file_id="file-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_metadata(
            source_id, file_id, include_content=include_content, request_options=request_options
        )
        return _response.data

    async def delete_file_from_source(
        self, source_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a data source.

        Parameters
        ----------
        source_id : str
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
            await client.sources.delete_file_from_source(
                source_id="source-123e4567-e89b-42d3-8456-426614174000",
                file_id="file-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_from_source(source_id, file_id, request_options=request_options)
        return _response.data
