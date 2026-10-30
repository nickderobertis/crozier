

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPresetsClient, RawPresetsClient


class PresetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPresetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPresetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPresetsClient
        """
        return self._raw_client

    def get_mcu_key_short_click(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=MCUKeyShortClick:%d

        %d: Range is from 1 to 12

        Parameters
        ----------
        n : int
            Preset number

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
        client.presets.get_mcu_key_short_click(
            n=1,
        )
        """
        _response = self._raw_client.get_mcu_key_short_click(n, request_options=request_options)
        return _response.data

    def get_mcu_key_short_click_track(
        self, n: int, t: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=MCUKeyShortClick:%d:%t

        %d: Range is from 1 to 12
        %t: Track number, start from 1, default is 1

        Parameters
        ----------
        n : int
            Preset number

        t : int
            Track number, start from 1, default is 1

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
        client.presets.get_mcu_key_short_click_track(
            n=1,
            t=1,
        )
        """
        _response = self._raw_client.get_mcu_key_short_click_track(n, t, request_options=request_options)
        return _response.data

    def get_preset_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=getPresetInfo


        JSON Response

        {
          "preset_num": 3,
          "preset_list": [
          {
            "number": 1,
            "name": "BBC Radio Norfolk",
            "url": "http:\\/\\/as-hls-wwlive.akamaized.net\\/pool_904\\/live\\/ww\\/bbc_radio_norfolk\\/bbc_radio_norfolk.isml\\/bbc_radio_norfolk-audio%3d96000.norewind.m3u8",
            "source": "Linkplay Radio",
            "picurl": "http:\\/\\/cdnprofiles.tunein.com\\/s6852\\/images\\/logoq.jpg?t=638353933090000000"
          },
          {
            "number": 6,
            "name": "Radio Paradise",
            "url": "http:\\/\\/stream.radioparadise.com\\/flacm",
            "source": "RadioParadise",
            "picurl": "https:\\/\\/cdnprofiles.tunein.com\\/s13606\\/images\\/logod.png?t=637541039930000000"
          },
          {
            "number": 8,
            "name": "1. Country Heat",
            "url": "unknow",
            "source": "Prime",
            "picurl": "https:\\/\\/m.media-amazon.com\\/images\\/I\\/51uR6AJUAQL.jpg"
          }
          ]
        }


        Description

        Field type Description

        preset_num int Total number of presets

        preset_list json array Preset list information

        number int Preset index (Start from 1)

        name string Playlist name

        url string Play url

        source string Music source

        picurl string Cover picture url

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
        client.presets.get_preset_info()
        """
        _response = self._raw_client.get_preset_info(request_options=request_options)
        return _response.data


class AsyncPresetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPresetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPresetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPresetsClient
        """
        return self._raw_client

    async def get_mcu_key_short_click(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=MCUKeyShortClick:%d

        %d: Range is from 1 to 12

        Parameters
        ----------
        n : int
            Preset number

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
            await client.presets.get_mcu_key_short_click(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mcu_key_short_click(n, request_options=request_options)
        return _response.data

    async def get_mcu_key_short_click_track(
        self, n: int, t: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=MCUKeyShortClick:%d:%t

        %d: Range is from 1 to 12
        %t: Track number, start from 1, default is 1

        Parameters
        ----------
        n : int
            Preset number

        t : int
            Track number, start from 1, default is 1

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
            await client.presets.get_mcu_key_short_click_track(
                n=1,
                t=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mcu_key_short_click_track(n, t, request_options=request_options)
        return _response.data

    async def get_preset_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=getPresetInfo


        JSON Response

        {
          "preset_num": 3,
          "preset_list": [
          {
            "number": 1,
            "name": "BBC Radio Norfolk",
            "url": "http:\\/\\/as-hls-wwlive.akamaized.net\\/pool_904\\/live\\/ww\\/bbc_radio_norfolk\\/bbc_radio_norfolk.isml\\/bbc_radio_norfolk-audio%3d96000.norewind.m3u8",
            "source": "Linkplay Radio",
            "picurl": "http:\\/\\/cdnprofiles.tunein.com\\/s6852\\/images\\/logoq.jpg?t=638353933090000000"
          },
          {
            "number": 6,
            "name": "Radio Paradise",
            "url": "http:\\/\\/stream.radioparadise.com\\/flacm",
            "source": "RadioParadise",
            "picurl": "https:\\/\\/cdnprofiles.tunein.com\\/s13606\\/images\\/logod.png?t=637541039930000000"
          },
          {
            "number": 8,
            "name": "1. Country Heat",
            "url": "unknow",
            "source": "Prime",
            "picurl": "https:\\/\\/m.media-amazon.com\\/images\\/I\\/51uR6AJUAQL.jpg"
          }
          ]
        }


        Description

        Field type Description

        preset_num int Total number of presets

        preset_list json array Preset list information

        number int Preset index (Start from 1)

        name string Playlist name

        url string Play url

        source string Music source

        picurl string Cover picture url

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
            await client.presets.get_preset_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_preset_info(request_options=request_options)
        return _response.data
