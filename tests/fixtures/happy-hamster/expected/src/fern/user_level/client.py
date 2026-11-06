

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.level import Level
from .raw_client import AsyncRawUserLevelClient, RawUserLevelClient


class UserLevelClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserLevelClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserLevelClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserLevelClient
        """
        return self._raw_client

    def get_level(self, *, request_options: typing.Optional[RequestOptions] = None) -> Level:
        """
        provides the level, stage, total xp, xp needed for the next level and current xp in this level for the logged in user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Level
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_level.get_level()
        """
        _response = self._raw_client.get_level(request_options=request_options)
        return _response.data


class AsyncUserLevelClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserLevelClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserLevelClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserLevelClient
        """
        return self._raw_client

    async def get_level(self, *, request_options: typing.Optional[RequestOptions] = None) -> Level:
        """
        provides the level, stage, total xp, xp needed for the next level and current xp in this level for the logged in user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Level
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_level.get_level()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_level(request_options=request_options)
        return _response.data
