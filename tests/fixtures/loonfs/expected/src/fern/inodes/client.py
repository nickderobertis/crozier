

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.create_download_by_inode_response import CreateDownloadByInodeResponse
from ..types.file_revision import FileRevision
from ..types.list_file_revisions_response import ListFileRevisionsResponse
from ..types.list_inode_children_response import ListInodeChildrenResponse
from ..types.path_entry import PathEntry
from ..types.pin_id import PinId
from ..types.read_consistency import ReadConsistency
from ..types.revision_no import RevisionNo
from .raw_client import AsyncRawInodesClient, RawInodesClient


OMIT = typing.cast(typing.Any, ...)


class InodesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInodesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInodesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInodesClient
        """
        return self._raw_client

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
    ) -> PathEntry:
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
        PathEntry
            Path entry for the inode

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
        client.inodes.retrieve(
            namespace_id="namespace_id",
            inode_id="ino_123",
            snapshot_id="pin_00000000000000000001-0000000000000002",
        )
        """
        _response = self._raw_client.retrieve(
            namespace_id,
            inode_id,
            include_attributes=include_attributes,
            snapshot_id=snapshot_id,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )
        return _response.data

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
        response = client.inodes.list_children(
            namespace_id="namespace_id",
            inode_id="ino_123",
            snapshot_id="pin_00000000000000000001-0000000000000002",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_children(
            namespace_id,
            inode_id,
            limit=limit,
            cursor=cursor,
            include_attributes=include_attributes,
            recursive=recursive,
            snapshot_id=snapshot_id,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )

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
    ) -> typing.Iterator[bytes]:
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
        client.inodes.content(
            namespace_id="namespace_id",
            inode_id="inode_id",
        )
        """
        with self._raw_client.content(
            namespace_id,
            inode_id,
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
        inode_id: str,
        *,
        consistency: typing.Optional[ReadConsistency] = OMIT,
        max_staleness_ms: typing.Optional[int] = OMIT,
        snapshot_id: typing.Optional[PinId] = OMIT,
        start_offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDownloadByInodeResponse:
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
        CreateDownloadByInodeResponse
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
        client.inodes.create_download(
            namespace_id="namespace_id",
            inode_id="ino_123",
        )
        """
        _response = self._raw_client.create_download(
            namespace_id,
            inode_id,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            snapshot_id=snapshot_id,
            start_offset=start_offset,
            request_options=request_options,
        )
        return _response.data

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
        response = client.inodes.list_revisions(
            namespace_id="namespace_id",
            inode_id="ino_123",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_revisions(
            namespace_id,
            inode_id,
            limit=limit,
            cursor=cursor,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )

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
    ) -> typing.Iterator[bytes]:
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
        typing.Iterator[bytes]
            Revision bytes

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
        client.inodes.revision_content(
            namespace_id="namespace_id",
            inode_id="inode_id",
            revision_no=1000000,
        )
        """
        with self._raw_client.revision_content(
            namespace_id,
            inode_id,
            revision_no,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            range=range,
            request_options=request_options,
        ) as r:
            yield from r.data

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
    ) -> CreateDownloadByInodeResponse:
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
        CreateDownloadByInodeResponse
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
        client.inodes.create_revision_download(
            namespace_id="namespace_id",
            inode_id="ino_123",
            revision_no=1000000,
        )
        """
        _response = self._raw_client.create_revision_download(
            namespace_id,
            inode_id,
            revision_no,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            start_offset=start_offset,
            request_options=request_options,
        )
        return _response.data


class AsyncInodesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInodesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInodesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInodesClient
        """
        return self._raw_client

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
    ) -> PathEntry:
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
        PathEntry
            Path entry for the inode

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
            await client.inodes.retrieve(
                namespace_id="namespace_id",
                inode_id="ino_123",
                snapshot_id="pin_00000000000000000001-0000000000000002",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve(
            namespace_id,
            inode_id,
            include_attributes=include_attributes,
            snapshot_id=snapshot_id,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )
        return _response.data

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
            response = await client.inodes.list_children(
                namespace_id="namespace_id",
                inode_id="ino_123",
                snapshot_id="pin_00000000000000000001-0000000000000002",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_children(
            namespace_id,
            inode_id,
            limit=limit,
            cursor=cursor,
            include_attributes=include_attributes,
            recursive=recursive,
            snapshot_id=snapshot_id,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )

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
    ) -> typing.AsyncIterator[bytes]:
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
            await client.inodes.content(
                namespace_id="namespace_id",
                inode_id="inode_id",
            )


        asyncio.run(main())
        """
        async with self._raw_client.content(
            namespace_id,
            inode_id,
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
        inode_id: str,
        *,
        consistency: typing.Optional[ReadConsistency] = OMIT,
        max_staleness_ms: typing.Optional[int] = OMIT,
        snapshot_id: typing.Optional[PinId] = OMIT,
        start_offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDownloadByInodeResponse:
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
        CreateDownloadByInodeResponse
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
            await client.inodes.create_download(
                namespace_id="namespace_id",
                inode_id="ino_123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_download(
            namespace_id,
            inode_id,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            snapshot_id=snapshot_id,
            start_offset=start_offset,
            request_options=request_options,
        )
        return _response.data

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
            response = await client.inodes.list_revisions(
                namespace_id="namespace_id",
                inode_id="ino_123",
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
            inode_id,
            limit=limit,
            cursor=cursor,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )

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
    ) -> typing.AsyncIterator[bytes]:
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
        typing.AsyncIterator[bytes]
            Revision bytes

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
            await client.inodes.revision_content(
                namespace_id="namespace_id",
                inode_id="inode_id",
                revision_no=1000000,
            )


        asyncio.run(main())
        """
        async with self._raw_client.revision_content(
            namespace_id,
            inode_id,
            revision_no,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            range=range,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

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
    ) -> CreateDownloadByInodeResponse:
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
        CreateDownloadByInodeResponse
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
            await client.inodes.create_revision_download(
                namespace_id="namespace_id",
                inode_id="ino_123",
                revision_no=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_revision_download(
            namespace_id,
            inode_id,
            revision_no,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            start_offset=start_offset,
            request_options=request_options,
        )
        return _response.data
