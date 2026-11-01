

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPlatesClient, RawPlatesClient


class PlatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPlatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPlatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPlatesClient
        """
        return self._raw_client

    def list_plates(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Photographic plates.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.plates.list_plates()
        """
        _response = self._raw_client.list_plates(request_options=request_options)
        return _response.data

    def flag_plate(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The flagged plate.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.plates.flag_plate()
        """
        _response = self._raw_client.flag_plate(request_options=request_options)
        return _response.data


class AsyncPlatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPlatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPlatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPlatesClient
        """
        return self._raw_client

    async def list_plates(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Photographic plates.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.plates.list_plates()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_plates(request_options=request_options)
        return _response.data

    async def flag_plate(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The flagged plate.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.plates.flag_plate()


        asyncio.run(main())
        """
        _response = await self._raw_client.flag_plate(request_options=request_options)
        return _response.data
