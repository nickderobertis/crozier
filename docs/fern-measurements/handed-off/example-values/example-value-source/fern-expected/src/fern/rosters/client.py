

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.roster_entry import RosterEntry
from .raw_client import AsyncRawRostersClient, RawRostersClient


OMIT = typing.cast(typing.Any, ...)


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

    def add_roster_entry(
        self,
        id: str,
        *,
        watch_token: str,
        request: RosterEntry,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        A required header on an operation whose body has no worked example.

        Parameters
        ----------
        id : str

        watch_token : str

        request : RosterEntry

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rosters.add_roster_entry(
            id="id",
            watch_token="watchToken",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.add_roster_entry(
            id, watch_token=watch_token, request=request, request_options=request_options
        )
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

    async def add_roster_entry(
        self,
        id: str,
        *,
        watch_token: str,
        request: RosterEntry,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        A required header on an operation whose body has no worked example.

        Parameters
        ----------
        id : str

        watch_token : str

        request : RosterEntry

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rosters.add_roster_entry(
                id="id",
                watch_token="watchToken",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_roster_entry(
            id, watch_token=watch_token, request=request, request_options=request_options
        )
        return _response.data
