

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
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
from .types.get_best_podcasts_request_sort import GetBestPodcastsRequestSort
from .types.get_podcast_by_id_request_sort import GetPodcastByIdRequestSort
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDirectoryApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[BestPodcastsResponse]:
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
        HttpResponse[BestPodcastsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "best_podcasts",
            method="GET",
            params={
                "genre_id": genre_id,
                "page": page,
                "region": region,
                "publisher_region": publisher_region,
                "language": language,
                "sort": sort,
                "safe_mode": safe_mode,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BestPodcastsResponse,
                    parse_obj_as(
                        type_=BestPodcastsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def get_curated_podcasts(
        self, *, page: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetCuratedPodcastsResponse]:
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
        HttpResponse[GetCuratedPodcastsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "curated_podcasts",
            method="GET",
            params={
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCuratedPodcastsResponse,
                    parse_obj_as(
                        type_=GetCuratedPodcastsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def get_curated_podcast_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CuratedListFull]:
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
        HttpResponse[CuratedListFull]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"curated_podcasts/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CuratedListFull,
                    parse_obj_as(
                        type_=CuratedListFull,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def get_episodes_in_batch(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetEpisodesInBatchResponse]:
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
        HttpResponse[GetEpisodesInBatchResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "episodes",
            method="POST",
            data={
                "ids": ids,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEpisodesInBatchResponse,
                    parse_obj_as(
                        type_=GetEpisodesInBatchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def get_episode_by_id(
        self,
        id: str,
        *,
        show_transcript: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EpisodeFull]:
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
        HttpResponse[EpisodeFull]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"episodes/{encode_path_param(id)}",
            method="GET",
            params={
                "show_transcript": show_transcript,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EpisodeFull,
                    parse_obj_as(
                        type_=EpisodeFull,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def get_episode_recommendations(
        self,
        id: str,
        *,
        safe_mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetEpisodeRecommendationsResponse]:
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
        HttpResponse[GetEpisodeRecommendationsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"episodes/{encode_path_param(id)}/recommendations",
            method="GET",
            params={
                "safe_mode": safe_mode,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEpisodeRecommendationsResponse,
                    parse_obj_as(
                        type_=GetEpisodeRecommendationsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def get_genres(
        self, *, top_level_only: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetGenresResponse]:
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
        HttpResponse[GetGenresResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "genres",
            method="GET",
            params={
                "top_level_only": top_level_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGenresResponse,
                    parse_obj_as(
                        type_=GetGenresResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def just_listen(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[EpisodeSimple]:
        """
        Recently published episodes are more likely to be fetched. Good luck!

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EpisodeSimple]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "just_listen",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EpisodeSimple,
                    parse_obj_as(
                        type_=EpisodeSimple,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def get_languages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetLanguagesResponse]:
        """
        Get a list of languages that are supported in Listen Notes database. You can use the language string as query parameter in `GET /search`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLanguagesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "languages",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLanguagesResponse,
                    parse_obj_as(
                        type_=GetLanguagesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
    ) -> HttpResponse[GetPodcastsInBatchResponse]:
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
        HttpResponse[GetPodcastsInBatchResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "podcasts",
            method="POST",
            data={
                "ids": ids,
                "itunes_ids": itunes_ids,
                "next_episode_pub_date": next_episode_pub_date,
                "rsses": rsses,
                "show_latest_episodes": show_latest_episodes,
                "spotify_ids": spotify_ids,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPodcastsInBatchResponse,
                    parse_obj_as(
                        type_=GetPodcastsInBatchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def get_podcast_by_id(
        self,
        id: str,
        *,
        next_episode_pub_date: typing.Optional[int] = None,
        sort: typing.Optional[GetPodcastByIdRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PodcastFull]:
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
        HttpResponse[PodcastFull]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"podcasts/{encode_path_param(id)}",
            method="GET",
            params={
                "next_episode_pub_date": next_episode_pub_date,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PodcastFull,
                    parse_obj_as(
                        type_=PodcastFull,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def get_podcast_recommendations(
        self,
        id: str,
        *,
        safe_mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPodcastRecommendationsResponse]:
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
        HttpResponse[GetPodcastRecommendationsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"podcasts/{encode_path_param(id)}/recommendations",
            method="GET",
            params={
                "safe_mode": safe_mode,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPodcastRecommendationsResponse,
                    parse_obj_as(
                        type_=GetPodcastRecommendationsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def get_regions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetRegionsResponse]:
        """
        It returns a dictionary of country codes (e.g., us, gb...) & country names (United States, United Kingdom...). The country code is used in the query parameter **region** of `GET /best_podcasts`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetRegionsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "regions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRegionsResponse,
                    parse_obj_as(
                        type_=GetRegionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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


class AsyncRawDirectoryApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[BestPodcastsResponse]:
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
        AsyncHttpResponse[BestPodcastsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "best_podcasts",
            method="GET",
            params={
                "genre_id": genre_id,
                "page": page,
                "region": region,
                "publisher_region": publisher_region,
                "language": language,
                "sort": sort,
                "safe_mode": safe_mode,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BestPodcastsResponse,
                    parse_obj_as(
                        type_=BestPodcastsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def get_curated_podcasts(
        self, *, page: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetCuratedPodcastsResponse]:
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
        AsyncHttpResponse[GetCuratedPodcastsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "curated_podcasts",
            method="GET",
            params={
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCuratedPodcastsResponse,
                    parse_obj_as(
                        type_=GetCuratedPodcastsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def get_curated_podcast_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CuratedListFull]:
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
        AsyncHttpResponse[CuratedListFull]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"curated_podcasts/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CuratedListFull,
                    parse_obj_as(
                        type_=CuratedListFull,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def get_episodes_in_batch(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetEpisodesInBatchResponse]:
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
        AsyncHttpResponse[GetEpisodesInBatchResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "episodes",
            method="POST",
            data={
                "ids": ids,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEpisodesInBatchResponse,
                    parse_obj_as(
                        type_=GetEpisodesInBatchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def get_episode_by_id(
        self,
        id: str,
        *,
        show_transcript: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EpisodeFull]:
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
        AsyncHttpResponse[EpisodeFull]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"episodes/{encode_path_param(id)}",
            method="GET",
            params={
                "show_transcript": show_transcript,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EpisodeFull,
                    parse_obj_as(
                        type_=EpisodeFull,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def get_episode_recommendations(
        self,
        id: str,
        *,
        safe_mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetEpisodeRecommendationsResponse]:
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
        AsyncHttpResponse[GetEpisodeRecommendationsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"episodes/{encode_path_param(id)}/recommendations",
            method="GET",
            params={
                "safe_mode": safe_mode,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEpisodeRecommendationsResponse,
                    parse_obj_as(
                        type_=GetEpisodeRecommendationsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def get_genres(
        self, *, top_level_only: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetGenresResponse]:
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
        AsyncHttpResponse[GetGenresResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "genres",
            method="GET",
            params={
                "top_level_only": top_level_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGenresResponse,
                    parse_obj_as(
                        type_=GetGenresResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def just_listen(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EpisodeSimple]:
        """
        Recently published episodes are more likely to be fetched. Good luck!

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EpisodeSimple]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "just_listen",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EpisodeSimple,
                    parse_obj_as(
                        type_=EpisodeSimple,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def get_languages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetLanguagesResponse]:
        """
        Get a list of languages that are supported in Listen Notes database. You can use the language string as query parameter in `GET /search`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLanguagesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "languages",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLanguagesResponse,
                    parse_obj_as(
                        type_=GetLanguagesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
    ) -> AsyncHttpResponse[GetPodcastsInBatchResponse]:
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
        AsyncHttpResponse[GetPodcastsInBatchResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "podcasts",
            method="POST",
            data={
                "ids": ids,
                "itunes_ids": itunes_ids,
                "next_episode_pub_date": next_episode_pub_date,
                "rsses": rsses,
                "show_latest_episodes": show_latest_episodes,
                "spotify_ids": spotify_ids,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPodcastsInBatchResponse,
                    parse_obj_as(
                        type_=GetPodcastsInBatchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def get_podcast_by_id(
        self,
        id: str,
        *,
        next_episode_pub_date: typing.Optional[int] = None,
        sort: typing.Optional[GetPodcastByIdRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PodcastFull]:
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
        AsyncHttpResponse[PodcastFull]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"podcasts/{encode_path_param(id)}",
            method="GET",
            params={
                "next_episode_pub_date": next_episode_pub_date,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PodcastFull,
                    parse_obj_as(
                        type_=PodcastFull,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def get_podcast_recommendations(
        self,
        id: str,
        *,
        safe_mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetPodcastRecommendationsResponse]:
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
        AsyncHttpResponse[GetPodcastRecommendationsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"podcasts/{encode_path_param(id)}/recommendations",
            method="GET",
            params={
                "safe_mode": safe_mode,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPodcastRecommendationsResponse,
                    parse_obj_as(
                        type_=GetPodcastRecommendationsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def get_regions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetRegionsResponse]:
        """
        It returns a dictionary of country codes (e.g., us, gb...) & country names (United States, United Kingdom...). The country code is used in the query parameter **region** of `GET /best_podcasts`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetRegionsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "regions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRegionsResponse,
                    parse_obj_as(
                        type_=GetRegionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
