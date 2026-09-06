

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_filter import AppFilter
from ..types.apps_include import AppsInclude
from ..types.config_filter import ConfigFilter
from ..types.config_include import ConfigInclude
from ..types.config_rank import ConfigRank
from ..types.search_response_body import SearchResponseBody
from .raw_client import AsyncRawSearchClient, RawSearchClient
from .types.post_v1search_configs_response import PostV1SearchConfigsResponse
from .types.post_v1search_games_response import PostV1SearchGamesResponse


OMIT = typing.cast(typing.Any, ...)


class SearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSearchClient
        """
        return self._raw_client

    def search_steam_games_and_configurations_all_at_once(
        self,
        *,
        search_term: str,
        limit: typing.Optional[int] = OMIT,
        limit_configs: typing.Optional[int] = OMIT,
        limit_games: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchResponseBody:
        """
        Search for games that are available on Steam
        **and** Search for SteamInput configurations for Steam and non-Steam games
        **all at once**

        This endpoint supports no pagination and has pretty strict limits, it's intended for the "main-page" of the Frontend only

        Parameters
        ----------
        search_term : str

        limit : typing.Optional[int]

        limit_configs : typing.Optional[int]

        limit_games : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchResponseBody
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.search.search_steam_games_and_configurations_all_at_once(
            search_term="search_term",
        )
        """
        _response = self._raw_client.search_steam_games_and_configurations_all_at_once(
            search_term=search_term,
            limit=limit,
            limit_configs=limit_configs,
            limit_games=limit_games,
            request_options=request_options,
        )
        return _response.data

    def search_steam_input_configurations(
        self,
        *,
        query_text: str,
        filter: typing.Optional[ConfigFilter] = OMIT,
        include: typing.Optional[ConfigInclude] = OMIT,
        limit: typing.Optional[int] = OMIT,
        page: typing.Optional[int] = OMIT,
        rank: typing.Optional[ConfigRank] = OMIT,
        raw: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1SearchConfigsResponse:
        """
        Search for SteamInput configurations for Steam and non-Steam games

        Parameters
        ----------
        query_text : str
            The search query string

        filter : typing.Optional[ConfigFilter]

        include : typing.Optional[ConfigInclude]

        limit : typing.Optional[int]
            Maximum number of results to return

        page : typing.Optional[int]
            Page number for paginated results

        rank : typing.Optional[ConfigRank]

        raw : typing.Optional[bool]
            Return raw Steam API response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1SearchConfigsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.search.search_steam_input_configurations(
            query_text="query_text",
        )
        """
        _response = self._raw_client.search_steam_input_configurations(
            query_text=query_text,
            filter=filter,
            include=include,
            limit=limit,
            page=page,
            rank=rank,
            raw=raw,
            request_options=request_options,
        )
        return _response.data

    def search_steam_games(
        self,
        *,
        query_text: str,
        filter: typing.Optional[AppFilter] = OMIT,
        include: typing.Optional[AppsInclude] = OMIT,
        limit: typing.Optional[int] = OMIT,
        raw: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1SearchGamesResponse:
        """
        Search for games that are available on Steam

        Parameters
        ----------
        query_text : str
            The search query string

        filter : typing.Optional[AppFilter]

        include : typing.Optional[AppsInclude]

        limit : typing.Optional[int]
            Maximum number of results to return

        raw : typing.Optional[bool]
            Return raw Steam API response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1SearchGamesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.search.search_steam_games(
            query_text="query_text",
        )
        """
        _response = self._raw_client.search_steam_games(
            query_text=query_text, filter=filter, include=include, limit=limit, raw=raw, request_options=request_options
        )
        return _response.data


class AsyncSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSearchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSearchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSearchClient
        """
        return self._raw_client

    async def search_steam_games_and_configurations_all_at_once(
        self,
        *,
        search_term: str,
        limit: typing.Optional[int] = OMIT,
        limit_configs: typing.Optional[int] = OMIT,
        limit_games: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchResponseBody:
        """
        Search for games that are available on Steam
        **and** Search for SteamInput configurations for Steam and non-Steam games
        **all at once**

        This endpoint supports no pagination and has pretty strict limits, it's intended for the "main-page" of the Frontend only

        Parameters
        ----------
        search_term : str

        limit : typing.Optional[int]

        limit_configs : typing.Optional[int]

        limit_games : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchResponseBody
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.search.search_steam_games_and_configurations_all_at_once(
                search_term="search_term",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_steam_games_and_configurations_all_at_once(
            search_term=search_term,
            limit=limit,
            limit_configs=limit_configs,
            limit_games=limit_games,
            request_options=request_options,
        )
        return _response.data

    async def search_steam_input_configurations(
        self,
        *,
        query_text: str,
        filter: typing.Optional[ConfigFilter] = OMIT,
        include: typing.Optional[ConfigInclude] = OMIT,
        limit: typing.Optional[int] = OMIT,
        page: typing.Optional[int] = OMIT,
        rank: typing.Optional[ConfigRank] = OMIT,
        raw: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1SearchConfigsResponse:
        """
        Search for SteamInput configurations for Steam and non-Steam games

        Parameters
        ----------
        query_text : str
            The search query string

        filter : typing.Optional[ConfigFilter]

        include : typing.Optional[ConfigInclude]

        limit : typing.Optional[int]
            Maximum number of results to return

        page : typing.Optional[int]
            Page number for paginated results

        rank : typing.Optional[ConfigRank]

        raw : typing.Optional[bool]
            Return raw Steam API response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1SearchConfigsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.search.search_steam_input_configurations(
                query_text="query_text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_steam_input_configurations(
            query_text=query_text,
            filter=filter,
            include=include,
            limit=limit,
            page=page,
            rank=rank,
            raw=raw,
            request_options=request_options,
        )
        return _response.data

    async def search_steam_games(
        self,
        *,
        query_text: str,
        filter: typing.Optional[AppFilter] = OMIT,
        include: typing.Optional[AppsInclude] = OMIT,
        limit: typing.Optional[int] = OMIT,
        raw: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1SearchGamesResponse:
        """
        Search for games that are available on Steam

        Parameters
        ----------
        query_text : str
            The search query string

        filter : typing.Optional[AppFilter]

        include : typing.Optional[AppsInclude]

        limit : typing.Optional[int]
            Maximum number of results to return

        raw : typing.Optional[bool]
            Return raw Steam API response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1SearchGamesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.search.search_steam_games(
                query_text="query_text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_steam_games(
            query_text=query_text, filter=filter, include=include, limit=limit, raw=raw, request_options=request_options
        )
        return _response.data
