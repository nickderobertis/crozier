

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
from ..errors.conflict_error import ConflictError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.gone_error import GoneError
from ..errors.not_found_error import NotFoundError
from ..errors.not_implemented_error import NotImplementedError
from ..errors.range_not_satisfiable_error import RangeNotSatisfiableError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.create_download_by_inode_response import CreateDownloadByInodeResponse
from ..types.error_response import ErrorResponse
from ..types.file_revision import FileRevision
from ..types.list_file_revisions_response import ListFileRevisionsResponse
from ..types.list_inode_children_response import ListInodeChildrenResponse
from ..types.path_entry import PathEntry
from ..types.pin_id import PinId
from ..types.read_consistency import ReadConsistency
from ..types.revision_no import RevisionNo
from ..types.service_unavailable_error_body import ServiceUnavailableErrorBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawInodesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve(
        self,
        namespace_id: str,
        inode_id: str,
        *,
        include_attributes: typing.Optional[bool] = None,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PathEntry]:
        """
        Returns the path entry for a visible inode, from the current state or an unexpired snapshot. An unknown or hidden inode returns `inode_not_found`.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        inode_id : str
            The inode ID.

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
            Path entry for the inode
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/inodes/{encode_path_param(inode_id)}",
            method="GET",
            params={
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

    def list_children(
        self,
        namespace_id: str,
        inode_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        include_attributes: typing.Optional[bool] = None,
        recursive: typing.Optional[bool] = None,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[PathEntry, ListInodeChildrenResponse]:
        """
        Lists one page of a directory's children, in canonical name key order, from the current state or an unexpired snapshot. The request identifies the directory by its inode ID, so a listing and its later pages stay on the same directory even if the directory is renamed or moved at the same time.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        inode_id : str
            The directory's inode ID.

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
        SyncPager[PathEntry, ListInodeChildrenResponse]
            One page of directory children
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/inodes/{encode_path_param(inode_id)}/children",
            method="GET",
            params={
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
                    ListInodeChildrenResponse,
                    parse_obj_as(
                        type_=ListInodeChildrenResponse,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.entries
                _parsed_next = _parsed_response.next_cursor
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list_children(
                    namespace_id,
                    inode_id,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    @contextlib.contextmanager
    def content(
        self,
        namespace_id: str,
        inode_id: str,
        *,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Reads and verifies the current revision of a visible file inode, wherever the inode is bound, or the revision that an unexpired snapshot captured. A `Range` header asks for one byte range of the file instead. An unknown or hidden inode returns `inode_not_found`.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        inode_id : str
            The file's inode ID.

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
            f"v0/namespaces/{encode_path_param(namespace_id)}/inodes/{encode_path_param(inode_id)}/content",
            method="GET",
            params={
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
                    if _response.status_code == 409:
                        raise ConflictError(
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
        inode_id: str,
        *,
        consistency: typing.Optional[ReadConsistency] = OMIT,
        max_staleness_ms: typing.Optional[int] = OMIT,
        snapshot_id: typing.Optional[PinId] = OMIT,
        start_offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateDownloadByInodeResponse]:
        """
        Authorizes a direct read of the current revision of a visible file inode, wherever the inode is bound, or of the revision that an unexpired snapshot captured. The capability reads exactly `[start_offset, size_bytes)`, as on the path route. The response doesn't include a path.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        inode_id : str
            The file's inode ID.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read. It can't be combined with `snapshot_id`.

        max_staleness_ms : typing.Optional[int]
            With `consistency` set to `eventual`, how old the server's last confirmation of the head can
            be, in milliseconds. The default is the server's `max_staleness_ms`.

        snapshot_id : typing.Optional[PinId]
            A snapshot to read the file from. The download reads the revision that the snapshot
            captured.

        start_offset : typing.Optional[int]
            The first byte that the grant reads. It defaults to 0 and must be less than the file's size.
            For a file of zero bytes, it must be 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateDownloadByInodeResponse]
            Download authorized
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/inodes/{encode_path_param(inode_id)}/downloads",
            method="POST",
            json={
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
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
                    CreateDownloadByInodeResponse,
                    parse_obj_as(
                        type_=CreateDownloadByInodeResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def list_revisions(
        self,
        namespace_id: str,
        inode_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[FileRevision, ListFileRevisionsResponse]:
        """
        Returns the retained revisions of a file inode. The file doesn't need a current path.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        inode_id : str
            The file's inode ID.

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
            f"v0/namespaces/{encode_path_param(namespace_id)}/inodes/{encode_path_param(inode_id)}/revisions",
            method="GET",
            params={
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
                    inode_id,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    @contextlib.contextmanager
    def revision_content(
        self,
        namespace_id: str,
        inode_id: str,
        revision_no: RevisionNo,
        *,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Reads and verifies one retained file revision by inode ID and revision number. A `Range` header asks for one byte range of the revision instead.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        inode_id : str
            The file's inode ID.

        revision_no : RevisionNo
            The revision number.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head that it finds the revision in. `eventual`
            (the default, unless the server's `consistency` setting is `strong`) reads at the head that
            the server confirmed last while that confirmation is younger than the maximum staleness, and
            `strong` confirms the head before the read.

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
            Revision bytes
        """
        with self._client_wrapper.httpx_client.stream(
            f"v0/namespaces/{encode_path_param(namespace_id)}/inodes/{encode_path_param(inode_id)}/revisions/{encode_path_param(revision_no)}/content",
            method="GET",
            params={
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
                    if _response.status_code == 409:
                        raise ConflictError(
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

    def create_revision_download(
        self,
        namespace_id: str,
        inode_id: str,
        revision_no: RevisionNo,
        *,
        consistency: typing.Optional[ReadConsistency] = OMIT,
        max_staleness_ms: typing.Optional[int] = OMIT,
        start_offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateDownloadByInodeResponse]:
        """
        Authorizes a direct read of one retained inode revision. The capability reads exactly `[start_offset, size_bytes)`, as on the path route. The response doesn't include a path.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        inode_id : str
            The file's inode ID.

        revision_no : RevisionNo
            The revision number.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head that it finds the revision in. `eventual`
            (the default, unless the server's `consistency` setting is `strong`) reads at the head that
            the server confirmed last while that confirmation is younger than the maximum staleness,
            and `strong` confirms the head before the read.

        max_staleness_ms : typing.Optional[int]
            With `consistency` set to `eventual`, how old the server's last confirmation of the head can
            be, in milliseconds. The default is the server's `max_staleness_ms`.

        start_offset : typing.Optional[int]
            The first byte that the grant reads. It defaults to 0 and must be less than the revision's
            size. For a revision of zero bytes, it must be 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateDownloadByInodeResponse]
            Download authorized
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/inodes/{encode_path_param(inode_id)}/revisions/{encode_path_param(revision_no)}/downloads",
            method="POST",
            json={
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
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
                    CreateDownloadByInodeResponse,
                    parse_obj_as(
                        type_=CreateDownloadByInodeResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
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


class AsyncRawInodesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve(
        self,
        namespace_id: str,
        inode_id: str,
        *,
        include_attributes: typing.Optional[bool] = None,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PathEntry]:
        """
        Returns the path entry for a visible inode, from the current state or an unexpired snapshot. An unknown or hidden inode returns `inode_not_found`.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        inode_id : str
            The inode ID.

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
            Path entry for the inode
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/inodes/{encode_path_param(inode_id)}",
            method="GET",
            params={
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

    async def list_children(
        self,
        namespace_id: str,
        inode_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        include_attributes: typing.Optional[bool] = None,
        recursive: typing.Optional[bool] = None,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[PathEntry, ListInodeChildrenResponse]:
        """
        Lists one page of a directory's children, in canonical name key order, from the current state or an unexpired snapshot. The request identifies the directory by its inode ID, so a listing and its later pages stay on the same directory even if the directory is renamed or moved at the same time.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        inode_id : str
            The directory's inode ID.

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
        AsyncPager[PathEntry, ListInodeChildrenResponse]
            One page of directory children
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/inodes/{encode_path_param(inode_id)}/children",
            method="GET",
            params={
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
                    ListInodeChildrenResponse,
                    parse_obj_as(
                        type_=ListInodeChildrenResponse,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.entries
                _parsed_next = _parsed_response.next_cursor
                _has_next = _parsed_next is not None and _parsed_next != ""

                async def _get_next():
                    return await self.list_children(
                        namespace_id,
                        inode_id,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    @contextlib.asynccontextmanager
    async def content(
        self,
        namespace_id: str,
        inode_id: str,
        *,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Reads and verifies the current revision of a visible file inode, wherever the inode is bound, or the revision that an unexpired snapshot captured. A `Range` header asks for one byte range of the file instead. An unknown or hidden inode returns `inode_not_found`.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        inode_id : str
            The file's inode ID.

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
            f"v0/namespaces/{encode_path_param(namespace_id)}/inodes/{encode_path_param(inode_id)}/content",
            method="GET",
            params={
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
                    if _response.status_code == 409:
                        raise ConflictError(
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
        inode_id: str,
        *,
        consistency: typing.Optional[ReadConsistency] = OMIT,
        max_staleness_ms: typing.Optional[int] = OMIT,
        snapshot_id: typing.Optional[PinId] = OMIT,
        start_offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateDownloadByInodeResponse]:
        """
        Authorizes a direct read of the current revision of a visible file inode, wherever the inode is bound, or of the revision that an unexpired snapshot captured. The capability reads exactly `[start_offset, size_bytes)`, as on the path route. The response doesn't include a path.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        inode_id : str
            The file's inode ID.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head. `eventual` (the default, unless the
            server's `consistency` setting is `strong`) reads at the head that the server confirmed last
            while that confirmation is younger than the maximum staleness, and `strong` confirms the
            head before the read. It can't be combined with `snapshot_id`.

        max_staleness_ms : typing.Optional[int]
            With `consistency` set to `eventual`, how old the server's last confirmation of the head can
            be, in milliseconds. The default is the server's `max_staleness_ms`.

        snapshot_id : typing.Optional[PinId]
            A snapshot to read the file from. The download reads the revision that the snapshot
            captured.

        start_offset : typing.Optional[int]
            The first byte that the grant reads. It defaults to 0 and must be less than the file's size.
            For a file of zero bytes, it must be 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateDownloadByInodeResponse]
            Download authorized
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/inodes/{encode_path_param(inode_id)}/downloads",
            method="POST",
            json={
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
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
                    CreateDownloadByInodeResponse,
                    parse_obj_as(
                        type_=CreateDownloadByInodeResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def list_revisions(
        self,
        namespace_id: str,
        inode_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[FileRevision, ListFileRevisionsResponse]:
        """
        Returns the retained revisions of a file inode. The file doesn't need a current path.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        inode_id : str
            The file's inode ID.

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
            f"v0/namespaces/{encode_path_param(namespace_id)}/inodes/{encode_path_param(inode_id)}/revisions",
            method="GET",
            params={
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
                        inode_id,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    @contextlib.asynccontextmanager
    async def revision_content(
        self,
        namespace_id: str,
        inode_id: str,
        revision_no: RevisionNo,
        *,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        range: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Reads and verifies one retained file revision by inode ID and revision number. A `Range` header asks for one byte range of the revision instead.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        inode_id : str
            The file's inode ID.

        revision_no : RevisionNo
            The revision number.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head that it finds the revision in. `eventual`
            (the default, unless the server's `consistency` setting is `strong`) reads at the head that
            the server confirmed last while that confirmation is younger than the maximum staleness, and
            `strong` confirms the head before the read.

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
            Revision bytes
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v0/namespaces/{encode_path_param(namespace_id)}/inodes/{encode_path_param(inode_id)}/revisions/{encode_path_param(revision_no)}/content",
            method="GET",
            params={
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
                    if _response.status_code == 409:
                        raise ConflictError(
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

    async def create_revision_download(
        self,
        namespace_id: str,
        inode_id: str,
        revision_no: RevisionNo,
        *,
        consistency: typing.Optional[ReadConsistency] = OMIT,
        max_staleness_ms: typing.Optional[int] = OMIT,
        start_offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateDownloadByInodeResponse]:
        """
        Authorizes a direct read of one retained inode revision. The capability reads exactly `[start_offset, size_bytes)`, as on the path route. The response doesn't include a path.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        inode_id : str
            The file's inode ID.

        revision_no : RevisionNo
            The revision number.

        consistency : typing.Optional[ReadConsistency]
            How recently the read confirms the namespace head that it finds the revision in. `eventual`
            (the default, unless the server's `consistency` setting is `strong`) reads at the head that
            the server confirmed last while that confirmation is younger than the maximum staleness,
            and `strong` confirms the head before the read.

        max_staleness_ms : typing.Optional[int]
            With `consistency` set to `eventual`, how old the server's last confirmation of the head can
            be, in milliseconds. The default is the server's `max_staleness_ms`.

        start_offset : typing.Optional[int]
            The first byte that the grant reads. It defaults to 0 and must be less than the revision's
            size. For a revision of zero bytes, it must be 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateDownloadByInodeResponse]
            Download authorized
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/namespaces/{encode_path_param(namespace_id)}/inodes/{encode_path_param(inode_id)}/revisions/{encode_path_param(revision_no)}/downloads",
            method="POST",
            json={
                "consistency": consistency,
                "max_staleness_ms": max_staleness_ms,
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
                    CreateDownloadByInodeResponse,
                    parse_obj_as(
                        type_=CreateDownloadByInodeResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
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
