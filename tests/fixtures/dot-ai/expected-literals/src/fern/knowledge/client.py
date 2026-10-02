

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.knowledge_ask_post_response import KnowledgeAskPostResponse
from ..types.knowledge_source_source_identifier_delete_response import KnowledgeSourceSourceIdentifierDeleteResponse
from ..types.tool_execution_response import ToolExecutionResponse
from .raw_client import AsyncRawKnowledgeClient, RawKnowledgeClient
from .types.manage_knowledge_request_operation import ManageKnowledgeRequestOperation


OMIT = typing.cast(typing.Any, ...)


class KnowledgeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKnowledgeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKnowledgeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKnowledgeClient
        """
        return self._raw_client

    def execute_manage_knowledge_tool(
        self,
        *,
        operation: ManageKnowledgeRequestOperation,
        content: typing.Optional[str] = OMIT,
        uri: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        query: typing.Optional[str] = OMIT,
        limit: typing.Optional[float] = OMIT,
        uri_filter: typing.Optional[str] = OMIT,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        Manage the knowledge base: ingest documents, search with natural language, or delete chunks. Use "ingest" to store organizational documentation, "search" to find relevant content semantically, or "deleteByUri" to remove all chunks for a document. TIP: For complex questions, you can call search multiple times with different phrasings to gather comprehensive information before synthesizing your answer.

        Parameters
        ----------
        operation : ManageKnowledgeRequestOperation
            Operation to perform: "ingest" to add documents, "search" for semantic search, "deleteByUri" to remove all chunks for a document.

        content : typing.Optional[str]
            Document content to ingest (required for ingest operation).

        uri : typing.Optional[str]
            Full URL identifying the document (required for ingest and deleteByUri). E.g., https://github.com/org/repo/blob/main/docs/guide.md

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata to store with chunks

        query : typing.Optional[str]
            Natural language search query (required for search operation).

        limit : typing.Optional[float]
            Maximum number of results to return for search (default: 20).

        uri_filter : typing.Optional[str]
            Optional URL prefix to filter search results (e.g., "https://github.com/org/repo/").

        interaction_id : typing.Optional[str]
            INTERNAL ONLY - Do not populate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolExecutionResponse
            Tool execution result

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.knowledge.execute_manage_knowledge_tool(
            operation="ingest",
            content="example content",
            uri="example uri",
            metadata={"key": "value"},
            query="example query",
            limit=42.0,
            uri_filter="example uriFilter",
            interaction_id="example interaction_id",
        )
        """
        _response = self._raw_client.execute_manage_knowledge_tool(
            operation=operation,
            content=content,
            uri=uri,
            metadata=metadata,
            query=query,
            limit=limit,
            uri_filter=uri_filter,
            interaction_id=interaction_id,
            request_options=request_options,
        )
        return _response.data

    def delete_all_knowledge_base_chunks_for_a_source_identifier_used_by_controller_for_git_knowledge_source_cleanup(
        self, source_identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> KnowledgeSourceSourceIdentifierDeleteResponse:
        """
        Delete all knowledge base chunks for a source identifier. Used by controller for GitKnowledgeSource cleanup.

        Parameters
        ----------
        source_identifier : str
            Source identifier (e.g., namespace/name of GitKnowledgeSource CR)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeSourceSourceIdentifierDeleteResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.knowledge.delete_all_knowledge_base_chunks_for_a_source_identifier_used_by_controller_for_git_knowledge_source_cleanup(
            source_identifier="sourceIdentifier",
        )
        """
        _response = self._raw_client.delete_all_knowledge_base_chunks_for_a_source_identifier_used_by_controller_for_git_knowledge_source_cleanup(
            source_identifier, request_options=request_options
        )
        return _response.data

    def ask_a_question_and_receive_an_ai_synthesized_answer_from_the_knowledge_base_uses_an_agentic_approach_that_can_search_multiple_times_with_different_phrasings_for_comprehensive_answers(
        self,
        *,
        query: str,
        limit: float,
        uri_filter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KnowledgeAskPostResponse:
        """
        Ask a question and receive an AI-synthesized answer from the knowledge base. Uses an agentic approach that can search multiple times with different phrasings for comprehensive answers.

        Parameters
        ----------
        query : str
            The question to answer from the knowledge base

        limit : float
            Maximum chunks to retrieve per search (default: 20)

        uri_filter : typing.Optional[str]
            Optional: filter searches to specific document URI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeAskPostResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.knowledge.ask_a_question_and_receive_an_ai_synthesized_answer_from_the_knowledge_base_uses_an_agentic_approach_that_can_search_multiple_times_with_different_phrasings_for_comprehensive_answers(
            query="query",
            limit=1.1,
        )
        """
        _response = self._raw_client.ask_a_question_and_receive_an_ai_synthesized_answer_from_the_knowledge_base_uses_an_agentic_approach_that_can_search_multiple_times_with_different_phrasings_for_comprehensive_answers(
            query=query, limit=limit, uri_filter=uri_filter, request_options=request_options
        )
        return _response.data


class AsyncKnowledgeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKnowledgeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKnowledgeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKnowledgeClient
        """
        return self._raw_client

    async def execute_manage_knowledge_tool(
        self,
        *,
        operation: ManageKnowledgeRequestOperation,
        content: typing.Optional[str] = OMIT,
        uri: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        query: typing.Optional[str] = OMIT,
        limit: typing.Optional[float] = OMIT,
        uri_filter: typing.Optional[str] = OMIT,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ToolExecutionResponse:
        """
        Manage the knowledge base: ingest documents, search with natural language, or delete chunks. Use "ingest" to store organizational documentation, "search" to find relevant content semantically, or "deleteByUri" to remove all chunks for a document. TIP: For complex questions, you can call search multiple times with different phrasings to gather comprehensive information before synthesizing your answer.

        Parameters
        ----------
        operation : ManageKnowledgeRequestOperation
            Operation to perform: "ingest" to add documents, "search" for semantic search, "deleteByUri" to remove all chunks for a document.

        content : typing.Optional[str]
            Document content to ingest (required for ingest operation).

        uri : typing.Optional[str]
            Full URL identifying the document (required for ingest and deleteByUri). E.g., https://github.com/org/repo/blob/main/docs/guide.md

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Optional metadata to store with chunks

        query : typing.Optional[str]
            Natural language search query (required for search operation).

        limit : typing.Optional[float]
            Maximum number of results to return for search (default: 20).

        uri_filter : typing.Optional[str]
            Optional URL prefix to filter search results (e.g., "https://github.com/org/repo/").

        interaction_id : typing.Optional[str]
            INTERNAL ONLY - Do not populate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolExecutionResponse
            Tool execution result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.knowledge.execute_manage_knowledge_tool(
                operation="ingest",
                content="example content",
                uri="example uri",
                metadata={"key": "value"},
                query="example query",
                limit=42.0,
                uri_filter="example uriFilter",
                interaction_id="example interaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_manage_knowledge_tool(
            operation=operation,
            content=content,
            uri=uri,
            metadata=metadata,
            query=query,
            limit=limit,
            uri_filter=uri_filter,
            interaction_id=interaction_id,
            request_options=request_options,
        )
        return _response.data

    async def delete_all_knowledge_base_chunks_for_a_source_identifier_used_by_controller_for_git_knowledge_source_cleanup(
        self, source_identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> KnowledgeSourceSourceIdentifierDeleteResponse:
        """
        Delete all knowledge base chunks for a source identifier. Used by controller for GitKnowledgeSource cleanup.

        Parameters
        ----------
        source_identifier : str
            Source identifier (e.g., namespace/name of GitKnowledgeSource CR)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeSourceSourceIdentifierDeleteResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.knowledge.delete_all_knowledge_base_chunks_for_a_source_identifier_used_by_controller_for_git_knowledge_source_cleanup(
                source_identifier="sourceIdentifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_all_knowledge_base_chunks_for_a_source_identifier_used_by_controller_for_git_knowledge_source_cleanup(
            source_identifier, request_options=request_options
        )
        return _response.data

    async def ask_a_question_and_receive_an_ai_synthesized_answer_from_the_knowledge_base_uses_an_agentic_approach_that_can_search_multiple_times_with_different_phrasings_for_comprehensive_answers(
        self,
        *,
        query: str,
        limit: float,
        uri_filter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KnowledgeAskPostResponse:
        """
        Ask a question and receive an AI-synthesized answer from the knowledge base. Uses an agentic approach that can search multiple times with different phrasings for comprehensive answers.

        Parameters
        ----------
        query : str
            The question to answer from the knowledge base

        limit : float
            Maximum chunks to retrieve per search (default: 20)

        uri_filter : typing.Optional[str]
            Optional: filter searches to specific document URI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeAskPostResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.knowledge.ask_a_question_and_receive_an_ai_synthesized_answer_from_the_knowledge_base_uses_an_agentic_approach_that_can_search_multiple_times_with_different_phrasings_for_comprehensive_answers(
                query="query",
                limit=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ask_a_question_and_receive_an_ai_synthesized_answer_from_the_knowledge_base_uses_an_agentic_approach_that_can_search_multiple_times_with_different_phrasings_for_comprehensive_answers(
            query=query, limit=limit, uri_filter=uri_filter, request_options=request_options
        )
        return _response.data
