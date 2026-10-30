

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDeviceControlClient, RawDeviceControlClient
from .types.get_hw_error_info_response import GetHwErrorInfoResponse


class DeviceControlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeviceControlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeviceControlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeviceControlClient
        """
        return self._raw_client

    def reboot_device(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=reboot

        JSON Response:
        {"status":"OK"}

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
        client.device_control.reboot_device()
        """
        _response = self._raw_client.reboot_device(request_options=request_options)
        return _response.data

    def set_shutdown_timer(self, sec: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=setShutdown:sec

        Shutdown device in sec

        sec:
        0: shutdown immediately
        -1: cancel the previous shutdown timer

        Parameters
        ----------
        sec : str
            Shutdown device in sec

            0: shutdown immediately
            -1: cancel the previous shutdown timer

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
        client.device_control.set_shutdown_timer(
            sec="sec",
        )
        """
        _response = self._raw_client.set_shutdown_timer(sec, request_options=request_options)
        return _response.data

    def get_shutdown_timer(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=getShutdown

        Return the seconds

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
        client.device_control.get_shutdown_timer()
        """
        _response = self._raw_client.get_shutdown_timer(request_options=request_options)
        return _response.data

    def set_led_switch(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=LED_SWITCH_SET:0

        Observations:
        - Value is either 1 (on) or 0 (off)

        Parameters
        ----------
        n : int
            1 (on) or 0 (off)

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
        client.device_control.set_led_switch(
            n=1,
        )
        """
        _response = self._raw_client.set_led_switch(n, request_options=request_options)
        return _response.data

    def set_touch_controls(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=Button_Enable_SET:0

        Observations:
        - Value is either 1 (on) or 0 (off)

        Parameters
        ----------
        n : int
            1 (on) or 0 (off)

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
        client.device_control.set_touch_controls(
            n=1,
        )
        """
        _response = self._raw_client.set_touch_controls(n, request_options=request_options)
        return _response.data

    def button_enable_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.device_control.button_enable_get()
        """
        _response = self._raw_client.button_enable_get(request_options=request_options)
        return _response.data

    def get_firmware_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.device_control.get_firmware_version()
        """
        _response = self._raw_client.get_firmware_version(request_options=request_options)
        return _response.data

    def get_device_name_changeable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.device_control.get_device_name_changeable()
        """
        _response = self._raw_client.get_device_name_changeable(request_options=request_options)
        return _response.data

    def restore_to_default(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=restoreToDefault

        To restore factory settings, erasing defined configurations. The device restarts.

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
        client.device_control.restore_to_default()
        """
        _response = self._raw_client.restore_to_default(request_options=request_options)
        return _response.data

    def set_device_name(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setDeviceName:%s

        Sets the name UPnP, DLNA and Airplay of the device (Hex)

        Parameters
        ----------
        name : str
            The new device name to set for UPnP, DLNA, and Airplay, in hexadecimal format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.device_control.set_device_name(
            name="name",
        )
        """
        _response = self._raw_client.set_device_name(name, request_options=request_options)
        return _response.data

    def getsyslog(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.device_control.getsyslog()
        """
        _response = self._raw_client.getsyslog(request_options=request_options)
        return _response.data

    def set_hex_device_name(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.device_control.set_hex_device_name(
            str="str",
        )
        """
        _response = self._raw_client.set_hex_device_name(str, request_options=request_options)
        return _response.data

    def no_send_more_device_event(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.device_control.no_send_more_device_event()
        """
        _response = self._raw_client.no_send_more_device_event(request_options=request_options)
        return _response.data

    def get_hw_error_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetHwErrorInfoResponse:
        """
        ...

        Returns: { "ethError": 0, "mfiChipError": 0, "flashSpaceError": 0, "badBlockNum": 3, "totalBlockNum": 2000, "hdmiError": 0, "temperatureSensorError": 0, "ledError": 0, "soundCardHwError": { "es9018": 0, "pcm5121": 0 } }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetHwErrorInfoResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.device_control.get_hw_error_info()
        """
        _response = self._raw_client.get_hw_error_info(request_options=request_options)
        return _response.data


class AsyncDeviceControlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeviceControlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeviceControlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeviceControlClient
        """
        return self._raw_client

    async def reboot_device(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=reboot

        JSON Response:
        {"status":"OK"}

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
            await client.device_control.reboot_device()


        asyncio.run(main())
        """
        _response = await self._raw_client.reboot_device(request_options=request_options)
        return _response.data

    async def set_shutdown_timer(self, sec: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=setShutdown:sec

        Shutdown device in sec

        sec:
        0: shutdown immediately
        -1: cancel the previous shutdown timer

        Parameters
        ----------
        sec : str
            Shutdown device in sec

            0: shutdown immediately
            -1: cancel the previous shutdown timer

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
            await client.device_control.set_shutdown_timer(
                sec="sec",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_shutdown_timer(sec, request_options=request_options)
        return _response.data

    async def get_shutdown_timer(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        http://10.10.10.254/httpapi.asp?command=getShutdown

        Return the seconds

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
            await client.device_control.get_shutdown_timer()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_shutdown_timer(request_options=request_options)
        return _response.data

    async def set_led_switch(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=LED_SWITCH_SET:0

        Observations:
        - Value is either 1 (on) or 0 (off)

        Parameters
        ----------
        n : int
            1 (on) or 0 (off)

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
            await client.device_control.set_led_switch(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_led_switch(n, request_options=request_options)
        return _response.data

    async def set_touch_controls(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=Button_Enable_SET:0

        Observations:
        - Value is either 1 (on) or 0 (off)

        Parameters
        ----------
        n : int
            1 (on) or 0 (off)

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
            await client.device_control.set_touch_controls(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_touch_controls(n, request_options=request_options)
        return _response.data

    async def button_enable_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.device_control.button_enable_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.button_enable_get(request_options=request_options)
        return _response.data

    async def get_firmware_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.device_control.get_firmware_version()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_firmware_version(request_options=request_options)
        return _response.data

    async def get_device_name_changeable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.device_control.get_device_name_changeable()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_device_name_changeable(request_options=request_options)
        return _response.data

    async def restore_to_default(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=restoreToDefault

        To restore factory settings, erasing defined configurations. The device restarts.

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
            await client.device_control.restore_to_default()


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_to_default(request_options=request_options)
        return _response.data

    async def set_device_name(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setDeviceName:%s

        Sets the name UPnP, DLNA and Airplay of the device (Hex)

        Parameters
        ----------
        name : str
            The new device name to set for UPnP, DLNA, and Airplay, in hexadecimal format.

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
            await client.device_control.set_device_name(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_device_name(name, request_options=request_options)
        return _response.data

    async def getsyslog(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.device_control.getsyslog()


        asyncio.run(main())
        """
        _response = await self._raw_client.getsyslog(request_options=request_options)
        return _response.data

    async def set_hex_device_name(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.device_control.set_hex_device_name(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_hex_device_name(str, request_options=request_options)
        return _response.data

    async def no_send_more_device_event(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.device_control.no_send_more_device_event()


        asyncio.run(main())
        """
        _response = await self._raw_client.no_send_more_device_event(request_options=request_options)
        return _response.data

    async def get_hw_error_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetHwErrorInfoResponse:
        """
        ...

        Returns: { "ethError": 0, "mfiChipError": 0, "flashSpaceError": 0, "badBlockNum": 3, "totalBlockNum": 2000, "hdmiError": 0, "temperatureSensorError": 0, "ledError": 0, "soundCardHwError": { "es9018": 0, "pcm5121": 0 } }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetHwErrorInfoResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.device_control.get_hw_error_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_hw_error_info(request_options=request_options)
        return _response.data
