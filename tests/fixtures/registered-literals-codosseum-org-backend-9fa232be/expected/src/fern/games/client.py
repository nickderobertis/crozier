

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.game import Game
from ..types.game_mode import GameMode
from ..types.game_settings import GameSettings
from ..types.players import Players
from ..types.round import Round
from .raw_client import AsyncRawGamesClient, RawGamesClient
from .types.create_game_response import CreateGameResponse
from .types.join_game_response import JoinGameResponse
from .types.subscribe_to_game_events_response_item import SubscribeToGameEventsResponseItem
from .types.test_solution_response import TestSolutionResponse


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

    def create_game(
        self,
        *,
        allowed_game_modes: typing.Optional[typing.Sequence[GameMode]] = OMIT,
        allowed_languages: typing.Optional[typing.Sequence[str]] = OMIT,
        game_mode: typing.Optional[GameMode] = OMIT,
        max_players: typing.Optional[int] = OMIT,
        time_limit: typing.Optional[int] = OMIT,
        max_warmup_time: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateGameResponse:
        """
        Parameters
        ----------
        allowed_game_modes : typing.Optional[typing.Sequence[GameMode]]

        allowed_languages : typing.Optional[typing.Sequence[str]]
            Which programming languages are allowed to be used for submissions. If omitted, all languages are allowed.

        game_mode : typing.Optional[GameMode]
            Game mode of this game

        max_players : typing.Optional[int]
            Maximum player count for the game

        time_limit : typing.Optional[int]
            Time limit for the game, in seconds.

        max_warmup_time : typing.Optional[int]
            Maximum warmup time for a game in seconds - that is, a timer that starts once 2 or more players have joined the game that delays the starting of the game to allow more players to join.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateGameResponse
            new game created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.games.create_game()
        """
        _response = self._raw_client.create_game(
            allowed_game_modes=allowed_game_modes,
            allowed_languages=allowed_languages,
            game_mode=game_mode,
            max_players=max_players,
            time_limit=time_limit,
            max_warmup_time=max_warmup_time,
            request_options=request_options,
        )
        return _response.data

    def get_game(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Game:
        """
        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Game
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.games.get_game(
            id="id",
        )
        """
        _response = self._raw_client.get_game(id, request_options=request_options)
        return _response.data

    def delete_game(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Can be used by the admin of a game to delete it while in warmup.

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.games.delete_game(
            id="id",
        )
        """
        _response = self._raw_client.delete_game(id, request_options=request_options)
        return _response.data

    def update_game(
        self,
        id: str,
        *,
        allowed_languages: typing.Optional[typing.Sequence[str]] = OMIT,
        game_mode: typing.Optional[GameMode] = OMIT,
        max_players: typing.Optional[int] = OMIT,
        time_limit: typing.Optional[int] = OMIT,
        max_warmup_time: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GameSettings:
        """
        (Partially) updates the settings of an existing game. This is only possible during the warmup phase of the game.

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        allowed_languages : typing.Optional[typing.Sequence[str]]
            Which programming languages are allowed to be used for submissions. If omitted, all languages are allowed.

        game_mode : typing.Optional[GameMode]
            Game mode of this game

        max_players : typing.Optional[int]
            Maximum player count for the game

        time_limit : typing.Optional[int]
            Time limit for the game, in seconds.

        max_warmup_time : typing.Optional[int]
            Maximum warmup time for a game in seconds - that is, a timer that starts once 2 or more players have joined the game that delays the starting of the game to allow more players to join.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GameSettings
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.games.update_game(
            id="id",
        )
        """
        _response = self._raw_client.update_game(
            id,
            allowed_languages=allowed_languages,
            game_mode=game_mode,
            max_players=max_players,
            time_limit=time_limit,
            max_warmup_time=max_warmup_time,
            request_options=request_options,
        )
        return _response.data

    def get_players(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Players:
        """
        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Players
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.games.get_players(
            id="id",
        )
        """
        _response = self._raw_client.get_players(id, request_options=request_options)
        return _response.data

    def join_game(
        self, id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> JoinGameResponse:
        """
        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JoinGameResponse
            Successfully joined the game

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.games.join_game(
            id="id",
            name="name",
        )
        """
        _response = self._raw_client.join_game(id, name=name, request_options=request_options)
        return _response.data

    def leave_game(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.games.leave_game(
            id="id",
        )
        """
        _response = self._raw_client.leave_game(id, request_options=request_options)
        return _response.data

    def start_game(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Forcefully start a game, regardless of player-count and warmup time

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.games.start_game(
            id="id",
        )
        """
        _response = self._raw_client.start_game(id, request_options=request_options)
        return _response.data

    def get_code_template(self, id: str, *, lang: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a code template for the current challenge for the specified programming language

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        lang : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Template created and sent successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.games.get_code_template(
            id="id",
            lang="lang",
        )
        """
        _response = self._raw_client.get_code_template(id, lang=lang, request_options=request_options)
        return _response.data

    def test_solution(
        self,
        id: str,
        *,
        language: str,
        code: str,
        test_numbers: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestSolutionResponse:
        """
        Test a given solution to a game's challenges, returning the test results without submitting the solution

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        language : str
            The language of the solution attempt, as an identifier supported by Piston

        code : str
            The code to test, which is assumed to be in the language specified

        test_numbers : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            The test numbers (public tests) to run the code against. If omitted, all tests will be run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSolutionResponse
            Acknowledgement that the solution was received and is being tested, results will be sent via Server-Sent Events

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.games.test_solution(
            id="id",
            language="language",
            code="code",
        )
        """
        _response = self._raw_client.test_solution(
            id, language=language, code=code, test_numbers=test_numbers, request_options=request_options
        )
        return _response.data

    def submit_solution(
        self, id: str, *, language: str, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Submit a solution to a game's challenges

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        language : str
            The language of the solution attempt, as an identifier supported by Piston

        code : str
            The code to test, which is assumed to be in the language specified

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.games.submit_solution(
            id="id",
            language="language",
            code="code",
        )
        """
        _response = self._raw_client.submit_solution(id, language=language, code=code, request_options=request_options)
        return _response.data

    def get_round(
        self,
        id: str,
        round: int,
        *,
        with_code: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Round:
        """
        Get the details of a specific round, including (interim) results, or the most recent round if none specified.
        If authenticated with a game key and the corresponding player has already submitted a solution in
        the round in question, the response may also contain the code of the other players who have participated.
        Regardless of authentication, all the info may be returned if the round is already over.
        To request the transmission of the code players have submitted, set the withCode query parameter.

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        round : int
            The number of the round in question

        with_code : typing.Optional[bool]
            Whether to include the code of all players

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Round
            Returns the result in winning order.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.games.get_round(
            id="id",
            round=1,
        )
        """
        _response = self._raw_client.get_round(id, round, with_code=with_code, request_options=request_options)
        return _response.data

    def get_round_results(
        self, id: str, round: int, player: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns the full result of a player for a specific round.
        This is useful as a supplement to GET /games/{id}/rounds/{round}
        if you want to display the code of each player upon request but don't want to request everything at once.
        The same authentication rules as in this other endpoint apply regarding visibility of code.

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        round : int
            The number of the round in question

        player : str
            Name of the player whose results should be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.games.get_round_results(
            id="id",
            round=1,
            player="player",
        )
        """
        _response = self._raw_client.get_round_results(id, round, player, request_options=request_options)
        return _response.data

    def subscribe_to_game_events(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[typing.List[SubscribeToGameEventsResponseItem]]:
        """
        You should use a tool specifically for server-sent events for interacting with this endpoint.
        Authentication with a *game key* is optional - if a game key for the specified game is provided,
        the server will send events that are exclusive to the corresponding player, such as test results.

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[typing.List[SubscribeToGameEventsResponseItem]]
            Success - events will be sent.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        response = client.games.subscribe_to_game_events(
            id="id",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.subscribe_to_game_events(id, request_options=request_options) as r:
            yield from r.data


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

    async def create_game(
        self,
        *,
        allowed_game_modes: typing.Optional[typing.Sequence[GameMode]] = OMIT,
        allowed_languages: typing.Optional[typing.Sequence[str]] = OMIT,
        game_mode: typing.Optional[GameMode] = OMIT,
        max_players: typing.Optional[int] = OMIT,
        time_limit: typing.Optional[int] = OMIT,
        max_warmup_time: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateGameResponse:
        """
        Parameters
        ----------
        allowed_game_modes : typing.Optional[typing.Sequence[GameMode]]

        allowed_languages : typing.Optional[typing.Sequence[str]]
            Which programming languages are allowed to be used for submissions. If omitted, all languages are allowed.

        game_mode : typing.Optional[GameMode]
            Game mode of this game

        max_players : typing.Optional[int]
            Maximum player count for the game

        time_limit : typing.Optional[int]
            Time limit for the game, in seconds.

        max_warmup_time : typing.Optional[int]
            Maximum warmup time for a game in seconds - that is, a timer that starts once 2 or more players have joined the game that delays the starting of the game to allow more players to join.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateGameResponse
            new game created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.games.create_game()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_game(
            allowed_game_modes=allowed_game_modes,
            allowed_languages=allowed_languages,
            game_mode=game_mode,
            max_players=max_players,
            time_limit=time_limit,
            max_warmup_time=max_warmup_time,
            request_options=request_options,
        )
        return _response.data

    async def get_game(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Game:
        """
        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Game
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.games.get_game(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_game(id, request_options=request_options)
        return _response.data

    async def delete_game(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Can be used by the admin of a game to delete it while in warmup.

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.games.delete_game(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_game(id, request_options=request_options)
        return _response.data

    async def update_game(
        self,
        id: str,
        *,
        allowed_languages: typing.Optional[typing.Sequence[str]] = OMIT,
        game_mode: typing.Optional[GameMode] = OMIT,
        max_players: typing.Optional[int] = OMIT,
        time_limit: typing.Optional[int] = OMIT,
        max_warmup_time: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GameSettings:
        """
        (Partially) updates the settings of an existing game. This is only possible during the warmup phase of the game.

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        allowed_languages : typing.Optional[typing.Sequence[str]]
            Which programming languages are allowed to be used for submissions. If omitted, all languages are allowed.

        game_mode : typing.Optional[GameMode]
            Game mode of this game

        max_players : typing.Optional[int]
            Maximum player count for the game

        time_limit : typing.Optional[int]
            Time limit for the game, in seconds.

        max_warmup_time : typing.Optional[int]
            Maximum warmup time for a game in seconds - that is, a timer that starts once 2 or more players have joined the game that delays the starting of the game to allow more players to join.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GameSettings
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.games.update_game(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_game(
            id,
            allowed_languages=allowed_languages,
            game_mode=game_mode,
            max_players=max_players,
            time_limit=time_limit,
            max_warmup_time=max_warmup_time,
            request_options=request_options,
        )
        return _response.data

    async def get_players(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Players:
        """
        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Players
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.games.get_players(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_players(id, request_options=request_options)
        return _response.data

    async def join_game(
        self, id: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> JoinGameResponse:
        """
        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JoinGameResponse
            Successfully joined the game

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.games.join_game(
                id="id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.join_game(id, name=name, request_options=request_options)
        return _response.data

    async def leave_game(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.games.leave_game(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.leave_game(id, request_options=request_options)
        return _response.data

    async def start_game(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Forcefully start a game, regardless of player-count and warmup time

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.games.start_game(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_game(id, request_options=request_options)
        return _response.data

    async def get_code_template(
        self, id: str, *, lang: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get a code template for the current challenge for the specified programming language

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        lang : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Template created and sent successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.games.get_code_template(
                id="id",
                lang="lang",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_code_template(id, lang=lang, request_options=request_options)
        return _response.data

    async def test_solution(
        self,
        id: str,
        *,
        language: str,
        code: str,
        test_numbers: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TestSolutionResponse:
        """
        Test a given solution to a game's challenges, returning the test results without submitting the solution

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        language : str
            The language of the solution attempt, as an identifier supported by Piston

        code : str
            The code to test, which is assumed to be in the language specified

        test_numbers : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            The test numbers (public tests) to run the code against. If omitted, all tests will be run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestSolutionResponse
            Acknowledgement that the solution was received and is being tested, results will be sent via Server-Sent Events

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.games.test_solution(
                id="id",
                language="language",
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.test_solution(
            id, language=language, code=code, test_numbers=test_numbers, request_options=request_options
        )
        return _response.data

    async def submit_solution(
        self, id: str, *, language: str, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Submit a solution to a game's challenges

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        language : str
            The language of the solution attempt, as an identifier supported by Piston

        code : str
            The code to test, which is assumed to be in the language specified

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.games.submit_solution(
                id="id",
                language="language",
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_solution(
            id, language=language, code=code, request_options=request_options
        )
        return _response.data

    async def get_round(
        self,
        id: str,
        round: int,
        *,
        with_code: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Round:
        """
        Get the details of a specific round, including (interim) results, or the most recent round if none specified.
        If authenticated with a game key and the corresponding player has already submitted a solution in
        the round in question, the response may also contain the code of the other players who have participated.
        Regardless of authentication, all the info may be returned if the round is already over.
        To request the transmission of the code players have submitted, set the withCode query parameter.

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        round : int
            The number of the round in question

        with_code : typing.Optional[bool]
            Whether to include the code of all players

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Round
            Returns the result in winning order.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.games.get_round(
                id="id",
                round=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_round(id, round, with_code=with_code, request_options=request_options)
        return _response.data

    async def get_round_results(
        self, id: str, round: int, player: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns the full result of a player for a specific round.
        This is useful as a supplement to GET /games/{id}/rounds/{round}
        if you want to display the code of each player upon request but don't want to request everything at once.
        The same authentication rules as in this other endpoint apply regarding visibility of code.

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        round : int
            The number of the round in question

        player : str
            Name of the player whose results should be retrieved

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.games.get_round_results(
                id="id",
                round=1,
                player="player",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_round_results(id, round, player, request_options=request_options)
        return _response.data

    async def subscribe_to_game_events(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[typing.List[SubscribeToGameEventsResponseItem]]:
        """
        You should use a tool specifically for server-sent events for interacting with this endpoint.
        Authentication with a *game key* is optional - if a game key for the specified game is provided,
        the server will send events that are exclusive to the corresponding player, such as test results.

        Parameters
        ----------
        id : str
            Game ID (returned from creating a game)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[typing.List[SubscribeToGameEventsResponseItem]]
            Success - events will be sent.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            response = client.games.subscribe_to_game_events(
                id="id",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.subscribe_to_game_events(id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
