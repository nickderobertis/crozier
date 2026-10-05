

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.telescope import Telescope
from .raw_client import AsyncRawTelescopesClient, RawTelescopesClient


class TelescopesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTelescopesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTelescopesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTelescopesClient
        """
        return self._raw_client

    def get_telescope(self, telescope_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Telescope:
        """
        Parameters
        ----------
        telescope_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Telescope
            One telescope.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.telescopes.get_telescope(
            telescope_id="telescope_id",
        )
        """
        _response = self._raw_client.get_telescope(telescope_id, request_options=request_options)
        return _response.data


class AsyncTelescopesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTelescopesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTelescopesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTelescopesClient
        """
        return self._raw_client

    async def get_telescope(
        self, telescope_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Telescope:
        """
        Parameters
        ----------
        telescope_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Telescope
            One telescope.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.telescopes.get_telescope(
                telescope_id="telescope_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_telescope(telescope_id, request_options=request_options)
        return _response.data
