

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agent_state import AgentState
from ..types.archive import Archive
from ..types.embedding_config import EmbeddingConfig
from ..types.passage import Passage
from .raw_client import AsyncRawArchivesClient, RawArchivesClient
from .types.list_agents_for_archive_request_include_item import ListAgentsForArchiveRequestIncludeItem
from .types.list_agents_for_archive_request_order import ListAgentsForArchiveRequestOrder
from .types.list_archives_request_order import ListArchivesRequestOrder
from .types.list_archives_request_order_by import ListArchivesRequestOrderBy


OMIT = typing.cast(typing.Any, ...)


class ArchivesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawArchivesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawArchivesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawArchivesClient
        """
        return self._raw_client

    def list_archives(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListArchivesRequestOrder] = None,
        order_by: typing.Optional[ListArchivesRequestOrderBy] = None,
        name: typing.Optional[str] = None,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Archive]:
        """
        Get a list of all archives for the current organization with optional filters and pagination.

        Parameters
        ----------
        before : typing.Optional[str]
            Archive ID cursor for pagination. Returns archives that come before this archive ID in the specified sort order

        after : typing.Optional[str]
            Archive ID cursor for pagination. Returns archives that come after this archive ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of archives to return

        order : typing.Optional[ListArchivesRequestOrder]
            Sort order for archives by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListArchivesRequestOrderBy]
            Field to sort by

        name : typing.Optional[str]
            Filter by archive name (exact match)

        agent_id : typing.Optional[str]
            Only archives attached to this agent ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Archive]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.archives.list_archives()
        """
        _response = self._raw_client.list_archives(
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            name=name,
            agent_id=agent_id,
            request_options=request_options,
        )
        return _response.data

    def create_archive(
        self,
        *,
        name: str,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        embedding: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Archive:
        """
        Create a new archive.

        Parameters
        ----------
        name : str

        embedding_config : typing.Optional[EmbeddingConfig]
            Deprecated: Use `embedding` field instead. Embedding configuration for the archive

        embedding : typing.Optional[str]
            Embedding model handle for the archive

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Archive
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.archives.create_archive(
            name="name",
        )
        """
        _response = self._raw_client.create_archive(
            name=name,
            embedding_config=embedding_config,
            embedding=embedding,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def retrieve_archive(self, archive_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Archive:
        """
        Get a single archive by its ID.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Archive
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.archives.retrieve_archive(
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.retrieve_archive(archive_id, request_options=request_options)
        return _response.data

    def delete_archive(self, archive_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an archive by its ID.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

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
        client.archives.delete_archive(
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.delete_archive(archive_id, request_options=request_options)
        return _response.data

    def modify_archive(
        self,
        archive_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Archive:
        """
        Update an existing archive's name and/or description.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Archive
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.archives.modify_archive(
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.modify_archive(
            archive_id, name=name, description=description, request_options=request_options
        )
        return _response.data

    def list_agents_for_archive(
        self,
        archive_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForArchiveRequestOrder] = None,
        include: typing.Optional[
            typing.Union[
                ListAgentsForArchiveRequestIncludeItem, typing.Sequence[ListAgentsForArchiveRequestIncludeItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AgentState]:
        """
        Get a list of agents that have access to an archive with pagination support.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForArchiveRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        include : typing.Optional[typing.Union[ListAgentsForArchiveRequestIncludeItem, typing.Sequence[ListAgentsForArchiveRequestIncludeItem]]]
            Specify which relational fields to include in the response. No relationships are included by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AgentState]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.archives.list_agents_for_archive(
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.list_agents_for_archive(
            archive_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            include=include,
            request_options=request_options,
        )
        return _response.data

    def create_passage_in_archive(
        self,
        archive_id: str,
        *,
        text: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Passage:
        """
        Create a new passage in an archive.

        This adds a passage to the archive and creates embeddings for vector storage.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        text : str
            The text content of the passage

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata for the passage

        tags : typing.Optional[typing.Sequence[str]]
            Optional tags for categorizing the passage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Passage
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.archives.create_passage_in_archive(
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
            text="text",
        )
        """
        _response = self._raw_client.create_passage_in_archive(
            archive_id, text=text, metadata=metadata, tags=tags, request_options=request_options
        )
        return _response.data

    def delete_passage_from_archive(
        self, archive_id: str, passage_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a passage from an archive.

        This permanently removes the passage from both the database and vector storage (if applicable).

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        passage_id : str
            The ID of the passage in the format 'passage-<uuid4>'

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
        client.archives.delete_passage_from_archive(
            archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
            passage_id="passage-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.delete_passage_from_archive(
            archive_id, passage_id, request_options=request_options
        )
        return _response.data


class AsyncArchivesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawArchivesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawArchivesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawArchivesClient
        """
        return self._raw_client

    async def list_archives(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListArchivesRequestOrder] = None,
        order_by: typing.Optional[ListArchivesRequestOrderBy] = None,
        name: typing.Optional[str] = None,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Archive]:
        """
        Get a list of all archives for the current organization with optional filters and pagination.

        Parameters
        ----------
        before : typing.Optional[str]
            Archive ID cursor for pagination. Returns archives that come before this archive ID in the specified sort order

        after : typing.Optional[str]
            Archive ID cursor for pagination. Returns archives that come after this archive ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of archives to return

        order : typing.Optional[ListArchivesRequestOrder]
            Sort order for archives by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListArchivesRequestOrderBy]
            Field to sort by

        name : typing.Optional[str]
            Filter by archive name (exact match)

        agent_id : typing.Optional[str]
            Only archives attached to this agent ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Archive]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.archives.list_archives()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_archives(
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            name=name,
            agent_id=agent_id,
            request_options=request_options,
        )
        return _response.data

    async def create_archive(
        self,
        *,
        name: str,
        embedding_config: typing.Optional[EmbeddingConfig] = OMIT,
        embedding: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Archive:
        """
        Create a new archive.

        Parameters
        ----------
        name : str

        embedding_config : typing.Optional[EmbeddingConfig]
            Deprecated: Use `embedding` field instead. Embedding configuration for the archive

        embedding : typing.Optional[str]
            Embedding model handle for the archive

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Archive
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.archives.create_archive(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_archive(
            name=name,
            embedding_config=embedding_config,
            embedding=embedding,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_archive(
        self, archive_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Archive:
        """
        Get a single archive by its ID.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Archive
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.archives.retrieve_archive(
                archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_archive(archive_id, request_options=request_options)
        return _response.data

    async def delete_archive(self, archive_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an archive by its ID.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

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
            await client.archives.delete_archive(
                archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_archive(archive_id, request_options=request_options)
        return _response.data

    async def modify_archive(
        self,
        archive_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Archive:
        """
        Update an existing archive's name and/or description.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Archive
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.archives.modify_archive(
                archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_archive(
            archive_id, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def list_agents_for_archive(
        self,
        archive_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForArchiveRequestOrder] = None,
        include: typing.Optional[
            typing.Union[
                ListAgentsForArchiveRequestIncludeItem, typing.Sequence[ListAgentsForArchiveRequestIncludeItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AgentState]:
        """
        Get a list of agents that have access to an archive with pagination support.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForArchiveRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        include : typing.Optional[typing.Union[ListAgentsForArchiveRequestIncludeItem, typing.Sequence[ListAgentsForArchiveRequestIncludeItem]]]
            Specify which relational fields to include in the response. No relationships are included by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AgentState]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.archives.list_agents_for_archive(
                archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_agents_for_archive(
            archive_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            include=include,
            request_options=request_options,
        )
        return _response.data

    async def create_passage_in_archive(
        self,
        archive_id: str,
        *,
        text: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Passage:
        """
        Create a new passage in an archive.

        This adds a passage to the archive and creates embeddings for vector storage.

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        text : str
            The text content of the passage

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata for the passage

        tags : typing.Optional[typing.Sequence[str]]
            Optional tags for categorizing the passage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Passage
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.archives.create_passage_in_archive(
                archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
                text="text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_passage_in_archive(
            archive_id, text=text, metadata=metadata, tags=tags, request_options=request_options
        )
        return _response.data

    async def delete_passage_from_archive(
        self, archive_id: str, passage_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a passage from an archive.

        This permanently removes the passage from both the database and vector storage (if applicable).

        Parameters
        ----------
        archive_id : str
            The ID of the archive in the format 'archive-<uuid4>'

        passage_id : str
            The ID of the passage in the format 'passage-<uuid4>'

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
            await client.archives.delete_passage_from_archive(
                archive_id="archive-123e4567-e89b-42d3-8456-426614174000",
                passage_id="passage-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_passage_from_archive(
            archive_id, passage_id, request_options=request_options
        )
        return _response.data
