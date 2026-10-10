

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRelaysClient, RawRelaysClient


OMIT = typing.cast(typing.Any, ...)


class RelaysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRelaysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRelaysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRelaysClient
        """
        return self._raw_client

    def reset(self, *, relay: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        relay : str
            The relay's lever number.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client._relays.reset(
            relay="relay",
        )
        """
        _response = self._raw_client.reset(relay=relay, request_options=request_options)
        return _response.data


class AsyncRelaysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRelaysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRelaysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRelaysClient
        """
        return self._raw_client

    async def reset(self, *, relay: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        relay : str
            The relay's lever number.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client._relays.reset(
                relay="relay",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset(relay=relay, request_options=request_options)
        return _response.data
