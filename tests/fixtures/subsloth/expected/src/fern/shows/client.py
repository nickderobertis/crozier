

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.language_code import LanguageCode
from ..types.show_detail_response import ShowDetailResponse
from ..types.show_list_response import ShowListResponse
from .raw_client import AsyncRawShowsClient, RawShowsClient
from .types.list_shows_request_sort import ListShowsRequestSort


class ShowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawShowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawShowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawShowsClient
        """
        return self._raw_client

    def list_shows(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        sort: typing.Optional[ListShowsRequestSort] = None,
        genre: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        subtitles: typing.Optional[LanguageCode] = None,
        year_from: typing.Optional[int] = None,
        year_to: typing.Optional[int] = None,
        rating_from: typing.Optional[float] = None,
        rating_to: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ShowListResponse:
        """
        Returns shows visible to the authenticated account. Exact pagination,
        sorting, and filter names must be verified by live drift tests.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.

        per_page : typing.Optional[int]
            Results per page for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.

        q : typing.Optional[str]
            Free-text search query for catalog filtering. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise search locally over fetched data.

        sort : typing.Optional[ListShowsRequestSort]
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
        ShowListResponse
            Show list.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.shows.list_shows(
            subtitles="en",
        )
        """
        _response = self._raw_client.list_shows(
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

    def get_show(self, show_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> ShowDetailResponse:
        """
        Parameters
        ----------
        show_id : int
            Show numeric id, as observed in live Kodi API responses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShowDetailResponse
            Show detail with seasons and episodes.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.shows.get_show(
            show_id=1,
        )
        """
        _response = self._raw_client.get_show(show_id, request_options=request_options)
        return _response.data


class AsyncShowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawShowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawShowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawShowsClient
        """
        return self._raw_client

    async def list_shows(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        sort: typing.Optional[ListShowsRequestSort] = None,
        genre: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        subtitles: typing.Optional[LanguageCode] = None,
        year_from: typing.Optional[int] = None,
        year_to: typing.Optional[int] = None,
        rating_from: typing.Optional[float] = None,
        rating_to: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ShowListResponse:
        """
        Returns shows visible to the authenticated account. Exact pagination,
        sorting, and filter names must be verified by live drift tests.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.

        per_page : typing.Optional[int]
            Results per page for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.

        q : typing.Optional[str]
            Free-text search query for catalog filtering. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise search locally over fetched data.

        sort : typing.Optional[ListShowsRequestSort]
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
        ShowListResponse
            Show list.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.shows.list_shows(
                subtitles="en",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_shows(
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

    async def get_show(
        self, show_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ShowDetailResponse:
        """
        Parameters
        ----------
        show_id : int
            Show numeric id, as observed in live Kodi API responses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShowDetailResponse
            Show detail with seasons and episodes.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.shows.get_show(
                show_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_show(show_id, request_options=request_options)
        return _response.data
