

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNetworkClient, RawNetworkClient


class NetworkClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNetworkClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNetworkClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNetworkClient
        """
        return self._raw_client

    def get_static_ip_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=getStaticIpInfo

        If the WiiM device is configured to use DHCP, the above string values will be empty (see the ethernet related keys).

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
        client.network.get_static_ip_info()
        """
        _response = self._raw_client.get_static_ip_info(request_options=request_options)
        return _response.data

    def get_static_ip(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Query current networking status

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
        client.network.get_static_ip()
        """
        _response = self._raw_client.get_static_ip(request_options=request_options)
        return _response.data

    def wlan_get_connect_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Makes a call to
        https://10.10.10.254/httpapi.asp?command=wlanGetConnectState


        Note the return result is not in json.


        Return string:

        Return string Description

        PROCESS In progress

        PAIRFAIL Wrong password

        FAIL Connect fail

        OK connected

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
        client.network.wlan_get_connect_state()
        """
        _response = self._raw_client.wlan_get_connect_state(request_options=request_options)
        return _response.data

    def set_wlan_static_ip(
        self,
        ip_address: str,
        gateway_ip: str,
        dns_server_ip: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=setWlanStaticIp:ipAddr=192.168.1.100/24:gateWay=192.168.1.1:dnsServer=8.8.8.8

        Keyword args:
        - ipAddr: Static IP address to set + netmask
        - gateWay: Gateway
        - dnsServer: The DNS Server (default: 8.8.8.8)

        Parameters
        ----------
        ip_address : str
            Static IP address to set + netmask

        gateway_ip : str
            Gateway IP address

        dns_server_ip : str
            The DNS Server (default: 8.8.8.8)

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
        client.network.set_wlan_static_ip(
            ip_address="IpAddress",
            gateway_ip="GatewayIp",
            dns_server_ip="DnsServerIp",
        )
        """
        _response = self._raw_client.set_wlan_static_ip(
            ip_address, gateway_ip, dns_server_ip, request_options=request_options
        )
        return _response.data

    def set_eth_static_ip(
        self,
        ip_address: str,
        gateway_ip: str,
        dns_server_ip: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=setEthStaticIp:ipAddr=192.168.1.100/24:gateWay=192.168.1.1:dnsServer=8.8.8.8

        Keyword args:
        - ipAddr: Static IP address to set + netmask
        - gateWay: Gateway
        - dnsServer: The DNS Server (default: 8.8.8.8)

        Parameters
        ----------
        ip_address : str
            Static IP address to set + netmask

        gateway_ip : str
            Gateway IP address

        dns_server_ip : str
            The DNS Server (default: 8.8.8.8)

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
        client.network.set_eth_static_ip(
            ip_address="IpAddress",
            gateway_ip="GatewayIp",
            dns_server_ip="DnsServerIp",
        )
        """
        _response = self._raw_client.set_eth_static_ip(
            ip_address, gateway_ip, dns_server_ip, request_options=request_options
        )
        return _response.data

    def set_ssid(self, value: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setSSID:value

        Sets a new network name (SSID) of the device in hexadecimal format

        Parameters
        ----------
        value : str
            The new SSID name to set for the device, in hexadecimal format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.network.set_ssid(
            value="value",
        )
        """
        _response = self._raw_client.set_ssid(value, request_options=request_options)
        return _response.data

    def set_network(self, n: int, password: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setNetwork:1:password

        Setting a new password using letters and / or numbers and crossing of setnetwork setting: 1 (Securing WIFI network (WPAPSK) in contrast, setnetwork: 0 (OPEN) makes the network open WIFI.

        No response The system restarts after the validation of the new password.

        Parameters
        ----------
        n : int
            Network security type, where 1 secures the WIFI network with WPAPSK and 0 makes the network open.

        password : str
            The new password to set for the WIFI network, using letters and/or numbers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.network.set_network(
            n=1,
            password="password",
        )
        """
        _response = self._raw_client.set_network(n, password, request_options=request_options)
        return _response.data

    def get_network_prefer_dns(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.network.get_network_prefer_dns()
        """
        _response = self._raw_client.get_network_prefer_dns(request_options=request_options)
        return _response.data

    def get_wlan_band_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.network.get_wlan_band_config()
        """
        _response = self._raw_client.get_wlan_band_config(request_options=request_options)
        return _response.data

    def get_wlan_roam_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.network.get_wlan_roam_config()
        """
        _response = self._raw_client.get_wlan_roam_config(request_options=request_options)
        return _response.data

    def get_ipv6enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.network.get_ipv6enable()
        """
        _response = self._raw_client.get_ipv6enable(request_options=request_options)
        return _response.data

    def set_power_wifi_down(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setPowerWifiDown

        Turns off the wifi

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
        client.network.set_power_wifi_down()
        """
        _response = self._raw_client.set_power_wifi_down(request_options=request_options)
        return _response.data

    def wlan_connect_hide_ap(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.network.wlan_connect_hide_ap(
            str="str",
        )
        """
        _response = self._raw_client.wlan_connect_hide_ap(str, request_options=request_options)
        return _response.data

    def wlan_connect_hide_ap_ex(
        self, str1: str, str2: str, str3: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str1 : str
            Unknown

        str2 : str
            Unknown

        str3 : str
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
        client.network.wlan_connect_hide_ap_ex(
            str1="str1",
            str2="str2",
            str3="str3",
        )
        """
        _response = self._raw_client.wlan_connect_hide_ap_ex(str1, str2, str3, request_options=request_options)
        return _response.data

    def get_network(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.network.get_network()
        """
        _response = self._raw_client.get_network(request_options=request_options)
        return _response.data

    def wlan_get_ap_list_ex(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: {"res":"0"}

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
        client.network.wlan_get_ap_list_ex()
        """
        _response = self._raw_client.wlan_get_ap_list_ex(request_options=request_options)
        return _response.data

    def set_hide_ssid(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.network.set_hide_ssid(
            str="str",
        )
        """
        _response = self._raw_client.set_hide_ssid(str, request_options=request_options)
        return _response.data

    def set_network_ex_aes(
        self, n: int, password: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        password : str
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
        client.network.set_network_ex_aes(
            n=1,
            password="password",
        )
        """
        _response = self._raw_client.set_network_ex_aes(n, password, request_options=request_options)
        return _response.data

    def set_wlan_band_config(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.network.set_wlan_band_config(
            str="str",
        )
        """
        _response = self._raw_client.set_wlan_band_config(str, request_options=request_options)
        return _response.data

    def set_wlan_connect_disable(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.network.set_wlan_connect_disable(
            str="str",
        )
        """
        _response = self._raw_client.set_wlan_connect_disable(str, request_options=request_options)
        return _response.data

    def set_wlan_roam_config(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.network.set_wlan_roam_config(
            str="str",
        )
        """
        _response = self._raw_client.set_wlan_roam_config(str, request_options=request_options)
        return _response.data

    def set_network_prefer_dns(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.network.set_network_prefer_dns(
            str="str",
        )
        """
        _response = self._raw_client.set_network_prefer_dns(str, request_options=request_options)
        return _response.data

    def wlan_get_ap_full_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.network.wlan_get_ap_full_list()
        """
        _response = self._raw_client.wlan_get_ap_full_list(request_options=request_options)
        return _response.data

    def wlan_switch_connected_ap(
        self, ssid: str, bssid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        ssid : str
            Unknown

        bssid : str
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
        client.network.wlan_switch_connected_ap(
            ssid="ssid",
            bssid="bssid",
        )
        """
        _response = self._raw_client.wlan_switch_connected_ap(ssid, bssid, request_options=request_options)
        return _response.data

    def set_ipv6enable(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.network.set_ipv6enable(
            str="str",
        )
        """
        _response = self._raw_client.set_ipv6enable(str, request_options=request_options)
        return _response.data

    def get_wlan_connect_disable_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.network.get_wlan_connect_disable_status()
        """
        _response = self._raw_client.get_wlan_connect_disable_status(request_options=request_options)
        return _response.data

    def get_network_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: {"wlanDhcpTime":0, "ethDhcpTime":1, "wlanIpChanged":0, "wlanRoamingOn":0, "wlanBand":0, "wlanHistoryNum":0, "disconnectedCount":1, "lastDisconnectedTime":1, "ethDisconnectedCount":0, "lastDisconnectedMsg":"",  "ethNotReady":0, "pingCheckFailedCount":0, "wlanConnectTime":0, "wlanAbnormalRebootTimes":0, "wlanIsStaticIp":0, "ethIsStaticIp":0}

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
        client.network.get_network_health()
        """
        _response = self._raw_client.get_network_health(request_options=request_options)
        return _response.data

    def wpscannel(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: http://10.10.10.254/httpapi.asp?command=wpscannel

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
        client.network.wpscannel()
        """
        _response = self._raw_client.wpscannel(request_options=request_options)
        return _response.data

    def wpsclientmode(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: http://10.10.10.254/httpapi.asp?command=wpsclientmode

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
        client.network.wpsclientmode()
        """
        _response = self._raw_client.wpsclientmode(request_options=request_options)
        return _response.data

    def wpsservermode(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: http://10.10.10.254/httpapi.asp?command=wpsservermode

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
        client.network.wpsservermode()
        """
        _response = self._raw_client.wpsservermode(request_options=request_options)
        return _response.data


class AsyncNetworkClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNetworkClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNetworkClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNetworkClient
        """
        return self._raw_client

    async def get_static_ip_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=getStaticIpInfo

        If the WiiM device is configured to use DHCP, the above string values will be empty (see the ethernet related keys).

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
            await client.network.get_static_ip_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_static_ip_info(request_options=request_options)
        return _response.data

    async def get_static_ip(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Query current networking status

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
            await client.network.get_static_ip()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_static_ip(request_options=request_options)
        return _response.data

    async def wlan_get_connect_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Makes a call to
        https://10.10.10.254/httpapi.asp?command=wlanGetConnectState


        Note the return result is not in json.


        Return string:

        Return string Description

        PROCESS In progress

        PAIRFAIL Wrong password

        FAIL Connect fail

        OK connected

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
            await client.network.wlan_get_connect_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.wlan_get_connect_state(request_options=request_options)
        return _response.data

    async def set_wlan_static_ip(
        self,
        ip_address: str,
        gateway_ip: str,
        dns_server_ip: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=setWlanStaticIp:ipAddr=192.168.1.100/24:gateWay=192.168.1.1:dnsServer=8.8.8.8

        Keyword args:
        - ipAddr: Static IP address to set + netmask
        - gateWay: Gateway
        - dnsServer: The DNS Server (default: 8.8.8.8)

        Parameters
        ----------
        ip_address : str
            Static IP address to set + netmask

        gateway_ip : str
            Gateway IP address

        dns_server_ip : str
            The DNS Server (default: 8.8.8.8)

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
            await client.network.set_wlan_static_ip(
                ip_address="IpAddress",
                gateway_ip="GatewayIp",
                dns_server_ip="DnsServerIp",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_wlan_static_ip(
            ip_address, gateway_ip, dns_server_ip, request_options=request_options
        )
        return _response.data

    async def set_eth_static_ip(
        self,
        ip_address: str,
        gateway_ip: str,
        dns_server_ip: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Example: https://10.10.10.254/httpapi.asp?command=setEthStaticIp:ipAddr=192.168.1.100/24:gateWay=192.168.1.1:dnsServer=8.8.8.8

        Keyword args:
        - ipAddr: Static IP address to set + netmask
        - gateWay: Gateway
        - dnsServer: The DNS Server (default: 8.8.8.8)

        Parameters
        ----------
        ip_address : str
            Static IP address to set + netmask

        gateway_ip : str
            Gateway IP address

        dns_server_ip : str
            The DNS Server (default: 8.8.8.8)

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
            await client.network.set_eth_static_ip(
                ip_address="IpAddress",
                gateway_ip="GatewayIp",
                dns_server_ip="DnsServerIp",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_eth_static_ip(
            ip_address, gateway_ip, dns_server_ip, request_options=request_options
        )
        return _response.data

    async def set_ssid(self, value: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setSSID:value

        Sets a new network name (SSID) of the device in hexadecimal format

        Parameters
        ----------
        value : str
            The new SSID name to set for the device, in hexadecimal format.

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
            await client.network.set_ssid(
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_ssid(value, request_options=request_options)
        return _response.data

    async def set_network(
        self, n: int, password: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setNetwork:1:password

        Setting a new password using letters and / or numbers and crossing of setnetwork setting: 1 (Securing WIFI network (WPAPSK) in contrast, setnetwork: 0 (OPEN) makes the network open WIFI.

        No response The system restarts after the validation of the new password.

        Parameters
        ----------
        n : int
            Network security type, where 1 secures the WIFI network with WPAPSK and 0 makes the network open.

        password : str
            The new password to set for the WIFI network, using letters and/or numbers.

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
            await client.network.set_network(
                n=1,
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_network(n, password, request_options=request_options)
        return _response.data

    async def get_network_prefer_dns(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.network.get_network_prefer_dns()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_network_prefer_dns(request_options=request_options)
        return _response.data

    async def get_wlan_band_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.network.get_wlan_band_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wlan_band_config(request_options=request_options)
        return _response.data

    async def get_wlan_roam_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.network.get_wlan_roam_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wlan_roam_config(request_options=request_options)
        return _response.data

    async def get_ipv6enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.network.get_ipv6enable()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ipv6enable(request_options=request_options)
        return _response.data

    async def set_power_wifi_down(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setPowerWifiDown

        Turns off the wifi

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
            await client.network.set_power_wifi_down()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_power_wifi_down(request_options=request_options)
        return _response.data

    async def wlan_connect_hide_ap(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.network.wlan_connect_hide_ap(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wlan_connect_hide_ap(str, request_options=request_options)
        return _response.data

    async def wlan_connect_hide_ap_ex(
        self, str1: str, str2: str, str3: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str1 : str
            Unknown

        str2 : str
            Unknown

        str3 : str
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
            await client.network.wlan_connect_hide_ap_ex(
                str1="str1",
                str2="str2",
                str3="str3",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wlan_connect_hide_ap_ex(str1, str2, str3, request_options=request_options)
        return _response.data

    async def get_network(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.network.get_network()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_network(request_options=request_options)
        return _response.data

    async def wlan_get_ap_list_ex(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: {"res":"0"}

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
            await client.network.wlan_get_ap_list_ex()


        asyncio.run(main())
        """
        _response = await self._raw_client.wlan_get_ap_list_ex(request_options=request_options)
        return _response.data

    async def set_hide_ssid(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.network.set_hide_ssid(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_hide_ssid(str, request_options=request_options)
        return _response.data

    async def set_network_ex_aes(
        self, n: int, password: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        password : str
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
            await client.network.set_network_ex_aes(
                n=1,
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_network_ex_aes(n, password, request_options=request_options)
        return _response.data

    async def set_wlan_band_config(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.network.set_wlan_band_config(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_wlan_band_config(str, request_options=request_options)
        return _response.data

    async def set_wlan_connect_disable(
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
            await client.network.set_wlan_connect_disable(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_wlan_connect_disable(str, request_options=request_options)
        return _response.data

    async def set_wlan_roam_config(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.network.set_wlan_roam_config(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_wlan_roam_config(str, request_options=request_options)
        return _response.data

    async def set_network_prefer_dns(
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
            await client.network.set_network_prefer_dns(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_network_prefer_dns(str, request_options=request_options)
        return _response.data

    async def wlan_get_ap_full_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.network.wlan_get_ap_full_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.wlan_get_ap_full_list(request_options=request_options)
        return _response.data

    async def wlan_switch_connected_ap(
        self, ssid: str, bssid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        ssid : str
            Unknown

        bssid : str
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
            await client.network.wlan_switch_connected_ap(
                ssid="ssid",
                bssid="bssid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wlan_switch_connected_ap(ssid, bssid, request_options=request_options)
        return _response.data

    async def set_ipv6enable(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.network.set_ipv6enable(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_ipv6enable(str, request_options=request_options)
        return _response.data

    async def get_wlan_connect_disable_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.network.get_wlan_connect_disable_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wlan_connect_disable_status(request_options=request_options)
        return _response.data

    async def get_network_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: {"wlanDhcpTime":0, "ethDhcpTime":1, "wlanIpChanged":0, "wlanRoamingOn":0, "wlanBand":0, "wlanHistoryNum":0, "disconnectedCount":1, "lastDisconnectedTime":1, "ethDisconnectedCount":0, "lastDisconnectedMsg":"",  "ethNotReady":0, "pingCheckFailedCount":0, "wlanConnectTime":0, "wlanAbnormalRebootTimes":0, "wlanIsStaticIp":0, "ethIsStaticIp":0}

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
            await client.network.get_network_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_network_health(request_options=request_options)
        return _response.data

    async def wpscannel(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: http://10.10.10.254/httpapi.asp?command=wpscannel

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
            await client.network.wpscannel()


        asyncio.run(main())
        """
        _response = await self._raw_client.wpscannel(request_options=request_options)
        return _response.data

    async def wpsclientmode(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: http://10.10.10.254/httpapi.asp?command=wpsclientmode

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
            await client.network.wpsclientmode()


        asyncio.run(main())
        """
        _response = await self._raw_client.wpsclientmode(request_options=request_options)
        return _response.data

    async def wpsservermode(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: http://10.10.10.254/httpapi.asp?command=wpsservermode

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
            await client.network.wpsservermode()


        asyncio.run(main())
        """
        _response = await self._raw_client.wpsservermode(request_options=request_options)
        return _response.data
