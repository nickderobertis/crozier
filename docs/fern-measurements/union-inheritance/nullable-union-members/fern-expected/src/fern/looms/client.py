

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.loom_reading import LoomReading
from .raw_client import AsyncRawLoomsClient, RawLoomsClient


class LoomsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLoomsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLoomsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLoomsClient
        """
        return self._raw_client

    def get_loom_reading(self, loom_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> LoomReading:
        """
        Parameters
        ----------
        loom_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoomReading
            The latest reading.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.looms.get_loom_reading(
            loom_id="loomId",
        )
        """
        _response = self._raw_client.get_loom_reading(loom_id, request_options=request_options)
        return _response.data


class AsyncLoomsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLoomsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLoomsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLoomsClient
        """
        return self._raw_client

    async def get_loom_reading(
        self, loom_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LoomReading:
        """
        Parameters
        ----------
        loom_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LoomReading
            The latest reading.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.looms.get_loom_reading(
                loom_id="loomId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_loom_reading(loom_id, request_options=request_options)
        return _response.data
