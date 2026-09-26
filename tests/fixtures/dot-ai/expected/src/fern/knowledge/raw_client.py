

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..types.knowledge_ask_post_response import KnowledgeAskPostResponse
from ..types.knowledge_source_source_identifier_delete_response import KnowledgeSourceSourceIdentifierDeleteResponse
from ..types.tool_execution_response import ToolExecutionResponse
from .types.manage_knowledge_request_operation import ManageKnowledgeRequestOperation
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawKnowledgeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[ToolExecutionResponse]:
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
        HttpResponse[ToolExecutionResponse]
            Tool execution result
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/tools/manageKnowledge",
            method="POST",
            json={
                "operation": operation,
                "content": content,
                "uri": uri,
                "metadata": metadata,
                "query": query,
                "limit": limit,
                "uriFilter": uri_filter,
                "interaction_id": interaction_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToolExecutionResponse,
                    parse_obj_as(
                        type_=ToolExecutionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_all_knowledge_base_chunks_for_a_source_identifier_used_by_controller_for_git_knowledge_source_cleanup(
        self, source_identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[KnowledgeSourceSourceIdentifierDeleteResponse]:
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
        HttpResponse[KnowledgeSourceSourceIdentifierDeleteResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/knowledge/source/{encode_path_param(source_identifier)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KnowledgeSourceSourceIdentifierDeleteResponse,
                    parse_obj_as(
                        type_=KnowledgeSourceSourceIdentifierDeleteResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ask_a_question_and_receive_an_ai_synthesized_answer_from_the_knowledge_base_uses_an_agentic_approach_that_can_search_multiple_times_with_different_phrasings_for_comprehensive_answers(
        self,
        *,
        query: str,
        limit: float,
        uri_filter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[KnowledgeAskPostResponse]:
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
        HttpResponse[KnowledgeAskPostResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/knowledge/ask",
            method="POST",
            json={
                "query": query,
                "limit": limit,
                "uriFilter": uri_filter,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KnowledgeAskPostResponse,
                    parse_obj_as(
                        type_=KnowledgeAskPostResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawKnowledgeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[ToolExecutionResponse]:
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
        AsyncHttpResponse[ToolExecutionResponse]
            Tool execution result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/tools/manageKnowledge",
            method="POST",
            json={
                "operation": operation,
                "content": content,
                "uri": uri,
                "metadata": metadata,
                "query": query,
                "limit": limit,
                "uriFilter": uri_filter,
                "interaction_id": interaction_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToolExecutionResponse,
                    parse_obj_as(
                        type_=ToolExecutionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_all_knowledge_base_chunks_for_a_source_identifier_used_by_controller_for_git_knowledge_source_cleanup(
        self, source_identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[KnowledgeSourceSourceIdentifierDeleteResponse]:
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
        AsyncHttpResponse[KnowledgeSourceSourceIdentifierDeleteResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/knowledge/source/{encode_path_param(source_identifier)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KnowledgeSourceSourceIdentifierDeleteResponse,
                    parse_obj_as(
                        type_=KnowledgeSourceSourceIdentifierDeleteResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ask_a_question_and_receive_an_ai_synthesized_answer_from_the_knowledge_base_uses_an_agentic_approach_that_can_search_multiple_times_with_different_phrasings_for_comprehensive_answers(
        self,
        *,
        query: str,
        limit: float,
        uri_filter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[KnowledgeAskPostResponse]:
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
        AsyncHttpResponse[KnowledgeAskPostResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/knowledge/ask",
            method="POST",
            json={
                "query": query,
                "limit": limit,
                "uriFilter": uri_filter,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KnowledgeAskPostResponse,
                    parse_obj_as(
                        type_=KnowledgeAskPostResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
