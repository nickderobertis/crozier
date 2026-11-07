

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.distance_field import DistanceField
from ..types.facet_filter import FacetFilter
from ..types.highlight import Highlight
from ..types.query_facet import QueryFacet
from ..types.query_rewriting import QueryRewriting
from ..types.query_type import QueryType
from ..types.result_sort import ResultSort
from ..types.result_type import ResultType
from ..types.search_mode import SearchMode
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDocumentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def index_document(
        self,
        index_id: int,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Index a JSON document or an array of JSON documents (bulk), each consisting of arbitrary key-value pairs to the index with the specified apikey and index_id, and return the number of indexed docs.
        Index documents enables true real-time search (as opposed to near realtime.search):
        When in query_index the parameter `realtime` is set to `true` then indexed, but uncommitted documents are immediately included in the search results, without requiring a commit or refresh.
        Therefore a explicit commit_index is almost never required, as it is invoked automatically after 64k documents are indexed **per shard** or on close_index for persistence.

        Parameters
        ----------
        index_id : int
            index id

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Document indexed, returns the number of indexed documents
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/doc",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_document_by_request_object(
        self,
        index_id: int,
        *,
        query: str,
        query_vector: typing.Optional[typing.Any] = OMIT,
        enable_empty_query: typing.Optional[bool] = OMIT,
        offset: typing.Optional[int] = OMIT,
        length: typing.Optional[int] = OMIT,
        result_type: typing.Optional[ResultType] = OMIT,
        realtime: typing.Optional[bool] = OMIT,
        highlights: typing.Optional[typing.Sequence[Highlight]] = OMIT,
        field_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        distance_fields: typing.Optional[typing.Sequence[DistanceField]] = OMIT,
        query_facets: typing.Optional[typing.Sequence[QueryFacet]] = OMIT,
        facet_filter: typing.Optional[typing.Sequence[FacetFilter]] = OMIT,
        result_sort: typing.Optional[typing.Sequence[ResultSort]] = OMIT,
        query_type_default: typing.Optional[QueryType] = OMIT,
        query_rewriting: typing.Optional[QueryRewriting] = OMIT,
        search_mode: typing.Optional[SearchMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Delete document by document_id, by array of document_id (bulk), by query (SearchRequestObject) from index with index_id, or clear all documents from index.
        Immediately effective, independent of commit.
        Index space used by deleted documents is not reclaimed (until compaction is implemented), but result_count_total is updated.
        By manually deleting the delete.bin file the deleted documents can be recovered (until compaction).
        Deleted documents impact performance, especially but not limited to counting (Count, TopKCount). They also increase the size of the index (until compaction is implemented).
        For minimal query latency delete index and reindexing documents is preferred over deleting documents (until compaction is implemented).
        BM25 scores are not updated (until compaction is implemented), but the impact is minimal.
        Document ID can by obtained by search. When deleting by query (SearchRequestObject), it is advised to perform a dry run search first, to see which documents will be deleted.

        Parameters
        ----------
        index_id : int
            index id

        query : str
            Query string, search operators + - "" are recognized.

        query_vector : typing.Optional[typing.Any]
            Optional query vector: If None, then the query vector is derived from the query string using the specified model. If Some, then the query vector is used for semantic search and the query string is only used for lexical search and highlighting.

        enable_empty_query : typing.Optional[bool]
            Enable empty query: if true, an empty query string iterates through all indexed documents, supporting the query parameters: offset, length, query_facets, facet_filter, result_sort,
            otherwise an empty query string returns no results.
            Typical use cases include index browsing, index export, conversion, analytics, audits, and inspection.

        offset : typing.Optional[int]
            Offset of search results to return.

        length : typing.Optional[int]
            Number of search results to return.

        result_type : typing.Optional[ResultType]
            Specify the type of search result.

        realtime : typing.Optional[bool]
            True realtime search: include indexed, but uncommitted documents into search results.

        highlights : typing.Optional[typing.Sequence[Highlight]]
            Specify field names where to create keyword-in-context fragments and highlight query terms.

        field_filter : typing.Optional[typing.Sequence[str]]
            Specify field names where to search at querytime, whereas SchemaField.indexed is set at indextime. If empty then all indexed fields are searched.

        fields : typing.Optional[typing.Sequence[str]]
            Specify names of fields to return in the search results, where SchemaField.store is set at indextime. If empty then all stored fields are returned.

        distance_fields : typing.Optional[typing.Sequence[DistanceField]]
            Specify distance fields to derive at query time and return in the search results.

        query_facets : typing.Optional[typing.Sequence[QueryFacet]]
            Facets to return with search results: if empty then no facets are returned. Facets are only enabled on facet fields that are defined in schema at create_index!

        facet_filter : typing.Optional[typing.Sequence[FacetFilter]]
            Facet filters to filter search results by facet values: if empty then no facet filters are applied. Facet filters are only enabled on facet fields that are defined in schema at create_index!

        result_sort : typing.Optional[typing.Sequence[ResultSort]]
            Sort field and order:
            Search results are sorted by the specified facet field, either in ascending or descending order.
            If no sort field is specified, then the search results are sorted by rank in descending order per default.
            Multiple sort fields are combined by a "sort by, then sort by"-method ("tie-breaking"-algorithm).
            The results are sorted by the first field, and only for those results where the first field value is identical (tie) the results are sub-sorted by the second field,
            until the n-th field value is either not equal or the last field is reached.
            A special _score field (BM25x), reflecting how relevant the result is for a given search query (phrase match, match in title etc.) can be combined with any of the other sort fields as primary, secondary or n-th search criterium.
            Sort is only enabled on facet fields that are defined in schema at create_index!
            Examples:
            - result_sort = vec![ResultSort {field: "price".into(), order: SortOrder::Descending, base: FacetValue::None},ResultSort {field: "language".into(), order: SortOrder::Ascending, base: FacetValue::None}];
            - result_sort = vec![ResultSort {field: "location".into(),order: SortOrder::Ascending, base: FacetValue::Point(vec![38.8951, -77.0364])}];

        query_type_default : typing.Optional[QueryType]
            Specify default query type: (default=Intersection). This can be overwritten by search operator within the query string (+-"").

        query_rewriting : typing.Optional[QueryRewriting]
            Specify query rewriting method for search query correction and completion: (default=SearchOnly).

        search_mode : typing.Optional[SearchMode]
            Specify search mode: (default=Lexical).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Document deleted, returns indexed documents count
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/doc",
            method="DELETE",
            json={
                "query": query,
                "query_vector": query_vector,
                "enable_empty_query": enable_empty_query,
                "offset": offset,
                "length": length,
                "result_type": result_type,
                "realtime": realtime,
                "highlights": convert_and_respect_annotation_metadata(
                    object_=highlights, annotation=typing.Sequence[Highlight], direction="write"
                ),
                "field_filter": field_filter,
                "fields": fields,
                "distance_fields": convert_and_respect_annotation_metadata(
                    object_=distance_fields, annotation=typing.Sequence[DistanceField], direction="write"
                ),
                "query_facets": convert_and_respect_annotation_metadata(
                    object_=query_facets, annotation=typing.Sequence[QueryFacet], direction="write"
                ),
                "facet_filter": convert_and_respect_annotation_metadata(
                    object_=facet_filter, annotation=typing.Sequence[FacetFilter], direction="write"
                ),
                "result_sort": convert_and_respect_annotation_metadata(
                    object_=result_sort, annotation=typing.Sequence[ResultSort], direction="write"
                ),
                "query_type_default": query_type_default,
                "query_rewriting": convert_and_respect_annotation_metadata(
                    object_=query_rewriting, annotation=QueryRewriting, direction="write"
                ),
                "search_mode": convert_and_respect_annotation_metadata(
                    object_=search_mode, annotation=SearchMode, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_document(
        self,
        index_id: int,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Update a JSON document or an array of JSON documents (bulk), each consisting of arbitrary key-value pairs to the index with the specified apikey and index_id, and return the number of indexed docs.
        Update document is a combination of delete_document and index_document.
        All current limitations of delete_document apply.
        Update documents enables true real-time search (as opposed to near realtime.search):
        When in query_index the parameter `realtime` is set to `true` then indexed, but uncommitted documents are immediately included in the search results, without requiring a commit or refresh.
        Therefore a explicit commit_index is almost never required, as it is invoked automatically after 64k documents are indexed **per shard** or on close_index for persistence.

        Parameters
        ----------
        index_id : int
            index id

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Document indexed, returns the number of indexed documents
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/doc",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_document(
        self, index_id: int, document_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Get document from index with index_id
        ⚠️ Use search or get_iterator first to obtain a valid doc_id. Document IDs are not guaranteed to be continuous and gapless!

        Parameters
        ----------
        index_id : int
            index id

        document_id : int
            document id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Document found, returns the JSON document consisting of arbitrary key-value pairs
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/doc/{encode_path_param(document_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_document_by_parameter(
        self, index_id: int, document_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Delete document by document_id from index with index_id
        ⚠️ Use search or get_iterator first to obtain a valid doc_id. Document IDs are not guaranteed to be continuous and gapless!
        Immediately effective, independent of commit.
        Index space used by deleted documents is not reclaimed (until compaction is implemented), but result_count_total is updated.
        By manually deleting the delete.bin file the deleted documents can be recovered (until compaction).
        Deleted documents impact performance, especially but not limited to counting (Count, TopKCount). They also increase the size of the index (until compaction is implemented).
        For minimal query latency delete index and reindexing documents is preferred over deleting documents (until compaction is implemented).
        BM25 scores are not updated (until compaction is implemented), but the impact is minimal.

        Parameters
        ----------
        index_id : int
            index id

        document_id : int
            document id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Document deleted, returns indexed documents count
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/doc/{encode_path_param(document_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawDocumentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def index_document(
        self,
        index_id: int,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Index a JSON document or an array of JSON documents (bulk), each consisting of arbitrary key-value pairs to the index with the specified apikey and index_id, and return the number of indexed docs.
        Index documents enables true real-time search (as opposed to near realtime.search):
        When in query_index the parameter `realtime` is set to `true` then indexed, but uncommitted documents are immediately included in the search results, without requiring a commit or refresh.
        Therefore a explicit commit_index is almost never required, as it is invoked automatically after 64k documents are indexed **per shard** or on close_index for persistence.

        Parameters
        ----------
        index_id : int
            index id

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Document indexed, returns the number of indexed documents
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/doc",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_document_by_request_object(
        self,
        index_id: int,
        *,
        query: str,
        query_vector: typing.Optional[typing.Any] = OMIT,
        enable_empty_query: typing.Optional[bool] = OMIT,
        offset: typing.Optional[int] = OMIT,
        length: typing.Optional[int] = OMIT,
        result_type: typing.Optional[ResultType] = OMIT,
        realtime: typing.Optional[bool] = OMIT,
        highlights: typing.Optional[typing.Sequence[Highlight]] = OMIT,
        field_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        distance_fields: typing.Optional[typing.Sequence[DistanceField]] = OMIT,
        query_facets: typing.Optional[typing.Sequence[QueryFacet]] = OMIT,
        facet_filter: typing.Optional[typing.Sequence[FacetFilter]] = OMIT,
        result_sort: typing.Optional[typing.Sequence[ResultSort]] = OMIT,
        query_type_default: typing.Optional[QueryType] = OMIT,
        query_rewriting: typing.Optional[QueryRewriting] = OMIT,
        search_mode: typing.Optional[SearchMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Delete document by document_id, by array of document_id (bulk), by query (SearchRequestObject) from index with index_id, or clear all documents from index.
        Immediately effective, independent of commit.
        Index space used by deleted documents is not reclaimed (until compaction is implemented), but result_count_total is updated.
        By manually deleting the delete.bin file the deleted documents can be recovered (until compaction).
        Deleted documents impact performance, especially but not limited to counting (Count, TopKCount). They also increase the size of the index (until compaction is implemented).
        For minimal query latency delete index and reindexing documents is preferred over deleting documents (until compaction is implemented).
        BM25 scores are not updated (until compaction is implemented), but the impact is minimal.
        Document ID can by obtained by search. When deleting by query (SearchRequestObject), it is advised to perform a dry run search first, to see which documents will be deleted.

        Parameters
        ----------
        index_id : int
            index id

        query : str
            Query string, search operators + - "" are recognized.

        query_vector : typing.Optional[typing.Any]
            Optional query vector: If None, then the query vector is derived from the query string using the specified model. If Some, then the query vector is used for semantic search and the query string is only used for lexical search and highlighting.

        enable_empty_query : typing.Optional[bool]
            Enable empty query: if true, an empty query string iterates through all indexed documents, supporting the query parameters: offset, length, query_facets, facet_filter, result_sort,
            otherwise an empty query string returns no results.
            Typical use cases include index browsing, index export, conversion, analytics, audits, and inspection.

        offset : typing.Optional[int]
            Offset of search results to return.

        length : typing.Optional[int]
            Number of search results to return.

        result_type : typing.Optional[ResultType]
            Specify the type of search result.

        realtime : typing.Optional[bool]
            True realtime search: include indexed, but uncommitted documents into search results.

        highlights : typing.Optional[typing.Sequence[Highlight]]
            Specify field names where to create keyword-in-context fragments and highlight query terms.

        field_filter : typing.Optional[typing.Sequence[str]]
            Specify field names where to search at querytime, whereas SchemaField.indexed is set at indextime. If empty then all indexed fields are searched.

        fields : typing.Optional[typing.Sequence[str]]
            Specify names of fields to return in the search results, where SchemaField.store is set at indextime. If empty then all stored fields are returned.

        distance_fields : typing.Optional[typing.Sequence[DistanceField]]
            Specify distance fields to derive at query time and return in the search results.

        query_facets : typing.Optional[typing.Sequence[QueryFacet]]
            Facets to return with search results: if empty then no facets are returned. Facets are only enabled on facet fields that are defined in schema at create_index!

        facet_filter : typing.Optional[typing.Sequence[FacetFilter]]
            Facet filters to filter search results by facet values: if empty then no facet filters are applied. Facet filters are only enabled on facet fields that are defined in schema at create_index!

        result_sort : typing.Optional[typing.Sequence[ResultSort]]
            Sort field and order:
            Search results are sorted by the specified facet field, either in ascending or descending order.
            If no sort field is specified, then the search results are sorted by rank in descending order per default.
            Multiple sort fields are combined by a "sort by, then sort by"-method ("tie-breaking"-algorithm).
            The results are sorted by the first field, and only for those results where the first field value is identical (tie) the results are sub-sorted by the second field,
            until the n-th field value is either not equal or the last field is reached.
            A special _score field (BM25x), reflecting how relevant the result is for a given search query (phrase match, match in title etc.) can be combined with any of the other sort fields as primary, secondary or n-th search criterium.
            Sort is only enabled on facet fields that are defined in schema at create_index!
            Examples:
            - result_sort = vec![ResultSort {field: "price".into(), order: SortOrder::Descending, base: FacetValue::None},ResultSort {field: "language".into(), order: SortOrder::Ascending, base: FacetValue::None}];
            - result_sort = vec![ResultSort {field: "location".into(),order: SortOrder::Ascending, base: FacetValue::Point(vec![38.8951, -77.0364])}];

        query_type_default : typing.Optional[QueryType]
            Specify default query type: (default=Intersection). This can be overwritten by search operator within the query string (+-"").

        query_rewriting : typing.Optional[QueryRewriting]
            Specify query rewriting method for search query correction and completion: (default=SearchOnly).

        search_mode : typing.Optional[SearchMode]
            Specify search mode: (default=Lexical).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Document deleted, returns indexed documents count
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/doc",
            method="DELETE",
            json={
                "query": query,
                "query_vector": query_vector,
                "enable_empty_query": enable_empty_query,
                "offset": offset,
                "length": length,
                "result_type": result_type,
                "realtime": realtime,
                "highlights": convert_and_respect_annotation_metadata(
                    object_=highlights, annotation=typing.Sequence[Highlight], direction="write"
                ),
                "field_filter": field_filter,
                "fields": fields,
                "distance_fields": convert_and_respect_annotation_metadata(
                    object_=distance_fields, annotation=typing.Sequence[DistanceField], direction="write"
                ),
                "query_facets": convert_and_respect_annotation_metadata(
                    object_=query_facets, annotation=typing.Sequence[QueryFacet], direction="write"
                ),
                "facet_filter": convert_and_respect_annotation_metadata(
                    object_=facet_filter, annotation=typing.Sequence[FacetFilter], direction="write"
                ),
                "result_sort": convert_and_respect_annotation_metadata(
                    object_=result_sort, annotation=typing.Sequence[ResultSort], direction="write"
                ),
                "query_type_default": query_type_default,
                "query_rewriting": convert_and_respect_annotation_metadata(
                    object_=query_rewriting, annotation=QueryRewriting, direction="write"
                ),
                "search_mode": convert_and_respect_annotation_metadata(
                    object_=search_mode, annotation=SearchMode, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_document(
        self,
        index_id: int,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Update a JSON document or an array of JSON documents (bulk), each consisting of arbitrary key-value pairs to the index with the specified apikey and index_id, and return the number of indexed docs.
        Update document is a combination of delete_document and index_document.
        All current limitations of delete_document apply.
        Update documents enables true real-time search (as opposed to near realtime.search):
        When in query_index the parameter `realtime` is set to `true` then indexed, but uncommitted documents are immediately included in the search results, without requiring a commit or refresh.
        Therefore a explicit commit_index is almost never required, as it is invoked automatically after 64k documents are indexed **per shard** or on close_index for persistence.

        Parameters
        ----------
        index_id : int
            index id

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Document indexed, returns the number of indexed documents
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/doc",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_document(
        self, index_id: int, document_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Get document from index with index_id
        ⚠️ Use search or get_iterator first to obtain a valid doc_id. Document IDs are not guaranteed to be continuous and gapless!

        Parameters
        ----------
        index_id : int
            index id

        document_id : int
            document id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Document found, returns the JSON document consisting of arbitrary key-value pairs
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/doc/{encode_path_param(document_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_document_by_parameter(
        self, index_id: int, document_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Delete document by document_id from index with index_id
        ⚠️ Use search or get_iterator first to obtain a valid doc_id. Document IDs are not guaranteed to be continuous and gapless!
        Immediately effective, independent of commit.
        Index space used by deleted documents is not reclaimed (until compaction is implemented), but result_count_total is updated.
        By manually deleting the delete.bin file the deleted documents can be recovered (until compaction).
        Deleted documents impact performance, especially but not limited to counting (Count, TopKCount). They also increase the size of the index (until compaction is implemented).
        For minimal query latency delete index and reindexing documents is preferred over deleting documents (until compaction is implemented).
        BM25 scores are not updated (until compaction is implemented), but the impact is minimal.

        Parameters
        ----------
        index_id : int
            index id

        document_id : int
            document id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Document deleted, returns indexed documents count
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/doc/{encode_path_param(document_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
