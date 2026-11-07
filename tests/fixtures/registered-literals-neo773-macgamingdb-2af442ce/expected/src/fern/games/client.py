

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawGamesClient, RawGamesClient
from .types.game_get_by_id_response import GameGetByIdResponse
from .types.game_get_cover_art_response import GameGetCoverArtResponse
from .types.game_get_filter_counts_request_chipset import GameGetFilterCountsRequestChipset
from .types.game_get_filter_counts_request_chipset_variant import GameGetFilterCountsRequestChipsetVariant
from .types.game_get_filter_counts_request_play_method import GameGetFilterCountsRequestPlayMethod
from .types.game_get_filter_counts_response import GameGetFilterCountsResponse
from .types.game_get_games_request_chipset import GameGetGamesRequestChipset
from .types.game_get_games_request_chipset_variant import GameGetGamesRequestChipsetVariant
from .types.game_get_games_request_performance import GameGetGamesRequestPerformance
from .types.game_get_games_request_play_method import GameGetGamesRequestPlayMethod
from .types.game_get_games_response import GameGetGamesResponse
from .types.game_get_prices_response import GameGetPricesResponse
from .types.game_get_screenshot_signed_urls_response_item import GameGetScreenshotSignedUrlsResponseItem
from .types.game_get_sitemap_entries_response_item import GameGetSitemapEntriesResponseItem
from .types.game_search_response_item import GameSearchResponseItem


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

    def game_search(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GameSearchResponseItem]:
        """
        Parameters
        ----------
        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GameSearchResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.games.game_search(
            query="query",
        )
        """
        _response = self._raw_client.game_search(query=query, request_options=request_options)
        return _response.data

    def game_get_cover_art(
        self, game_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GameGetCoverArtResponse:
        """
        Parameters
        ----------
        game_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GameGetCoverArtResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.games.game_get_cover_art(
            game_id="gameId",
        )
        """
        _response = self._raw_client.game_get_cover_art(game_id, request_options=request_options)
        return _response.data

    def game_get_filter_counts(
        self,
        *,
        chipset: typing.Optional[GameGetFilterCountsRequestChipset] = None,
        chipset_variant: typing.Optional[GameGetFilterCountsRequestChipsetVariant] = None,
        play_method: typing.Optional[GameGetFilterCountsRequestPlayMethod] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GameGetFilterCountsResponse:
        """
        Parameters
        ----------
        chipset : typing.Optional[GameGetFilterCountsRequestChipset]

        chipset_variant : typing.Optional[GameGetFilterCountsRequestChipsetVariant]

        play_method : typing.Optional[GameGetFilterCountsRequestPlayMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GameGetFilterCountsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.games.game_get_filter_counts()
        """
        _response = self._raw_client.game_get_filter_counts(
            chipset=chipset, chipset_variant=chipset_variant, play_method=play_method, request_options=request_options
        )
        return _response.data

    def game_get_games(
        self,
        *,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[float] = None,
        performance: typing.Optional[GameGetGamesRequestPerformance] = None,
        chipset: typing.Optional[GameGetGamesRequestChipset] = None,
        chipset_variant: typing.Optional[GameGetGamesRequestChipsetVariant] = None,
        play_method: typing.Optional[GameGetGamesRequestPlayMethod] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GameGetGamesResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[float]

        cursor : typing.Optional[float]

        performance : typing.Optional[GameGetGamesRequestPerformance]

        chipset : typing.Optional[GameGetGamesRequestChipset]

        chipset_variant : typing.Optional[GameGetGamesRequestChipsetVariant]

        play_method : typing.Optional[GameGetGamesRequestPlayMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GameGetGamesResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.games.game_get_games()
        """
        _response = self._raw_client.game_get_games(
            limit=limit,
            cursor=cursor,
            performance=performance,
            chipset=chipset,
            chipset_variant=chipset_variant,
            play_method=play_method,
            request_options=request_options,
        )
        return _response.data

    def game_get_sitemap_entries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GameGetSitemapEntriesResponseItem]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GameGetSitemapEntriesResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.games.game_get_sitemap_entries()
        """
        _response = self._raw_client.game_get_sitemap_entries(request_options=request_options)
        return _response.data

    def game_get_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GameGetByIdResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GameGetByIdResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.games.game_get_by_id(
            id="id",
        )
        """
        _response = self._raw_client.game_get_by_id(id, request_options=request_options)
        return _response.data

    def game_get_screenshot_signed_urls(
        self,
        *,
        screenshots: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GameGetScreenshotSignedUrlsResponseItem]:
        """
        Parameters
        ----------
        screenshots : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GameGetScreenshotSignedUrlsResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.games.game_get_screenshot_signed_urls(
            screenshots=["screenshots"],
        )
        """
        _response = self._raw_client.game_get_screenshot_signed_urls(
            screenshots=screenshots, request_options=request_options
        )
        return _response.data

    def game_get_prices(
        self, game_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[GameGetPricesResponse]:
        """
        Parameters
        ----------
        game_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[GameGetPricesResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.games.game_get_prices(
            game_id="gameId",
        )
        """
        _response = self._raw_client.game_get_prices(game_id, request_options=request_options)
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

    async def game_search(
        self, *, query: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GameSearchResponseItem]:
        """
        Parameters
        ----------
        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GameSearchResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.games.game_search(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.game_search(query=query, request_options=request_options)
        return _response.data

    async def game_get_cover_art(
        self, game_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GameGetCoverArtResponse:
        """
        Parameters
        ----------
        game_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GameGetCoverArtResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.games.game_get_cover_art(
                game_id="gameId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.game_get_cover_art(game_id, request_options=request_options)
        return _response.data

    async def game_get_filter_counts(
        self,
        *,
        chipset: typing.Optional[GameGetFilterCountsRequestChipset] = None,
        chipset_variant: typing.Optional[GameGetFilterCountsRequestChipsetVariant] = None,
        play_method: typing.Optional[GameGetFilterCountsRequestPlayMethod] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GameGetFilterCountsResponse:
        """
        Parameters
        ----------
        chipset : typing.Optional[GameGetFilterCountsRequestChipset]

        chipset_variant : typing.Optional[GameGetFilterCountsRequestChipsetVariant]

        play_method : typing.Optional[GameGetFilterCountsRequestPlayMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GameGetFilterCountsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.games.game_get_filter_counts()


        asyncio.run(main())
        """
        _response = await self._raw_client.game_get_filter_counts(
            chipset=chipset, chipset_variant=chipset_variant, play_method=play_method, request_options=request_options
        )
        return _response.data

    async def game_get_games(
        self,
        *,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[float] = None,
        performance: typing.Optional[GameGetGamesRequestPerformance] = None,
        chipset: typing.Optional[GameGetGamesRequestChipset] = None,
        chipset_variant: typing.Optional[GameGetGamesRequestChipsetVariant] = None,
        play_method: typing.Optional[GameGetGamesRequestPlayMethod] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GameGetGamesResponse:
        """
        Parameters
        ----------
        limit : typing.Optional[float]

        cursor : typing.Optional[float]

        performance : typing.Optional[GameGetGamesRequestPerformance]

        chipset : typing.Optional[GameGetGamesRequestChipset]

        chipset_variant : typing.Optional[GameGetGamesRequestChipsetVariant]

        play_method : typing.Optional[GameGetGamesRequestPlayMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GameGetGamesResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.games.game_get_games()


        asyncio.run(main())
        """
        _response = await self._raw_client.game_get_games(
            limit=limit,
            cursor=cursor,
            performance=performance,
            chipset=chipset,
            chipset_variant=chipset_variant,
            play_method=play_method,
            request_options=request_options,
        )
        return _response.data

    async def game_get_sitemap_entries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GameGetSitemapEntriesResponseItem]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GameGetSitemapEntriesResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.games.game_get_sitemap_entries()


        asyncio.run(main())
        """
        _response = await self._raw_client.game_get_sitemap_entries(request_options=request_options)
        return _response.data

    async def game_get_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GameGetByIdResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GameGetByIdResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.games.game_get_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.game_get_by_id(id, request_options=request_options)
        return _response.data

    async def game_get_screenshot_signed_urls(
        self,
        *,
        screenshots: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GameGetScreenshotSignedUrlsResponseItem]:
        """
        Parameters
        ----------
        screenshots : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GameGetScreenshotSignedUrlsResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.games.game_get_screenshot_signed_urls(
                screenshots=["screenshots"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.game_get_screenshot_signed_urls(
            screenshots=screenshots, request_options=request_options
        )
        return _response.data

    async def game_get_prices(
        self, game_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[GameGetPricesResponse]:
        """
        Parameters
        ----------
        game_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[GameGetPricesResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.games.game_get_prices(
                game_id="gameId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.game_get_prices(game_id, request_options=request_options)
        return _response.data
