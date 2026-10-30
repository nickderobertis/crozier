

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPlaybackControlClient, RawPlaybackControlClient


class PlaybackControlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPlaybackControlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPlaybackControlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPlaybackControlClient
        """
        return self._raw_client

    def get_player_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=getPlayerStatus

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.playback_control.get_player_status()
        """
        _response = self._raw_client.get_player_status(request_options=request_options)
        return _response.data

    def set_player_cmd_hex_playlist_url(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        http://10.10.10.254/httpapi.asp?command=setPlayerCmd:hex_playlist:url:<index>

        Play the URl (URI is the m3u or ASX playlist link, index is the start
        index), here, url should be hexed (please refer to 1.3)

        Parameters
        ----------
        index : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.playback_control.set_player_cmd_hex_playlist_url(
            index="index",
        )
        """
        _response = self._raw_client.set_player_cmd_hex_playlist_url(index, request_options=request_options)
        return _response.data

    def set_player_cmd_pause(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:pause

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.playback_control.set_player_cmd_pause()
        """
        _response = self._raw_client.set_player_cmd_pause(request_options=request_options)
        return _response.data

    def set_player_cmd_resume(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:resume

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.playback_control.set_player_cmd_resume()
        """
        _response = self._raw_client.set_player_cmd_resume(request_options=request_options)
        return _response.data

    def set_player_cmd_one_pause(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:onepause

        If the state is paused, resume it; otherwise, pause it.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.playback_control.set_player_cmd_one_pause()
        """
        _response = self._raw_client.set_player_cmd_one_pause(request_options=request_options)
        return _response.data

    def set_player_cmd_play_url(self, url: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:play:url
        Play the URL. URL points to an audio stream address.
        Response is always 'OK' now

        Parameters
        ----------
        url : str
            URL points to an audio stream address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.playback_control.set_player_cmd_play_url(
            url="url",
        )
        """
        _response = self._raw_client.set_player_cmd_play_url(url, request_options=request_options)
        return _response.data

    def set_player_cmd_playlist_url(
        self, url: str, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:playlist:url:<index>

        Play the playlist with the URL (URL points to the m3u or ASX playlist
        link, index is the start index).

        Response is always 'OK' now.

        Parameters
        ----------
        url : str

        index : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.playback_control.set_player_cmd_playlist_url(
            url="url",
            index="index",
        )
        """
        _response = self._raw_client.set_player_cmd_playlist_url(url, index, request_options=request_options)
        return _response.data

    def set_player_cmd_prev(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:prev

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.playback_control.set_player_cmd_prev()
        """
        _response = self._raw_client.set_player_cmd_prev(request_options=request_options)
        return _response.data

    def set_player_cmd_next(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:next

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.playback_control.set_player_cmd_next()
        """
        _response = self._raw_client.set_player_cmd_next(request_options=request_options)
        return _response.data

    def set_player_cmd_seek_position(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:seek:position
        Position is from 0 to duration in second.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.playback_control.set_player_cmd_seek_position()
        """
        _response = self._raw_client.set_player_cmd_seek_position(request_options=request_options)
        return _response.data

    def set_player_cmd_stop(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:stop

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.playback_control.set_player_cmd_stop()
        """
        _response = self._raw_client.set_player_cmd_stop(request_options=request_options)
        return _response.data

    def set_player_cmd_vol(self, value: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:vol:value
        Value can be 0 to 100.

        Parameters
        ----------
        value : int
            Value can be 0 to 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.playback_control.set_player_cmd_vol(
            value=1,
        )
        """
        _response = self._raw_client.set_player_cmd_vol(value, request_options=request_options)
        return _response.data

    def set_player_cmd_mute(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:mute:n

        Mute: n=1

        Unmute: n=0

        The slave mute state will be set at the same time when it's in group
        play.

        Parameters
        ----------
        n : int
            Mute: n=1
            Unmute: n=0

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.playback_control.set_player_cmd_mute(
            n=1,
        )
        """
        _response = self._raw_client.set_player_cmd_mute(n, request_options=request_options)
        return _response.data

    def set_player_cmd_loopmode(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:loopmode:n

        n =
        - -1: ...
        - 0: Shuffle disabled, Repeat enabled - loop
        - 1: Shuffle disabled, Repeat enabled - loop once
        - 2: Shuffle enabled, Repeat enabled - loop
        - 3: Shuffle enabled, Repeat disabled
        - 4: Shuffle disabled, Repeat disabled
        - 5: Shuffle enabled, Repeat enabled - loop once

        Parameters
        ----------
        n : int
            - -1: ...
            - 0: Shuffle disabled, Repeat enabled - loop
            - 1: Shuffle disabled, Repeat enabled - loop once
            - 2: Shuffle enabled, Repeat enabled - loop
            - 3: Shuffle enabled, Repeat disabled
            - 4: Shuffle disabled, Repeat disabled
            - 5: Shuffle enabled, Repeat enabled - loop once

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.playback_control.set_player_cmd_loopmode(
            n=1,
        )
        """
        _response = self._raw_client.set_player_cmd_loopmode(n, request_options=request_options)
        return _response.data


class AsyncPlaybackControlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPlaybackControlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPlaybackControlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPlaybackControlClient
        """
        return self._raw_client

    async def get_player_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=getPlayerStatus

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.playback_control.get_player_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_player_status(request_options=request_options)
        return _response.data

    async def set_player_cmd_hex_playlist_url(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        http://10.10.10.254/httpapi.asp?command=setPlayerCmd:hex_playlist:url:<index>

        Play the URl (URI is the m3u or ASX playlist link, index is the start
        index), here, url should be hexed (please refer to 1.3)

        Parameters
        ----------
        index : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.playback_control.set_player_cmd_hex_playlist_url(
                index="index",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_hex_playlist_url(index, request_options=request_options)
        return _response.data

    async def set_player_cmd_pause(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:pause

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.playback_control.set_player_cmd_pause()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_pause(request_options=request_options)
        return _response.data

    async def set_player_cmd_resume(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:resume

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.playback_control.set_player_cmd_resume()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_resume(request_options=request_options)
        return _response.data

    async def set_player_cmd_one_pause(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:onepause

        If the state is paused, resume it; otherwise, pause it.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.playback_control.set_player_cmd_one_pause()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_one_pause(request_options=request_options)
        return _response.data

    async def set_player_cmd_play_url(
        self, url: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:play:url
        Play the URL. URL points to an audio stream address.
        Response is always 'OK' now

        Parameters
        ----------
        url : str
            URL points to an audio stream address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.playback_control.set_player_cmd_play_url(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_play_url(url, request_options=request_options)
        return _response.data

    async def set_player_cmd_playlist_url(
        self, url: str, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:playlist:url:<index>

        Play the playlist with the URL (URL points to the m3u or ASX playlist
        link, index is the start index).

        Response is always 'OK' now.

        Parameters
        ----------
        url : str

        index : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.playback_control.set_player_cmd_playlist_url(
                url="url",
                index="index",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_playlist_url(url, index, request_options=request_options)
        return _response.data

    async def set_player_cmd_prev(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:prev

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.playback_control.set_player_cmd_prev()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_prev(request_options=request_options)
        return _response.data

    async def set_player_cmd_next(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:next

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.playback_control.set_player_cmd_next()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_next(request_options=request_options)
        return _response.data

    async def set_player_cmd_seek_position(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:seek:position
        Position is from 0 to duration in second.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.playback_control.set_player_cmd_seek_position()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_seek_position(request_options=request_options)
        return _response.data

    async def set_player_cmd_stop(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:stop

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.playback_control.set_player_cmd_stop()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_stop(request_options=request_options)
        return _response.data

    async def set_player_cmd_vol(self, value: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:vol:value
        Value can be 0 to 100.

        Parameters
        ----------
        value : int
            Value can be 0 to 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.playback_control.set_player_cmd_vol(
                value=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_vol(value, request_options=request_options)
        return _response.data

    async def set_player_cmd_mute(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:mute:n

        Mute: n=1

        Unmute: n=0

        The slave mute state will be set at the same time when it's in group
        play.

        Parameters
        ----------
        n : int
            Mute: n=1
            Unmute: n=0

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.playback_control.set_player_cmd_mute(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_mute(n, request_options=request_options)
        return _response.data

    async def set_player_cmd_loopmode(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=setPlayerCmd:loopmode:n

        n =
        - -1: ...
        - 0: Shuffle disabled, Repeat enabled - loop
        - 1: Shuffle disabled, Repeat enabled - loop once
        - 2: Shuffle enabled, Repeat enabled - loop
        - 3: Shuffle enabled, Repeat disabled
        - 4: Shuffle disabled, Repeat disabled
        - 5: Shuffle enabled, Repeat enabled - loop once

        Parameters
        ----------
        n : int
            - -1: ...
            - 0: Shuffle disabled, Repeat enabled - loop
            - 1: Shuffle disabled, Repeat enabled - loop once
            - 2: Shuffle enabled, Repeat enabled - loop
            - 3: Shuffle enabled, Repeat disabled
            - 4: Shuffle disabled, Repeat disabled
            - 5: Shuffle enabled, Repeat enabled - loop once

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.playback_control.set_player_cmd_loopmode(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_loopmode(n, request_options=request_options)
        return _response.data
