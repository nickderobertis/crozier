

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.auto_download_episodes import AutoDownloadEpisodes
from ..types.folder_id import FolderId
from ..types.library_id import LibraryId
from ..types.library_item_id import LibraryItemId
from ..types.podcast import Podcast
from ..types.podcast_episode import PodcastEpisode
from ..types.podcast_id import PodcastId
from ..types.podcast_metadata import PodcastMetadata
from .types.check_new_episodes_response import CheckNewEpisodesResponse
from .types.find_episode_response import FindEpisodeResponse
from .types.get_episode_downloads_response import GetEpisodeDownloadsResponse
from .types.get_feeds_from_opml_text_response import GetFeedsFromOpmlTextResponse
from .types.get_podcast_feed_response import GetPodcastFeedResponse
from .types.quick_match_episodes_response import QuickMatchEpisodesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPodcastsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[Podcast]:
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
        HttpResponse[Podcast]
            Successfully created a podcast
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/podcasts",
            method="POST",
            json={
                "id": id,
                "libraryItemId": library_item_id,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=PodcastMetadata, direction="write"
                ),
                "coverPath": cover_path,
                "tags": tags,
                "episodes": convert_and_respect_annotation_metadata(
                    object_=episodes, annotation=typing.Sequence[PodcastEpisode], direction="write"
                ),
                "autoDownloadEpisodes": auto_download_episodes,
                "autoDownloadSchedule": auto_download_schedule,
                "lastEpisodeCheck": last_episode_check,
                "maxEpisodesToKeep": max_episodes_to_keep,
                "maxNewEpisodesToDownload": max_new_episodes_to_download,
                "lastCoverSearch": last_cover_search,
                "lastCoverSearchQuery": last_cover_search_query,
                "size": size,
                "duration": duration,
                "numTracks": num_tracks,
                "latestEpisodePublished": latest_episode_published,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Podcast,
                    parse_obj_as(
                        type_=Podcast,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_podcast_feed(
        self, *, rss_feed: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetPodcastFeedResponse]:
        """
        Parameters
        ----------
        rss_feed : typing.Optional[str]
            The RSS feed URL of the podcast

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPodcastFeedResponse]
            Successfully retrieved podcast feed
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/podcasts/feed",
            method="POST",
            json={
                "rssFeed": rss_feed,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPodcastFeedResponse,
                    parse_obj_as(
                        type_=GetPodcastFeedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_feeds_from_opml_text(
        self, *, opml_text: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetFeedsFromOpmlTextResponse]:
        """
        Parse OPML text and return an array of feeds

        Parameters
        ----------
        opml_text : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetFeedsFromOpmlTextResponse]
            Successfully parsed OPML text and returned feeds
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/podcasts/opml/parse",
            method="POST",
            json={
                "opmlText": opml_text,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFeedsFromOpmlTextResponse,
                    parse_obj_as(
                        type_=GetFeedsFromOpmlTextResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bulk_create_podcasts_from_opml_feed_urls(
        self,
        *,
        feeds: typing.Optional[typing.Sequence[str]] = OMIT,
        library_id: typing.Optional[LibraryId] = OMIT,
        folder_id: typing.Optional[FolderId] = OMIT,
        auto_download_episodes: typing.Optional[AutoDownloadEpisodes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/podcasts/opml/create",
            method="POST",
            json={
                "feeds": feeds,
                "libraryId": library_id,
                "folderId": folder_id,
                "autoDownloadEpisodes": auto_download_episodes,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def check_new_episodes(
        self,
        id: PodcastId,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CheckNewEpisodesResponse]:
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
        HttpResponse[CheckNewEpisodesResponse]
            Successfully checked and downloaded new episodes
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/checknew",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckNewEpisodesResponse,
                    parse_obj_as(
                        type_=CheckNewEpisodesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def clear_episode_download_queue(
        self, id: PodcastId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/clear-queue",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_episode_downloads(
        self, id: PodcastId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetEpisodeDownloadsResponse]:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetEpisodeDownloadsResponse]
            Successfully retrieved episode downloads
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/downloads",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEpisodeDownloadsResponse,
                    parse_obj_as(
                        type_=GetEpisodeDownloadsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def find_episode(
        self, id: PodcastId, *, title: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FindEpisodeResponse]:
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
        HttpResponse[FindEpisodeResponse]
            Successfully found episodes
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/search-episode",
            method="GET",
            params={
                "title": title,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FindEpisodeResponse,
                    parse_obj_as(
                        type_=FindEpisodeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def download_episodes(
        self, id: PodcastId, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/download-episodes",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def quick_match_episodes(
        self,
        id: PodcastId,
        *,
        override: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QuickMatchEpisodesResponse]:
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
        HttpResponse[QuickMatchEpisodesResponse]
            Successfully matched episodes
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/match-episodes",
            method="POST",
            params={
                "override": override,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QuickMatchEpisodesResponse,
                    parse_obj_as(
                        type_=QuickMatchEpisodesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_episode(
        self, id: PodcastId, episode_id: PodcastId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PodcastEpisode]:
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
        HttpResponse[PodcastEpisode]
            Successfully retrieved episode
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/episode/{encode_path_param(episode_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PodcastEpisode,
                    parse_obj_as(
                        type_=PodcastEpisode,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def remove_episode(
        self,
        id: PodcastId,
        episode_id: PodcastId,
        *,
        hard: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Podcast]:
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
        HttpResponse[Podcast]
            Successfully removed episode
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/episode/{encode_path_param(episode_id)}",
            method="DELETE",
            params={
                "hard": hard,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Podcast,
                    parse_obj_as(
                        type_=Podcast,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_episode(
        self,
        id: PodcastId,
        episode_id: PodcastId,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Podcast]:
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
        HttpResponse[Podcast]
            Successfully updated episode
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/episode/{encode_path_param(episode_id)}",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Podcast,
                    parse_obj_as(
                        type_=Podcast,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPodcastsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[Podcast]:
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
        AsyncHttpResponse[Podcast]
            Successfully created a podcast
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/podcasts",
            method="POST",
            json={
                "id": id,
                "libraryItemId": library_item_id,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=PodcastMetadata, direction="write"
                ),
                "coverPath": cover_path,
                "tags": tags,
                "episodes": convert_and_respect_annotation_metadata(
                    object_=episodes, annotation=typing.Sequence[PodcastEpisode], direction="write"
                ),
                "autoDownloadEpisodes": auto_download_episodes,
                "autoDownloadSchedule": auto_download_schedule,
                "lastEpisodeCheck": last_episode_check,
                "maxEpisodesToKeep": max_episodes_to_keep,
                "maxNewEpisodesToDownload": max_new_episodes_to_download,
                "lastCoverSearch": last_cover_search,
                "lastCoverSearchQuery": last_cover_search_query,
                "size": size,
                "duration": duration,
                "numTracks": num_tracks,
                "latestEpisodePublished": latest_episode_published,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Podcast,
                    parse_obj_as(
                        type_=Podcast,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_podcast_feed(
        self, *, rss_feed: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetPodcastFeedResponse]:
        """
        Parameters
        ----------
        rss_feed : typing.Optional[str]
            The RSS feed URL of the podcast

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPodcastFeedResponse]
            Successfully retrieved podcast feed
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/podcasts/feed",
            method="POST",
            json={
                "rssFeed": rss_feed,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPodcastFeedResponse,
                    parse_obj_as(
                        type_=GetPodcastFeedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_feeds_from_opml_text(
        self, *, opml_text: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetFeedsFromOpmlTextResponse]:
        """
        Parse OPML text and return an array of feeds

        Parameters
        ----------
        opml_text : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetFeedsFromOpmlTextResponse]
            Successfully parsed OPML text and returned feeds
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/podcasts/opml/parse",
            method="POST",
            json={
                "opmlText": opml_text,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFeedsFromOpmlTextResponse,
                    parse_obj_as(
                        type_=GetFeedsFromOpmlTextResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bulk_create_podcasts_from_opml_feed_urls(
        self,
        *,
        feeds: typing.Optional[typing.Sequence[str]] = OMIT,
        library_id: typing.Optional[LibraryId] = OMIT,
        folder_id: typing.Optional[FolderId] = OMIT,
        auto_download_episodes: typing.Optional[AutoDownloadEpisodes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/podcasts/opml/create",
            method="POST",
            json={
                "feeds": feeds,
                "libraryId": library_id,
                "folderId": folder_id,
                "autoDownloadEpisodes": auto_download_episodes,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def check_new_episodes(
        self,
        id: PodcastId,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CheckNewEpisodesResponse]:
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
        AsyncHttpResponse[CheckNewEpisodesResponse]
            Successfully checked and downloaded new episodes
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/checknew",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckNewEpisodesResponse,
                    parse_obj_as(
                        type_=CheckNewEpisodesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def clear_episode_download_queue(
        self, id: PodcastId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/clear-queue",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_episode_downloads(
        self, id: PodcastId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetEpisodeDownloadsResponse]:
        """
        Parameters
        ----------
        id : PodcastId
            Podcast ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetEpisodeDownloadsResponse]
            Successfully retrieved episode downloads
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/downloads",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEpisodeDownloadsResponse,
                    parse_obj_as(
                        type_=GetEpisodeDownloadsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def find_episode(
        self, id: PodcastId, *, title: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FindEpisodeResponse]:
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
        AsyncHttpResponse[FindEpisodeResponse]
            Successfully found episodes
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/search-episode",
            method="GET",
            params={
                "title": title,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FindEpisodeResponse,
                    parse_obj_as(
                        type_=FindEpisodeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def download_episodes(
        self, id: PodcastId, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/download-episodes",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def quick_match_episodes(
        self,
        id: PodcastId,
        *,
        override: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QuickMatchEpisodesResponse]:
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
        AsyncHttpResponse[QuickMatchEpisodesResponse]
            Successfully matched episodes
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/match-episodes",
            method="POST",
            params={
                "override": override,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QuickMatchEpisodesResponse,
                    parse_obj_as(
                        type_=QuickMatchEpisodesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_episode(
        self, id: PodcastId, episode_id: PodcastId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PodcastEpisode]:
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
        AsyncHttpResponse[PodcastEpisode]
            Successfully retrieved episode
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/episode/{encode_path_param(episode_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PodcastEpisode,
                    parse_obj_as(
                        type_=PodcastEpisode,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def remove_episode(
        self,
        id: PodcastId,
        episode_id: PodcastId,
        *,
        hard: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Podcast]:
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
        AsyncHttpResponse[Podcast]
            Successfully removed episode
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/episode/{encode_path_param(episode_id)}",
            method="DELETE",
            params={
                "hard": hard,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Podcast,
                    parse_obj_as(
                        type_=Podcast,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_episode(
        self,
        id: PodcastId,
        episode_id: PodcastId,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Podcast]:
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
        AsyncHttpResponse[Podcast]
            Successfully updated episode
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/podcasts/{encode_path_param(id)}/episode/{encode_path_param(episode_id)}",
            method="PATCH",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Podcast,
                    parse_obj_as(
                        type_=Podcast,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
