

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
from ..types.playlist_response import PlaylistResponse
from ..types.playlists_response import PlaylistsResponse
from .types.get_playlist_by_id_request_sort import GetPlaylistByIdRequestSort
from .types.get_playlist_by_id_request_type import GetPlaylistByIdRequestType
from .types.get_playlists_request_sort import GetPlaylistsRequestSort
from pydantic import ValidationError


class RawPlaylistApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_playlists(
        self,
        *,
        sort: typing.Optional[GetPlaylistsRequestSort] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PlaylistsResponse]:
        """
        This endpoint returns same data as listennotes.com/listen under your account.
        You can use the **page** parameter to do pagination and fetch more playlists.

        Parameters
        ----------
        sort : typing.Optional[GetPlaylistsRequestSort]
            How do you want to sort playlists?

        page : typing.Optional[int]
            Page number of playlists.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PlaylistsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "playlists",
            method="GET",
            params={
                "sort": sort,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlaylistsResponse,
                    parse_obj_as(
                        type_=PlaylistsResponse,
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

    def get_playlist_by_id(
        self,
        id: str,
        *,
        type: typing.Optional[GetPlaylistByIdRequestType] = None,
        last_timestamp_ms: typing.Optional[int] = None,
        sort: typing.Optional[GetPlaylistByIdRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PlaylistResponse]:
        """
        A playlist can be an episode list (i.e., all items are episodes) or a podcast list (i.e., all items are podcasts),
        which is essentially the same as those created via listennotes.com/listen/.
        This endpoint fetches a list of items (i.e., episodes or podcasts) in the playlist.
        You can use the **last_pub_date_ms** parameter to do pagination and fetch more items.
        A playlist can be **public** (discoverable on ListenNotes.com),
        **unlisted** (accessible to anyone who knows the playlist id),
        or **private** (accessible to its owner).
        You can fetch all playlists created by you, and **public** / **unlisted** playlists created by others.

        Parameters
        ----------
        id : str
            Playlist id (always 11 characters, e.g., m1pe7z60bsw).
            You can get the podcast id from the url of a playlist, e.g.,
            m1pe7z60bsw is the playlist id of listennotes.com/listen/podcasts-about-podcasting-m1pe7z60bsw

        type : typing.Optional[GetPlaylistByIdRequestType]
            The type of this playlist, which should be either **episode_list** or **podcast_list**.

        last_timestamp_ms : typing.Optional[int]
            For playlist items pagination.
            It's the value of **last_timestamp_ms** from the response of last request.
            If it's 0 or not specified, just return the latest or the oldest 20 items,
            depending on the value of the **sort** parameter.

        sort : typing.Optional[GetPlaylistByIdRequestSort]
            How do you want to sort playlist items?

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PlaylistResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"playlists/{encode_path_param(id)}",
            method="GET",
            params={
                "type": type,
                "last_timestamp_ms": last_timestamp_ms,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlaylistResponse,
                    parse_obj_as(
                        type_=PlaylistResponse,
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


class AsyncRawPlaylistApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_playlists(
        self,
        *,
        sort: typing.Optional[GetPlaylistsRequestSort] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PlaylistsResponse]:
        """
        This endpoint returns same data as listennotes.com/listen under your account.
        You can use the **page** parameter to do pagination and fetch more playlists.

        Parameters
        ----------
        sort : typing.Optional[GetPlaylistsRequestSort]
            How do you want to sort playlists?

        page : typing.Optional[int]
            Page number of playlists.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PlaylistsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "playlists",
            method="GET",
            params={
                "sort": sort,
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlaylistsResponse,
                    parse_obj_as(
                        type_=PlaylistsResponse,
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

    async def get_playlist_by_id(
        self,
        id: str,
        *,
        type: typing.Optional[GetPlaylistByIdRequestType] = None,
        last_timestamp_ms: typing.Optional[int] = None,
        sort: typing.Optional[GetPlaylistByIdRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PlaylistResponse]:
        """
        A playlist can be an episode list (i.e., all items are episodes) or a podcast list (i.e., all items are podcasts),
        which is essentially the same as those created via listennotes.com/listen/.
        This endpoint fetches a list of items (i.e., episodes or podcasts) in the playlist.
        You can use the **last_pub_date_ms** parameter to do pagination and fetch more items.
        A playlist can be **public** (discoverable on ListenNotes.com),
        **unlisted** (accessible to anyone who knows the playlist id),
        or **private** (accessible to its owner).
        You can fetch all playlists created by you, and **public** / **unlisted** playlists created by others.

        Parameters
        ----------
        id : str
            Playlist id (always 11 characters, e.g., m1pe7z60bsw).
            You can get the podcast id from the url of a playlist, e.g.,
            m1pe7z60bsw is the playlist id of listennotes.com/listen/podcasts-about-podcasting-m1pe7z60bsw

        type : typing.Optional[GetPlaylistByIdRequestType]
            The type of this playlist, which should be either **episode_list** or **podcast_list**.

        last_timestamp_ms : typing.Optional[int]
            For playlist items pagination.
            It's the value of **last_timestamp_ms** from the response of last request.
            If it's 0 or not specified, just return the latest or the oldest 20 items,
            depending on the value of the **sort** parameter.

        sort : typing.Optional[GetPlaylistByIdRequestSort]
            How do you want to sort playlist items?

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PlaylistResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"playlists/{encode_path_param(id)}",
            method="GET",
            params={
                "type": type,
                "last_timestamp_ms": last_timestamp_ms,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlaylistResponse,
                    parse_obj_as(
                        type_=PlaylistResponse,
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
