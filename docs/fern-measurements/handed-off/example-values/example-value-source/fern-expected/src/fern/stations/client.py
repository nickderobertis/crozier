

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawStationsClient, RawStationsClient


class StationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStationsClient
        """
        return self._raw_client

    def list_stations(
        self,
        *,
        codes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        A required array query parameter's example.

        Parameters
        ----------
        codes : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Stations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stations.list_stations(
            codes=["PLY", "FAL"],
        )
        """
        _response = self._raw_client.list_stations(codes=codes, request_options=request_options)
        return _response.data


class AsyncStationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStationsClient
        """
        return self._raw_client

    async def list_stations(
        self,
        *,
        codes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        A required array query parameter's example.

        Parameters
        ----------
        codes : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Stations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stations.list_stations(
                codes=["PLY", "FAL"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_stations(codes=codes, request_options=request_options)
        return _response.data
