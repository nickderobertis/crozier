

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawReadingsClient, RawReadingsClient
from .types.list_readings_request_gauges_item import ListReadingsRequestGaugesItem


class ReadingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReadingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReadingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReadingsClient
        """
        return self._raw_client

    def list_readings(
        self,
        *,
        gauges: typing.Optional[
            typing.Union[ListReadingsRequestGaugesItem, typing.Sequence[ListReadingsRequestGaugesItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[float]:
        """
        Parameters
        ----------
        gauges : typing.Optional[typing.Union[ListReadingsRequestGaugesItem, typing.Sequence[ListReadingsRequestGaugesItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[float]
            Readings.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.readings.list_readings()
        """
        _response = self._raw_client.list_readings(gauges=gauges, request_options=request_options)
        return _response.data


class AsyncReadingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReadingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReadingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReadingsClient
        """
        return self._raw_client

    async def list_readings(
        self,
        *,
        gauges: typing.Optional[
            typing.Union[ListReadingsRequestGaugesItem, typing.Sequence[ListReadingsRequestGaugesItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[float]:
        """
        Parameters
        ----------
        gauges : typing.Optional[typing.Union[ListReadingsRequestGaugesItem, typing.Sequence[ListReadingsRequestGaugesItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[float]
            Readings.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.readings.list_readings()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_readings(gauges=gauges, request_options=request_options)
        return _response.data
