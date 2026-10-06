

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_entries_request_season import ListEntriesRequestSeason
from ..types.list_entries_request_since import ListEntriesRequestSince
from ..types.list_entries_request_until import ListEntriesRequestUntil
from .raw_client import AsyncRawEntriesClient, RawEntriesClient
from .types.list_entries_request_tide import ListEntriesRequestTide


class EntriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEntriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEntriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEntriesClient
        """
        return self._raw_client

    def list_entries(
        self,
        *,
        tide: ListEntriesRequestTide,
        since: typing.Optional[ListEntriesRequestSince] = None,
        until: typing.Optional[ListEntriesRequestUntil] = None,
        season: typing.Optional[ListEntriesRequestSeason] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        tide : ListEntriesRequestTide

        since : typing.Optional[ListEntriesRequestSince]

        until : typing.Optional[ListEntriesRequestUntil]

        season : typing.Optional[ListEntriesRequestSeason]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Entries.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.entries.list_entries(
            tide=1,
        )
        """
        _response = self._raw_client.list_entries(
            tide=tide, since=since, until=until, season=season, request_options=request_options
        )
        return _response.data


class AsyncEntriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEntriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEntriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEntriesClient
        """
        return self._raw_client

    async def list_entries(
        self,
        *,
        tide: ListEntriesRequestTide,
        since: typing.Optional[ListEntriesRequestSince] = None,
        until: typing.Optional[ListEntriesRequestUntil] = None,
        season: typing.Optional[ListEntriesRequestSeason] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        tide : ListEntriesRequestTide

        since : typing.Optional[ListEntriesRequestSince]

        until : typing.Optional[ListEntriesRequestUntil]

        season : typing.Optional[ListEntriesRequestSeason]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Entries.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.entries.list_entries(
                tide=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_entries(
            tide=tide, since=since, until=until, season=season, request_options=request_options
        )
        return _response.data
