

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.delete_snapshot_response import DeleteSnapshotResponse
from ..types.list_snapshots_response import ListSnapshotsResponse
from ..types.pin_id import PinId
from ..types.snapshot import Snapshot
from .raw_client import AsyncRawSnapshotsClient, RawSnapshotsClient


OMIT = typing.cast(typing.Any, ...)


class SnapshotsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSnapshotsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSnapshotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSnapshotsClient
        """
        return self._raw_client

    def list(
        self,
        namespace_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[Snapshot, ListSnapshotsResponse]:
        """
        Lists snapshots in snapshot ID order. An expired snapshot stays in the list until garbage collection deletes it, after its expiry plus the grace window. The list leaves out fork pins, which the maintenance checkpoint inventory lists.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        limit : typing.Optional[int]
            The maximum page size.

        cursor : typing.Optional[str]
            The opaque cursor that the previous page returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[Snapshot, ListSnapshotsResponse]
            Snapshots

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
        response = client.snapshots.list(
            namespace_id="namespace_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(namespace_id, limit=limit, cursor=cursor, request_options=request_options)

    def create(
        self,
        namespace_id: str,
        *,
        name: str,
        ttl_ms: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Snapshot:
        """
        Creates a snapshot of the current namespace state. The server first folds any WAL tail after the current manifest. Every accepted call creates a new snapshot with a new ID, and the name is a label, not a key. A snapshot with `ttl_ms` expires that many milliseconds from the server's current time, and a snapshot without it doesn't expire. The snapshot keeps its manifest until it's deleted, either explicitly or by garbage collection after it expires and its grace window passes.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        name : str
            The snapshot's label, which doesn't need to be unique.

        ttl_ms : typing.Optional[int]
            The snapshot's lifetime in milliseconds, counted from the server's current time. Omit it to
            keep the snapshot until it's deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snapshot
            Snapshot created

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
        client.snapshots.create(
            namespace_id="namespace_id",
            name="name",
        )
        """
        _response = self._raw_client.create(namespace_id, name=name, ttl_ms=ttl_ms, request_options=request_options)
        return _response.data

    def retrieve(
        self, namespace_id: str, snapshot_id: PinId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Snapshot:
        """
        Returns one snapshot, as the snapshot listing returns it, including an expired snapshot that garbage collection hasn't deleted. A missing ID, or the ID of a fork pin, returns `snapshot_not_found`.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        snapshot_id : PinId
            The snapshot ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snapshot
            Snapshot

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
        client.snapshots.retrieve(
            namespace_id="namespace_id",
            snapshot_id="pin_00000000000000000001-0000000000000002",
        )
        """
        _response = self._raw_client.retrieve(namespace_id, snapshot_id, request_options=request_options)
        return _response.data

    def delete(
        self, namespace_id: str, snapshot_id: PinId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSnapshotResponse:
        """
        Deletes a snapshot. Garbage collection can then reclaim its unreferenced manifest and runs. Deleting a missing snapshot succeeds, so repeating the request has the same result. The ID of a fork pin returns `snapshot_not_found`. Deletion stays available after the namespace is deleted.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        snapshot_id : PinId
            The snapshot ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSnapshotResponse
            Snapshot deleted, or already absent

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
        client.snapshots.delete(
            namespace_id="namespace_id",
            snapshot_id="pin_00000000000000000001-0000000000000002",
        )
        """
        _response = self._raw_client.delete(namespace_id, snapshot_id, request_options=request_options)
        return _response.data

    def extend(
        self,
        namespace_id: str,
        snapshot_id: PinId,
        *,
        ttl_ms: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Snapshot:
        """
        Moves an unexpired snapshot's expiry to `ttl_ms` from the server's current time. The expiry never moves earlier, so a snapshot without an expiry is returned unchanged. A missing or expired snapshot returns `snapshot_not_found`. Repeating the request has the same result.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        snapshot_id : PinId
            The snapshot ID.

        ttl_ms : int
            The new lifetime in milliseconds, counted from the server's current time.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snapshot
            Snapshot extended

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
        client.snapshots.extend(
            namespace_id="namespace_id",
            snapshot_id="pin_00000000000000000001-0000000000000002",
            ttl_ms=1000000,
        )
        """
        _response = self._raw_client.extend(namespace_id, snapshot_id, ttl_ms=ttl_ms, request_options=request_options)
        return _response.data


class AsyncSnapshotsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSnapshotsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSnapshotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSnapshotsClient
        """
        return self._raw_client

    async def list(
        self,
        namespace_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[Snapshot, ListSnapshotsResponse]:
        """
        Lists snapshots in snapshot ID order. An expired snapshot stays in the list until garbage collection deletes it, after its expiry plus the grace window. The list leaves out fork pins, which the maintenance checkpoint inventory lists.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        limit : typing.Optional[int]
            The maximum page size.

        cursor : typing.Optional[str]
            The opaque cursor that the previous page returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[Snapshot, ListSnapshotsResponse]
            Snapshots

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
            response = await client.snapshots.list(
                namespace_id="namespace_id",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(namespace_id, limit=limit, cursor=cursor, request_options=request_options)

    async def create(
        self,
        namespace_id: str,
        *,
        name: str,
        ttl_ms: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Snapshot:
        """
        Creates a snapshot of the current namespace state. The server first folds any WAL tail after the current manifest. Every accepted call creates a new snapshot with a new ID, and the name is a label, not a key. A snapshot with `ttl_ms` expires that many milliseconds from the server's current time, and a snapshot without it doesn't expire. The snapshot keeps its manifest until it's deleted, either explicitly or by garbage collection after it expires and its grace window passes.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        name : str
            The snapshot's label, which doesn't need to be unique.

        ttl_ms : typing.Optional[int]
            The snapshot's lifetime in milliseconds, counted from the server's current time. Omit it to
            keep the snapshot until it's deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snapshot
            Snapshot created

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
            await client.snapshots.create(
                namespace_id="namespace_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            namespace_id, name=name, ttl_ms=ttl_ms, request_options=request_options
        )
        return _response.data

    async def retrieve(
        self, namespace_id: str, snapshot_id: PinId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Snapshot:
        """
        Returns one snapshot, as the snapshot listing returns it, including an expired snapshot that garbage collection hasn't deleted. A missing ID, or the ID of a fork pin, returns `snapshot_not_found`.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        snapshot_id : PinId
            The snapshot ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snapshot
            Snapshot

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
            await client.snapshots.retrieve(
                namespace_id="namespace_id",
                snapshot_id="pin_00000000000000000001-0000000000000002",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve(namespace_id, snapshot_id, request_options=request_options)
        return _response.data

    async def delete(
        self, namespace_id: str, snapshot_id: PinId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSnapshotResponse:
        """
        Deletes a snapshot. Garbage collection can then reclaim its unreferenced manifest and runs. Deleting a missing snapshot succeeds, so repeating the request has the same result. The ID of a fork pin returns `snapshot_not_found`. Deletion stays available after the namespace is deleted.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        snapshot_id : PinId
            The snapshot ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSnapshotResponse
            Snapshot deleted, or already absent

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
            await client.snapshots.delete(
                namespace_id="namespace_id",
                snapshot_id="pin_00000000000000000001-0000000000000002",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(namespace_id, snapshot_id, request_options=request_options)
        return _response.data

    async def extend(
        self,
        namespace_id: str,
        snapshot_id: PinId,
        *,
        ttl_ms: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Snapshot:
        """
        Moves an unexpired snapshot's expiry to `ttl_ms` from the server's current time. The expiry never moves earlier, so a snapshot without an expiry is returned unchanged. A missing or expired snapshot returns `snapshot_not_found`. Repeating the request has the same result.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        snapshot_id : PinId
            The snapshot ID.

        ttl_ms : int
            The new lifetime in milliseconds, counted from the server's current time.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snapshot
            Snapshot extended

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
            await client.snapshots.extend(
                namespace_id="namespace_id",
                snapshot_id="pin_00000000000000000001-0000000000000002",
                ttl_ms=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.extend(
            namespace_id, snapshot_id, ttl_ms=ttl_ms, request_options=request_options
        )
        return _response.data
