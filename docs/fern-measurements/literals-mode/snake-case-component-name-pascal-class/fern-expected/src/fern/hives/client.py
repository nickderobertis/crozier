

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.honey_yield import HoneyYield
from .raw_client import AsyncRawHivesClient, RawHivesClient


class HivesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHivesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHivesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHivesClient
        """
        return self._raw_client

    def fetch_yield(self, hive_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HoneyYield:
        """
        Parameters
        ----------
        hive_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HoneyYield
            The season's honey yield.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.hives.fetch_yield(
            hive_id="hiveId",
        )
        """
        _response = self._raw_client.fetch_yield(hive_id, request_options=request_options)
        return _response.data


class AsyncHivesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHivesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHivesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHivesClient
        """
        return self._raw_client

    async def fetch_yield(self, hive_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HoneyYield:
        """
        Parameters
        ----------
        hive_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HoneyYield
            The season's honey yield.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.hives.fetch_yield(
                hive_id="hiveId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_yield(hive_id, request_options=request_options)
        return _response.data
