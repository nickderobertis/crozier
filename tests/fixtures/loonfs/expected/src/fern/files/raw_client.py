

import contextlib
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.pagination import AsyncPager, SyncPager
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.gone_error import GoneError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.not_implemented_error import NotImplementedError
from ..errors.range_not_satisfiable_error import RangeNotSatisfiableError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.absolute_path import AbsolutePath
from ..types.create_download_response import CreateDownloadResponse
from ..types.error_response import ErrorResponse
from ..types.file_revision import FileRevision
from ..types.grep_match import GrepMatch
from ..types.grep_response import GrepResponse
from ..types.list_file_revisions_response import ListFileRevisionsResponse
from ..types.list_path_entries_response import ListPathEntriesResponse
from ..types.path_entry import PathEntry
from ..types.pin_id import PinId
from ..types.read_consistency import ReadConsistency
from ..types.revision_no import RevisionNo
from ..types.service_unavailable_error_body import ServiceUnavailableErrorBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def content(
        self,
        namespace_id: str,
        *,
        path: str,
        revision_no: typing.Optional[RevisionNo] = None,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Returns the current file bytes, a retained revision, or the revision captured by an unexpired snapshot. A `Range` header asks for one byte range of the file instead.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        path : str
            The absolute path of the file to read.

        revision_no : typing.Optional[RevisionNo]
            An earlier revision to read. It can't be combined with `snapshot_id`.

        snapshot_id : typing.Optional[PinId]
            The snapshot whose captured file revision to read.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read. It can't be combined with `snapshot_id`.

        max_staleness_ms : typing.Optional[int]
            With `consistency=eventual`, how old the server's last confirmation of the head can be, in
            milliseconds. The default is the server's `max_staleness_ms`.

        range : typing.Optional[str]
            One byte range of the file to read instead of the whole file, as `bytes=start-end`, where `end` is the offset of the last byte, or as `bytes=start-`. An `end` past the last byte reads to the end of the file. Any other value, including a suffix range or several ranges, returns 400 `invalid_request`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            File bytes
        """
        with self._client_wrapper.httpx_client.stream(
            f"v0/namespaces/{encode_path_param(namespace_id)}/filesystem/content",
            method="GET",
            params={
                "path": path,
                "revision_no": revision_no,
                "snapshot_id": snapshot_id,
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
            },
            headers={
                "Range": str(range) if range is not None else None,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 410:
                        raise GoneError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 413:
                        raise ContentTooLargeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 416:
                        raise RangeNotSatisfiableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ServiceUnavailableErrorBody,
                                parse_obj_as(
                                    type_=ServiceUnavailableErrorBody,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def create_download(
        self,
        namespace_id: str,
        *,
        path: AbsolutePath,
        consistency: typing.Optional[ReadConsistency] = OMIT,
        max_staleness_ms: typing.Optional[int] = OMIT,
        revision_no: typing.Optional[RevisionNo] = OMIT,
        snapshot_id: typing.Optional[PinId] = OMIT,
        start_offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateDownloadResponse]:
        """
        Returns ordered, signed object ranges that cover exactly `[start_offset, size_bytes)` of the selected revision. Each range includes its signed headers in `access.headers`, and the client sends them unchanged. The client checks each range's length and the complete revision's checksum. To resume a download, a client asks for a new grant from its current offset. A deployment that can't presign URLs returns 501 `not_supported`. The proxied `GET /filesystem/content` route is still available, up to the `download.service_proxied.max_content_bytes` limit.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        path : AbsolutePath
            The absolute path of the file to read.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read. It can't be combined with `snapshot_id`.

        max_staleness_ms : typing.Optional[int]
            With `consistency` set to `eventual`, how old the server's last confirmation of the head can
            be, in milliseconds. The default is the server's `max_staleness_ms`.

        revision_no : typing.Optional[RevisionNo]
            The revision to read. Omit it to read the path's current revision. It can't be combined with
            `snapshot_id`.

        snapshot_id : typing.Optional[PinId]
            A snapshot to read the file from. The download reads the revision that the snapshot
            captured. It can't be combined with `revision_no`.

        start_offset : typing.Optional[int]
            The first byte that the grant reads. The grant covers the revision's bytes from
            `start_offset` up to `size_bytes`, so a client that resumes a download asks for a new grant
            that starts after the bytes it already has. The offset must be less than the revision's
            size. For a revision of zero bytes, it must be 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateDownloadResponse]
            Download authorized
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/filesystem/downloads",
            method="POST",
            json={
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
                "path": path,
                "revision_no": revision_no,
                "snapshot_id": snapshot_id,
                "start_offset": start_offset,
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
                    CreateDownloadResponse,
                    parse_obj_as(
                        type_=CreateDownloadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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

    def list(
        self,
        namespace_id: str,
        *,
        path: str,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        include_attributes: typing.Optional[bool] = None,
        recursive: typing.Optional[bool] = None,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[PathEntry, ListPathEntriesResponse]:
        """
        Lists a directory from the current state or an unexpired snapshot.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        path : str
            The absolute path of the directory to list.

        limit : typing.Optional[int]
            The maximum page size.

        cursor : typing.Optional[str]
            The opaque cursor that the previous page returned.

        include_attributes : typing.Optional[bool]
            Whether the response includes each entry's attribute map and attribute revision. The default
            is `false`, because a page can have many entries and each map can be up to 64 KiB.

        recursive : typing.Optional[bool]
            Whether the listing includes the directory's whole subtree, depth first, with each
            directory's entry before its descendants. The default is `false`, which lists the
            directory's children only.

        snapshot_id : typing.Optional[PinId]
            The snapshot whose captured directory state to read.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read. It can't be combined with `snapshot_id`.

        max_staleness_ms : typing.Optional[int]
            With `consistency=eventual`, how old the server's last confirmation of the head can be, in
            milliseconds. The default is the server's `max_staleness_ms`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[PathEntry, ListPathEntriesResponse]
            Directory listing page
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/filesystem/entries",
            method="GET",
            params={
                "path": path,
                "limit": limit,
                "cursor": cursor,
                "include_attributes": include_attributes,
                "recursive": recursive,
                "snapshot_id": snapshot_id,
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListPathEntriesResponse,
                    parse_obj_as(
                        type_=ListPathEntriesResponse,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.entries
                _parsed_next = _parsed_response.next_cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list(
                    namespace_id,
                    path=path,
                    limit=limit,
                    cursor=_parsed_next,
                    include_attributes=include_attributes,
                    recursive=recursive,
                    snapshot_id=snapshot_id,
                    consistency=consistency,
                    max_staleness_ms=max_staleness_ms,
                    request_options=request_options,
                )
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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

    def retrieve(
        self,
        namespace_id: str,
        *,
        path: str,
        include_attributes: typing.Optional[bool] = None,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PathEntry]:
        """
        Returns path metadata from the current state or an unexpired snapshot.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        path : str
            The absolute path to read.

        include_attributes : typing.Optional[bool]
            Whether the response includes the inode's attribute map and attribute revision. The default
            is `true`, because a stat reads one path and a map is at most 64 KiB.

        snapshot_id : typing.Optional[PinId]
            The snapshot whose captured path state to read.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read. It can't be combined with `snapshot_id`.

        max_staleness_ms : typing.Optional[int]
            With `consistency=eventual`, how old the server's last confirmation of the head can be, in
            milliseconds. The default is the server's `max_staleness_ms`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PathEntry]
            Path entry
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/filesystem/entry",
            method="GET",
            params={
                "path": path,
                "include_attributes": include_attributes,
                "snapshot_id": snapshot_id,
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PathEntry,
                    parse_obj_as(
                        type_=PathEntry,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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

    def list_revisions(
        self,
        namespace_id: str,
        *,
        path: str,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[FileRevision, ListFileRevisionsResponse]:
        """
        Resolves the current path to a file inode and returns that file's revisions. If the file might be renamed, use the inode revisions route, which identifies the file by a stable ID.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        path : str
            The absolute path of the file.

        limit : typing.Optional[int]
            The maximum page size.

        cursor : typing.Optional[str]
            The opaque cursor that the previous page returned.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read.

        max_staleness_ms : typing.Optional[int]
            With `consistency=eventual`, how old the server's last confirmation of the head can be, in
            milliseconds. The default is the server's `max_staleness_ms`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[FileRevision, ListFileRevisionsResponse]
            File revisions
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/filesystem/revisions",
            method="GET",
            params={
                "path": path,
                "limit": limit,
                "cursor": cursor,
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListFileRevisionsResponse,
                    parse_obj_as(
                        type_=ListFileRevisionsResponse,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.revisions
                _parsed_next = _parsed_response.next_cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list_revisions(
                    namespace_id,
                    path=path,
                    limit=limit,
                    cursor=_parsed_next,
                    consistency=consistency,
                    max_staleness_ms=max_staleness_ms,
                    request_options=request_options,
                )
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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

    def grep(
        self,
        namespace_id: str,
        *,
        pattern: str,
        case_insensitive: typing.Optional[bool] = None,
        path_prefix: typing.Optional[str] = None,
        inode_id: typing.Optional[str] = None,
        allow_scan: typing.Optional[bool] = None,
        allow_stale: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[GrepMatch, GrepResponse]:
        """
        Searches file content with a regular expression, using the namespace's grep index to narrow the candidates. The server checks each candidate against the full pattern and returns matches in ascending `(inode_id, byte_offset)` order. It scans every revision committed after the index watermark, unless `allow_stale` skips them. The deployment must serve grep, and the namespace must have a materialized, active grep index.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        pattern : str
            The search pattern, in the Rust `regex` crate's syntax. Its UTF-8 encoding must be at most
            1024 bytes.

        case_insensitive : typing.Optional[bool]
            Whether matching ignores case. The default is `false`.

        path_prefix : typing.Optional[str]
            A complete absolute path that limits matches to its descendants. It can't be combined with
            `inode_id`.

        inode_id : typing.Optional[str]
            An inode that limits matches to its descendants. It can't be combined with `path_prefix`.

        allow_scan : typing.Optional[bool]
            Whether a pattern with no required literal bytes can use a capped exhaustive scan. The
            default is `false`.

        allow_stale : typing.Optional[bool]
            Whether the server returns results from the index alone when the unindexed tail exceeds the
            scan budget. The default is `false`.

        limit : typing.Optional[int]
            The maximum number of matches per page.

        cursor : typing.Optional[str]
            The opaque cursor that the previous page returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[GrepMatch, GrepResponse]
            One page of matches
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/grep",
            method="GET",
            params={
                "pattern": pattern,
                "case_insensitive": case_insensitive,
                "path_prefix": path_prefix,
                "inode_id": inode_id,
                "allow_scan": allow_scan,
                "allow_stale": allow_stale,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    GrepResponse,
                    parse_obj_as(
                        type_=GrepResponse,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.matches
                _parsed_next = _parsed_response.next_cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.grep(
                    namespace_id,
                    pattern=pattern,
                    case_insensitive=case_insensitive,
                    path_prefix=path_prefix,
                    inode_id=inode_id,
                    allow_scan=allow_scan,
                    allow_stale=allow_stale,
                    limit=limit,
                    cursor=_parsed_next,
                    request_options=request_options,
                )
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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


class AsyncRawFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def content(
        self,
        namespace_id: str,
        *,
        path: str,
        revision_no: typing.Optional[RevisionNo] = None,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Returns the current file bytes, a retained revision, or the revision captured by an unexpired snapshot. A `Range` header asks for one byte range of the file instead.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        path : str
            The absolute path of the file to read.

        revision_no : typing.Optional[RevisionNo]
            An earlier revision to read. It can't be combined with `snapshot_id`.

        snapshot_id : typing.Optional[PinId]
            The snapshot whose captured file revision to read.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read. It can't be combined with `snapshot_id`.

        max_staleness_ms : typing.Optional[int]
            With `consistency=eventual`, how old the server's last confirmation of the head can be, in
            milliseconds. The default is the server's `max_staleness_ms`.

        range : typing.Optional[str]
            One byte range of the file to read instead of the whole file, as `bytes=start-end`, where `end` is the offset of the last byte, or as `bytes=start-`. An `end` past the last byte reads to the end of the file. Any other value, including a suffix range or several ranges, returns 400 `invalid_request`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            File bytes
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v0/namespaces/{encode_path_param(namespace_id)}/filesystem/content",
            method="GET",
            params={
                "path": path,
                "revision_no": revision_no,
                "snapshot_id": snapshot_id,
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
            },
            headers={
                "Range": str(range) if range is not None else None,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 410:
                        raise GoneError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 413:
                        raise ContentTooLargeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 416:
                        raise RangeNotSatisfiableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ServiceUnavailableErrorBody,
                                parse_obj_as(
                                    type_=ServiceUnavailableErrorBody,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def create_download(
        self,
        namespace_id: str,
        *,
        path: AbsolutePath,
        consistency: typing.Optional[ReadConsistency] = OMIT,
        max_staleness_ms: typing.Optional[int] = OMIT,
        revision_no: typing.Optional[RevisionNo] = OMIT,
        snapshot_id: typing.Optional[PinId] = OMIT,
        start_offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateDownloadResponse]:
        """
        Returns ordered, signed object ranges that cover exactly `[start_offset, size_bytes)` of the selected revision. Each range includes its signed headers in `access.headers`, and the client sends them unchanged. The client checks each range's length and the complete revision's checksum. To resume a download, a client asks for a new grant from its current offset. A deployment that can't presign URLs returns 501 `not_supported`. The proxied `GET /filesystem/content` route is still available, up to the `download.service_proxied.max_content_bytes` limit.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        path : AbsolutePath
            The absolute path of the file to read.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read. It can't be combined with `snapshot_id`.

        max_staleness_ms : typing.Optional[int]
            With `consistency` set to `eventual`, how old the server's last confirmation of the head can
            be, in milliseconds. The default is the server's `max_staleness_ms`.

        revision_no : typing.Optional[RevisionNo]
            The revision to read. Omit it to read the path's current revision. It can't be combined with
            `snapshot_id`.

        snapshot_id : typing.Optional[PinId]
            A snapshot to read the file from. The download reads the revision that the snapshot
            captured. It can't be combined with `revision_no`.

        start_offset : typing.Optional[int]
            The first byte that the grant reads. The grant covers the revision's bytes from
            `start_offset` up to `size_bytes`, so a client that resumes a download asks for a new grant
            that starts after the bytes it already has. The offset must be less than the revision's
            size. For a revision of zero bytes, it must be 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateDownloadResponse]
            Download authorized
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/filesystem/downloads",
            method="POST",
            json={
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
                "path": path,
                "revision_no": revision_no,
                "snapshot_id": snapshot_id,
                "start_offset": start_offset,
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
                    CreateDownloadResponse,
                    parse_obj_as(
                        type_=CreateDownloadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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

    async def list(
        self,
        namespace_id: str,
        *,
        path: str,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        include_attributes: typing.Optional[bool] = None,
        recursive: typing.Optional[bool] = None,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[PathEntry, ListPathEntriesResponse]:
        """
        Lists a directory from the current state or an unexpired snapshot.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        path : str
            The absolute path of the directory to list.

        limit : typing.Optional[int]
            The maximum page size.

        cursor : typing.Optional[str]
            The opaque cursor that the previous page returned.

        include_attributes : typing.Optional[bool]
            Whether the response includes each entry's attribute map and attribute revision. The default
            is `false`, because a page can have many entries and each map can be up to 64 KiB.

        recursive : typing.Optional[bool]
            Whether the listing includes the directory's whole subtree, depth first, with each
            directory's entry before its descendants. The default is `false`, which lists the
            directory's children only.

        snapshot_id : typing.Optional[PinId]
            The snapshot whose captured directory state to read.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read. It can't be combined with `snapshot_id`.

        max_staleness_ms : typing.Optional[int]
            With `consistency=eventual`, how old the server's last confirmation of the head can be, in
            milliseconds. The default is the server's `max_staleness_ms`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[PathEntry, ListPathEntriesResponse]
            Directory listing page
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/filesystem/entries",
            method="GET",
            params={
                "path": path,
                "limit": limit,
                "cursor": cursor,
                "include_attributes": include_attributes,
                "recursive": recursive,
                "snapshot_id": snapshot_id,
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListPathEntriesResponse,
                    parse_obj_as(
                        type_=ListPathEntriesResponse,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.entries
                _parsed_next = _parsed_response.next_cursor
                _has_next = _parsed_next is not None and _parsed_next != ""

                async def _get_next():
                    return await self.list(
                        namespace_id,
                        path=path,
                        limit=limit,
                        cursor=_parsed_next,
                        include_attributes=include_attributes,
                        recursive=recursive,
                        snapshot_id=snapshot_id,
                        consistency=consistency,
                        max_staleness_ms=max_staleness_ms,
                        request_options=request_options,
                    )

                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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

    async def retrieve(
        self,
        namespace_id: str,
        *,
        path: str,
        include_attributes: typing.Optional[bool] = None,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PathEntry]:
        """
        Returns path metadata from the current state or an unexpired snapshot.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        path : str
            The absolute path to read.

        include_attributes : typing.Optional[bool]
            Whether the response includes the inode's attribute map and attribute revision. The default
            is `true`, because a stat reads one path and a map is at most 64 KiB.

        snapshot_id : typing.Optional[PinId]
            The snapshot whose captured path state to read.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read. It can't be combined with `snapshot_id`.

        max_staleness_ms : typing.Optional[int]
            With `consistency=eventual`, how old the server's last confirmation of the head can be, in
            milliseconds. The default is the server's `max_staleness_ms`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PathEntry]
            Path entry
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/filesystem/entry",
            method="GET",
            params={
                "path": path,
                "include_attributes": include_attributes,
                "snapshot_id": snapshot_id,
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PathEntry,
                    parse_obj_as(
                        type_=PathEntry,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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

    async def list_revisions(
        self,
        namespace_id: str,
        *,
        path: str,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[FileRevision, ListFileRevisionsResponse]:
        """
        Resolves the current path to a file inode and returns that file's revisions. If the file might be renamed, use the inode revisions route, which identifies the file by a stable ID.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        path : str
            The absolute path of the file.

        limit : typing.Optional[int]
            The maximum page size.

        cursor : typing.Optional[str]
            The opaque cursor that the previous page returned.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read.

        max_staleness_ms : typing.Optional[int]
            With `consistency=eventual`, how old the server's last confirmation of the head can be, in
            milliseconds. The default is the server's `max_staleness_ms`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[FileRevision, ListFileRevisionsResponse]
            File revisions
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/filesystem/revisions",
            method="GET",
            params={
                "path": path,
                "limit": limit,
                "cursor": cursor,
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListFileRevisionsResponse,
                    parse_obj_as(
                        type_=ListFileRevisionsResponse,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.revisions
                _parsed_next = _parsed_response.next_cursor
                _has_next = _parsed_next is not None and _parsed_next != ""

                async def _get_next():
                    return await self.list_revisions(
                        namespace_id,
                        path=path,
                        limit=limit,
                        cursor=_parsed_next,
                        consistency=consistency,
                        max_staleness_ms=max_staleness_ms,
                        request_options=request_options,
                    )

                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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

    async def grep(
        self,
        namespace_id: str,
        *,
        pattern: str,
        case_insensitive: typing.Optional[bool] = None,
        path_prefix: typing.Optional[str] = None,
        inode_id: typing.Optional[str] = None,
        allow_scan: typing.Optional[bool] = None,
        allow_stale: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[GrepMatch, GrepResponse]:
        """
        Searches file content with a regular expression, using the namespace's grep index to narrow the candidates. The server checks each candidate against the full pattern and returns matches in ascending `(inode_id, byte_offset)` order. It scans every revision committed after the index watermark, unless `allow_stale` skips them. The deployment must serve grep, and the namespace must have a materialized, active grep index.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        pattern : str
            The search pattern, in the Rust `regex` crate's syntax. Its UTF-8 encoding must be at most
            1024 bytes.

        case_insensitive : typing.Optional[bool]
            Whether matching ignores case. The default is `false`.

        path_prefix : typing.Optional[str]
            A complete absolute path that limits matches to its descendants. It can't be combined with
            `inode_id`.

        inode_id : typing.Optional[str]
            An inode that limits matches to its descendants. It can't be combined with `path_prefix`.

        allow_scan : typing.Optional[bool]
            Whether a pattern with no required literal bytes can use a capped exhaustive scan. The
            default is `false`.

        allow_stale : typing.Optional[bool]
            Whether the server returns results from the index alone when the unindexed tail exceeds the
            scan budget. The default is `false`.

        limit : typing.Optional[int]
            The maximum number of matches per page.

        cursor : typing.Optional[str]
            The opaque cursor that the previous page returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[GrepMatch, GrepResponse]
            One page of matches
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/grep",
            method="GET",
            params={
                "pattern": pattern,
                "case_insensitive": case_insensitive,
                "path_prefix": path_prefix,
                "inode_id": inode_id,
                "allow_scan": allow_scan,
                "allow_stale": allow_stale,
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    GrepResponse,
                    parse_obj_as(
                        type_=GrepResponse,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.matches
                _parsed_next = _parsed_response.next_cursor
                _has_next = _parsed_next is not None and _parsed_next != ""

                async def _get_next():
                    return await self.grep(
                        namespace_id,
                        pattern=pattern,
                        case_insensitive=case_insensitive,
                        path_prefix=path_prefix,
                        inode_id=inode_id,
                        allow_scan=allow_scan,
                        allow_stale=allow_stale,
                        limit=limit,
                        cursor=_parsed_next,
                        request_options=request_options,
                    )

                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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
