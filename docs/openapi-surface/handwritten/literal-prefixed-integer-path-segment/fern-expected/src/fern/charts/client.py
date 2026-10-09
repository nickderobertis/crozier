

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawChartsClient, RawChartsClient


class ChartsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChartsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChartsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChartsClient
        """
        return self._raw_client

    def fetch_sheet(self, sheet: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        sheet : int

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
        client.charts.fetch_sheet(
            sheet=1,
        )
        """
        _response = self._raw_client.fetch_sheet(sheet, request_options=request_options)
        return _response.data


class AsyncChartsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChartsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChartsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChartsClient
        """
        return self._raw_client

    async def fetch_sheet(self, sheet: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        sheet : int

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
            await client.charts.fetch_sheet(
                sheet=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_sheet(sheet, request_options=request_options)
        return _response.data
