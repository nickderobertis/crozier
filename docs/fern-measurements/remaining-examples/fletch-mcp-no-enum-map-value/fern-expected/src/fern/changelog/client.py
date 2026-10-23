

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawChangelogClient, RawChangelogClient
from .types.get_chains_chain_id_events_response import GetChainsChainIdEventsResponse


class ChangelogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChangelogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChangelogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChangelogClient
        """
        return self._raw_client

    def the_registry_changelog_every_pause_block_upgrade_multiplier_change_stale_feed_supply_residual_listing_corporate_action_and_chain_status_change_the_daemon_recorded(
        self,
        chain_id: int,
        *,
        kind: typing.Optional[str] = None,
        symbol: typing.Optional[str] = None,
        since: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChainsChainIdEventsResponse:
        """
        Public. Without `since`/`cursor`: newest first, with `kinds` (every kind the daemon can emit) and `nextCursor`. With `since` or `cursor` (an ISO instant, use the previous `nextCursor`): only newer rows, oldest first, so a consumer catches up without gaps; a `since` or `cursor` that does not parse is a 400, never a silent restart from now. `kind` matches exactly or by prefix (`registry.`, `multiplier.`) and `symbol` narrows to one token, on the newest-first read only: the cursor read returns every kind, and a consumer following a cursor filters on `kind` itself. `limit` up to 500. When the changelog is empty, `nextCursor` is the epoch, which passed back yields every event from the first.

        Parameters
        ----------
        chain_id : int

        kind : typing.Optional[str]

        symbol : typing.Optional[str]

        since : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]
            An opaque position, `${observedAt}|${id}`, as returned in `nextCursor`. Pass it back verbatim; a bare ISO instant is also accepted.

        limit : typing.Optional[int]
            A malformed value reads as the default, a larger one as the maximum

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdEventsResponse
            Events

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.changelog.the_registry_changelog_every_pause_block_upgrade_multiplier_change_stale_feed_supply_residual_listing_corporate_action_and_chain_status_change_the_daemon_recorded(
            chain_id=1,
            kind="multiplier.",
            symbol="TSLA",
            cursor="2026-09-05T11:50:43.476Z|ev_9f3256ce83b6dd98fedbe4ec",
        )
        """
        _response = self._raw_client.the_registry_changelog_every_pause_block_upgrade_multiplier_change_stale_feed_supply_residual_listing_corporate_action_and_chain_status_change_the_daemon_recorded(
            chain_id, kind=kind, symbol=symbol, since=since, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    def the_same_changelog_as_server_sent_events_each_frames_id_is_the_events_cursor_observed_at_id_so_last_event_id_or_since_resumes_without_gaps(
        self,
        chain_id: int,
        *,
        since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        chain_id : int

        since : typing.Optional[str]
            An ISO instant or a cursor `${observedAt}|${id}`; the Last-Event-ID header takes precedence. Without either the stream starts at now.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.changelog.the_same_changelog_as_server_sent_events_each_frames_id_is_the_events_cursor_observed_at_id_so_last_event_id_or_since_resumes_without_gaps(
            chain_id=1,
        )
        """
        _response = self._raw_client.the_same_changelog_as_server_sent_events_each_frames_id_is_the_events_cursor_observed_at_id_so_last_event_id_or_since_resumes_without_gaps(
            chain_id, since=since, request_options=request_options
        )
        return _response.data


class AsyncChangelogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChangelogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChangelogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChangelogClient
        """
        return self._raw_client

    async def the_registry_changelog_every_pause_block_upgrade_multiplier_change_stale_feed_supply_residual_listing_corporate_action_and_chain_status_change_the_daemon_recorded(
        self,
        chain_id: int,
        *,
        kind: typing.Optional[str] = None,
        symbol: typing.Optional[str] = None,
        since: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChainsChainIdEventsResponse:
        """
        Public. Without `since`/`cursor`: newest first, with `kinds` (every kind the daemon can emit) and `nextCursor`. With `since` or `cursor` (an ISO instant, use the previous `nextCursor`): only newer rows, oldest first, so a consumer catches up without gaps; a `since` or `cursor` that does not parse is a 400, never a silent restart from now. `kind` matches exactly or by prefix (`registry.`, `multiplier.`) and `symbol` narrows to one token, on the newest-first read only: the cursor read returns every kind, and a consumer following a cursor filters on `kind` itself. `limit` up to 500. When the changelog is empty, `nextCursor` is the epoch, which passed back yields every event from the first.

        Parameters
        ----------
        chain_id : int

        kind : typing.Optional[str]

        symbol : typing.Optional[str]

        since : typing.Optional[dt.datetime]

        cursor : typing.Optional[str]
            An opaque position, `${observedAt}|${id}`, as returned in `nextCursor`. Pass it back verbatim; a bare ISO instant is also accepted.

        limit : typing.Optional[int]
            A malformed value reads as the default, a larger one as the maximum

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdEventsResponse
            Events

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.changelog.the_registry_changelog_every_pause_block_upgrade_multiplier_change_stale_feed_supply_residual_listing_corporate_action_and_chain_status_change_the_daemon_recorded(
                chain_id=1,
                kind="multiplier.",
                symbol="TSLA",
                cursor="2026-09-05T11:50:43.476Z|ev_9f3256ce83b6dd98fedbe4ec",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.the_registry_changelog_every_pause_block_upgrade_multiplier_change_stale_feed_supply_residual_listing_corporate_action_and_chain_status_change_the_daemon_recorded(
            chain_id, kind=kind, symbol=symbol, since=since, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    async def the_same_changelog_as_server_sent_events_each_frames_id_is_the_events_cursor_observed_at_id_so_last_event_id_or_since_resumes_without_gaps(
        self,
        chain_id: int,
        *,
        since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        chain_id : int

        since : typing.Optional[str]
            An ISO instant or a cursor `${observedAt}|${id}`; the Last-Event-ID header takes precedence. Without either the stream starts at now.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.changelog.the_same_changelog_as_server_sent_events_each_frames_id_is_the_events_cursor_observed_at_id_so_last_event_id_or_since_resumes_without_gaps(
                chain_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.the_same_changelog_as_server_sent_events_each_frames_id_is_the_events_cursor_observed_at_id_so_last_event_id_or_since_resumes_without_gaps(
            chain_id, since=since, request_options=request_options
        )
        return _response.data
