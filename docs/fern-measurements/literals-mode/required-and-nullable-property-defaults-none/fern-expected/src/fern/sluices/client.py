

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.sluice import Sluice
from .raw_client import AsyncRawSluicesClient, RawSluicesClient


class SluicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSluicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSluicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSluicesClient
        """
        return self._raw_client

    def fetch_sluice(self, sluice_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Sluice:
        """
        Parameters
        ----------
        sluice_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Sluice
            The sluice.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.sluices.fetch_sluice(
            sluice_id="sluiceId",
        )
        """
        _response = self._raw_client.fetch_sluice(sluice_id, request_options=request_options)
        return _response.data


class AsyncSluicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSluicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSluicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSluicesClient
        """
        return self._raw_client

    async def fetch_sluice(self, sluice_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Sluice:
        """
        Parameters
        ----------
        sluice_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Sluice
            The sluice.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.sluices.fetch_sluice(
                sluice_id="sluiceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_sluice(sluice_id, request_options=request_options)
        return _response.data
