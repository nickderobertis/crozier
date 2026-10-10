

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawGalleysClient, RawGalleysClient


OMIT = typing.cast(typing.Any, ...)


class GalleysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGalleysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGalleysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGalleysClient
        """
        return self._raw_client

    def set_galley(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : str

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
        client.galleys.set_galley(
            request="head\\nbody\\tfoot",
        )
        """
        _response = self._raw_client.set_galley(request=request, request_options=request_options)
        return _response.data


class AsyncGalleysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGalleysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGalleysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGalleysClient
        """
        return self._raw_client

    async def set_galley(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : str

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
            await client.galleys.set_galley(
                request="head\\nbody\\tfoot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_galley(request=request, request_options=request_options)
        return _response.data
