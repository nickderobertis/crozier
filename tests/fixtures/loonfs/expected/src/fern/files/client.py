

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.absolute_path import AbsolutePath
from ..types.create_download_response import CreateDownloadResponse
from ..types.file_revision import FileRevision
from ..types.grep_match import GrepMatch
from ..types.grep_response import GrepResponse
from ..types.list_file_revisions_response import ListFileRevisionsResponse
from ..types.list_path_entries_response import ListPathEntriesResponse
from ..types.path_entry import PathEntry
from ..types.pin_id import PinId
from ..types.read_consistency import ReadConsistency
from ..types.revision_no import RevisionNo
from .raw_client import AsyncRawFilesClient, RawFilesClient


OMIT = typing.cast(typing.Any, ...)


class FilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFilesClient
        """
        return self._raw_client

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
    ) -> typing.Iterator[bytes]:
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
        typing.Iterator[bytes]
            File bytes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.content(
            namespace_id="namespace_id",
            path="path",
        )
        """
        with self._raw_client.content(
            namespace_id,
            path=path,
            revision_no=revision_no,
            snapshot_id=snapshot_id,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            range=range,
            request_options=request_options,
        ) as r:
            yield from r.data

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
    ) -> CreateDownloadResponse:
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
        CreateDownloadResponse
            Download authorized

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.create_download(
            namespace_id="namespace_id",
            path="/docs/report.txt",
        )
        """
        _response = self._raw_client.create_download(
            namespace_id,
            path=path,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            revision_no=revision_no,
            snapshot_id=snapshot_id,
            start_offset=start_offset,
            request_options=request_options,
        )
        return _response.data

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

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.files.list(
            namespace_id="namespace_id",
            path="path",
            snapshot_id="pin_00000000000000000001-0000000000000002",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(
            namespace_id,
            path=path,
            limit=limit,
            cursor=cursor,
            include_attributes=include_attributes,
            recursive=recursive,
            snapshot_id=snapshot_id,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )

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
    ) -> PathEntry:
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
        PathEntry
            Path entry

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.files.retrieve(
            namespace_id="namespace_id",
            path="path",
            snapshot_id="pin_00000000000000000001-0000000000000002",
        )
        """
        _response = self._raw_client.retrieve(
            namespace_id,
            path=path,
            include_attributes=include_attributes,
            snapshot_id=snapshot_id,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )
        return _response.data

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

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.files.list_revisions(
            namespace_id="namespace_id",
            path="path",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_revisions(
            namespace_id,
            path=path,
            limit=limit,
            cursor=cursor,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )

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

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.files.grep(
            namespace_id="namespace_id",
            pattern="pattern",
            inode_id="ino_123",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.grep(
            namespace_id,
            pattern=pattern,
            case_insensitive=case_insensitive,
            path_prefix=path_prefix,
            inode_id=inode_id,
            allow_scan=allow_scan,
            allow_stale=allow_stale,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        )


class AsyncFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFilesClient
        """
        return self._raw_client

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
    ) -> typing.AsyncIterator[bytes]:
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
        typing.AsyncIterator[bytes]
            File bytes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.content(
                namespace_id="namespace_id",
                path="path",
            )


        asyncio.run(main())
        """
        async with self._raw_client.content(
            namespace_id,
            path=path,
            revision_no=revision_no,
            snapshot_id=snapshot_id,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            range=range,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

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
    ) -> CreateDownloadResponse:
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
        CreateDownloadResponse
            Download authorized

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.create_download(
                namespace_id="namespace_id",
                path="/docs/report.txt",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_download(
            namespace_id,
            path=path,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            revision_no=revision_no,
            snapshot_id=snapshot_id,
            start_offset=start_offset,
            request_options=request_options,
        )
        return _response.data

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

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.files.list(
                namespace_id="namespace_id",
                path="path",
                snapshot_id="pin_00000000000000000001-0000000000000002",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(
            namespace_id,
            path=path,
            limit=limit,
            cursor=cursor,
            include_attributes=include_attributes,
            recursive=recursive,
            snapshot_id=snapshot_id,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )

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
    ) -> PathEntry:
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
        PathEntry
            Path entry

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.files.retrieve(
                namespace_id="namespace_id",
                path="path",
                snapshot_id="pin_00000000000000000001-0000000000000002",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve(
            namespace_id,
            path=path,
            include_attributes=include_attributes,
            snapshot_id=snapshot_id,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )
        return _response.data

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

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.files.list_revisions(
                namespace_id="namespace_id",
                path="path",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_revisions(
            namespace_id,
            path=path,
            limit=limit,
            cursor=cursor,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )

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

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.files.grep(
                namespace_id="namespace_id",
                pattern="pattern",
                inode_id="ino_123",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.grep(
            namespace_id,
            pattern=pattern,
            case_insensitive=case_insensitive,
            path_prefix=path_prefix,
            inode_id=inode_id,
            allow_scan=allow_scan,
            allow_stale=allow_stale,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        )
