

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.game_record_visibility import GameRecordVisibility
from ..types.get_game_response import GetGameResponse
from ..types.list_games_response import ListGamesResponse
from ..types.update_game_visibility_response import UpdateGameVisibilityResponse
from .raw_client import AsyncRawGamesClient, RawGamesClient


OMIT = typing.cast(typing.Any, ...)


class GamesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGamesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGamesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGamesClient
        """
        return self._raw_client

    def list_games(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListGamesResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListGamesResponse
            List accessible games

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.games.list_games()
        """
        _response = self._raw_client.list_games(limit=limit, cursor=cursor, request_options=request_options)
        return _response.data

    def get_game(self, game_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetGameResponse:
        """
        Parameters
        ----------
        game_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGameResponse
            Get game detail

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.games.get_game(
            game_id="gameId",
        )
        """
        _response = self._raw_client.get_game(game_id, request_options=request_options)
        return _response.data

    def update_game_visibility(
        self, game_id: str, *, visibility: GameRecordVisibility, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateGameVisibilityResponse:
        """
        Parameters
        ----------
        game_id : str

        visibility : GameRecordVisibility

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateGameVisibilityResponse
            Updated game visibility

        Examples
        --------
        from fern import FernApi, GameRecordVisibility

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.games.update_game_visibility(
            game_id="gameId",
            visibility=GameRecordVisibility.PRIVATE,
        )
        """
        _response = self._raw_client.update_game_visibility(
            game_id, visibility=visibility, request_options=request_options
        )
        return _response.data


class AsyncGamesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGamesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGamesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGamesClient
        """
        return self._raw_client

    async def list_games(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListGamesResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListGamesResponse
            List accessible games

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.games.list_games()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_games(limit=limit, cursor=cursor, request_options=request_options)
        return _response.data

    async def get_game(
        self, game_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetGameResponse:
        """
        Parameters
        ----------
        game_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGameResponse
            Get game detail

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.games.get_game(
                game_id="gameId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_game(game_id, request_options=request_options)
        return _response.data

    async def update_game_visibility(
        self, game_id: str, *, visibility: GameRecordVisibility, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateGameVisibilityResponse:
        """
        Parameters
        ----------
        game_id : str

        visibility : GameRecordVisibility

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateGameVisibilityResponse
            Updated game visibility

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GameRecordVisibility

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.games.update_game_visibility(
                game_id="gameId",
                visibility=GameRecordVisibility.PRIVATE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_game_visibility(
            game_id, visibility=visibility, request_options=request_options
        )
        return _response.data
