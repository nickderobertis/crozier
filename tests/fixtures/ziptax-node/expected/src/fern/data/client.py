

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tic_response import TicResponse
from .raw_client import AsyncRawDataClient, RawDataClient
from .types.get_tic_data_request_format import GetTicDataRequestFormat


class DataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDataClient
        """
        return self._raw_client

    def get_tic_data(
        self,
        *,
        format: typing.Optional[GetTicDataRequestFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicResponse:
        """
        Returns Taxability Information Code (TIC) data

        Parameters
        ----------
        format : typing.Optional[GetTicDataRequestFormat]
            Serialization format of the response body: 'json' (default) or 'xml'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data.get_tic_data()
        """
        _response = self._raw_client.get_tic_data(format=format, request_options=request_options)
        return _response.data


class AsyncDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDataClient
        """
        return self._raw_client

    async def get_tic_data(
        self,
        *,
        format: typing.Optional[GetTicDataRequestFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicResponse:
        """
        Returns Taxability Information Code (TIC) data

        Parameters
        ----------
        format : typing.Optional[GetTicDataRequestFormat]
            Serialization format of the response body: 'json' (default) or 'xml'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data.get_tic_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tic_data(format=format, request_options=request_options)
        return _response.data
