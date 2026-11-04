

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWiFiClient, RawWiFiClient
from .types.get_wifi_sta_settings_response import GetWifiStaSettingsResponse
from .types.replace_wifi_sta_settings_response import ReplaceWifiStaSettingsResponse
from .types.scan_wifi_response_item import ScanWifiResponseItem
from .types.update_wifi_sta_settings_response import UpdateWifiStaSettingsResponse


OMIT = typing.cast(typing.Any, ...)


class WiFiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWiFiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWiFiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWiFiClient
        """
        return self._raw_client

    def scan_wifi(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ScanWifiResponseItem]:
        """
        Performs a scan and returns visible access points with RSSI and channel information.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ScanWifiResponseItem]
            Array of detected networks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.wi_fi.scan_wifi()
        """
        _response = self._raw_client.scan_wifi(request_options=request_options)
        return _response.data

    def get_wifi_sta_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWifiStaSettingsResponse:
        """
        Reads the STA (client) configuration. Changes apply without reboot.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWifiStaSettingsResponse
            Current station settings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.wi_fi.get_wifi_sta_settings()
        """
        _response = self._raw_client.get_wifi_sta_settings(request_options=request_options)
        return _response.data

    def replace_wifi_sta_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        max_power: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReplaceWifiStaSettingsResponse:
        """
        Replaces the STA (client) configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        name : typing.Optional[str]
            SSID

        password : typing.Optional[str]
            Wi‑Fi password (empty for open networks)

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        max_power : typing.Optional[float]
            dBm; resolution 0.5

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplaceWifiStaSettingsResponse
            Replaced settings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.wi_fi.replace_wifi_sta_settings()
        """
        _response = self._raw_client.replace_wifi_sta_settings(
            enable=enable,
            name=name,
            password=password,
            static_ip=static_ip,
            ip=ip,
            netmask=netmask,
            gateway=gateway,
            dns=dns,
            max_power=max_power,
            request_options=request_options,
        )
        return _response.data

    def update_wifi_sta_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        max_power: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWifiStaSettingsResponse:
        """
        Partially updates the STA (client) configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        name : typing.Optional[str]
            SSID

        password : typing.Optional[str]
            Wi‑Fi password (empty for open networks)

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        max_power : typing.Optional[float]
            dBm; resolution 0.5

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWifiStaSettingsResponse
            Updated settings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.wi_fi.update_wifi_sta_settings()
        """
        _response = self._raw_client.update_wifi_sta_settings(
            enable=enable,
            name=name,
            password=password,
            static_ip=static_ip,
            ip=ip,
            netmask=netmask,
            gateway=gateway,
            dns=dns,
            max_power=max_power,
            request_options=request_options,
        )
        return _response.data

    def delete_wifi_sta_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Clears the STA (client) configuration and disables the client.

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

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.wi_fi.delete_wifi_sta_settings()
        """
        _response = self._raw_client.delete_wifi_sta_settings(request_options=request_options)
        return _response.data


class AsyncWiFiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWiFiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWiFiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWiFiClient
        """
        return self._raw_client

    async def scan_wifi(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ScanWifiResponseItem]:
        """
        Performs a scan and returns visible access points with RSSI and channel information.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ScanWifiResponseItem]
            Array of detected networks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.wi_fi.scan_wifi()


        asyncio.run(main())
        """
        _response = await self._raw_client.scan_wifi(request_options=request_options)
        return _response.data

    async def get_wifi_sta_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWifiStaSettingsResponse:
        """
        Reads the STA (client) configuration. Changes apply without reboot.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWifiStaSettingsResponse
            Current station settings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.wi_fi.get_wifi_sta_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wifi_sta_settings(request_options=request_options)
        return _response.data

    async def replace_wifi_sta_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        max_power: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReplaceWifiStaSettingsResponse:
        """
        Replaces the STA (client) configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        name : typing.Optional[str]
            SSID

        password : typing.Optional[str]
            Wi‑Fi password (empty for open networks)

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        max_power : typing.Optional[float]
            dBm; resolution 0.5

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplaceWifiStaSettingsResponse
            Replaced settings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.wi_fi.replace_wifi_sta_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_wifi_sta_settings(
            enable=enable,
            name=name,
            password=password,
            static_ip=static_ip,
            ip=ip,
            netmask=netmask,
            gateway=gateway,
            dns=dns,
            max_power=max_power,
            request_options=request_options,
        )
        return _response.data

    async def update_wifi_sta_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        max_power: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWifiStaSettingsResponse:
        """
        Partially updates the STA (client) configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        name : typing.Optional[str]
            SSID

        password : typing.Optional[str]
            Wi‑Fi password (empty for open networks)

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        max_power : typing.Optional[float]
            dBm; resolution 0.5

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWifiStaSettingsResponse
            Updated settings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.wi_fi.update_wifi_sta_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_wifi_sta_settings(
            enable=enable,
            name=name,
            password=password,
            static_ip=static_ip,
            ip=ip,
            netmask=netmask,
            gateway=gateway,
            dns=dns,
            max_power=max_power,
            request_options=request_options,
        )
        return _response.data

    async def delete_wifi_sta_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Clears the STA (client) configuration and disables the client.

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

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.wi_fi.delete_wifi_sta_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_wifi_sta_settings(request_options=request_options)
        return _response.data
