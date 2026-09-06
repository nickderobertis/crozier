

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.page_historical_event_dto import PageHistoricalEventDto
from .raw_client import AsyncRawHistoryClient, RawHistoryClient


class HistoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHistoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHistoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHistoryClient
        """
        return self._raw_client

    def get_historical_events(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageHistoricalEventDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageHistoricalEventDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.history.get_historical_events()
        """
        _response = self._raw_client.get_historical_events(
            page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data


class AsyncHistoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHistoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHistoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHistoryClient
        """
        return self._raw_client

    async def get_historical_events(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageHistoricalEventDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        page : typing.Optional[int]
            Zero-based page index (0..N)

        size : typing.Optional[int]
            The size of the page to be returned

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageHistoricalEventDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.history.get_historical_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_historical_events(
            page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data
