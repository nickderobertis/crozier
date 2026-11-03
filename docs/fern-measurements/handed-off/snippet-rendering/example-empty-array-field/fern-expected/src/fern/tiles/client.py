

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.criteria import Criteria
from ..types.finish import Finish
from ..types.tile import Tile
from .raw_client import AsyncRawTilesClient, RawTilesClient


OMIT = typing.cast(typing.Any, ...)


class TilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTilesClient
        """
        return self._raw_client

    def retire_tiles(self, *, criteria: Criteria, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        criteria : Criteria

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import Criteria, FernApi

        client = FernApi()
        client.tiles.retire_tiles(
            criteria=Criteria(),
        )
        """
        _response = self._raw_client.retire_tiles(criteria=criteria, request_options=request_options)
        return _response.data

    def search_tiles(
        self, *, label: str, finish: Finish, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Tile]:
        """
        Parameters
        ----------
        label : str

        finish : Finish

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tile]
            The matching tiles.

        Examples
        --------
        from fern import FernApi, Finish

        client = FernApi()
        client.tiles.search_tiles(
            label="kitchen splashback",
            finish=Finish(
                glazes=["glazes"],
                sheen="matte",
            ),
        )
        """
        _response = self._raw_client.search_tiles(label=label, finish=finish, request_options=request_options)
        return _response.data


class AsyncTilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTilesClient
        """
        return self._raw_client

    async def retire_tiles(
        self, *, criteria: Criteria, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        criteria : Criteria

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Criteria

        client = AsyncFernApi()


        async def main() -> None:
            await client.tiles.retire_tiles(
                criteria=Criteria(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retire_tiles(criteria=criteria, request_options=request_options)
        return _response.data

    async def search_tiles(
        self, *, label: str, finish: Finish, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Tile]:
        """
        Parameters
        ----------
        label : str

        finish : Finish

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Tile]
            The matching tiles.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Finish

        client = AsyncFernApi()


        async def main() -> None:
            await client.tiles.search_tiles(
                label="kitchen splashback",
                finish=Finish(
                    glazes=["glazes"],
                    sheen="matte",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_tiles(label=label, finish=finish, request_options=request_options)
        return _response.data
