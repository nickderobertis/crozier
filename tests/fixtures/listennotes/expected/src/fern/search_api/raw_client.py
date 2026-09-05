

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.related_searches_response import RelatedSearchesResponse
from ..types.search_response import SearchResponse
from ..types.spell_check_response import SpellCheckResponse
from ..types.trending_searches_response import TrendingSearchesResponse
from ..types.typeahead_response import TypeaheadResponse
from .types.search_request_type import SearchRequestType
from pydantic import ValidationError


class RawSearchApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_related_searches(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RelatedSearchesResponse]:
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
        HttpResponse[RelatedSearchesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "related_searches",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RelatedSearchesResponse,
                    parse_obj_as(
                        type_=RelatedSearchesResponse,
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
    ) -> HttpResponse[SearchResponse]:
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
        HttpResponse[SearchResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "search",
            method="GET",
            params={
                "q": q,
                "sort_by_date": sort_by_date,
                "type": type,
                "offset": offset,
                "len_min": len_min,
                "len_max": len_max,
                "episode_count_min": episode_count_min,
                "episode_count_max": episode_count_max,
                "update_freq_min": update_freq_min,
                "update_freq_max": update_freq_max,
                "genre_ids": genre_ids,
                "published_before": published_before,
                "published_after": published_after,
                "only_in": only_in,
                "language": language,
                "region": region,
                "ocid": ocid,
                "ncid": ncid,
                "safe_mode": safe_mode,
                "unique_podcasts": unique_podcasts,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchResponse,
                    parse_obj_as(
                        type_=SearchResponse,
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

    def spellcheck(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SpellCheckResponse]:
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
        HttpResponse[SpellCheckResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "spellcheck",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SpellCheckResponse,
                    parse_obj_as(
                        type_=SpellCheckResponse,
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

    def get_trending_searches(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TrendingSearchesResponse]:
        """
        Fetch up to 10 most recent trending search terms on the Listen Notes platform.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TrendingSearchesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "trending_searches",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrendingSearchesResponse,
                    parse_obj_as(
                        type_=TrendingSearchesResponse,
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

    def typeahead(
        self,
        *,
        q: str,
        show_podcasts: typing.Optional[int] = None,
        show_genres: typing.Optional[int] = None,
        safe_mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TypeaheadResponse]:
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
        HttpResponse[TypeaheadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "typeahead",
            method="GET",
            params={
                "q": q,
                "show_podcasts": show_podcasts,
                "show_genres": show_genres,
                "safe_mode": safe_mode,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TypeaheadResponse,
                    parse_obj_as(
                        type_=TypeaheadResponse,
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


class AsyncRawSearchApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_related_searches(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RelatedSearchesResponse]:
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
        AsyncHttpResponse[RelatedSearchesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "related_searches",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RelatedSearchesResponse,
                    parse_obj_as(
                        type_=RelatedSearchesResponse,
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
    ) -> AsyncHttpResponse[SearchResponse]:
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
        AsyncHttpResponse[SearchResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "search",
            method="GET",
            params={
                "q": q,
                "sort_by_date": sort_by_date,
                "type": type,
                "offset": offset,
                "len_min": len_min,
                "len_max": len_max,
                "episode_count_min": episode_count_min,
                "episode_count_max": episode_count_max,
                "update_freq_min": update_freq_min,
                "update_freq_max": update_freq_max,
                "genre_ids": genre_ids,
                "published_before": published_before,
                "published_after": published_after,
                "only_in": only_in,
                "language": language,
                "region": region,
                "ocid": ocid,
                "ncid": ncid,
                "safe_mode": safe_mode,
                "unique_podcasts": unique_podcasts,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchResponse,
                    parse_obj_as(
                        type_=SearchResponse,
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

    async def spellcheck(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SpellCheckResponse]:
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
        AsyncHttpResponse[SpellCheckResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "spellcheck",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SpellCheckResponse,
                    parse_obj_as(
                        type_=SpellCheckResponse,
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

    async def get_trending_searches(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TrendingSearchesResponse]:
        """
        Fetch up to 10 most recent trending search terms on the Listen Notes platform.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TrendingSearchesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "trending_searches",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrendingSearchesResponse,
                    parse_obj_as(
                        type_=TrendingSearchesResponse,
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

    async def typeahead(
        self,
        *,
        q: str,
        show_podcasts: typing.Optional[int] = None,
        show_genres: typing.Optional[int] = None,
        safe_mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TypeaheadResponse]:
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
        AsyncHttpResponse[TypeaheadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "typeahead",
            method="GET",
            params={
                "q": q,
                "show_podcasts": show_podcasts,
                "show_genres": show_genres,
                "safe_mode": safe_mode,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TypeaheadResponse,
                    parse_obj_as(
                        type_=TypeaheadResponse,
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
