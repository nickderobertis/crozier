

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBluetoothClient, RawBluetoothClient


class BluetoothClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBluetoothClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBluetoothClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBluetoothClient
        """
        return self._raw_client

    def start_bt_discovery(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Args: 3 (Not sure what this argument means, I've only seen the app use the value 3 for it. Works with other integers and successfully starts a BT scan. Maybe a max list size?)

        Parameters
        ----------
        n : int
            Not sure what this argument means, I've only seen the app use the value 3 for it. Works with other integers and successfully starts a BT scan. Maybe a max list size?

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
        client.bluetooth.start_bt_discovery(
            n=1,
        )
        """
        _response = self._raw_client.start_bt_discovery(n, request_options=request_options)
        return _response.data

    def get_bt_discovery_result(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        First do a startbtdiscovery:3: to start the scan, then use this to get the result.

        Output (JSON):
        num: Number of found devices
        scan_status: BT scan step
          0: Not started
          1: Initializing
          2: ??? (never seen it)
          3: Scanning
          4: Finished scanning
        list: List of found devices

        Already paired devices may be listed as well.

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
        client.bluetooth.get_bt_discovery_result()
        """
        _response = self._raw_client.get_bt_discovery_result(request_options=request_options)
        return _response.data

    def clear_bt_discovery_result(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Clears the Bluetooth device scan results

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
        client.bluetooth.clear_bt_discovery_result()
        """
        _response = self._raw_client.clear_bt_discovery_result(request_options=request_options)
        return _response.data

    def get_bt_history(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Output (JSON):

        num: Number of found devices
        scan_status: BT scan step
        1: Initializing
        2: ??? (never seen it)
        3: Scanning
        4: Finished scanning
        list: List of found devices

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
        client.bluetooth.get_bt_history()
        """
        _response = self._raw_client.get_bt_history(request_options=request_options)
        return _response.data

    def connect_bt_a2dpsynk(
        self, bt_mac_address: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Example: https://192.168.1.100/httpapi.asp?command=connectbta2dpsynk:9c:2a:be:2e:ce:f1

        Output:
        Success: OK
        Error: Failed

        Observations: The device should be an Audio Sink (e.g. speaker, A/V reciever). The audio output will be changed to the device.

        Parameters
        ----------
        bt_mac_address : str
            The Bluetooth MAC address of the device you want to connect to or disconnect from

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
        client.bluetooth.connect_bt_a2dpsynk(
            bt_mac_address="BT_MAC_ADDRESS",
        )
        """
        _response = self._raw_client.connect_bt_a2dpsynk(bt_mac_address, request_options=request_options)
        return _response.data

    def disconnect_bt_a2dpsynk(
        self, bt_mac_address: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Example: https://192.168.1.100/httpapi.asp?command=disconnectbta2dpsynk:9c:2a:be:2e:ce:f1

        Parameters
        ----------
        bt_mac_address : str
            The Bluetooth MAC address of the device you want to connect to or disconnect from

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
        client.bluetooth.disconnect_bt_a2dpsynk(
            bt_mac_address="BT_MAC_ADDRESS",
        )
        """
        _response = self._raw_client.disconnect_bt_a2dpsynk(bt_mac_address, request_options=request_options)
        return _response.data

    def get_bt_pair_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: https://192.168.1.100/httpapi.asp?command=getbtpairstatus

        Output (JSON):
        result: Pair status
        0: Not paired
        1: Disconnected
        2: Connecting (assumption, never seen it)
        3: Connected

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
        client.bluetooth.get_bt_pair_status()
        """
        _response = self._raw_client.get_bt_pair_status(request_options=request_options)
        return _response.data

    def connectbta2dpsource(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.connectbta2dpsource(
            str="str",
        )
        """
        _response = self._raw_client.connectbta2dpsource(str, request_options=request_options)
        return _response.data

    def delbthistory(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.delbthistory(
            str="str",
        )
        """
        _response = self._raw_client.delbthistory(str, request_options=request_options)
        return _response.data

    def btdisconnectall(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.btdisconnectall()
        """
        _response = self._raw_client.btdisconnectall(request_options=request_options)
        return _response.data

    def getbt_pair_dev_stat(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.getbt_pair_dev_stat()
        """
        _response = self._raw_client.getbt_pair_dev_stat(request_options=request_options)
        return _response.data

    def getbtstatus(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.getbtstatus()
        """
        _response = self._raw_client.getbtstatus(request_options=request_options)
        return _response.data

    def startbtserver(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.startbtserver()
        """
        _response = self._raw_client.startbtserver(request_options=request_options)
        return _response.data

    def startgetbt_pair_dev_stat(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.startgetbt_pair_dev_stat()
        """
        _response = self._raw_client.startgetbt_pair_dev_stat(request_options=request_options)
        return _response.data

    def stopbtdiscovery(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.stopbtdiscovery()
        """
        _response = self._raw_client.stopbtdiscovery(request_options=request_options)
        return _response.data

    def stopbtserver(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.stopbtserver(
            n=1,
        )
        """
        _response = self._raw_client.stopbtserver(n, request_options=request_options)
        return _response.data

    def btavkenterpair(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.btavkenterpair()
        """
        _response = self._raw_client.btavkenterpair(request_options=request_options)
        return _response.data

    def blehidpair(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.blehidpair(
            str="str",
        )
        """
        _response = self._raw_client.blehidpair(str, request_options=request_options)
        return _response.data

    def blehidremoveall(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.blehidremoveall()
        """
        _response = self._raw_client.blehidremoveall(request_options=request_options)
        return _response.data

    def btrecovery(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.btrecovery()
        """
        _response = self._raw_client.btrecovery(request_options=request_options)
        return _response.data

    def get_ble_hid_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.get_ble_hid_status()
        """
        _response = self._raw_client.get_ble_hid_status(request_options=request_options)
        return _response.data

    def start_ble_scan(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.start_ble_scan(
            n=1,
        )
        """
        _response = self._raw_client.start_ble_scan(n, request_options=request_options)
        return _response.data

    def get_ble_discovery_result(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.bluetooth.get_ble_discovery_result()
        """
        _response = self._raw_client.get_ble_discovery_result(request_options=request_options)
        return _response.data


class AsyncBluetoothClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBluetoothClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBluetoothClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBluetoothClient
        """
        return self._raw_client

    async def start_bt_discovery(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Args: 3 (Not sure what this argument means, I've only seen the app use the value 3 for it. Works with other integers and successfully starts a BT scan. Maybe a max list size?)

        Parameters
        ----------
        n : int
            Not sure what this argument means, I've only seen the app use the value 3 for it. Works with other integers and successfully starts a BT scan. Maybe a max list size?

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
            await client.bluetooth.start_bt_discovery(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_bt_discovery(n, request_options=request_options)
        return _response.data

    async def get_bt_discovery_result(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        First do a startbtdiscovery:3: to start the scan, then use this to get the result.

        Output (JSON):
        num: Number of found devices
        scan_status: BT scan step
          0: Not started
          1: Initializing
          2: ??? (never seen it)
          3: Scanning
          4: Finished scanning
        list: List of found devices

        Already paired devices may be listed as well.

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
            await client.bluetooth.get_bt_discovery_result()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bt_discovery_result(request_options=request_options)
        return _response.data

    async def clear_bt_discovery_result(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Clears the Bluetooth device scan results

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
            await client.bluetooth.clear_bt_discovery_result()


        asyncio.run(main())
        """
        _response = await self._raw_client.clear_bt_discovery_result(request_options=request_options)
        return _response.data

    async def get_bt_history(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Output (JSON):

        num: Number of found devices
        scan_status: BT scan step
        1: Initializing
        2: ??? (never seen it)
        3: Scanning
        4: Finished scanning
        list: List of found devices

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
            await client.bluetooth.get_bt_history()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bt_history(request_options=request_options)
        return _response.data

    async def connect_bt_a2dpsynk(
        self, bt_mac_address: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Example: https://192.168.1.100/httpapi.asp?command=connectbta2dpsynk:9c:2a:be:2e:ce:f1

        Output:
        Success: OK
        Error: Failed

        Observations: The device should be an Audio Sink (e.g. speaker, A/V reciever). The audio output will be changed to the device.

        Parameters
        ----------
        bt_mac_address : str
            The Bluetooth MAC address of the device you want to connect to or disconnect from

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
            await client.bluetooth.connect_bt_a2dpsynk(
                bt_mac_address="BT_MAC_ADDRESS",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.connect_bt_a2dpsynk(bt_mac_address, request_options=request_options)
        return _response.data

    async def disconnect_bt_a2dpsynk(
        self, bt_mac_address: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Example: https://192.168.1.100/httpapi.asp?command=disconnectbta2dpsynk:9c:2a:be:2e:ce:f1

        Parameters
        ----------
        bt_mac_address : str
            The Bluetooth MAC address of the device you want to connect to or disconnect from

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
            await client.bluetooth.disconnect_bt_a2dpsynk(
                bt_mac_address="BT_MAC_ADDRESS",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disconnect_bt_a2dpsynk(bt_mac_address, request_options=request_options)
        return _response.data

    async def get_bt_pair_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: https://192.168.1.100/httpapi.asp?command=getbtpairstatus

        Output (JSON):
        result: Pair status
        0: Not paired
        1: Disconnected
        2: Connecting (assumption, never seen it)
        3: Connected

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
            await client.bluetooth.get_bt_pair_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bt_pair_status(request_options=request_options)
        return _response.data

    async def connectbta2dpsource(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.connectbta2dpsource(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.connectbta2dpsource(str, request_options=request_options)
        return _response.data

    async def delbthistory(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.delbthistory(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delbthistory(str, request_options=request_options)
        return _response.data

    async def btdisconnectall(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.btdisconnectall()


        asyncio.run(main())
        """
        _response = await self._raw_client.btdisconnectall(request_options=request_options)
        return _response.data

    async def getbt_pair_dev_stat(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.getbt_pair_dev_stat()


        asyncio.run(main())
        """
        _response = await self._raw_client.getbt_pair_dev_stat(request_options=request_options)
        return _response.data

    async def getbtstatus(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.getbtstatus()


        asyncio.run(main())
        """
        _response = await self._raw_client.getbtstatus(request_options=request_options)
        return _response.data

    async def startbtserver(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.startbtserver()


        asyncio.run(main())
        """
        _response = await self._raw_client.startbtserver(request_options=request_options)
        return _response.data

    async def startgetbt_pair_dev_stat(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.startgetbt_pair_dev_stat()


        asyncio.run(main())
        """
        _response = await self._raw_client.startgetbt_pair_dev_stat(request_options=request_options)
        return _response.data

    async def stopbtdiscovery(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.stopbtdiscovery()


        asyncio.run(main())
        """
        _response = await self._raw_client.stopbtdiscovery(request_options=request_options)
        return _response.data

    async def stopbtserver(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.stopbtserver(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stopbtserver(n, request_options=request_options)
        return _response.data

    async def btavkenterpair(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.btavkenterpair()


        asyncio.run(main())
        """
        _response = await self._raw_client.btavkenterpair(request_options=request_options)
        return _response.data

    async def blehidpair(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.blehidpair(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.blehidpair(str, request_options=request_options)
        return _response.data

    async def blehidremoveall(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.blehidremoveall()


        asyncio.run(main())
        """
        _response = await self._raw_client.blehidremoveall(request_options=request_options)
        return _response.data

    async def btrecovery(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.btrecovery()


        asyncio.run(main())
        """
        _response = await self._raw_client.btrecovery(request_options=request_options)
        return _response.data

    async def get_ble_hid_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.get_ble_hid_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ble_hid_status(request_options=request_options)
        return _response.data

    async def start_ble_scan(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.start_ble_scan(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_ble_scan(n, request_options=request_options)
        return _response.data

    async def get_ble_discovery_result(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.bluetooth.get_ble_discovery_result()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ble_discovery_result(request_options=request_options)
        return _response.data
