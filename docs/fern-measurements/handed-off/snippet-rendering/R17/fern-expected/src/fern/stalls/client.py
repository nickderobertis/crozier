

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawStallsClient, RawStallsClient
from .types.check_availability_response import CheckAvailabilityResponse


class StallsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStallsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStallsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStallsClient
        """
        return self._raw_client

    def check_availability(
        self,
        *,
        row: str,
        stall: int,
        market: typing.Optional[str] = None,
        week: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckAvailabilityResponse:
        """
        Parameters
        ----------
        row : str
            The stall row.

        stall : int

        market : typing.Optional[str]
            The market's short name.

        week : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckAvailabilityResponse
            The stall's availability.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.stalls.check_availability(
            market="riverside",
            row="B",
            stall=1,
        )
        """
        _response = self._raw_client.check_availability(
            row=row, stall=stall, market=market, week=week, request_options=request_options
        )
        return _response.data


class AsyncStallsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStallsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStallsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStallsClient
        """
        return self._raw_client

    async def check_availability(
        self,
        *,
        row: str,
        stall: int,
        market: typing.Optional[str] = None,
        week: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckAvailabilityResponse:
        """
        Parameters
        ----------
        row : str
            The stall row.

        stall : int

        market : typing.Optional[str]
            The market's short name.

        week : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckAvailabilityResponse
            The stall's availability.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.stalls.check_availability(
                market="riverside",
                row="B",
                stall=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_availability(
            row=row, stall=stall, market=market, week=week, request_options=request_options
        )
        return _response.data
