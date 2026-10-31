

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEqualizerClient, RawEqualizerClient
from .types.eq_get_source_modes_response_item import EqGetSourceModesResponseItem
from .types.get_eq_stat_response import GetEqStatResponse
from .types.load_eq_by_name_request_name import LoadEqByNameRequestName


class EqualizerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEqualizerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEqualizerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEqualizerClient
        """
        return self._raw_client

    def set_eq_on(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=EQOn

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Default response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.set_eq_on()
        """
        _response = self._raw_client.set_eq_on(request_options=request_options)
        return _response.data

    def set_eq_off(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=EQOff

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Default response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.set_eq_off()
        """
        _response = self._raw_client.set_eq_off(request_options=request_options)
        return _response.data

    def get_eq_stat(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetEqStatResponse:
        """
        http://10.10.10.254/httpapi.asp?command=EQGetStat

        JSON Response:
        {"EQStat":"On"} or {"EQStat":"Off"}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEqStatResponse
            Default response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.get_eq_stat()
        """
        _response = self._raw_client.get_eq_stat(request_options=request_options)
        return _response.data

    def get_eq_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=EQGetList


        Response:

        ["Flat", "Acoustic", "Bass Booster", "Bass Reducer", "Classical",
        "Dance", "Deep", "Electronic",

        "Hip-Hop", "Jazz", "Latin", "Loudness", "Lounge", "Piano", "Pop", "R&B",
        "Rock", "Small

        Speakers", "Spoken Word", "Treble Booster", "Treble Reducer", "Vocal
        Booster"]

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Default response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.get_eq_list()
        """
        _response = self._raw_client.get_eq_list(request_options=request_options)
        return _response.data

    def get_eq_band(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=EQGetBand

        Response:

        {"status":"OK","source_name":"wifi","EQStat":"Off","Name":"Rock","pluginURI":"http://moddevices.com/plugins/caps/Eq10HP","channelMode":"Stereo","EQBand":[{"index":0,"param_name":"band31hz","value":71},{"index":1,"param_name":"band63hz","value":67},{"index":2,"param_name":"band125hz","value":63},{"index":3,"param_name":"band250hz","value":56},{"index":4,"param_name":"band500hz","value":48},{"index":5,"param_name":"band1khz","value":46},{"index":6,"param_name":"band2khz","value":52},{"index":7,"param_name":"band4khz","value":60},{"index":8,"param_name":"band8khz","value":65},{"index":9,"param_name":"band16khz","value":56}]}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Default response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.get_eq_band()
        """
        _response = self._raw_client.get_eq_band(request_options=request_options)
        return _response.data

    def load_eq_by_name(
        self, name: LoadEqByNameRequestName, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=EQLoad:xxx


        Note: xxx is the one of the name in the list returned by EQGetList,
        i.e., EQLoad:Flat

        Parameters
        ----------
        name : LoadEqByNameRequestName
            The name in the list returned by EQGetList, i.e., EQLoad:Flat

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Default response

        Examples
        --------
        from fern.equalizer import LoadEqByNameRequestName

        from fern import FernApi

        client = FernApi()
        client.equalizer.load_eq_by_name(
            name=LoadEqByNameRequestName.FLAT,
        )
        """
        _response = self._raw_client.load_eq_by_name(name, request_options=request_options)
        return _response.data

    def eq_set_bass(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_set_bass(
            n=1,
        )
        """
        _response = self._raw_client.eq_set_bass(n, request_options=request_options)
        return _response.data

    def eq_set_treble(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_set_treble(
            n=1,
        )
        """
        _response = self._raw_client.eq_set_treble(n, request_options=request_options)
        return _response.data

    def eq_enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_enable()
        """
        _response = self._raw_client.eq_enable(request_options=request_options)
        return _response.data

    def eq_disable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_disable()
        """
        _response = self._raw_client.eq_disable(request_options=request_options)
        return _response.data

    def eq_set_band(
        self, n1: int, str: str, n2: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        https://10.10.10.254/httpapi.asp?command=EQSetBand:{"EQBand":[{"index":0,"param_name":"band31hz","value":10}]}

        A way to control the 10-band EQ, including real-time updates from external inputs.

        Example 1 - single band change to 10:

        https://10.10.10.254/httpapi.asp?command=EQSetBand:{"EQBand":[{"index":0,"param_name":"band31hz","value":10}]}'

        Example 2 - sets all bands to 52:

        https://10.10.10.254/httpapi.asp?command=EQSetBand:{"EQBand":[{"index":0,"param_name":"band31hz","value":52},{"index":1,"param_name":"band63hz","value":52},{"index":2,"param_name":"band125hz","value":52},{"index":3,"param_name":"band250hz","value":52},{"index":4,"param_name":"band500hz","value":52},{"index":5,"param_name":"band1khz","value":52},{"index":6,"param_name":"band2khz","value":52},{"index":7,"param_name":"band4khz","value":52},{"index":8,"param_name":"band8khz","value":52},{"index":9,"param_name":"band16khz","value":52}]}'


        Notes:
        - using WiiM Ultra with firmware version 5.2.809757 (beta), build date 20260304
        - works instantly on the device
        - changes the currently selected source's EQ
        - values are 0-99 (50 = flat)
        - app UI reflects changes after leaving/re-entering the EQ screen for that source
        - driven from a wireless EQ deck that posts physical slider positions to MQTT, which are then read, scaled, and sent on to the WiiM
        - with ~0.4s throttle the WiiM keeps up and tracks slider movements well
        - EQGetBand tells you info about your current source, including the band values, which is how I worked this out.

        Parameters
        ----------
        n1 : int
            Index of the EQ band to set, where 0 corresponds to the 31Hz band, 1 to the 62Hz band, and so on up to 9 for the 16kHz band.

        str : str
            Name of the parameter to set, which should be in the format "band{frequency}hz", where {frequency} is the center frequency of the band (e.g., "band31hz", "band63hz", "band125hz", "band250hz", "band500hz", "band1khz", "band2khz", "band4khz", "band8khz", "band16khz").

        n2 : int
            Value to set for the specified EQ band, where 0-99 represents the gain level (50 = flat, values above 50 boost the band, and values below 50 cut the band).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_set_band(
            n1=1,
            str="str",
            n2=1,
        )
        """
        _response = self._raw_client.eq_set_band(n1, str, n2, request_options=request_options)
        return _response.data

    def eq_set_lv2band(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_set_lv2band(
            str="str",
        )
        """
        _response = self._raw_client.eq_set_lv2band(str, request_options=request_options)
        return _response.data

    def eq_set_lv2source_band(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_set_lv2source_band(
            str="str",
        )
        """
        _response = self._raw_client.eq_set_lv2source_band(str, request_options=request_options)
        return _response.data

    def eqv2delete(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eqv2delete(
            str="str",
        )
        """
        _response = self._raw_client.eqv2delete(str, request_options=request_options)
        return _response.data

    def eqv2rename(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eqv2rename(
            str="str",
        )
        """
        _response = self._raw_client.eqv2rename(str, request_options=request_options)
        return _response.data

    def eq_change_source_fx(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_change_source_fx(
            str="str",
        )
        """
        _response = self._raw_client.eq_change_source_fx(str, request_options=request_options)
        return _response.data

    def eq_change_fx(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_change_fx(
            str="str",
        )
        """
        _response = self._raw_client.eq_change_fx(str, request_options=request_options)
        return _response.data

    def eq_get_lv2band(self, plugin_uri: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        plugin_uri : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_get_lv2band(
            plugin_uri="http://moddevices.com/plugins/caps/Eq10HP",
        )
        """
        _response = self._raw_client.eq_get_lv2band(plugin_uri, request_options=request_options)
        return _response.data

    def eq_get_lv2source_band(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_get_lv2source_band(
            str="str",
        )
        """
        _response = self._raw_client.eq_get_lv2source_band(str, request_options=request_options)
        return _response.data

    def eq_get_lv2source_band_ex(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_get_lv2source_band_ex(
            str="str",
        )
        """
        _response = self._raw_client.eq_get_lv2source_band_ex(str, request_options=request_options)
        return _response.data

    def eqv2get_list(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eqv2get_list(
            str="str",
        )
        """
        _response = self._raw_client.eqv2get_list(str, request_options=request_options)
        return _response.data

    def eqv2get_new_list(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eqv2get_new_list(
            str="str",
        )
        """
        _response = self._raw_client.eqv2get_new_list(str, request_options=request_options)
        return _response.data

    def eqv2load(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eqv2load(
            str="str",
        )
        """
        _response = self._raw_client.eqv2load(str, request_options=request_options)
        return _response.data

    def eqv2source_load(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eqv2source_load(
            str="str",
        )
        """
        _response = self._raw_client.eqv2source_load(str, request_options=request_options)
        return _response.data

    def eq_source_off(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_source_off(
            str="str",
        )
        """
        _response = self._raw_client.eq_source_off(str, request_options=request_options)
        return _response.data

    def eq_set_channel_mode(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_set_channel_mode(
            str="str",
        )
        """
        _response = self._raw_client.eq_set_channel_mode(str, request_options=request_options)
        return _response.data

    def eq_source_save(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_source_save(
            str="str",
        )
        """
        _response = self._raw_client.eq_source_save(str, request_options=request_options)
        return _response.data

    def eq_save(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_save(
            str="str",
        )
        """
        _response = self._raw_client.eq_save(str, request_options=request_options)
        return _response.data

    def eq_get_lv2band_ex(self, plugin_uri: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        plugin_uri : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_get_lv2band_ex(
            plugin_uri="http://moddevices.com/plugins/caps/Eq10HP",
        )
        """
        _response = self._raw_client.eq_get_lv2band_ex(plugin_uri, request_options=request_options)
        return _response.data

    def eq_get_source_modes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EqGetSourceModesResponseItem]:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=EQGetSourceModes

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EqGetSourceModesResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_get_source_modes()
        """
        _response = self._raw_client.eq_get_source_modes(request_options=request_options)
        return _response.data

    def eq_save_custom(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=EQSave:Custom

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.equalizer.eq_save_custom()
        """
        _response = self._raw_client.eq_save_custom(request_options=request_options)
        return _response.data


class AsyncEqualizerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEqualizerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEqualizerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEqualizerClient
        """
        return self._raw_client

    async def set_eq_on(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=EQOn

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.equalizer.set_eq_on()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_eq_on(request_options=request_options)
        return _response.data

    async def set_eq_off(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        https://10.10.10.254/httpapi.asp?command=EQOff

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.equalizer.set_eq_off()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_eq_off(request_options=request_options)
        return _response.data

    async def get_eq_stat(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetEqStatResponse:
        """
        http://10.10.10.254/httpapi.asp?command=EQGetStat

        JSON Response:
        {"EQStat":"On"} or {"EQStat":"Off"}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEqStatResponse
            Default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.equalizer.get_eq_stat()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_eq_stat(request_options=request_options)
        return _response.data

    async def get_eq_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=EQGetList


        Response:

        ["Flat", "Acoustic", "Bass Booster", "Bass Reducer", "Classical",
        "Dance", "Deep", "Electronic",

        "Hip-Hop", "Jazz", "Latin", "Loudness", "Lounge", "Piano", "Pop", "R&B",
        "Rock", "Small

        Speakers", "Spoken Word", "Treble Booster", "Treble Reducer", "Vocal
        Booster"]

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.equalizer.get_eq_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_eq_list(request_options=request_options)
        return _response.data

    async def get_eq_band(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=EQGetBand

        Response:

        {"status":"OK","source_name":"wifi","EQStat":"Off","Name":"Rock","pluginURI":"http://moddevices.com/plugins/caps/Eq10HP","channelMode":"Stereo","EQBand":[{"index":0,"param_name":"band31hz","value":71},{"index":1,"param_name":"band63hz","value":67},{"index":2,"param_name":"band125hz","value":63},{"index":3,"param_name":"band250hz","value":56},{"index":4,"param_name":"band500hz","value":48},{"index":5,"param_name":"band1khz","value":46},{"index":6,"param_name":"band2khz","value":52},{"index":7,"param_name":"band4khz","value":60},{"index":8,"param_name":"band8khz","value":65},{"index":9,"param_name":"band16khz","value":56}]}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.equalizer.get_eq_band()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_eq_band(request_options=request_options)
        return _response.data

    async def load_eq_by_name(
        self, name: LoadEqByNameRequestName, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=EQLoad:xxx


        Note: xxx is the one of the name in the list returned by EQGetList,
        i.e., EQLoad:Flat

        Parameters
        ----------
        name : LoadEqByNameRequestName
            The name in the list returned by EQGetList, i.e., EQLoad:Flat

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Default response

        Examples
        --------
        import asyncio

        from fern.equalizer import LoadEqByNameRequestName

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.equalizer.load_eq_by_name(
                name=LoadEqByNameRequestName.FLAT,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.load_eq_by_name(name, request_options=request_options)
        return _response.data

    async def eq_set_bass(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

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
            await client.equalizer.eq_set_bass(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_set_bass(n, request_options=request_options)
        return _response.data

    async def eq_set_treble(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

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
            await client.equalizer.eq_set_treble(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_set_treble(n, request_options=request_options)
        return _response.data

    async def eq_enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
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
            await client.equalizer.eq_enable()


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_enable(request_options=request_options)
        return _response.data

    async def eq_disable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
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
            await client.equalizer.eq_disable()


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_disable(request_options=request_options)
        return _response.data

    async def eq_set_band(
        self, n1: int, str: str, n2: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        https://10.10.10.254/httpapi.asp?command=EQSetBand:{"EQBand":[{"index":0,"param_name":"band31hz","value":10}]}

        A way to control the 10-band EQ, including real-time updates from external inputs.

        Example 1 - single band change to 10:

        https://10.10.10.254/httpapi.asp?command=EQSetBand:{"EQBand":[{"index":0,"param_name":"band31hz","value":10}]}'

        Example 2 - sets all bands to 52:

        https://10.10.10.254/httpapi.asp?command=EQSetBand:{"EQBand":[{"index":0,"param_name":"band31hz","value":52},{"index":1,"param_name":"band63hz","value":52},{"index":2,"param_name":"band125hz","value":52},{"index":3,"param_name":"band250hz","value":52},{"index":4,"param_name":"band500hz","value":52},{"index":5,"param_name":"band1khz","value":52},{"index":6,"param_name":"band2khz","value":52},{"index":7,"param_name":"band4khz","value":52},{"index":8,"param_name":"band8khz","value":52},{"index":9,"param_name":"band16khz","value":52}]}'


        Notes:
        - using WiiM Ultra with firmware version 5.2.809757 (beta), build date 20260304
        - works instantly on the device
        - changes the currently selected source's EQ
        - values are 0-99 (50 = flat)
        - app UI reflects changes after leaving/re-entering the EQ screen for that source
        - driven from a wireless EQ deck that posts physical slider positions to MQTT, which are then read, scaled, and sent on to the WiiM
        - with ~0.4s throttle the WiiM keeps up and tracks slider movements well
        - EQGetBand tells you info about your current source, including the band values, which is how I worked this out.

        Parameters
        ----------
        n1 : int
            Index of the EQ band to set, where 0 corresponds to the 31Hz band, 1 to the 62Hz band, and so on up to 9 for the 16kHz band.

        str : str
            Name of the parameter to set, which should be in the format "band{frequency}hz", where {frequency} is the center frequency of the band (e.g., "band31hz", "band63hz", "band125hz", "band250hz", "band500hz", "band1khz", "band2khz", "band4khz", "band8khz", "band16khz").

        n2 : int
            Value to set for the specified EQ band, where 0-99 represents the gain level (50 = flat, values above 50 boost the band, and values below 50 cut the band).

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
            await client.equalizer.eq_set_band(
                n1=1,
                str="str",
                n2=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_set_band(n1, str, n2, request_options=request_options)
        return _response.data

    async def eq_set_lv2band(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eq_set_lv2band(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_set_lv2band(str, request_options=request_options)
        return _response.data

    async def eq_set_lv2source_band(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eq_set_lv2source_band(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_set_lv2source_band(str, request_options=request_options)
        return _response.data

    async def eqv2delete(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eqv2delete(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eqv2delete(str, request_options=request_options)
        return _response.data

    async def eqv2rename(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eqv2rename(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eqv2rename(str, request_options=request_options)
        return _response.data

    async def eq_change_source_fx(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eq_change_source_fx(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_change_source_fx(str, request_options=request_options)
        return _response.data

    async def eq_change_fx(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eq_change_fx(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_change_fx(str, request_options=request_options)
        return _response.data

    async def eq_get_lv2band(self, plugin_uri: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        plugin_uri : str
            Unknown

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
            await client.equalizer.eq_get_lv2band(
                plugin_uri="http://moddevices.com/plugins/caps/Eq10HP",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_get_lv2band(plugin_uri, request_options=request_options)
        return _response.data

    async def eq_get_lv2source_band(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eq_get_lv2source_band(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_get_lv2source_band(str, request_options=request_options)
        return _response.data

    async def eq_get_lv2source_band_ex(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eq_get_lv2source_band_ex(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_get_lv2source_band_ex(str, request_options=request_options)
        return _response.data

    async def eqv2get_list(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eqv2get_list(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eqv2get_list(str, request_options=request_options)
        return _response.data

    async def eqv2get_new_list(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eqv2get_new_list(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eqv2get_new_list(str, request_options=request_options)
        return _response.data

    async def eqv2load(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eqv2load(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eqv2load(str, request_options=request_options)
        return _response.data

    async def eqv2source_load(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eqv2source_load(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eqv2source_load(str, request_options=request_options)
        return _response.data

    async def eq_source_off(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eq_source_off(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_source_off(str, request_options=request_options)
        return _response.data

    async def eq_set_channel_mode(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eq_set_channel_mode(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_set_channel_mode(str, request_options=request_options)
        return _response.data

    async def eq_source_save(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eq_source_save(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_source_save(str, request_options=request_options)
        return _response.data

    async def eq_save(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

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
            await client.equalizer.eq_save(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_save(str, request_options=request_options)
        return _response.data

    async def eq_get_lv2band_ex(
        self, plugin_uri: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        plugin_uri : str
            Unknown

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
            await client.equalizer.eq_get_lv2band_ex(
                plugin_uri="http://moddevices.com/plugins/caps/Eq10HP",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_get_lv2band_ex(plugin_uri, request_options=request_options)
        return _response.data

    async def eq_get_source_modes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EqGetSourceModesResponseItem]:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=EQGetSourceModes

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EqGetSourceModesResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.equalizer.eq_get_source_modes()


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_get_source_modes(request_options=request_options)
        return _response.data

    async def eq_save_custom(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=EQSave:Custom

        Parameters
        ----------
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
            await client.equalizer.eq_save_custom()


        asyncio.run(main())
        """
        _response = await self._raw_client.eq_save_custom(request_options=request_options)
        return _response.data
