

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.change_seq import ChangeSeq
from ..types.list_changes_response import ListChangesResponse
from ..types.pin_id import PinId
from ..types.read_consistency import ReadConsistency
from .raw_client import AsyncRawChangesClient, RawChangesClient


class ChangesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChangesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChangesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChangesClient
        """
        return self._raw_client

    def list(
        self,
        namespace_id: str,
        *,
        after_seq: ChangeSeq,
        limit: typing.Optional[int] = None,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListChangesResponse:
        """
        Returns committed changes after a sequence. A snapshot limits the feed to its captured sequence.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        after_seq : ChangeSeq
            The sequence after which to return committed changes.

        limit : typing.Optional[int]
            The maximum page size.

        snapshot_id : typing.Optional[PinId]
            A snapshot to read the feed from. The feed ends at the sequence that the snapshot captured.

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
        ListChangesResponse
            Committed changes

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
        client.changes.list(
            namespace_id="namespace_id",
            after_seq=1000000,
            snapshot_id="pin_00000000000000000001-0000000000000002",
        )
        """
        _response = self._raw_client.list(
            namespace_id,
            after_seq=after_seq,
            limit=limit,
            snapshot_id=snapshot_id,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )
        return _response.data


class AsyncChangesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChangesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChangesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChangesClient
        """
        return self._raw_client

    async def list(
        self,
        namespace_id: str,
        *,
        after_seq: ChangeSeq,
        limit: typing.Optional[int] = None,
        snapshot_id: typing.Optional[PinId] = None,
        consistency: typing.Optional[ReadConsistency] = None,
        max_staleness_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListChangesResponse:
        """
        Returns committed changes after a sequence. A snapshot limits the feed to its captured sequence.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        after_seq : ChangeSeq
            The sequence after which to return committed changes.

        limit : typing.Optional[int]
            The maximum page size.

        snapshot_id : typing.Optional[PinId]
            A snapshot to read the feed from. The feed ends at the sequence that the snapshot captured.

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
        ListChangesResponse
            Committed changes

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
            await client.changes.list(
                namespace_id="namespace_id",
                after_seq=1000000,
                snapshot_id="pin_00000000000000000001-0000000000000002",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            namespace_id,
            after_seq=after_seq,
            limit=limit,
            snapshot_id=snapshot_id,
            consistency=consistency,
            max_staleness_ms=max_staleness_ms,
            request_options=request_options,
        )
        return _response.data
