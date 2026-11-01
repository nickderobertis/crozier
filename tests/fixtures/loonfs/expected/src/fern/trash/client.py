

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.list_trash_response import ListTrashResponse
from ..types.read_consistency import ReadConsistency
from ..types.trash_entry import TrashEntry
from .raw_client import AsyncRawTrashClient, RawTrashClient


class TrashClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTrashClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTrashClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTrashClient
        """
        return self._raw_client

    def list(
        self,
        namespace_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[TrashEntry, ListTrashResponse]:
        """
        Returns the namespace's recoverable deletions, oldest first. A deletion leaves the list when it's undeleted, or when the namespace's writer expires it after the retention floor reaches its `deletion_seq`. Each entry includes the inode ID and deletion sequence that an undelete needs, and the directory binding that the delete removed.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

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
        SyncPager[TrashEntry, ListTrashResponse]
            Recoverable deletions

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
        response = client.trash.list(
            namespace_id="namespace_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(
            namespace_id,
            limit=limit,
            cursor=cursor,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )


class AsyncTrashClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTrashClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTrashClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTrashClient
        """
        return self._raw_client

    async def list(
        self,
        namespace_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[TrashEntry, ListTrashResponse]:
        """
        Returns the namespace's recoverable deletions, oldest first. A deletion leaves the list when it's undeleted, or when the namespace's writer expires it after the retention floor reaches its `deletion_seq`. Each entry includes the inode ID and deletion sequence that an undelete needs, and the directory binding that the delete removed.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

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
        AsyncPager[TrashEntry, ListTrashResponse]
            Recoverable deletions

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
            response = await client.trash.list(
                namespace_id="namespace_id",
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
            limit=limit,
            cursor=cursor,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )
