

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.related_searches_response import RelatedSearchesResponse
from ..types.search_response import SearchResponse
from ..types.spell_check_response import SpellCheckResponse
from ..types.trending_searches_response import TrendingSearchesResponse
from ..types.typeahead_response import TypeaheadResponse
from .raw_client import AsyncRawSearchApiClient, RawSearchApiClient
from .types.search_request_type import SearchRequestType


class SearchApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSearchApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSearchApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSearchApiClient
        """
        return self._raw_client

    def get_related_searches(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RelatedSearchesResponse:
        """
        Suggest related search terms. The results are more comprehensive than from `GET /typeahead`. This endpoint is available only in the PRO/ENTERPRISE plan.

        Parameters
        ----------
        q : str
            Search term, e.g., person, place, topic...

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RelatedSearchesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.search_api.get_related_searches(
            q="evergrande",
        )
        """
        _response = self._raw_client.get_related_searches(q=q, request_options=request_options)
        return _response.data

    def search(
        self,
        *,
        q: str,
        sort_by_date: typing.Optional[int] = None,
        type: typing.Optional[SearchRequestType] = None,
        offset: typing.Optional[int] = None,
        len_min: typing.Optional[int] = None,
        len_max: typing.Optional[int] = None,
        episode_count_min: typing.Optional[int] = None,
        episode_count_max: typing.Optional[int] = None,
        update_freq_min: typing.Optional[int] = None,
        update_freq_max: typing.Optional[int] = None,
        genre_ids: typing.Optional[str] = None,
        published_before: typing.Optional[int] = None,
        published_after: typing.Optional[int] = None,
        only_in: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        ocid: typing.Optional[str] = None,
        ncid: typing.Optional[str] = None,
        safe_mode: typing.Optional[int] = None,
        unique_podcasts: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchResponse:
        """
        Full-text search on episodes, podcasts, or curated lists of podcasts.
        Use the `offset` parameter to paginate through search results.
        The FREE plan allows to see up to 30 search results (or `offset` < 30) per query.
        The PRO plan allows to see up to 300 search results (or `offset` < 300) per query.
        The ENTERPRISE plan allows to see up to 10,000 search results (or `offset` < 10000) per query.

        Parameters
        ----------
        q : str
            Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., "game of thrones". Otherwise, it's fuzzy search.

        sort_by_date : typing.Optional[int]
            Sort by date or not? If 0, then sort by relevance. If 1, then sort by date.

        type : typing.Optional[SearchRequestType]
            What type of contents do you want to search for?

        offset : typing.Optional[int]
            Offset for search results, for pagination. You'll use **next_offset** from response for this parameter.

        len_min : typing.Optional[int]
            Minimum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**.
            If **type** parameter is **episode**, it's for audio length of an episode.
            If **type** parameter is **podcast**, it's for average audio length of all episodes in a podcast.

        len_max : typing.Optional[int]
            Maximum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**.
            If **type** parameter is **episode**, it's for audio length of an episode.
            If **type** parameter is **podcast**, it's for average audio length of all episodes in a podcast.

        episode_count_min : typing.Optional[int]
            Minimum number of episodes. Applicable only when type parameter is **podcast**.

        episode_count_max : typing.Optional[int]
            Maximum number of episodes. Applicable only when type parameter is **podcast**.

        update_freq_min : typing.Optional[int]
            Minimum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find "weekly" podcasts, then you can set **update_freq_min**=144 hours (or 6 days) and **update_freq_max**=192 hours (or 8 days). Applicable only when type parameter is **podcast**.

        update_freq_max : typing.Optional[int]
            Maximum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find "weekly" podcasts, then you can set **update_freq_min**=144 hours (or 6 days) and **update_freq_max**=192 hours (or 8 days). Applicable only when type parameter is **podcast**.

        genre_ids : typing.Optional[str]
            A comma-delimited string of a list of genre ids. If not specified, then all genres are included. You can find the id and the name of all genres from `GET /genres`. It works only when **type** is *episode* or *podcast*.

        published_before : typing.Optional[int]
            Only show episodes/podcasts/curated lists published before this timestamp (in milliseconds). If **published_before** & **published_after** are used at the same time, **published_before** should be bigger than **published_after**.

        published_after : typing.Optional[int]
            Only show episodes/podcasts/curated lists published after this timestamp (in milliseconds). If **published_before** & **published_after** are used at the same time, **published_before** should be bigger than **published_after**.

        only_in : typing.Optional[str]
            A comma-delimited string to search only in specific fields. Allowed values are title, description, author, and audio. If not specified, then search every fields.

        language : typing.Optional[str]
            Limit search results to a specific language. If not specified, it'll be any language. You can get a list of supported languages from `GET /languages`. It works only when **type** is *episode* or *podcast*.

        region : typing.Optional[str]
            Limit search results to a specific region (e.g., us, gb, in...). If not specified, it'll be any region. You can get the supported country codes from `GET /regions`. It works only when **type** is *episode* or *podcast*.

        ocid : typing.Optional[str]
            A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to limit search results from only a few specific podcasts. It works only when **type** is *episode*.

        ncid : typing.Optional[str]
            A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to exclude search results of a few specific podcasts. It works only when **type** is *episode*.

        safe_mode : typing.Optional[int]
            Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **type** is *episode* or *podcast*.

        unique_podcasts : typing.Optional[int]
            Whether or not to keep only one episode per podcast in search results. 1 is yes and 0 is no. It works only when **type** is *episode*.

        page_size : typing.Optional[int]
            The maximum number of search results per page. A valid value should be an integer between 1 and 10 (inclusive).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.search_api.search(
            q="star wars",
            sort_by_date=0,
            offset=0,
            len_min=10,
            len_max=30,
            genre_ids="68,82",
            published_before=1580172454000,
            published_after=0,
            only_in="title,description",
            language="English",
            region="",
            safe_mode=0,
            unique_podcasts=0,
            page_size=10,
        )
        """
        _response = self._raw_client.search(
            q=q,
            sort_by_date=sort_by_date,
            type=type,
            offset=offset,
            len_min=len_min,
            len_max=len_max,
            episode_count_min=episode_count_min,
            episode_count_max=episode_count_max,
            update_freq_min=update_freq_min,
            update_freq_max=update_freq_max,
            genre_ids=genre_ids,
            published_before=published_before,
            published_after=published_after,
            only_in=only_in,
            language=language,
            region=region,
            ocid=ocid,
            ncid=ncid,
            safe_mode=safe_mode,
            unique_podcasts=unique_podcasts,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    def spellcheck(self, *, q: str, request_options: typing.Optional[RequestOptions] = None) -> SpellCheckResponse:
        """
        Suggest a list of words that correct the spelling errors of a search term. This endpoint is available only in the PRO/ENTERPRISE plan.

        Parameters
        ----------
        q : str
            Search term, e.g., person, place, topic...

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpellCheckResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.search_api.spellcheck(
            q="evergrand stok",
        )
        """
        _response = self._raw_client.spellcheck(q=q, request_options=request_options)
        return _response.data

    def get_trending_searches(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrendingSearchesResponse:
        """
        Fetch up to 10 most recent trending search terms on the Listen Notes platform.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrendingSearchesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.search_api.get_trending_searches()
        """
        _response = self._raw_client.get_trending_searches(request_options=request_options)
        return _response.data

    def typeahead(
        self,
        *,
        q: str,
        show_podcasts: typing.Optional[int] = None,
        show_genres: typing.Optional[int] = None,
        safe_mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TypeaheadResponse:
        """
        Suggest search terms, podcast genres, and podcasts.

        Parameters
        ----------
        q : str
            Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., "game of thrones". Otherwise, it's fuzzy search.

        show_podcasts : typing.Optional[int]
            Autosuggest podcasts. This only searches podcast title and publisher and returns very limited info of 5 podcasts. 1 is yes, 0 is no. It's a bit slow to autosuggest podcasts, so we turn it off by default. If show_podcasts=1, you can also pass iTunes id (e.g., 474722933) to the q parameter to fetch podcast meta data.

        show_genres : typing.Optional[int]
            Whether or not to autosuggest genres. 1 is yes, 0 is no.

        safe_mode : typing.Optional[int]
            Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **show_podcasts** is *1*.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TypeaheadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.search_api.typeahead(
            q="star wars",
            show_podcasts=1,
            show_genres=1,
            safe_mode=0,
        )
        """
        _response = self._raw_client.typeahead(
            q=q,
            show_podcasts=show_podcasts,
            show_genres=show_genres,
            safe_mode=safe_mode,
            request_options=request_options,
        )
        return _response.data


class AsyncSearchApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSearchApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSearchApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSearchApiClient
        """
        return self._raw_client

    async def get_related_searches(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RelatedSearchesResponse:
        """
        Suggest related search terms. The results are more comprehensive than from `GET /typeahead`. This endpoint is available only in the PRO/ENTERPRISE plan.

        Parameters
        ----------
        q : str
            Search term, e.g., person, place, topic...

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RelatedSearchesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.search_api.get_related_searches(
                q="evergrande",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_related_searches(q=q, request_options=request_options)
        return _response.data

    async def search(
        self,
        *,
        q: str,
        sort_by_date: typing.Optional[int] = None,
        type: typing.Optional[SearchRequestType] = None,
        offset: typing.Optional[int] = None,
        len_min: typing.Optional[int] = None,
        len_max: typing.Optional[int] = None,
        episode_count_min: typing.Optional[int] = None,
        episode_count_max: typing.Optional[int] = None,
        update_freq_min: typing.Optional[int] = None,
        update_freq_max: typing.Optional[int] = None,
        genre_ids: typing.Optional[str] = None,
        published_before: typing.Optional[int] = None,
        published_after: typing.Optional[int] = None,
        only_in: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        ocid: typing.Optional[str] = None,
        ncid: typing.Optional[str] = None,
        safe_mode: typing.Optional[int] = None,
        unique_podcasts: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchResponse:
        """
        Full-text search on episodes, podcasts, or curated lists of podcasts.
        Use the `offset` parameter to paginate through search results.
        The FREE plan allows to see up to 30 search results (or `offset` < 30) per query.
        The PRO plan allows to see up to 300 search results (or `offset` < 300) per query.
        The ENTERPRISE plan allows to see up to 10,000 search results (or `offset` < 10000) per query.

        Parameters
        ----------
        q : str
            Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., "game of thrones". Otherwise, it's fuzzy search.

        sort_by_date : typing.Optional[int]
            Sort by date or not? If 0, then sort by relevance. If 1, then sort by date.

        type : typing.Optional[SearchRequestType]
            What type of contents do you want to search for?

        offset : typing.Optional[int]
            Offset for search results, for pagination. You'll use **next_offset** from response for this parameter.

        len_min : typing.Optional[int]
            Minimum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**.
            If **type** parameter is **episode**, it's for audio length of an episode.
            If **type** parameter is **podcast**, it's for average audio length of all episodes in a podcast.

        len_max : typing.Optional[int]
            Maximum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**.
            If **type** parameter is **episode**, it's for audio length of an episode.
            If **type** parameter is **podcast**, it's for average audio length of all episodes in a podcast.

        episode_count_min : typing.Optional[int]
            Minimum number of episodes. Applicable only when type parameter is **podcast**.

        episode_count_max : typing.Optional[int]
            Maximum number of episodes. Applicable only when type parameter is **podcast**.

        update_freq_min : typing.Optional[int]
            Minimum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find "weekly" podcasts, then you can set **update_freq_min**=144 hours (or 6 days) and **update_freq_max**=192 hours (or 8 days). Applicable only when type parameter is **podcast**.

        update_freq_max : typing.Optional[int]
            Maximum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find "weekly" podcasts, then you can set **update_freq_min**=144 hours (or 6 days) and **update_freq_max**=192 hours (or 8 days). Applicable only when type parameter is **podcast**.

        genre_ids : typing.Optional[str]
            A comma-delimited string of a list of genre ids. If not specified, then all genres are included. You can find the id and the name of all genres from `GET /genres`. It works only when **type** is *episode* or *podcast*.

        published_before : typing.Optional[int]
            Only show episodes/podcasts/curated lists published before this timestamp (in milliseconds). If **published_before** & **published_after** are used at the same time, **published_before** should be bigger than **published_after**.

        published_after : typing.Optional[int]
            Only show episodes/podcasts/curated lists published after this timestamp (in milliseconds). If **published_before** & **published_after** are used at the same time, **published_before** should be bigger than **published_after**.

        only_in : typing.Optional[str]
            A comma-delimited string to search only in specific fields. Allowed values are title, description, author, and audio. If not specified, then search every fields.

        language : typing.Optional[str]
            Limit search results to a specific language. If not specified, it'll be any language. You can get a list of supported languages from `GET /languages`. It works only when **type** is *episode* or *podcast*.

        region : typing.Optional[str]
            Limit search results to a specific region (e.g., us, gb, in...). If not specified, it'll be any region. You can get the supported country codes from `GET /regions`. It works only when **type** is *episode* or *podcast*.

        ocid : typing.Optional[str]
            A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to limit search results from only a few specific podcasts. It works only when **type** is *episode*.

        ncid : typing.Optional[str]
            A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to exclude search results of a few specific podcasts. It works only when **type** is *episode*.

        safe_mode : typing.Optional[int]
            Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **type** is *episode* or *podcast*.

        unique_podcasts : typing.Optional[int]
            Whether or not to keep only one episode per podcast in search results. 1 is yes and 0 is no. It works only when **type** is *episode*.

        page_size : typing.Optional[int]
            The maximum number of search results per page. A valid value should be an integer between 1 and 10 (inclusive).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.search_api.search(
                q="star wars",
                sort_by_date=0,
                offset=0,
                len_min=10,
                len_max=30,
                genre_ids="68,82",
                published_before=1580172454000,
                published_after=0,
                only_in="title,description",
                language="English",
                region="",
                safe_mode=0,
                unique_podcasts=0,
                page_size=10,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search(
            q=q,
            sort_by_date=sort_by_date,
            type=type,
            offset=offset,
            len_min=len_min,
            len_max=len_max,
            episode_count_min=episode_count_min,
            episode_count_max=episode_count_max,
            update_freq_min=update_freq_min,
            update_freq_max=update_freq_max,
            genre_ids=genre_ids,
            published_before=published_before,
            published_after=published_after,
            only_in=only_in,
            language=language,
            region=region,
            ocid=ocid,
            ncid=ncid,
            safe_mode=safe_mode,
            unique_podcasts=unique_podcasts,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    async def spellcheck(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SpellCheckResponse:
        """
        Suggest a list of words that correct the spelling errors of a search term. This endpoint is available only in the PRO/ENTERPRISE plan.

        Parameters
        ----------
        q : str
            Search term, e.g., person, place, topic...

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpellCheckResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.search_api.spellcheck(
                q="evergrand stok",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.spellcheck(q=q, request_options=request_options)
        return _response.data

    async def get_trending_searches(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrendingSearchesResponse:
        """
        Fetch up to 10 most recent trending search terms on the Listen Notes platform.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrendingSearchesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.search_api.get_trending_searches()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_trending_searches(request_options=request_options)
        return _response.data

    async def typeahead(
        self,
        *,
        q: str,
        show_podcasts: typing.Optional[int] = None,
        show_genres: typing.Optional[int] = None,
        safe_mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TypeaheadResponse:
        """
        Suggest search terms, podcast genres, and podcasts.

        Parameters
        ----------
        q : str
            Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., "game of thrones". Otherwise, it's fuzzy search.

        show_podcasts : typing.Optional[int]
            Autosuggest podcasts. This only searches podcast title and publisher and returns very limited info of 5 podcasts. 1 is yes, 0 is no. It's a bit slow to autosuggest podcasts, so we turn it off by default. If show_podcasts=1, you can also pass iTunes id (e.g., 474722933) to the q parameter to fetch podcast meta data.

        show_genres : typing.Optional[int]
            Whether or not to autosuggest genres. 1 is yes, 0 is no.

        safe_mode : typing.Optional[int]
            Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **show_podcasts** is *1*.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TypeaheadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.search_api.typeahead(
                q="star wars",
                show_podcasts=1,
                show_genres=1,
                safe_mode=0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.typeahead(
            q=q,
            show_podcasts=show_podcasts,
            show_genres=show_genres,
            safe_mode=safe_mode,
            request_options=request_options,
        )
        return _response.data
