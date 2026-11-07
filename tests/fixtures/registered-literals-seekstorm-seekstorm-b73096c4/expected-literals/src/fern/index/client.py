

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawIndexClient, RawIndexClient


OMIT = typing.cast(typing.Any, ...)


class IndexClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIndexClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIndexClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIndexClient
        """
        return self._raw_client

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
    ) -> str:
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
        str
            Index created, returns the index_id

        Examples
        --------
        from fern import FernApi, SchemaField

        client = FernApi(
            apikey="YOUR_APIKEY",
        )
        client.index.create_index(
            index_name="index_name",
            schema=[
                SchemaField(
                    field="field",
                    store=True,
                    index_lexical=True,
                    field_type="U8",
                ),
                SchemaField(
                    field="field",
                    store=True,
                    index_lexical=True,
                    field_type="U8",
                ),
            ],
        )
        """
        _response = self._raw_client.create_index(
            index_name=index_name,
            schema=schema,
            similarity=similarity,
            tokenizer=tokenizer,
            stemmer=stemmer,
            stop_words=stop_words,
            frequent_words=frequent_words,
            ngram_indexing=ngram_indexing,
            document_compression=document_compression,
            synonyms=synonyms,
            spelling_correction=spelling_correction,
            query_completion=query_completion,
            clustering=clustering,
            inference=inference,
            request_options=request_options,
        )
        return _response.data

    def get_index_info(
        self, index_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> IndexResponseObject:
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
        IndexResponseObject
            Index found, returns the index info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apikey="YOUR_APIKEY",
        )
        client.index.get_index_info(
            index_id=1000000,
        )
        """
        _response = self._raw_client.get_index_info(index_id, request_options=request_options)
        return _response.data

    def delete_index(self, index_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
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
        str
            Index deleted, returns the number of indices

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apikey="YOUR_APIKEY",
        )
        client.index.delete_index(
            index_id=1000000,
        )
        """
        _response = self._raw_client.delete_index(index_id, request_options=request_options)
        return _response.data

    def commit_index(self, index_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
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
        str
            Index committed, returns the number of committed documents

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apikey="YOUR_APIKEY",
        )
        client.index.commit_index(
            index_id=1000000,
        )
        """
        _response = self._raw_client.commit_index(index_id, request_options=request_options)
        return _response.data


class AsyncIndexClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIndexClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIndexClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIndexClient
        """
        return self._raw_client

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
    ) -> str:
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
        str
            Index created, returns the index_id

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SchemaField

        client = AsyncFernApi(
            apikey="YOUR_APIKEY",
        )


        async def main() -> None:
            await client.index.create_index(
                index_name="index_name",
                schema=[
                    SchemaField(
                        field="field",
                        store=True,
                        index_lexical=True,
                        field_type="U8",
                    ),
                    SchemaField(
                        field="field",
                        store=True,
                        index_lexical=True,
                        field_type="U8",
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_index(
            index_name=index_name,
            schema=schema,
            similarity=similarity,
            tokenizer=tokenizer,
            stemmer=stemmer,
            stop_words=stop_words,
            frequent_words=frequent_words,
            ngram_indexing=ngram_indexing,
            document_compression=document_compression,
            synonyms=synonyms,
            spelling_correction=spelling_correction,
            query_completion=query_completion,
            clustering=clustering,
            inference=inference,
            request_options=request_options,
        )
        return _response.data

    async def get_index_info(
        self, index_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> IndexResponseObject:
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
        IndexResponseObject
            Index found, returns the index info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apikey="YOUR_APIKEY",
        )


        async def main() -> None:
            await client.index.get_index_info(
                index_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_index_info(index_id, request_options=request_options)
        return _response.data

    async def delete_index(self, index_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
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
        str
            Index deleted, returns the number of indices

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apikey="YOUR_APIKEY",
        )


        async def main() -> None:
            await client.index.delete_index(
                index_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_index(index_id, request_options=request_options)
        return _response.data

    async def commit_index(self, index_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
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
        str
            Index committed, returns the number of committed documents

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apikey="YOUR_APIKEY",
        )


        async def main() -> None:
            await client.index.commit_index(
                index_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.commit_index(index_id, request_options=request_options)
        return _response.data
