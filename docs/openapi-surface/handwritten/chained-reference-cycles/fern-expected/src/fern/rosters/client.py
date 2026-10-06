

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.roster import Roster
from .raw_client import AsyncRawRostersClient, RawRostersClient


class RostersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRostersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRostersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRostersClient
        """
        return self._raw_client

    def read_roster(self, roster_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Roster:
        """
        Parameters
        ----------
        roster_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Roster
            One crew roster.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rosters.read_roster(
            roster_id="rosterId",
        )
        """
        _response = self._raw_client.read_roster(roster_id, request_options=request_options)
        return _response.data


class AsyncRostersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRostersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRostersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRostersClient
        """
        return self._raw_client

    async def read_roster(self, roster_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Roster:
        """
        Parameters
        ----------
        roster_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Roster
            One crew roster.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rosters.read_roster(
                roster_id="rosterId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_roster(roster_id, request_options=request_options)
        return _response.data
