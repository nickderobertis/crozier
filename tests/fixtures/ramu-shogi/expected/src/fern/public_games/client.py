

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_public_game_response import GetPublicGameResponse
from ..types.list_public_games_response import ListPublicGamesResponse
from .raw_client import AsyncRawPublicGamesClient, RawPublicGamesClient


class PublicGamesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPublicGamesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPublicGamesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPublicGamesClient
        """
        return self._raw_client

    def list_public_games(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPublicGamesResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPublicGamesResponse
            List public games

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.public_games.list_public_games()
        """
        _response = self._raw_client.list_public_games(limit=limit, cursor=cursor, request_options=request_options)
        return _response.data

    def get_public_game(
        self, public_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPublicGameResponse:
        """
        Parameters
        ----------
        public_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPublicGameResponse
            Get public game detail

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.public_games.get_public_game(
            public_id="publicId",
        )
        """
        _response = self._raw_client.get_public_game(public_id, request_options=request_options)
        return _response.data


class AsyncPublicGamesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPublicGamesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPublicGamesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPublicGamesClient
        """
        return self._raw_client

    async def list_public_games(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPublicGamesResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPublicGamesResponse
            List public games

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.public_games.list_public_games()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_public_games(
            limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def get_public_game(
        self, public_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPublicGameResponse:
        """
        Parameters
        ----------
        public_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPublicGameResponse
            Get public game detail

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.public_games.get_public_game(
                public_id="publicId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_public_game(public_id, request_options=request_options)
        return _response.data
