

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
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.iterator_result import IteratorResult
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIteratorClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[IteratorResult]:
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
        HttpResponse[IteratorResult]
            Document ID found, returning an IteratorResult
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/iterator",
            method="GET",
            params={
                "document_id": document_id,
                "skip": skip,
                "take": take,
                "include_deleted": include_deleted,
                "include_document": include_document,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IteratorResult,
                    parse_obj_as(
                        type_=IteratorResult,
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
    ) -> HttpResponse[IteratorResult]:
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
        HttpResponse[IteratorResult]
            Document ID found, returning an IteratorResult
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/iterator",
            method="POST",
            json={
                "document_id": document_id,
                "skip": skip,
                "take": take,
                "include_deleted": include_deleted,
                "include_document": include_document,
                "fields": fields,
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
                    IteratorResult,
                    parse_obj_as(
                        type_=IteratorResult,
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


class AsyncRawIteratorClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[IteratorResult]:
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
        AsyncHttpResponse[IteratorResult]
            Document ID found, returning an IteratorResult
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/iterator",
            method="GET",
            params={
                "document_id": document_id,
                "skip": skip,
                "take": take,
                "include_deleted": include_deleted,
                "include_document": include_document,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IteratorResult,
                    parse_obj_as(
                        type_=IteratorResult,
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
    ) -> AsyncHttpResponse[IteratorResult]:
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
        AsyncHttpResponse[IteratorResult]
            Document ID found, returning an IteratorResult
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/index/{encode_path_param(index_id)}/iterator",
            method="POST",
            json={
                "document_id": document_id,
                "skip": skip,
                "take": take,
                "include_deleted": include_deleted,
                "include_document": include_document,
                "fields": fields,
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
                    IteratorResult,
                    parse_obj_as(
                        type_=IteratorResult,
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
