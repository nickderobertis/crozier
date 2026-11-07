

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEthernetClient, RawEthernetClient
from .types.get_ethernet_settings_response import GetEthernetSettingsResponse
from .types.replace_ethernet_settings_response import ReplaceEthernetSettingsResponse
from .types.update_ethernet_settings_response import UpdateEthernetSettingsResponse


OMIT = typing.cast(typing.Any, ...)


class EthernetClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEthernetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEthernetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEthernetClient
        """
        return self._raw_client

    def get_ethernet_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetEthernetSettingsResponse:
        """
        Reads Ethernet configuration. Changes usually apply dynamically.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEthernetSettingsResponse
            Current Ethernet settings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.ethernet.get_ethernet_settings()
        """
        _response = self._raw_client.get_ethernet_settings(request_options=request_options)
        return _response.data

    def replace_ethernet_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReplaceEthernetSettingsResponse:
        """
        Replaces Ethernet configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplaceEthernetSettingsResponse
            Replaced Ethernet settings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.ethernet.replace_ethernet_settings()
        """
        _response = self._raw_client.replace_ethernet_settings(
            enable=enable,
            static_ip=static_ip,
            ip=ip,
            netmask=netmask,
            gateway=gateway,
            dns=dns,
            request_options=request_options,
        )
        return _response.data

    def update_ethernet_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateEthernetSettingsResponse:
        """
        Partially updates Ethernet configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateEthernetSettingsResponse
            Updated Ethernet settings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.ethernet.update_ethernet_settings()
        """
        _response = self._raw_client.update_ethernet_settings(
            enable=enable,
            static_ip=static_ip,
            ip=ip,
            netmask=netmask,
            gateway=gateway,
            dns=dns,
            request_options=request_options,
        )
        return _response.data


class AsyncEthernetClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEthernetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEthernetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEthernetClient
        """
        return self._raw_client

    async def get_ethernet_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetEthernetSettingsResponse:
        """
        Reads Ethernet configuration. Changes usually apply dynamically.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEthernetSettingsResponse
            Current Ethernet settings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.ethernet.get_ethernet_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ethernet_settings(request_options=request_options)
        return _response.data

    async def replace_ethernet_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReplaceEthernetSettingsResponse:
        """
        Replaces Ethernet configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplaceEthernetSettingsResponse
            Replaced Ethernet settings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.ethernet.replace_ethernet_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_ethernet_settings(
            enable=enable,
            static_ip=static_ip,
            ip=ip,
            netmask=netmask,
            gateway=gateway,
            dns=dns,
            request_options=request_options,
        )
        return _response.data

    async def update_ethernet_settings(
        self,
        *,
        enable: typing.Optional[bool] = OMIT,
        static_ip: typing.Optional[bool] = OMIT,
        ip: typing.Optional[str] = OMIT,
        netmask: typing.Optional[str] = OMIT,
        gateway: typing.Optional[str] = OMIT,
        dns: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateEthernetSettingsResponse:
        """
        Partially updates Ethernet configuration.

        Parameters
        ----------
        enable : typing.Optional[bool]

        static_ip : typing.Optional[bool]

        ip : typing.Optional[str]

        netmask : typing.Optional[str]

        gateway : typing.Optional[str]

        dns : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateEthernetSettingsResponse
            Updated Ethernet settings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.ethernet.update_ethernet_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_ethernet_settings(
            enable=enable,
            static_ip=static_ip,
            ip=ip,
            netmask=netmask,
            gateway=gateway,
            dns=dns,
            request_options=request_options,
        )
        return _response.data
