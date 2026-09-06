

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.auto_download_episodes import AutoDownloadEpisodes
from ..types.folder_id import FolderId
from ..types.library_id import LibraryId
from ..types.library_item_id import LibraryItemId
from ..types.podcast import Podcast
from ..types.podcast_episode import PodcastEpisode
from ..types.podcast_id import PodcastId
from ..types.podcast_metadata import PodcastMetadata
from .raw_client import AsyncRawPodcastsClient, RawPodcastsClient
from .types.check_new_episodes_response import CheckNewEpisodesResponse
from .types.find_episode_response import FindEpisodeResponse
from .types.get_episode_downloads_response import GetEpisodeDownloadsResponse
from .types.get_feeds_from_opml_text_response import GetFeedsFromOpmlTextResponse
from .types.get_podcast_feed_response import GetPodcastFeedResponse
from .types.quick_match_episodes_response import QuickMatchEpisodesResponse


OMIT = typing.cast(typing.Any, ...)


class PodcastsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPodcastsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPodcastsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPodcastsClient
        """
        return self._raw_client

    def create_podcast(
        self,
        *,
        id: typing.Optional[PodcastId] = OMIT,
        library_item_id: typing.Optional[LibraryItemId] = OMIT,
        metadata: typing.Optional[PodcastMetadata] = OMIT,
        cover_path: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        episodes: typing.Optional[typing.Sequence[PodcastEpisode]] = OMIT,
        auto_download_episodes: typing.Optional[AutoDownloadEpisodes] = OMIT,
        auto_download_schedule: typing.Optional[str] = OMIT,
        last_episode_check: typing.Optional[int] = OMIT,
        max_episodes_to_keep: typing.Optional[int] = OMIT,
        max_new_episodes_to_download: typing.Optional[int] = OMIT,
        last_cover_search: typing.Optional[int] = OMIT,
        last_cover_search_query: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        duration: typing.Optional[int] = OMIT,
        num_tracks: typing.Optional[int] = OMIT,
        latest_episode_published: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Podcast:
        """
        Parameters
        ----------
        id : typing.Optional[PodcastId]

        library_item_id : typing.Optional[LibraryItemId]

        metadata : typing.Optional[PodcastMetadata]

        cover_path : typing.Optional[str]
            The file path to the podcast's cover image.

        tags : typing.Optional[typing.Sequence[str]]
            The tags associated with the podcast.

        episodes : typing.Optional[typing.Sequence[PodcastEpisode]]
            The episodes of the podcast.

        auto_download_episodes : typing.Optional[AutoDownloadEpisodes]

        auto_download_schedule : typing.Optional[str]
            The schedule for automatic episode downloads, in cron format.

        last_episode_check : typing.Optional[int]
            The timestamp of the last episode check.

        max_episodes_to_keep : typing.Optional[int]
            The maximum number of episodes to keep.

        max_new_episodes_to_download : typing.Optional[int]
            The maximum number of new episodes to download when automatically downloading epsiodes.

        last_cover_search : typing.Optional[int]
            The timestamp of the last cover search.

        last_cover_search_query : typing.Optional[str]
            The query used for the last cover search.

        size : typing.Optional[int]
            The total size of all episodes in bytes.

        duration : typing.Optional[int]
            The total duration of all episodes in seconds.

        num_tracks : typing.Optional[int]
            The number of tracks (episodes) in the podcast.

        latest_episode_published : typing.Optional[int]
            The timestamp of the most recently published episode.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Podcast
            Successfully created a podcast

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.podcasts.create_podcast()
        """
        _response = self._raw_client.create_podcast(
            id=id,
            library_item_id=library_item_id,
            metadata=metadata,
            cover_path=cover_path,
            tags=tags,
            episodes=episodes,
            auto_download_episodes=auto_download_episodes,
            auto_download_schedule=auto_download_schedule,
            last_episode_check=last_episode_check,
            max_episodes_to_keep=max_episodes_to_keep,
            max_new_episodes_to_download=max_new_episodes_to_download,
            last_cover_search=last_cover_search,
            last_cover_search_query=last_cover_search_query,
            size=size,
            duration=duration,
            num_tracks=num_tracks,
            latest_episode_published=latest_episode_published,
            request_options=request_options,
        )
        return _response.data

    def get_podcast_feed(
        self, *, rss_feed: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPodcastFeedResponse:
        """
        Parameters
        ----------
        rss_feed : typing.Optional[str]
            The RSS feed URL of the podcast

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPodcastFeedResponse
            Successfully retrieved podcast feed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.podcasts.get_podcast_feed()
        """
        _response = self._raw_client.get_podcast_feed(rss_feed=rss_feed, request_options=request_options)
        return _response.data

    def get_feeds_from_opml_text(
        self, *, opml_text: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFeedsFromOpmlTextResponse:
        """
        Parse OPML text and return an array of feeds

        Parameters
        ----------
        opml_text : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFeedsFromOpmlTextResponse
            Successfully parsed OPML text and returned feeds

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.podcasts.get_feeds_from_opml_text()
        """
        _response = self._raw_client.get_feeds_from_opml_text(opml_text=opml_text, request_options=request_options)
        return _response.data

    def bulk_create_podcasts_from_opml_feed_urls(
        self,
        *,
        feeds: typing.Optional[typing.Sequence[str]] = OMIT,
        library_id: typing.Optional[LibraryId] = OMIT,
        folder_id: typing.Optional[FolderId] = OMIT,
        auto_download_episodes: typing.Optional[AutoDownloadEpisodes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        feeds : typing.Optional[typing.Sequence[str]]

        library_id : typing.Optional[LibraryId]

        folder_id : typing.Optional[FolderId]

        auto_download_episodes : typing.Optional[AutoDownloadEpisodes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.podcasts.bulk_create_podcasts_from_opml_feed_urls()
        """
        _response = self._raw_client.bulk_create_podcasts_from_opml_feed_urls(
            feeds=feeds,
            library_id=library_id,
            folder_id=folder_id,
            auto_download_episodes=auto_download_episodes,
            request_options=request_options,
        )
        return _response.data

    def check_new_episodes(
        self,
        id: PodcastId,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckNewEpisodesResponse:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        limit : typing.Optional[int]
            Maximum number of episodes to download

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckNewEpisodesResponse
            Successfully checked and downloaded new episodes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.podcasts.check_new_episodes(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.check_new_episodes(id, limit=limit, request_options=request_options)
        return _response.data

    def clear_episode_download_queue(
        self, id: PodcastId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.podcasts.clear_episode_download_queue(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.clear_episode_download_queue(id, request_options=request_options)
        return _response.data

    def get_episode_downloads(
        self, id: PodcastId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetEpisodeDownloadsResponse:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEpisodeDownloadsResponse
            Successfully retrieved episode downloads

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.podcasts.get_episode_downloads(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.get_episode_downloads(id, request_options=request_options)
        return _response.data

    def find_episode(
        self, id: PodcastId, *, title: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FindEpisodeResponse:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        title : str
            Title of the episode to search for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FindEpisodeResponse
            Successfully found episodes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.podcasts.find_episode(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            title="title",
        )
        """
        _response = self._raw_client.find_episode(id, title=title, request_options=request_options)
        return _response.data

    def download_episodes(
        self, id: PodcastId, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.podcasts.download_episodes(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            request=["string"],
        )
        """
        _response = self._raw_client.download_episodes(id, request=request, request_options=request_options)
        return _response.data

    def quick_match_episodes(
        self,
        id: PodcastId,
        *,
        override: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QuickMatchEpisodesResponse:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        override : typing.Optional[str]
            Override existing details if set to 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QuickMatchEpisodesResponse
            Successfully matched episodes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.podcasts.quick_match_episodes(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.quick_match_episodes(id, override=override, request_options=request_options)
        return _response.data

    def get_episode(
        self, id: PodcastId, episode_id: PodcastId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PodcastEpisode:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        episode_id : PodcastId
            Episode ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PodcastEpisode
            Successfully retrieved episode

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.podcasts.get_episode(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            episode_id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.get_episode(id, episode_id, request_options=request_options)
        return _response.data

    def remove_episode(
        self,
        id: PodcastId,
        episode_id: PodcastId,
        *,
        hard: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Podcast:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        episode_id : PodcastId
            Episode ID

        hard : typing.Optional[str]
            Hard delete the episode if set to 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Podcast
            Successfully removed episode

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.podcasts.remove_episode(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            episode_id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
        )
        """
        _response = self._raw_client.remove_episode(id, episode_id, hard=hard, request_options=request_options)
        return _response.data

    def update_episode(
        self,
        id: PodcastId,
        episode_id: PodcastId,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Podcast:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        episode_id : PodcastId
            Episode ID

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Podcast
            Successfully updated episode

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.podcasts.update_episode(
            id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            episode_id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.update_episode(id, episode_id, request=request, request_options=request_options)
        return _response.data


class AsyncPodcastsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPodcastsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPodcastsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPodcastsClient
        """
        return self._raw_client

    async def create_podcast(
        self,
        *,
        id: typing.Optional[PodcastId] = OMIT,
        library_item_id: typing.Optional[LibraryItemId] = OMIT,
        metadata: typing.Optional[PodcastMetadata] = OMIT,
        cover_path: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        episodes: typing.Optional[typing.Sequence[PodcastEpisode]] = OMIT,
        auto_download_episodes: typing.Optional[AutoDownloadEpisodes] = OMIT,
        auto_download_schedule: typing.Optional[str] = OMIT,
        last_episode_check: typing.Optional[int] = OMIT,
        max_episodes_to_keep: typing.Optional[int] = OMIT,
        max_new_episodes_to_download: typing.Optional[int] = OMIT,
        last_cover_search: typing.Optional[int] = OMIT,
        last_cover_search_query: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        duration: typing.Optional[int] = OMIT,
        num_tracks: typing.Optional[int] = OMIT,
        latest_episode_published: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Podcast:
        """
        Parameters
        ----------
        id : typing.Optional[PodcastId]

        library_item_id : typing.Optional[LibraryItemId]

        metadata : typing.Optional[PodcastMetadata]

        cover_path : typing.Optional[str]
            The file path to the podcast's cover image.

        tags : typing.Optional[typing.Sequence[str]]
            The tags associated with the podcast.

        episodes : typing.Optional[typing.Sequence[PodcastEpisode]]
            The episodes of the podcast.

        auto_download_episodes : typing.Optional[AutoDownloadEpisodes]

        auto_download_schedule : typing.Optional[str]
            The schedule for automatic episode downloads, in cron format.

        last_episode_check : typing.Optional[int]
            The timestamp of the last episode check.

        max_episodes_to_keep : typing.Optional[int]
            The maximum number of episodes to keep.

        max_new_episodes_to_download : typing.Optional[int]
            The maximum number of new episodes to download when automatically downloading epsiodes.

        last_cover_search : typing.Optional[int]
            The timestamp of the last cover search.

        last_cover_search_query : typing.Optional[str]
            The query used for the last cover search.

        size : typing.Optional[int]
            The total size of all episodes in bytes.

        duration : typing.Optional[int]
            The total duration of all episodes in seconds.

        num_tracks : typing.Optional[int]
            The number of tracks (episodes) in the podcast.

        latest_episode_published : typing.Optional[int]
            The timestamp of the most recently published episode.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Podcast
            Successfully created a podcast

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.podcasts.create_podcast()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_podcast(
            id=id,
            library_item_id=library_item_id,
            metadata=metadata,
            cover_path=cover_path,
            tags=tags,
            episodes=episodes,
            auto_download_episodes=auto_download_episodes,
            auto_download_schedule=auto_download_schedule,
            last_episode_check=last_episode_check,
            max_episodes_to_keep=max_episodes_to_keep,
            max_new_episodes_to_download=max_new_episodes_to_download,
            last_cover_search=last_cover_search,
            last_cover_search_query=last_cover_search_query,
            size=size,
            duration=duration,
            num_tracks=num_tracks,
            latest_episode_published=latest_episode_published,
            request_options=request_options,
        )
        return _response.data

    async def get_podcast_feed(
        self, *, rss_feed: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPodcastFeedResponse:
        """
        Parameters
        ----------
        rss_feed : typing.Optional[str]
            The RSS feed URL of the podcast

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPodcastFeedResponse
            Successfully retrieved podcast feed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.podcasts.get_podcast_feed()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_podcast_feed(rss_feed=rss_feed, request_options=request_options)
        return _response.data

    async def get_feeds_from_opml_text(
        self, *, opml_text: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFeedsFromOpmlTextResponse:
        """
        Parse OPML text and return an array of feeds

        Parameters
        ----------
        opml_text : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFeedsFromOpmlTextResponse
            Successfully parsed OPML text and returned feeds

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.podcasts.get_feeds_from_opml_text()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_feeds_from_opml_text(
            opml_text=opml_text, request_options=request_options
        )
        return _response.data

    async def bulk_create_podcasts_from_opml_feed_urls(
        self,
        *,
        feeds: typing.Optional[typing.Sequence[str]] = OMIT,
        library_id: typing.Optional[LibraryId] = OMIT,
        folder_id: typing.Optional[FolderId] = OMIT,
        auto_download_episodes: typing.Optional[AutoDownloadEpisodes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        feeds : typing.Optional[typing.Sequence[str]]

        library_id : typing.Optional[LibraryId]

        folder_id : typing.Optional[FolderId]

        auto_download_episodes : typing.Optional[AutoDownloadEpisodes]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.podcasts.bulk_create_podcasts_from_opml_feed_urls()


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_create_podcasts_from_opml_feed_urls(
            feeds=feeds,
            library_id=library_id,
            folder_id=folder_id,
            auto_download_episodes=auto_download_episodes,
            request_options=request_options,
        )
        return _response.data

    async def check_new_episodes(
        self,
        id: PodcastId,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckNewEpisodesResponse:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        limit : typing.Optional[int]
            Maximum number of episodes to download

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckNewEpisodesResponse
            Successfully checked and downloaded new episodes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.podcasts.check_new_episodes(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_new_episodes(id, limit=limit, request_options=request_options)
        return _response.data

    async def clear_episode_download_queue(
        self, id: PodcastId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.podcasts.clear_episode_download_queue(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clear_episode_download_queue(id, request_options=request_options)
        return _response.data

    async def get_episode_downloads(
        self, id: PodcastId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetEpisodeDownloadsResponse:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEpisodeDownloadsResponse
            Successfully retrieved episode downloads

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.podcasts.get_episode_downloads(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_episode_downloads(id, request_options=request_options)
        return _response.data

    async def find_episode(
        self, id: PodcastId, *, title: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FindEpisodeResponse:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        title : str
            Title of the episode to search for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FindEpisodeResponse
            Successfully found episodes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.podcasts.find_episode(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
                title="title",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_episode(id, title=title, request_options=request_options)
        return _response.data

    async def download_episodes(
        self, id: PodcastId, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        request : typing.Sequence[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.podcasts.download_episodes(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_episodes(id, request=request, request_options=request_options)
        return _response.data

    async def quick_match_episodes(
        self,
        id: PodcastId,
        *,
        override: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QuickMatchEpisodesResponse:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        override : typing.Optional[str]
            Override existing details if set to 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QuickMatchEpisodesResponse
            Successfully matched episodes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.podcasts.quick_match_episodes(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.quick_match_episodes(id, override=override, request_options=request_options)
        return _response.data

    async def get_episode(
        self, id: PodcastId, episode_id: PodcastId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PodcastEpisode:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        episode_id : PodcastId
            Episode ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PodcastEpisode
            Successfully retrieved episode

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.podcasts.get_episode(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
                episode_id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_episode(id, episode_id, request_options=request_options)
        return _response.data

    async def remove_episode(
        self,
        id: PodcastId,
        episode_id: PodcastId,
        *,
        hard: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Podcast:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        episode_id : PodcastId
            Episode ID

        hard : typing.Optional[str]
            Hard delete the episode if set to 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Podcast
            Successfully removed episode

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.podcasts.remove_episode(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
                episode_id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_episode(id, episode_id, hard=hard, request_options=request_options)
        return _response.data

    async def update_episode(
        self,
        id: PodcastId,
        episode_id: PodcastId,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Podcast:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        episode_id : PodcastId
            Episode ID

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Podcast
            Successfully updated episode

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.podcasts.update_episode(
                id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
                episode_id="e4bb1afb-4a4f-4dd6-8be0-e615d233185b",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_episode(
            id, episode_id, request=request, request_options=request_options
        )
        return _response.data
