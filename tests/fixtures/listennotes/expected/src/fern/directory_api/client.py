

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.best_podcasts_response import BestPodcastsResponse
from ..types.curated_list_full import CuratedListFull
from ..types.episode_full import EpisodeFull
from ..types.episode_simple import EpisodeSimple
from ..types.get_curated_podcasts_response import GetCuratedPodcastsResponse
from ..types.get_episode_recommendations_response import GetEpisodeRecommendationsResponse
from ..types.get_episodes_in_batch_response import GetEpisodesInBatchResponse
from ..types.get_genres_response import GetGenresResponse
from ..types.get_languages_response import GetLanguagesResponse
from ..types.get_podcast_recommendations_response import GetPodcastRecommendationsResponse
from ..types.get_podcasts_in_batch_response import GetPodcastsInBatchResponse
from ..types.get_regions_response import GetRegionsResponse
from ..types.podcast_full import PodcastFull
from .raw_client import AsyncRawDirectoryApiClient, RawDirectoryApiClient
from .types.get_best_podcasts_request_sort import GetBestPodcastsRequestSort
from .types.get_podcast_by_id_request_sort import GetPodcastByIdRequestSort


OMIT = typing.cast(typing.Any, ...)


class DirectoryApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDirectoryApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDirectoryApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDirectoryApiClient
        """
        return self._raw_client

    def get_best_podcasts(
        self,
        *,
        genre_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        region: typing.Optional[str] = None,
        publisher_region: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        sort: typing.Optional[GetBestPodcastsRequestSort] = None,
        safe_mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BestPodcastsResponse:
        """
        Get a list of curated best podcasts by genre,
        which are curated by Listen Notes staffs based on various signals from the Internet, e.g.,
        top charts on other podcast platforms, recommendations from mainstream media,
        user activities on listennotes.com...
        You can get the genre ids from `GET /genres` endpoint.
        This endpoint returns same data as https://www.listennotes.com/best-podcasts/

        Parameters
        ----------
        genre_id : typing.Optional[str]
            You can get the id from `GET /genres`. If not specified, it'll be the overall best podcasts, which can be considered as a special genre.

        page : typing.Optional[int]
            Page number of those podcasts in this genre.

        region : typing.Optional[str]
            Filter best podcasts by country/region.
            Please note that podcasts that are "best" in a country/region may not be produced in that country/region.
            For example, a podcast from the US may be very popular in Canada.
            You can get the supported country codes (e.g., us, jp, gb...) from `GET /regions`.
            If not specified, you'll get "best podcasts" in United States.

        publisher_region : typing.Optional[str]
            Filter best podcasts by the publisher's country/region.
            This is to narrow down the results to include "best podcasts" produced in a specific country/region.
            You can get the supported country codes (e.g., us, jp, gb...) from `GET /regions`.
            If not specified, you'll get "best podcasts" produced in any country/region.
            If you want to get a country/region's "best podcasts" that are also produced in that country/region,
            then you need to specify both **region** and **publisher_region**,
            e.g., `region=jp` and `publisher_region=jp`.

        language : typing.Optional[str]
            Filter best podcasts by language.
            You can get a list of supported languages (e.g., English, Chinese, Japanese...) from `GET /languages`.
            If not specified, you'll get "best podcasts" in any language.

        sort : typing.Optional[GetBestPodcastsRequestSort]
            How do you want to sort these podcasts?
            If you'd like to sort by popularity, please use **listen_score**.

        safe_mode : typing.Optional[int]
            Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BestPodcastsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.directory_api.get_best_podcasts(
            page=2,
            region="us",
            safe_mode=0,
        )
        """
        _response = self._raw_client.get_best_podcasts(
            genre_id=genre_id,
            page=page,
            region=region,
            publisher_region=publisher_region,
            language=language,
            sort=sort,
            safe_mode=safe_mode,
            request_options=request_options,
        )
        return _response.data

    def get_curated_podcasts(
        self, *, page: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCuratedPodcastsResponse:
        """
        A bunch of curated lists from online media. For each list, you'll get basic info of up to 5 podcasts. To get detailed meta data of all podcasts in a specific list, you need to use `GET /curated_podcasts/{id}`. We add new curated lists to the database on a daily basis.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number of curated lists.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCuratedPodcastsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.directory_api.get_curated_podcasts()
        """
        _response = self._raw_client.get_curated_podcasts(page=page, request_options=request_options)
        return _response.data

    def get_curated_podcast_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CuratedListFull:
        """
        Get detailed meta data of all podcasts in a specific curated list.
        This endpoint returns same data as https://www.listennotes.com/curated-podcasts/

        Parameters
        ----------
        id : str
            id for a specific curated list of podcasts. You can get the id from the response of `GET /search?type=curated` or `GET /curated_podcasts`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CuratedListFull
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.directory_api.get_curated_podcast_by_id(
            id="SDFKduyJ47r",
        )
        """
        _response = self._raw_client.get_curated_podcast_by_id(id, request_options=request_options)
        return _response.data

    def get_episodes_in_batch(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetEpisodesInBatchResponse:
        """
        Batch fetch basic meta data for up to 10 episodes. This endpoint could be used to implement custom playlists for individual episodes. For detailed meta data of an individual episode, you need to use `GET /episodes/{id}`. This endpoint is available only in the PRO/ENTERPRISE plan.

        Parameters
        ----------
        ids : str
            Comma-separated list of episode ids.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEpisodesInBatchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.directory_api.get_episodes_in_batch(
            ids="c577d55b2b2b483c969fae3ceb58e362,0f34a9099579490993eec9e8c8cebb82",
        )
        """
        _response = self._raw_client.get_episodes_in_batch(ids=ids, request_options=request_options)
        return _response.data

    def get_episode_by_id(
        self,
        id: str,
        *,
        show_transcript: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EpisodeFull:
        """
        Fetch detailed meta data for a specific episode.

        Parameters
        ----------
        id : str
            id for a specific episode. You can get episode id from using other endpoints, e.g., `GET /search`...

        show_transcript : typing.Optional[int]
            To include the transcript of this episode or not? If it is 1, then include the transcript in the **transcript** field. The default value is 0 - we don't include transcript by default, because 1) it would make the response data very big, thus slow response time; 2) less than 1% of episodes have transcripts. The transcript field is available only in the PRO/ENTERPRISE plan.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EpisodeFull
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.directory_api.get_episode_by_id(
            id="6b6d65930c5a4f71b254465871fed370",
            show_transcript=1,
        )
        """
        _response = self._raw_client.get_episode_by_id(
            id, show_transcript=show_transcript, request_options=request_options
        )
        return _response.data

    def get_episode_recommendations(
        self,
        id: str,
        *,
        safe_mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEpisodeRecommendationsResponse:
        """
        Fetch up to 8 episode recommendations based on the given episode id.

        Parameters
        ----------
        id : str
            Episode id.

        safe_mode : typing.Optional[int]
            Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEpisodeRecommendationsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.directory_api.get_episode_recommendations(
            id="254444fa6cf64a43a95292a70eb6869b",
            safe_mode=0,
        )
        """
        _response = self._raw_client.get_episode_recommendations(
            id, safe_mode=safe_mode, request_options=request_options
        )
        return _response.data

    def get_genres(
        self, *, top_level_only: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetGenresResponse:
        """
        Get a list of podcast genres that are supported in Listen Notes.
        The genre id can be passed to other endpoints as a parameter to get podcasts in a specific genre,
        e.g., `GET /best_podcasts`, `GET /search`...
        You may want to cache the list of genres on the client side.

        Parameters
        ----------
        top_level_only : typing.Optional[int]
            Just show top level genres? If 1, yes, just show top level genres. If 0, no, show all genres.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGenresResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.directory_api.get_genres(
            top_level_only=1,
        )
        """
        _response = self._raw_client.get_genres(top_level_only=top_level_only, request_options=request_options)
        return _response.data

    def just_listen(self, *, request_options: typing.Optional[RequestOptions] = None) -> EpisodeSimple:
        """
        Recently published episodes are more likely to be fetched. Good luck!

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EpisodeSimple
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.directory_api.just_listen()
        """
        _response = self._raw_client.just_listen(request_options=request_options)
        return _response.data

    def get_languages(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetLanguagesResponse:
        """
        Get a list of languages that are supported in Listen Notes database. You can use the language string as query parameter in `GET /search`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLanguagesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.directory_api.get_languages()
        """
        _response = self._raw_client.get_languages(request_options=request_options)
        return _response.data

    def get_podcasts_in_batch(
        self,
        *,
        ids: typing.Optional[str] = OMIT,
        itunes_ids: typing.Optional[str] = OMIT,
        next_episode_pub_date: typing.Optional[int] = OMIT,
        rsses: typing.Optional[str] = OMIT,
        show_latest_episodes: typing.Optional[int] = OMIT,
        spotify_ids: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPodcastsInBatchResponse:
        """
        Batch fetch basic meta data for up to 10 podcasts.
        This endpoint could be used to build something like OPML import,
        allowing users to import a bunch of podcasts via rss urls.
        For detailed meta data (including episodes) of an individual podcast, you need to use `GET /podcasts/{id}`. This endpoint is available only in the PRO/ENTERPRISE plan.

        Parameters
        ----------
        ids : typing.Optional[str]
            Comma-separated list of podcast ids.

        itunes_ids : typing.Optional[str]
            Comma-separated Apple Podcasts (iTunes) ids, e.g., 659155419

        next_episode_pub_date : typing.Optional[int]
            For latest episodes pagination. It's the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 15 episodes.

        rsses : typing.Optional[str]
            Comma-separated rss urls.

        show_latest_episodes : typing.Optional[int]
            Whether or not to fetch up to 15 latest episodes from these podcasts, sorted by pub_date. 1 is yes, and 0 is no.

        spotify_ids : typing.Optional[str]
            Comma-separated Spotify ids, e.g., 3DDfEsKDIDrTlnPOiG4ZF4

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPodcastsInBatchResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.directory_api.get_podcasts_in_batch()
        """
        _response = self._raw_client.get_podcasts_in_batch(
            ids=ids,
            itunes_ids=itunes_ids,
            next_episode_pub_date=next_episode_pub_date,
            rsses=rsses,
            show_latest_episodes=show_latest_episodes,
            spotify_ids=spotify_ids,
            request_options=request_options,
        )
        return _response.data

    def get_podcast_by_id(
        self,
        id: str,
        *,
        next_episode_pub_date: typing.Optional[int] = None,
        sort: typing.Optional[GetPodcastByIdRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PodcastFull:
        """
        Fetch detailed meta data and episodes for a specific podcast (up to 10 episodes each time).
        You can use the **next_episode_pub_date** parameter to do pagination and fetch more episodes.

        Parameters
        ----------
        id : str
            Podcast id. You can get podcast id from using other endpoints, e.g., `GET /search`, `GET /best_podcasts`...

        next_episode_pub_date : typing.Optional[int]
            For episodes pagination. It's the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 10 episodes or oldest 10 episodes, depending on the value of the **sort** parameter.

        sort : typing.Optional[GetPodcastByIdRequestSort]
            How do you want to sort the episodes of this podcast?

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PodcastFull
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.directory_api.get_podcast_by_id(
            id="4d3fe717742d4963a85562e9f84d8c79",
        )
        """
        _response = self._raw_client.get_podcast_by_id(
            id, next_episode_pub_date=next_episode_pub_date, sort=sort, request_options=request_options
        )
        return _response.data

    def get_podcast_recommendations(
        self,
        id: str,
        *,
        safe_mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPodcastRecommendationsResponse:
        """
        Fetch up to 8 podcast recommendations based on the given podcast id.

        Parameters
        ----------
        id : str
            Podcast id.

        safe_mode : typing.Optional[int]
            Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPodcastRecommendationsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.directory_api.get_podcast_recommendations(
            id="25212ac3c53240a880dd5032e547047b",
            safe_mode=0,
        )
        """
        _response = self._raw_client.get_podcast_recommendations(
            id, safe_mode=safe_mode, request_options=request_options
        )
        return _response.data

    def get_regions(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetRegionsResponse:
        """
        It returns a dictionary of country codes (e.g., us, gb...) & country names (United States, United Kingdom...). The country code is used in the query parameter **region** of `GET /best_podcasts`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRegionsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.directory_api.get_regions()
        """
        _response = self._raw_client.get_regions(request_options=request_options)
        return _response.data


class AsyncDirectoryApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDirectoryApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDirectoryApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDirectoryApiClient
        """
        return self._raw_client

    async def get_best_podcasts(
        self,
        *,
        genre_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        region: typing.Optional[str] = None,
        publisher_region: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        sort: typing.Optional[GetBestPodcastsRequestSort] = None,
        safe_mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BestPodcastsResponse:
        """
        Get a list of curated best podcasts by genre,
        which are curated by Listen Notes staffs based on various signals from the Internet, e.g.,
        top charts on other podcast platforms, recommendations from mainstream media,
        user activities on listennotes.com...
        You can get the genre ids from `GET /genres` endpoint.
        This endpoint returns same data as https://www.listennotes.com/best-podcasts/

        Parameters
        ----------
        genre_id : typing.Optional[str]
            You can get the id from `GET /genres`. If not specified, it'll be the overall best podcasts, which can be considered as a special genre.

        page : typing.Optional[int]
            Page number of those podcasts in this genre.

        region : typing.Optional[str]
            Filter best podcasts by country/region.
            Please note that podcasts that are "best" in a country/region may not be produced in that country/region.
            For example, a podcast from the US may be very popular in Canada.
            You can get the supported country codes (e.g., us, jp, gb...) from `GET /regions`.
            If not specified, you'll get "best podcasts" in United States.

        publisher_region : typing.Optional[str]
            Filter best podcasts by the publisher's country/region.
            This is to narrow down the results to include "best podcasts" produced in a specific country/region.
            You can get the supported country codes (e.g., us, jp, gb...) from `GET /regions`.
            If not specified, you'll get "best podcasts" produced in any country/region.
            If you want to get a country/region's "best podcasts" that are also produced in that country/region,
            then you need to specify both **region** and **publisher_region**,
            e.g., `region=jp` and `publisher_region=jp`.

        language : typing.Optional[str]
            Filter best podcasts by language.
            You can get a list of supported languages (e.g., English, Chinese, Japanese...) from `GET /languages`.
            If not specified, you'll get "best podcasts" in any language.

        sort : typing.Optional[GetBestPodcastsRequestSort]
            How do you want to sort these podcasts?
            If you'd like to sort by popularity, please use **listen_score**.

        safe_mode : typing.Optional[int]
            Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BestPodcastsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.directory_api.get_best_podcasts(
                page=2,
                region="us",
                safe_mode=0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_best_podcasts(
            genre_id=genre_id,
            page=page,
            region=region,
            publisher_region=publisher_region,
            language=language,
            sort=sort,
            safe_mode=safe_mode,
            request_options=request_options,
        )
        return _response.data

    async def get_curated_podcasts(
        self, *, page: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCuratedPodcastsResponse:
        """
        A bunch of curated lists from online media. For each list, you'll get basic info of up to 5 podcasts. To get detailed meta data of all podcasts in a specific list, you need to use `GET /curated_podcasts/{id}`. We add new curated lists to the database on a daily basis.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number of curated lists.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCuratedPodcastsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.directory_api.get_curated_podcasts()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_curated_podcasts(page=page, request_options=request_options)
        return _response.data

    async def get_curated_podcast_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CuratedListFull:
        """
        Get detailed meta data of all podcasts in a specific curated list.
        This endpoint returns same data as https://www.listennotes.com/curated-podcasts/

        Parameters
        ----------
        id : str
            id for a specific curated list of podcasts. You can get the id from the response of `GET /search?type=curated` or `GET /curated_podcasts`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CuratedListFull
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.directory_api.get_curated_podcast_by_id(
                id="SDFKduyJ47r",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_curated_podcast_by_id(id, request_options=request_options)
        return _response.data

    async def get_episodes_in_batch(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetEpisodesInBatchResponse:
        """
        Batch fetch basic meta data for up to 10 episodes. This endpoint could be used to implement custom playlists for individual episodes. For detailed meta data of an individual episode, you need to use `GET /episodes/{id}`. This endpoint is available only in the PRO/ENTERPRISE plan.

        Parameters
        ----------
        ids : str
            Comma-separated list of episode ids.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEpisodesInBatchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.directory_api.get_episodes_in_batch(
                ids="c577d55b2b2b483c969fae3ceb58e362,0f34a9099579490993eec9e8c8cebb82",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_episodes_in_batch(ids=ids, request_options=request_options)
        return _response.data

    async def get_episode_by_id(
        self,
        id: str,
        *,
        show_transcript: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EpisodeFull:
        """
        Fetch detailed meta data for a specific episode.

        Parameters
        ----------
        id : str
            id for a specific episode. You can get episode id from using other endpoints, e.g., `GET /search`...

        show_transcript : typing.Optional[int]
            To include the transcript of this episode or not? If it is 1, then include the transcript in the **transcript** field. The default value is 0 - we don't include transcript by default, because 1) it would make the response data very big, thus slow response time; 2) less than 1% of episodes have transcripts. The transcript field is available only in the PRO/ENTERPRISE plan.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EpisodeFull
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.directory_api.get_episode_by_id(
                id="6b6d65930c5a4f71b254465871fed370",
                show_transcript=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_episode_by_id(
            id, show_transcript=show_transcript, request_options=request_options
        )
        return _response.data

    async def get_episode_recommendations(
        self,
        id: str,
        *,
        safe_mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEpisodeRecommendationsResponse:
        """
        Fetch up to 8 episode recommendations based on the given episode id.

        Parameters
        ----------
        id : str
            Episode id.

        safe_mode : typing.Optional[int]
            Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEpisodeRecommendationsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.directory_api.get_episode_recommendations(
                id="254444fa6cf64a43a95292a70eb6869b",
                safe_mode=0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_episode_recommendations(
            id, safe_mode=safe_mode, request_options=request_options
        )
        return _response.data

    async def get_genres(
        self, *, top_level_only: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetGenresResponse:
        """
        Get a list of podcast genres that are supported in Listen Notes.
        The genre id can be passed to other endpoints as a parameter to get podcasts in a specific genre,
        e.g., `GET /best_podcasts`, `GET /search`...
        You may want to cache the list of genres on the client side.

        Parameters
        ----------
        top_level_only : typing.Optional[int]
            Just show top level genres? If 1, yes, just show top level genres. If 0, no, show all genres.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGenresResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.directory_api.get_genres(
                top_level_only=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_genres(top_level_only=top_level_only, request_options=request_options)
        return _response.data

    async def just_listen(self, *, request_options: typing.Optional[RequestOptions] = None) -> EpisodeSimple:
        """
        Recently published episodes are more likely to be fetched. Good luck!

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EpisodeSimple
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.directory_api.just_listen()


        asyncio.run(main())
        """
        _response = await self._raw_client.just_listen(request_options=request_options)
        return _response.data

    async def get_languages(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetLanguagesResponse:
        """
        Get a list of languages that are supported in Listen Notes database. You can use the language string as query parameter in `GET /search`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLanguagesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.directory_api.get_languages()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_languages(request_options=request_options)
        return _response.data

    async def get_podcasts_in_batch(
        self,
        *,
        ids: typing.Optional[str] = OMIT,
        itunes_ids: typing.Optional[str] = OMIT,
        next_episode_pub_date: typing.Optional[int] = OMIT,
        rsses: typing.Optional[str] = OMIT,
        show_latest_episodes: typing.Optional[int] = OMIT,
        spotify_ids: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPodcastsInBatchResponse:
        """
        Batch fetch basic meta data for up to 10 podcasts.
        This endpoint could be used to build something like OPML import,
        allowing users to import a bunch of podcasts via rss urls.
        For detailed meta data (including episodes) of an individual podcast, you need to use `GET /podcasts/{id}`. This endpoint is available only in the PRO/ENTERPRISE plan.

        Parameters
        ----------
        ids : typing.Optional[str]
            Comma-separated list of podcast ids.

        itunes_ids : typing.Optional[str]
            Comma-separated Apple Podcasts (iTunes) ids, e.g., 659155419

        next_episode_pub_date : typing.Optional[int]
            For latest episodes pagination. It's the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 15 episodes.

        rsses : typing.Optional[str]
            Comma-separated rss urls.

        show_latest_episodes : typing.Optional[int]
            Whether or not to fetch up to 15 latest episodes from these podcasts, sorted by pub_date. 1 is yes, and 0 is no.

        spotify_ids : typing.Optional[str]
            Comma-separated Spotify ids, e.g., 3DDfEsKDIDrTlnPOiG4ZF4

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPodcastsInBatchResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.directory_api.get_podcasts_in_batch()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_podcasts_in_batch(
            ids=ids,
            itunes_ids=itunes_ids,
            next_episode_pub_date=next_episode_pub_date,
            rsses=rsses,
            show_latest_episodes=show_latest_episodes,
            spotify_ids=spotify_ids,
            request_options=request_options,
        )
        return _response.data

    async def get_podcast_by_id(
        self,
        id: str,
        *,
        next_episode_pub_date: typing.Optional[int] = None,
        sort: typing.Optional[GetPodcastByIdRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PodcastFull:
        """
        Fetch detailed meta data and episodes for a specific podcast (up to 10 episodes each time).
        You can use the **next_episode_pub_date** parameter to do pagination and fetch more episodes.

        Parameters
        ----------
        id : str
            Podcast id. You can get podcast id from using other endpoints, e.g., `GET /search`, `GET /best_podcasts`...

        next_episode_pub_date : typing.Optional[int]
            For episodes pagination. It's the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 10 episodes or oldest 10 episodes, depending on the value of the **sort** parameter.

        sort : typing.Optional[GetPodcastByIdRequestSort]
            How do you want to sort the episodes of this podcast?

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PodcastFull
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.directory_api.get_podcast_by_id(
                id="4d3fe717742d4963a85562e9f84d8c79",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_podcast_by_id(
            id, next_episode_pub_date=next_episode_pub_date, sort=sort, request_options=request_options
        )
        return _response.data

    async def get_podcast_recommendations(
        self,
        id: str,
        *,
        safe_mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPodcastRecommendationsResponse:
        """
        Fetch up to 8 podcast recommendations based on the given podcast id.

        Parameters
        ----------
        id : str
            Podcast id.

        safe_mode : typing.Optional[int]
            Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPodcastRecommendationsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.directory_api.get_podcast_recommendations(
                id="25212ac3c53240a880dd5032e547047b",
                safe_mode=0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_podcast_recommendations(
            id, safe_mode=safe_mode, request_options=request_options
        )
        return _response.data

    async def get_regions(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetRegionsResponse:
        """
        It returns a dictionary of country codes (e.g., us, gb...) & country names (United States, United Kingdom...). The country code is used in the query parameter **region** of `GET /best_podcasts`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRegionsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.directory_api.get_regions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_regions(request_options=request_options)
        return _response.data
