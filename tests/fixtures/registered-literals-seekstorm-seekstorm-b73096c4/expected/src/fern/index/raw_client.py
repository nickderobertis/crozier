

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
from ..types.clustering import Clustering
from ..types.document_compression import DocumentCompression
from ..types.frequentword_type import FrequentwordType
from ..types.index_response_object import IndexResponseObject
from ..types.inference import Inference
from ..types.lexical_similarity import LexicalSimilarity
from ..types.query_completion import QueryCompletion
from ..types.schema_field import SchemaField
from ..types.spelling_correction import SpellingCorrection
from ..types.stemmer_type import StemmerType
from ..types.stopword_type import StopwordType
from ..types.synonym import Synonym
from ..types.tokenizer_type import TokenizerType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIndexClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_index(
        self,
        *,
        index_name: str,
        schema: typing.Sequence[SchemaField],
        similarity: typing.Optional[LexicalSimilarity] = OMIT,
        tokenizer: typing.Optional[TokenizerType] = OMIT,
        stemmer: typing.Optional[StemmerType] = OMIT,
        stop_words: typing.Optional[StopwordType] = OMIT,
        frequent_words: typing.Optional[FrequentwordType] = OMIT,
        ngram_indexing: typing.Optional[int] = OMIT,
        document_compression: typing.Optional[DocumentCompression] = OMIT,
        synonyms: typing.Optional[typing.Sequence[Synonym]] = OMIT,
        spelling_correction: typing.Optional[SpellingCorrection] = OMIT,
        query_completion: typing.Optional[QueryCompletion] = OMIT,
        clustering: typing.Optional[Clustering] = OMIT,
        inference: typing.Optional[Inference] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Create an index within the directory associated with the specified API key and return the index_id.

        Parameters
        ----------
        index_name : str
            Index name, used for informational purposes only.

        schema : typing.Sequence[SchemaField]
            Schema definition for the index: field name, field type, and indexing options. The schema defines how documents are indexed and searched. It specifies the fields that are indexed, stored, and used for faceting, as well as the field types and their properties. It also defines whether lexical, hybrid, or vector search is enabled for each field.

        similarity : typing.Optional[LexicalSimilarity]
            Specify similarity measure for the index: (default=Bm25fProximity). The similarity function is used to calculate the relevance score of search results for a given search query. The choice of similarity function can affect search performance and relevance, depending on the characteristics of the text being indexed and the search queries being executed.

        tokenizer : typing.Optional[TokenizerType]
            Specify tokenizer type for the index: (default=UnicodeAlphanumeric). The tokenizer is used to split text into tokens for indexing and searching. The choice of tokenizer can affect search performance and relevance, depending on the language and characteristics of the text being indexed.

        stemmer : typing.Optional[StemmerType]
            Specify stemmer

        stop_words : typing.Optional[StopwordType]
            Specify stop words for the index. Stop words are not indexed and not searched for. This can be used to reduce index size and improve search performance by excluding high-frequency, low-information terms from the index.

        frequent_words : typing.Optional[FrequentwordType]
            Specify frequent words for the index. Frequent words are used to optimize search performance for high-frequency terms.

        ngram_indexing : typing.Optional[int]
            Specify n-gram indexing for the index. N-gram indexing can improve search performance for certain types of queries.
            The n-gram set is defined as a bitwise combination of the following values:
            - NgramSet::SingleTerm = 0b00000000,,
            - NgramSet::NgramFF = 0b00000001, (Ngram frequent frequent)
            - NgramSet::NgramFR = 0b00000010, (Ngram frequent rare)
            - NgramSet::NgramRF = 0b00000011, (Ngram rare frequent)
            - NgramSet::NgramFFF = 0b00000100, (Ngram frequent frequent frequent)
            - NgramSet::NgramRFF = 0b00000101, (Ngram rare frequent frequent)
            - NgramSet::NgramFFR = 0b00000110, (Ngram frequent frequent rare)
            - NgramSet::NgramFRF = 0b00000111, (Ngram frequent rare frequent)

            For example, to enable both NgramFF and NgramFFF, set ngram_indexing to 5 (1 | 4).
            Note: enabling n-gram indexing (ngram_indexing>0) will increase index size and indexing time, but improves search performance of phrase queries with frequent terms.

        document_compression : typing.Optional[DocumentCompression]
            Enable document compression for the index. This can reduce the index size on disk and in memory, but may increase indexing and search latency. Default: Snappy compression.

        synonyms : typing.Optional[typing.Sequence[Synonym]]
            Specify synonyms for the index. Synonyms are used to expand search queries with additional terms that have the same or similar meaning, improving recall and search relevance. The multiway option specifies whether the synonym relationship is multiway (if true, all terms in the synonym set are considered synonyms of each other) or one-way (if false, only the first term in the synonym set is considered the main term, and the other terms are considered synonyms of the main term).

        spelling_correction : typing.Optional[SpellingCorrection]

        query_completion : typing.Optional[QueryCompletion]

        clustering : typing.Optional[Clustering]
            Enable clustering for vector search.

        inference : typing.Optional[Inference]
            Enable inference for search and indexing. This can be used to create vector representations of documents and queries for semantic search, e.g. by using a model like PotionBase2M.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Index created, returns the index_id
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/index",
            method="POST",
            json={
                "index_name": index_name,
                "schema": convert_and_respect_annotation_metadata(
                    object_=schema, annotation=typing.Sequence[SchemaField], direction="write"
                ),
                "similarity": similarity,
                "tokenizer": tokenizer,
                "stemmer": stemmer,
                "stop_words": convert_and_respect_annotation_metadata(
                    object_=stop_words, annotation=StopwordType, direction="write"
                ),
                "frequent_words": convert_and_respect_annotation_metadata(
                    object_=frequent_words, annotation=FrequentwordType, direction="write"
                ),
                "ngram_indexing": ngram_indexing,
                "document_compression": document_compression,
                "synonyms": convert_and_respect_annotation_metadata(
                    object_=synonyms, annotation=typing.Sequence[Synonym], direction="write"
                ),
                "spelling_correction": convert_and_respect_annotation_metadata(
                    object_=spelling_correction, annotation=typing.Optional[SpellingCorrection], direction="write"
                ),
                "query_completion": convert_and_respect_annotation_metadata(
                    object_=query_completion, annotation=typing.Optional[QueryCompletion], direction="write"
                ),
                "clustering": convert_and_respect_annotation_metadata(
                    object_=clustering, annotation=Clustering, direction="write"
                ),
                "inference": convert_and_respect_annotation_metadata(
                    object_=inference, annotation=Inference, direction="write"
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

    def get_index_info(
        self, index_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[IndexResponseObject]:
        """
        Get index Info from index with index_id

        Parameters
        ----------
        index_id : int
            index id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IndexResponseObject]
            Index found, returns the index info
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IndexResponseObject,
                    parse_obj_as(
                        type_=IndexResponseObject,
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

    def delete_index(
        self, index_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Delete an index within the directory associated with the specified API key and return the number of remaining indices.

        Parameters
        ----------
        index_id : int
            index id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Index deleted, returns the number of indices
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}",
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

    def commit_index(
        self, index_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Commit moves indexed documents from the intermediate uncompressed data structure (array lists/HashMap, queryable by realtime search) in RAM
        to the final compressed data structure (roaring bitmap) on Mmap or disk -
        which is persistent, more compact, with lower query latency and allows search with realtime=false.
        Commit is invoked automatically each time 64K documents are newly indexed **per shard** as well as on close_index (e.g. server quit).
        There is no way to prevent this automatic commit by not manually invoking it.
        But commit can also be invoked manually at any time at any number of newly indexed documents.
        commit is a **hard commit** for persistence on disk. A **soft commit** for searchability
        is invoked implicitly with every index_doc,
        i.e. the document can immediately searched and included in the search results
        if it matches the query AND the query parameter realtime=true is enabled.
        **Use commit with caution, as it is an expensive operation**.
        **Usually, there is no need to invoke it manually**, as it is invoked automatically every 64k documents **per shard** and when the index is closed with close_index.
        Before terminating the program, always call close_index (commit), otherwise all documents indexed since last (manual or automatic) commit are lost.
        There are only 2 reasons that justify a manual commit:
        1. if you want to search newly indexed documents without using realtime=true for search performance reasons or
        2. if after indexing new documents there won't be more documents indexed (for some time),
           so there won't be (soon) a commit invoked automatically at the next 64k threshold **per shard** or close_index,
           but you still need immediate persistence guarantees on disk to protect against data loss in the event of a crash.

        Parameters
        ----------
        index_id : int
            index id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Index committed, returns the number of committed documents
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}",
            method="PATCH",
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


class AsyncRawIndexClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_index(
        self,
        *,
        index_name: str,
        schema: typing.Sequence[SchemaField],
        similarity: typing.Optional[LexicalSimilarity] = OMIT,
        tokenizer: typing.Optional[TokenizerType] = OMIT,
        stemmer: typing.Optional[StemmerType] = OMIT,
        stop_words: typing.Optional[StopwordType] = OMIT,
        frequent_words: typing.Optional[FrequentwordType] = OMIT,
        ngram_indexing: typing.Optional[int] = OMIT,
        document_compression: typing.Optional[DocumentCompression] = OMIT,
        synonyms: typing.Optional[typing.Sequence[Synonym]] = OMIT,
        spelling_correction: typing.Optional[SpellingCorrection] = OMIT,
        query_completion: typing.Optional[QueryCompletion] = OMIT,
        clustering: typing.Optional[Clustering] = OMIT,
        inference: typing.Optional[Inference] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Create an index within the directory associated with the specified API key and return the index_id.

        Parameters
        ----------
        index_name : str
            Index name, used for informational purposes only.

        schema : typing.Sequence[SchemaField]
            Schema definition for the index: field name, field type, and indexing options. The schema defines how documents are indexed and searched. It specifies the fields that are indexed, stored, and used for faceting, as well as the field types and their properties. It also defines whether lexical, hybrid, or vector search is enabled for each field.

        similarity : typing.Optional[LexicalSimilarity]
            Specify similarity measure for the index: (default=Bm25fProximity). The similarity function is used to calculate the relevance score of search results for a given search query. The choice of similarity function can affect search performance and relevance, depending on the characteristics of the text being indexed and the search queries being executed.

        tokenizer : typing.Optional[TokenizerType]
            Specify tokenizer type for the index: (default=UnicodeAlphanumeric). The tokenizer is used to split text into tokens for indexing and searching. The choice of tokenizer can affect search performance and relevance, depending on the language and characteristics of the text being indexed.

        stemmer : typing.Optional[StemmerType]
            Specify stemmer

        stop_words : typing.Optional[StopwordType]
            Specify stop words for the index. Stop words are not indexed and not searched for. This can be used to reduce index size and improve search performance by excluding high-frequency, low-information terms from the index.

        frequent_words : typing.Optional[FrequentwordType]
            Specify frequent words for the index. Frequent words are used to optimize search performance for high-frequency terms.

        ngram_indexing : typing.Optional[int]
            Specify n-gram indexing for the index. N-gram indexing can improve search performance for certain types of queries.
            The n-gram set is defined as a bitwise combination of the following values:
            - NgramSet::SingleTerm = 0b00000000,,
            - NgramSet::NgramFF = 0b00000001, (Ngram frequent frequent)
            - NgramSet::NgramFR = 0b00000010, (Ngram frequent rare)
            - NgramSet::NgramRF = 0b00000011, (Ngram rare frequent)
            - NgramSet::NgramFFF = 0b00000100, (Ngram frequent frequent frequent)
            - NgramSet::NgramRFF = 0b00000101, (Ngram rare frequent frequent)
            - NgramSet::NgramFFR = 0b00000110, (Ngram frequent frequent rare)
            - NgramSet::NgramFRF = 0b00000111, (Ngram frequent rare frequent)

            For example, to enable both NgramFF and NgramFFF, set ngram_indexing to 5 (1 | 4).
            Note: enabling n-gram indexing (ngram_indexing>0) will increase index size and indexing time, but improves search performance of phrase queries with frequent terms.

        document_compression : typing.Optional[DocumentCompression]
            Enable document compression for the index. This can reduce the index size on disk and in memory, but may increase indexing and search latency. Default: Snappy compression.

        synonyms : typing.Optional[typing.Sequence[Synonym]]
            Specify synonyms for the index. Synonyms are used to expand search queries with additional terms that have the same or similar meaning, improving recall and search relevance. The multiway option specifies whether the synonym relationship is multiway (if true, all terms in the synonym set are considered synonyms of each other) or one-way (if false, only the first term in the synonym set is considered the main term, and the other terms are considered synonyms of the main term).

        spelling_correction : typing.Optional[SpellingCorrection]

        query_completion : typing.Optional[QueryCompletion]

        clustering : typing.Optional[Clustering]
            Enable clustering for vector search.

        inference : typing.Optional[Inference]
            Enable inference for search and indexing. This can be used to create vector representations of documents and queries for semantic search, e.g. by using a model like PotionBase2M.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Index created, returns the index_id
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/index",
            method="POST",
            json={
                "index_name": index_name,
                "schema": convert_and_respect_annotation_metadata(
                    object_=schema, annotation=typing.Sequence[SchemaField], direction="write"
                ),
                "similarity": similarity,
                "tokenizer": tokenizer,
                "stemmer": stemmer,
                "stop_words": convert_and_respect_annotation_metadata(
                    object_=stop_words, annotation=StopwordType, direction="write"
                ),
                "frequent_words": convert_and_respect_annotation_metadata(
                    object_=frequent_words, annotation=FrequentwordType, direction="write"
                ),
                "ngram_indexing": ngram_indexing,
                "document_compression": document_compression,
                "synonyms": convert_and_respect_annotation_metadata(
                    object_=synonyms, annotation=typing.Sequence[Synonym], direction="write"
                ),
                "spelling_correction": convert_and_respect_annotation_metadata(
                    object_=spelling_correction, annotation=typing.Optional[SpellingCorrection], direction="write"
                ),
                "query_completion": convert_and_respect_annotation_metadata(
                    object_=query_completion, annotation=typing.Optional[QueryCompletion], direction="write"
                ),
                "clustering": convert_and_respect_annotation_metadata(
                    object_=clustering, annotation=Clustering, direction="write"
                ),
                "inference": convert_and_respect_annotation_metadata(
                    object_=inference, annotation=Inference, direction="write"
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

    async def get_index_info(
        self, index_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[IndexResponseObject]:
        """
        Get index Info from index with index_id

        Parameters
        ----------
        index_id : int
            index id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IndexResponseObject]
            Index found, returns the index info
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IndexResponseObject,
                    parse_obj_as(
                        type_=IndexResponseObject,
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

    async def delete_index(
        self, index_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Delete an index within the directory associated with the specified API key and return the number of remaining indices.

        Parameters
        ----------
        index_id : int
            index id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Index deleted, returns the number of indices
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}",
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

    async def commit_index(
        self, index_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Commit moves indexed documents from the intermediate uncompressed data structure (array lists/HashMap, queryable by realtime search) in RAM
        to the final compressed data structure (roaring bitmap) on Mmap or disk -
        which is persistent, more compact, with lower query latency and allows search with realtime=false.
        Commit is invoked automatically each time 64K documents are newly indexed **per shard** as well as on close_index (e.g. server quit).
        There is no way to prevent this automatic commit by not manually invoking it.
        But commit can also be invoked manually at any time at any number of newly indexed documents.
        commit is a **hard commit** for persistence on disk. A **soft commit** for searchability
        is invoked implicitly with every index_doc,
        i.e. the document can immediately searched and included in the search results
        if it matches the query AND the query parameter realtime=true is enabled.
        **Use commit with caution, as it is an expensive operation**.
        **Usually, there is no need to invoke it manually**, as it is invoked automatically every 64k documents **per shard** and when the index is closed with close_index.
        Before terminating the program, always call close_index (commit), otherwise all documents indexed since last (manual or automatic) commit are lost.
        There are only 2 reasons that justify a manual commit:
        1. if you want to search newly indexed documents without using realtime=true for search performance reasons or
        2. if after indexing new documents there won't be more documents indexed (for some time),
           so there won't be (soon) a commit invoked automatically at the next 64k threshold **per shard** or close_index,
           but you still need immediate persistence guarantees on disk to protect against data loss in the event of a crash.

        Parameters
        ----------
        index_id : int
            index id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Index committed, returns the number of committed documents
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}",
            method="PATCH",
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
