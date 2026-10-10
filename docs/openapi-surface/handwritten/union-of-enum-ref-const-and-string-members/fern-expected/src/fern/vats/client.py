

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.shade import Shade
from .raw_client import AsyncRawVatsClient, RawVatsClient


class VatsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVatsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVatsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVatsClient
        """
        return self._raw_client

    def fetch_shade(self, vat_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Shade:
        """
        Parameters
        ----------
        vat_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Shade
            The shade in that vat.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.vats.fetch_shade(
            vat_id="vatId",
        )
        """
        _response = self._raw_client.fetch_shade(vat_id, request_options=request_options)
        return _response.data


class AsyncVatsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVatsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVatsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVatsClient
        """
        return self._raw_client

    async def fetch_shade(self, vat_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Shade:
        """
        Parameters
        ----------
        vat_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Shade
            The shade in that vat.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vats.fetch_shade(
                vat_id="vatId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_shade(vat_id, request_options=request_options)
        return _response.data
