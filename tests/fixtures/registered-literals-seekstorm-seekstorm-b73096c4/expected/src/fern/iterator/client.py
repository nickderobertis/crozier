

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.iterator_result import IteratorResult
from .raw_client import AsyncRawIteratorClient, RawIteratorClient


OMIT = typing.cast(typing.Any, ...)


class IteratorClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIteratorClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIteratorClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIteratorClient
        """
        return self._raw_client

    def document_iterator_get(
        self,
        index_id: int,
        *,
        document_id: int,
        skip: int,
        take: int,
        include_deleted: bool,
        include_document: bool,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IteratorResult:
        """
        Document iterator via GET and POST are identical, only the way parameters are passed differ.
        The document iterator allows to iterate over all document IDs and documents in the entire index, forward or backward.
        It enables efficient sequential access to every document, even in very large indexes, without running a search.
        Paging through the index works without collecting document IDs to Min-heap in size-limited RAM first.
        The iterator guarantees that only valid document IDs are returned, even though document IDs are not strictly continuous.
        Document IDs can also be fetched in batches, reducing round trips and significantly improving performance, especially when using the REST API.
        Typical use cases include index export, conversion, analytics, audits, and inspection.
        Explanation of "eventually continuous" docid:
        In SeekStorm, document IDs become continuous over time. In a multi-sharded index, each shard maintains its own document ID space.
        Because documents are distributed across shards in a non-deterministic, load-dependent way, shard-local document IDs advance at different rates.
        When these are mapped to global document IDs, temporary gaps can appear.
        As a result, simply iterating from 0 to the total document count may encounter invalid IDs near the end.
        The Document Iterator abstracts this complexity and reliably returns only valid document IDs.
        # Parameters
        - docid=None, take>0: **skip first s document IDs**, then **take next t document IDs** of an index.
        - docid=None, take<0: **skip last s document IDs**, then **take previous t document IDs** of an index.
        - docid=Some, take>0: **skip next s document IDs**, then **take next t document IDs** of an index, relative to a given document ID, with end-of-index indicator.
        - docid=Some, take<0: **skip previous s document IDs**, then **take previous t document IDs**, relative to a given document ID, with start-of-index indicator.
        - take=0: does not make sense, that defies the purpose of get_iterator.
        - The sign of take indicates the direction of iteration: positive take for forward iteration, negative take for backward iteration.
        - The skip parameter is always positive, indicating the number of document IDs to skip before taking document IDs. The skip direction is determined by the sign of take too.
        - include_document: if true, the documents are also retrieved along with their document IDs.
        Next page:     take last  docid from previous result set, skip=1, take=+page_size
        Previous page: take first docid from previous result set, skip=1, take=-page_size
        Returns an IteratorResult, consisting of the number of actually skipped document IDs, and a list of taken document IDs and documents, sorted ascending).
        Detect end/begin of index during iteration: if returned vec.len() < requested take || if returned skip <requested skip

        Parameters
        ----------
        index_id : int
            index id

        document_id : int
            document id

        skip : int
            skip document IDs

        take : int
            take document IDs

        include_deleted : bool
            include deleted document IDs in results

        include_document : bool
            include documents in results

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            fields to include in document. If not specified, all fields are included

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IteratorResult
            Document ID found, returning an IteratorResult

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apikey="YOUR_APIKEY",
        )
        client.iterator.document_iterator_get(
            index_id=1000000,
            document_id=1000000,
            skip=1000000,
            take=1000000,
            include_deleted=True,
            include_document=True,
            fields=["title", "body"],
        )
        """
        _response = self._raw_client.document_iterator_get(
            index_id,
            document_id=document_id,
            skip=skip,
            take=take,
            include_deleted=include_deleted,
            include_document=include_document,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    def document_iterator_post(
        self,
        index_id: int,
        *,
        document_id: typing.Optional[int] = OMIT,
        skip: typing.Optional[int] = OMIT,
        take: typing.Optional[int] = OMIT,
        include_deleted: typing.Optional[bool] = OMIT,
        include_document: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IteratorResult:
        """
        Document iterator via GET and POST are identical, only the way parameters are passed differ.
        The document iterator allows to iterate over all document IDs and documents in the entire index, forward or backward.
        It enables efficient sequential access to every document, even in very large indexes, without running a search.
        Paging through the index works without collecting document IDs to Min-heap in size-limited RAM first.
        The iterator guarantees that only valid document IDs are returned, even though document IDs are not strictly continuous.
        Document IDs can also be fetched in batches, reducing round trips and significantly improving performance, especially when using the REST API.
        Typical use cases include index export, conversion, analytics, audits, and inspection.
        Explanation of "eventually continuous" docid:
        In SeekStorm, document IDs become continuous over time. In a multi-sharded index, each shard maintains its own document ID space.
        Because documents are distributed across shards in a non-deterministic, load-dependent way, shard-local document IDs advance at different rates.
        When these are mapped to global document IDs, temporary gaps can appear.
        As a result, simply iterating from 0 to the total document count may encounter invalid IDs near the end.
        The Document Iterator abstracts this complexity and reliably returns only valid document IDs.
        # Parameters
        - docid=None, take>0: **skip first s document IDs**, then **take next t document IDs** of an index.
        - docid=None, take<0: **skip last s document IDs**, then **take previous t document IDs** of an index.
        - docid=Some, take>0: **skip next s document IDs**, then **take next t document IDs** of an index, relative to a given document ID, with end-of-index indicator.
        - docid=Some, take<0: **skip previous s document IDs**, then **take previous t document IDs**, relative to a given document ID, with start-of-index indicator.
        - take=0: does not make sense, that defies the purpose of get_iterator.
        - The sign of take indicates the direction of iteration: positive take for forward iteration, negative take for backward iteration.
        - The skip parameter is always positive, indicating the number of document IDs to skip before taking document IDs. The skip direction is determined by the sign of take too.
        - include_document: if true, the documents are also retrieved along with their document IDs.
        Next page:     take last  docid from previous result set, skip=1, take=+page_size
        Previous page: take first docid from previous result set, skip=1, take=-page_size
        Returns an IteratorResult, consisting of the number of actually skipped document IDs, and a list of taken document IDs and documents, sorted ascending).
        Detect end/begin of index during iteration: if returned vec.len() < requested take || if returned skip <requested skip

        Parameters
        ----------
        index_id : int
            index id

        document_id : typing.Optional[int]
            base document ID to start the iteration from
            Use None to start from the beginning (take>0) or the end (take<0) of the index
            In JSON use null for None

        skip : typing.Optional[int]
            the number of document IDs to skip

        take : typing.Optional[int]
            the number of document IDs to return
            take>0: take next t document IDs, take<0: take previous t document IDs

        include_deleted : typing.Optional[bool]
            if true, also deleted document IDs are included in the result

        include_document : typing.Optional[bool]
            if true, the documents are also retrieved along with their document IDs

        fields : typing.Optional[typing.Sequence[str]]
            which fields to return (if include_document is true, if empty then return all stored fields)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IteratorResult
            Document ID found, returning an IteratorResult

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apikey="YOUR_APIKEY",
        )
        client.iterator.document_iterator_post(
            index_id=1000000,
            skip=0,
            take=-1,
        )
        """
        _response = self._raw_client.document_iterator_post(
            index_id,
            document_id=document_id,
            skip=skip,
            take=take,
            include_deleted=include_deleted,
            include_document=include_document,
            fields=fields,
            request_options=request_options,
        )
        return _response.data


class AsyncIteratorClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIteratorClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIteratorClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIteratorClient
        """
        return self._raw_client

    async def document_iterator_get(
        self,
        index_id: int,
        *,
        document_id: int,
        skip: int,
        take: int,
        include_deleted: bool,
        include_document: bool,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IteratorResult:
        """
        Document iterator via GET and POST are identical, only the way parameters are passed differ.
        The document iterator allows to iterate over all document IDs and documents in the entire index, forward or backward.
        It enables efficient sequential access to every document, even in very large indexes, without running a search.
        Paging through the index works without collecting document IDs to Min-heap in size-limited RAM first.
        The iterator guarantees that only valid document IDs are returned, even though document IDs are not strictly continuous.
        Document IDs can also be fetched in batches, reducing round trips and significantly improving performance, especially when using the REST API.
        Typical use cases include index export, conversion, analytics, audits, and inspection.
        Explanation of "eventually continuous" docid:
        In SeekStorm, document IDs become continuous over time. In a multi-sharded index, each shard maintains its own document ID space.
        Because documents are distributed across shards in a non-deterministic, load-dependent way, shard-local document IDs advance at different rates.
        When these are mapped to global document IDs, temporary gaps can appear.
        As a result, simply iterating from 0 to the total document count may encounter invalid IDs near the end.
        The Document Iterator abstracts this complexity and reliably returns only valid document IDs.
        # Parameters
        - docid=None, take>0: **skip first s document IDs**, then **take next t document IDs** of an index.
        - docid=None, take<0: **skip last s document IDs**, then **take previous t document IDs** of an index.
        - docid=Some, take>0: **skip next s document IDs**, then **take next t document IDs** of an index, relative to a given document ID, with end-of-index indicator.
        - docid=Some, take<0: **skip previous s document IDs**, then **take previous t document IDs**, relative to a given document ID, with start-of-index indicator.
        - take=0: does not make sense, that defies the purpose of get_iterator.
        - The sign of take indicates the direction of iteration: positive take for forward iteration, negative take for backward iteration.
        - The skip parameter is always positive, indicating the number of document IDs to skip before taking document IDs. The skip direction is determined by the sign of take too.
        - include_document: if true, the documents are also retrieved along with their document IDs.
        Next page:     take last  docid from previous result set, skip=1, take=+page_size
        Previous page: take first docid from previous result set, skip=1, take=-page_size
        Returns an IteratorResult, consisting of the number of actually skipped document IDs, and a list of taken document IDs and documents, sorted ascending).
        Detect end/begin of index during iteration: if returned vec.len() < requested take || if returned skip <requested skip

        Parameters
        ----------
        index_id : int
            index id

        document_id : int
            document id

        skip : int
            skip document IDs

        take : int
            take document IDs

        include_deleted : bool
            include deleted document IDs in results

        include_document : bool
            include documents in results

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            fields to include in document. If not specified, all fields are included

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IteratorResult
            Document ID found, returning an IteratorResult

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apikey="YOUR_APIKEY",
        )


        async def main() -> None:
            await client.iterator.document_iterator_get(
                index_id=1000000,
                document_id=1000000,
                skip=1000000,
                take=1000000,
                include_deleted=True,
                include_document=True,
                fields=["title", "body"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.document_iterator_get(
            index_id,
            document_id=document_id,
            skip=skip,
            take=take,
            include_deleted=include_deleted,
            include_document=include_document,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    async def document_iterator_post(
        self,
        index_id: int,
        *,
        document_id: typing.Optional[int] = OMIT,
        skip: typing.Optional[int] = OMIT,
        take: typing.Optional[int] = OMIT,
        include_deleted: typing.Optional[bool] = OMIT,
        include_document: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IteratorResult:
        """
        Document iterator via GET and POST are identical, only the way parameters are passed differ.
        The document iterator allows to iterate over all document IDs and documents in the entire index, forward or backward.
        It enables efficient sequential access to every document, even in very large indexes, without running a search.
        Paging through the index works without collecting document IDs to Min-heap in size-limited RAM first.
        The iterator guarantees that only valid document IDs are returned, even though document IDs are not strictly continuous.
        Document IDs can also be fetched in batches, reducing round trips and significantly improving performance, especially when using the REST API.
        Typical use cases include index export, conversion, analytics, audits, and inspection.
        Explanation of "eventually continuous" docid:
        In SeekStorm, document IDs become continuous over time. In a multi-sharded index, each shard maintains its own document ID space.
        Because documents are distributed across shards in a non-deterministic, load-dependent way, shard-local document IDs advance at different rates.
        When these are mapped to global document IDs, temporary gaps can appear.
        As a result, simply iterating from 0 to the total document count may encounter invalid IDs near the end.
        The Document Iterator abstracts this complexity and reliably returns only valid document IDs.
        # Parameters
        - docid=None, take>0: **skip first s document IDs**, then **take next t document IDs** of an index.
        - docid=None, take<0: **skip last s document IDs**, then **take previous t document IDs** of an index.
        - docid=Some, take>0: **skip next s document IDs**, then **take next t document IDs** of an index, relative to a given document ID, with end-of-index indicator.
        - docid=Some, take<0: **skip previous s document IDs**, then **take previous t document IDs**, relative to a given document ID, with start-of-index indicator.
        - take=0: does not make sense, that defies the purpose of get_iterator.
        - The sign of take indicates the direction of iteration: positive take for forward iteration, negative take for backward iteration.
        - The skip parameter is always positive, indicating the number of document IDs to skip before taking document IDs. The skip direction is determined by the sign of take too.
        - include_document: if true, the documents are also retrieved along with their document IDs.
        Next page:     take last  docid from previous result set, skip=1, take=+page_size
        Previous page: take first docid from previous result set, skip=1, take=-page_size
        Returns an IteratorResult, consisting of the number of actually skipped document IDs, and a list of taken document IDs and documents, sorted ascending).
        Detect end/begin of index during iteration: if returned vec.len() < requested take || if returned skip <requested skip

        Parameters
        ----------
        index_id : int
            index id

        document_id : typing.Optional[int]
            base document ID to start the iteration from
            Use None to start from the beginning (take>0) or the end (take<0) of the index
            In JSON use null for None

        skip : typing.Optional[int]
            the number of document IDs to skip

        take : typing.Optional[int]
            the number of document IDs to return
            take>0: take next t document IDs, take<0: take previous t document IDs

        include_deleted : typing.Optional[bool]
            if true, also deleted document IDs are included in the result

        include_document : typing.Optional[bool]
            if true, the documents are also retrieved along with their document IDs

        fields : typing.Optional[typing.Sequence[str]]
            which fields to return (if include_document is true, if empty then return all stored fields)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IteratorResult
            Document ID found, returning an IteratorResult

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apikey="YOUR_APIKEY",
        )


        async def main() -> None:
            await client.iterator.document_iterator_post(
                index_id=1000000,
                skip=0,
                take=-1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.document_iterator_post(
            index_id,
            document_id=document_id,
            skip=skip,
            take=take,
            include_deleted=include_deleted,
            include_document=include_document,
            fields=fields,
            request_options=request_options,
        )
        return _response.data
