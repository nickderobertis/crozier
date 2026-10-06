

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawStatusResourceClient, RawStatusResourceClient


class StatusResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStatusResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStatusResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStatusResourceClient
        """
        return self._raw_client

    def get_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
        client.status_resource.get_status()
        """
        _response = self._raw_client.get_status(request_options=request_options)
        return _response.data


class AsyncStatusResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStatusResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStatusResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStatusResourceClient
        """
        return self._raw_client

    async def get_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            await client.status_resource.get_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_status(request_options=request_options)
        return _response.data
