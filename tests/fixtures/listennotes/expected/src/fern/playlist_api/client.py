

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.playlist_response import PlaylistResponse
from ..types.playlists_response import PlaylistsResponse
from .raw_client import AsyncRawPlaylistApiClient, RawPlaylistApiClient
from .types.get_playlist_by_id_request_sort import GetPlaylistByIdRequestSort
from .types.get_playlist_by_id_request_type import GetPlaylistByIdRequestType
from .types.get_playlists_request_sort import GetPlaylistsRequestSort


class PlaylistApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPlaylistApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPlaylistApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPlaylistApiClient
        """
        return self._raw_client

    def get_playlists(
        self,
        *,
        sort: typing.Optional[GetPlaylistsRequestSort] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PlaylistsResponse:
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
        PlaylistsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.playlist_api.get_playlists(
            page=1,
        )
        """
        _response = self._raw_client.get_playlists(sort=sort, page=page, request_options=request_options)
        return _response.data

    def get_playlist_by_id(
        self,
        id: str,
        *,
        type: typing.Optional[GetPlaylistByIdRequestType] = None,
        last_timestamp_ms: typing.Optional[int] = None,
        sort: typing.Optional[GetPlaylistByIdRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PlaylistResponse:
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
        PlaylistResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.playlist_api.get_playlist_by_id(
            id="m1pe7z60bsw",
            last_timestamp_ms=0,
        )
        """
        _response = self._raw_client.get_playlist_by_id(
            id, type=type, last_timestamp_ms=last_timestamp_ms, sort=sort, request_options=request_options
        )
        return _response.data


class AsyncPlaylistApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPlaylistApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPlaylistApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPlaylistApiClient
        """
        return self._raw_client

    async def get_playlists(
        self,
        *,
        sort: typing.Optional[GetPlaylistsRequestSort] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PlaylistsResponse:
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
        PlaylistsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.playlist_api.get_playlists(
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_playlists(sort=sort, page=page, request_options=request_options)
        return _response.data

    async def get_playlist_by_id(
        self,
        id: str,
        *,
        type: typing.Optional[GetPlaylistByIdRequestType] = None,
        last_timestamp_ms: typing.Optional[int] = None,
        sort: typing.Optional[GetPlaylistByIdRequestSort] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PlaylistResponse:
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
        PlaylistResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.playlist_api.get_playlist_by_id(
                id="m1pe7z60bsw",
                last_timestamp_ms=0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_playlist_by_id(
            id, type=type, last_timestamp_ms=last_timestamp_ms, sort=sort, request_options=request_options
        )
        return _response.data
