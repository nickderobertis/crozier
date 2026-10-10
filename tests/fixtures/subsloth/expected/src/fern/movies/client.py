

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.language_code import LanguageCode
from ..types.movie_detail_response import MovieDetailResponse
from ..types.movie_list_response import MovieListResponse
from .raw_client import AsyncRawMoviesClient, RawMoviesClient
from .types.list_movies_request_sort import ListMoviesRequestSort


class MoviesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMoviesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMoviesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMoviesClient
        """
        return self._raw_client

    def list_movies(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        sort: typing.Optional[ListMoviesRequestSort] = None,
        genre: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        subtitles: typing.Optional[LanguageCode] = None,
        year_from: typing.Optional[int] = None,
        year_to: typing.Optional[int] = None,
        rating_from: typing.Optional[float] = None,
        rating_to: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MovieListResponse:
        """
        Returns movies visible to the authenticated account. Exact pagination,
        sorting, and filter names must be verified by live drift tests.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.

        per_page : typing.Optional[int]
            Results per page for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.

        q : typing.Optional[str]
            Free-text search query for catalog filtering. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise search locally over fetched data.

        sort : typing.Optional[ListMoviesRequestSort]
            Sort order for catalog results. Sort values and production use must be verified against the Kodi plugin request surface by live drift tests; otherwise sort locally over fetched data.

        genre : typing.Optional[str]
            Filter catalog by genre slug. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        country : typing.Optional[str]
            Filter catalog by country code. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        subtitles : typing.Optional[LanguageCode]
            Filter catalog by subtitle language code. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        year_from : typing.Optional[int]
            Filter catalog by minimum release year (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        year_to : typing.Optional[int]
            Filter catalog by maximum release year (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        rating_from : typing.Optional[float]
            Filter catalog by minimum rating (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        rating_to : typing.Optional[float]
            Filter catalog by maximum rating (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MovieListResponse
            Movie list.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.movies.list_movies(
            subtitles="en",
        )
        """
        _response = self._raw_client.list_movies(
            page=page,
            per_page=per_page,
            q=q,
            sort=sort,
            genre=genre,
            country=country,
            subtitles=subtitles,
            year_from=year_from,
            year_to=year_to,
            rating_from=rating_from,
            rating_to=rating_to,
            request_options=request_options,
        )
        return _response.data

    def get_movie(
        self, movie_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MovieDetailResponse:
        """
        Parameters
        ----------
        movie_id : int
            Movie numeric id, as observed in live Kodi API responses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MovieDetailResponse
            Movie detail.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.movies.get_movie(
            movie_id=1,
        )
        """
        _response = self._raw_client.get_movie(movie_id, request_options=request_options)
        return _response.data


class AsyncMoviesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMoviesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMoviesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMoviesClient
        """
        return self._raw_client

    async def list_movies(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        sort: typing.Optional[ListMoviesRequestSort] = None,
        genre: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        subtitles: typing.Optional[LanguageCode] = None,
        year_from: typing.Optional[int] = None,
        year_to: typing.Optional[int] = None,
        rating_from: typing.Optional[float] = None,
        rating_to: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MovieListResponse:
        """
        Returns movies visible to the authenticated account. Exact pagination,
        sorting, and filter names must be verified by live drift tests.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.

        per_page : typing.Optional[int]
            Results per page for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.

        q : typing.Optional[str]
            Free-text search query for catalog filtering. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise search locally over fetched data.

        sort : typing.Optional[ListMoviesRequestSort]
            Sort order for catalog results. Sort values and production use must be verified against the Kodi plugin request surface by live drift tests; otherwise sort locally over fetched data.

        genre : typing.Optional[str]
            Filter catalog by genre slug. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        country : typing.Optional[str]
            Filter catalog by country code. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        subtitles : typing.Optional[LanguageCode]
            Filter catalog by subtitle language code. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        year_from : typing.Optional[int]
            Filter catalog by minimum release year (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        year_to : typing.Optional[int]
            Filter catalog by maximum release year (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        rating_from : typing.Optional[float]
            Filter catalog by minimum rating (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        rating_to : typing.Optional[float]
            Filter catalog by maximum rating (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MovieListResponse
            Movie list.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.movies.list_movies(
                subtitles="en",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_movies(
            page=page,
            per_page=per_page,
            q=q,
            sort=sort,
            genre=genre,
            country=country,
            subtitles=subtitles,
            year_from=year_from,
            year_to=year_to,
            rating_from=rating_from,
            rating_to=rating_to,
            request_options=request_options,
        )
        return _response.data

    async def get_movie(
        self, movie_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MovieDetailResponse:
        """
        Parameters
        ----------
        movie_id : int
            Movie numeric id, as observed in live Kodi API responses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MovieDetailResponse
            Movie detail.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.movies.get_movie(
                movie_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_movie(movie_id, request_options=request_options)
        return _response.data
