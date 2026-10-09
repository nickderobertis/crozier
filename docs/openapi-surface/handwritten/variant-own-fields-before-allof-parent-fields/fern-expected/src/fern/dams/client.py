

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.wall import Wall
from .raw_client import AsyncRawDamsClient, RawDamsClient


class DamsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDamsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDamsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDamsClient
        """
        return self._raw_client

    def fetch_wall(self, dam_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Wall:
        """
        Parameters
        ----------
        dam_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Wall
            The dam wall.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.dams.fetch_wall(
            dam_id="damId",
        )
        """
        _response = self._raw_client.fetch_wall(dam_id, request_options=request_options)
        return _response.data


class AsyncDamsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDamsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDamsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDamsClient
        """
        return self._raw_client

    async def fetch_wall(self, dam_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Wall:
        """
        Parameters
        ----------
        dam_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Wall
            The dam wall.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dams.fetch_wall(
                dam_id="damId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_wall(dam_id, request_options=request_options)
        return _response.data
