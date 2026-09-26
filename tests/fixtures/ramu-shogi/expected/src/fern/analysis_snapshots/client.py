

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.analysis_snapshot_entry import AnalysisSnapshotEntry
from ..types.create_analysis_snapshot_response import CreateAnalysisSnapshotResponse
from ..types.get_analysis_snapshot_response import GetAnalysisSnapshotResponse
from ..types.json_value import JsonValue
from ..types.list_analysis_snapshots_response import ListAnalysisSnapshotsResponse
from .raw_client import AsyncRawAnalysisSnapshotsClient, RawAnalysisSnapshotsClient


OMIT = typing.cast(typing.Any, ...)


class AnalysisSnapshotsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAnalysisSnapshotsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAnalysisSnapshotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAnalysisSnapshotsClient
        """
        return self._raw_client

    def list_analysis_snapshots(
        self, game_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAnalysisSnapshotsResponse:
        """
        Parameters
        ----------
        game_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAnalysisSnapshotsResponse
            List analysis snapshots

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.analysis_snapshots.list_analysis_snapshots(
            game_id="gameId",
        )
        """
        _response = self._raw_client.list_analysis_snapshots(game_id, request_options=request_options)
        return _response.data

    def create_analysis_snapshot(
        self,
        game_id: str,
        *,
        line_moves: typing.Sequence[str],
        entries: typing.Sequence[AnalysisSnapshotEntry],
        label: typing.Optional[str] = OMIT,
        analysis_settings: typing.Optional[JsonValue] = OMIT,
        metadata: typing.Optional[JsonValue] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAnalysisSnapshotResponse:
        """
        Parameters
        ----------
        game_id : str

        line_moves : typing.Sequence[str]

        entries : typing.Sequence[AnalysisSnapshotEntry]

        label : typing.Optional[str]

        analysis_settings : typing.Optional[JsonValue]

        metadata : typing.Optional[JsonValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAnalysisSnapshotResponse
            Created analysis snapshot

        Examples
        --------
        from fern import AnalysisSnapshotEntry, FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.analysis_snapshots.create_analysis_snapshot(
            game_id="gameId",
            line_moves=["lineMoves"],
            entries=[
                AnalysisSnapshotEntry(
                    ply=1,
                )
            ],
        )
        """
        _response = self._raw_client.create_analysis_snapshot(
            game_id,
            line_moves=line_moves,
            entries=entries,
            label=label,
            analysis_settings=analysis_settings,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    def get_analysis_snapshot(
        self, game_id: str, snapshot_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAnalysisSnapshotResponse:
        """
        Parameters
        ----------
        game_id : str

        snapshot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAnalysisSnapshotResponse
            Get analysis snapshot

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.analysis_snapshots.get_analysis_snapshot(
            game_id="gameId",
            snapshot_id="snapshotId",
        )
        """
        _response = self._raw_client.get_analysis_snapshot(game_id, snapshot_id, request_options=request_options)
        return _response.data


class AsyncAnalysisSnapshotsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAnalysisSnapshotsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAnalysisSnapshotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAnalysisSnapshotsClient
        """
        return self._raw_client

    async def list_analysis_snapshots(
        self, game_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAnalysisSnapshotsResponse:
        """
        Parameters
        ----------
        game_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAnalysisSnapshotsResponse
            List analysis snapshots

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.analysis_snapshots.list_analysis_snapshots(
                game_id="gameId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_analysis_snapshots(game_id, request_options=request_options)
        return _response.data

    async def create_analysis_snapshot(
        self,
        game_id: str,
        *,
        line_moves: typing.Sequence[str],
        entries: typing.Sequence[AnalysisSnapshotEntry],
        label: typing.Optional[str] = OMIT,
        analysis_settings: typing.Optional[JsonValue] = OMIT,
        metadata: typing.Optional[JsonValue] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAnalysisSnapshotResponse:
        """
        Parameters
        ----------
        game_id : str

        line_moves : typing.Sequence[str]

        entries : typing.Sequence[AnalysisSnapshotEntry]

        label : typing.Optional[str]

        analysis_settings : typing.Optional[JsonValue]

        metadata : typing.Optional[JsonValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAnalysisSnapshotResponse
            Created analysis snapshot

        Examples
        --------
        import asyncio

        from fern import AnalysisSnapshotEntry, AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.analysis_snapshots.create_analysis_snapshot(
                game_id="gameId",
                line_moves=["lineMoves"],
                entries=[
                    AnalysisSnapshotEntry(
                        ply=1,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_analysis_snapshot(
            game_id,
            line_moves=line_moves,
            entries=entries,
            label=label,
            analysis_settings=analysis_settings,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    async def get_analysis_snapshot(
        self, game_id: str, snapshot_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAnalysisSnapshotResponse:
        """
        Parameters
        ----------
        game_id : str

        snapshot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAnalysisSnapshotResponse
            Get analysis snapshot

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.analysis_snapshots.get_analysis_snapshot(
                game_id="gameId",
                snapshot_id="snapshotId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_analysis_snapshot(game_id, snapshot_id, request_options=request_options)
        return _response.data
