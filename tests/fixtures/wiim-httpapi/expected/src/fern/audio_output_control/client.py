

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAudioOutputControlClient, RawAudioOutputControlClient


class AudioOutputControlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAudioOutputControlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAudioOutputControlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAudioOutputControlClient
        """
        return self._raw_client

    def get_new_audio_output_hardware_mode(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        JSON Response:
        {"hardware":"2","source":"0","audiocast":"0"}

        Description:
        Field Description
        hardware Hardware Interface output mode:
        1: AUDIO_OUTPUT_SPDIF_MODE
        2: AUDIO_OUTPUT_AUX_MODE
        3: AUDIO_OUTPUT_COAX_MODE
        source BT source output mode:
        0: disable
        1: active
        audiocast Audio cast output mode:
        0: disable
        1: active

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
        client.audio_output_control.get_new_audio_output_hardware_mode()
        """
        _response = self._raw_client.get_new_audio_output_hardware_mode(request_options=request_options)
        return _response.data

    def set_audio_output_hardware_mode(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Field Description
        Hardware Interface output mode:
        1: AUDIO_OUTPUT_SPDIF_MODE
        2: AUDIO_OUTPUT_AUX_MODE
        3: AUDIO_OUTPUT_COAX_MODE
        Response is 'OK'

        Parameters
        ----------
        n : int
            Hardware Interface output mode:
            1: AUDIO_OUTPUT_SPDIF_MODE
            2: AUDIO_OUTPUT_AUX_MODE
            3: AUDIO_OUTPUT_COAX_MODE

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
        client.audio_output_control.set_audio_output_hardware_mode(
            n=1,
        )
        """
        _response = self._raw_client.set_audio_output_hardware_mode(n, request_options=request_options)
        return _response.data

    def get_spdif_out_switch_delay_ms(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=getSpdifOutSwitchDelayMs

        Observations:
        - This value only makes sense if the output interface is SPDIF (optical out).
        - Value can be retrieved even if output is not SPDIF

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
        client.audio_output_control.get_spdif_out_switch_delay_ms()
        """
        _response = self._raw_client.get_spdif_out_switch_delay_ms(request_options=request_options)
        return _response.data

    def set_spdif_out_switch_delay_ms(
        self, delay: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=setSpdifOutSwitchDelayMs:800

        Observations:
        - Delay is in milliseconds
        - Value can be set even if output is not SPDIF
        - Delay is upper bound to 3000 milliseconds

        Parameters
        ----------
        delay : int
            The delay in milliseconds

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
        client.audio_output_control.set_spdif_out_switch_delay_ms(
            delay=1,
        )
        """
        _response = self._raw_client.set_spdif_out_switch_delay_ms(delay, request_options=request_options)
        return _response.data

    def get_channel_balance(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=getChannelBalance

        Observations:
        - The value will be a number ranging from -1.0 (fully panned left) to 1.0 (fully panned right).

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
        client.audio_output_control.get_channel_balance()
        """
        _response = self._raw_client.get_channel_balance(request_options=request_options)
        return _response.data

    def set_channel_balance(self, n: float, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=setChannelBalance:0

        Observations:
        - The value must be a number ranging from -1.0 (fully panned left) to 1.0 (fully panned right).

        Parameters
        ----------
        n : float
            Balance from -1.0 (left) to 1.0 (right)

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
        client.audio_output_control.set_channel_balance(
            n=1.1,
        )
        """
        _response = self._raw_client.set_channel_balance(n, request_options=request_options)
        return _response.data

    def get_fade_feature(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=GetFadeFeature

        Returns {"FadeFeature": 1}

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
        client.audio_output_control.get_fade_feature()
        """
        _response = self._raw_client.get_fade_feature(request_options=request_options)
        return _response.data

    def set_fade_feature(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=SetFadeFeature:0

        Parameters
        ----------
        n : int
            Fade feature value (0 or 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.audio_output_control.set_fade_feature(
            n=1,
        )
        """
        _response = self._raw_client.set_fade_feature(n, request_options=request_options)
        return _response.data


class AsyncAudioOutputControlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAudioOutputControlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAudioOutputControlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAudioOutputControlClient
        """
        return self._raw_client

    async def get_new_audio_output_hardware_mode(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        JSON Response:
        {"hardware":"2","source":"0","audiocast":"0"}

        Description:
        Field Description
        hardware Hardware Interface output mode:
        1: AUDIO_OUTPUT_SPDIF_MODE
        2: AUDIO_OUTPUT_AUX_MODE
        3: AUDIO_OUTPUT_COAX_MODE
        source BT source output mode:
        0: disable
        1: active
        audiocast Audio cast output mode:
        0: disable
        1: active

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
            await client.audio_output_control.get_new_audio_output_hardware_mode()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_new_audio_output_hardware_mode(request_options=request_options)
        return _response.data

    async def set_audio_output_hardware_mode(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Field Description
        Hardware Interface output mode:
        1: AUDIO_OUTPUT_SPDIF_MODE
        2: AUDIO_OUTPUT_AUX_MODE
        3: AUDIO_OUTPUT_COAX_MODE
        Response is 'OK'

        Parameters
        ----------
        n : int
            Hardware Interface output mode:
            1: AUDIO_OUTPUT_SPDIF_MODE
            2: AUDIO_OUTPUT_AUX_MODE
            3: AUDIO_OUTPUT_COAX_MODE

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
            await client.audio_output_control.set_audio_output_hardware_mode(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_audio_output_hardware_mode(n, request_options=request_options)
        return _response.data

    async def get_spdif_out_switch_delay_ms(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=getSpdifOutSwitchDelayMs

        Observations:
        - This value only makes sense if the output interface is SPDIF (optical out).
        - Value can be retrieved even if output is not SPDIF

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
            await client.audio_output_control.get_spdif_out_switch_delay_ms()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_spdif_out_switch_delay_ms(request_options=request_options)
        return _response.data

    async def set_spdif_out_switch_delay_ms(
        self, delay: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=setSpdifOutSwitchDelayMs:800

        Observations:
        - Delay is in milliseconds
        - Value can be set even if output is not SPDIF
        - Delay is upper bound to 3000 milliseconds

        Parameters
        ----------
        delay : int
            The delay in milliseconds

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
            await client.audio_output_control.set_spdif_out_switch_delay_ms(
                delay=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_spdif_out_switch_delay_ms(delay, request_options=request_options)
        return _response.data

    async def get_channel_balance(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=getChannelBalance

        Observations:
        - The value will be a number ranging from -1.0 (fully panned left) to 1.0 (fully panned right).

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
            await client.audio_output_control.get_channel_balance()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_channel_balance(request_options=request_options)
        return _response.data

    async def set_channel_balance(self, n: float, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=setChannelBalance:0

        Observations:
        - The value must be a number ranging from -1.0 (fully panned left) to 1.0 (fully panned right).

        Parameters
        ----------
        n : float
            Balance from -1.0 (left) to 1.0 (right)

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
            await client.audio_output_control.set_channel_balance(
                n=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_channel_balance(n, request_options=request_options)
        return _response.data

    async def get_fade_feature(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=GetFadeFeature

        Returns {"FadeFeature": 1}

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
            await client.audio_output_control.get_fade_feature()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fade_feature(request_options=request_options)
        return _response.data

    async def set_fade_feature(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=SetFadeFeature:0

        Parameters
        ----------
        n : int
            Fade feature value (0 or 1)

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
            await client.audio_output_control.set_fade_feature(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_fade_feature(n, request_options=request_options)
        return _response.data
