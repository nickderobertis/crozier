

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMultiroomClient, RawMultiroomClient


class MultiroomClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMultiroomClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMultiroomClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMultiroomClient
        """
        return self._raw_client

    def get_slave_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:getSlaveList

        Allows to obtain the list of the devices using the same communication protocol.

        JSON output:
        {
          "Slaves": "1",
          "Slave_list": [
            {
              "Name": "FA5100_a3f4",
              "Mask": "0",
              "Volume": "90",
              "Mute": "0",
              "Channel": "0",
              "Ip": "10.10.10.100",
              "Version": "WIFIAudio.1.2.2321"
            }
          ]
        }

        Field    Description
        Slaves    Number of LinkPlay available
        Slave_list    Information about each Sonoé iEast case available
        name    Name
        mask    Case already in Multi-Room mode, Yes = 1, No = 0
        Volume    Volume level
        Mute    Enable Mute mode, Yes = 1, Off = 0
        Channel    Wifi channel
        ip    IP address of the LinkPlay Boot
        version    firmware version

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
        client.multiroom.get_slave_list()
        """
        _response = self._raw_client.get_slave_list(request_options=request_options)
        return _response.data

    def slave_kickout(self, ip: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveKickout:ip

        Allows to remove from the multiroom mode a device Based on its IP address.

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to be removed from multi-room mode.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.multiroom.slave_kickout(
            ip="ip",
        )
        """
        _response = self._raw_client.slave_kickout(ip, request_options=request_options)
        return _response.data

    def slave_mask(self, ip: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveMask:ip

        Allows to integrate a multi-room mode a device Based on its IP address. It is thus rendered invisible from the IP network.

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to be hidden from the IP network in multi-room mode.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.multiroom.slave_mask(
            ip="ip",
        )
        """
        _response = self._raw_client.slave_mask(ip, request_options=request_options)
        return _response.data

    def slave_un_mask(self, ip: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveUnMask:ip

        Allows to release from the multi-room mode based on its IP address. It is thus visible on the IP network.

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to be released from multi-room mode.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.multiroom.slave_un_mask(
            ip="ip",
        )
        """
        _response = self._raw_client.slave_un_mask(ip, request_options=request_options)
        return _response.data

    def slave_volume(self, ip: str, volume: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveVolume:ip:volume

        Allows you to adjust the individual volume of the each of the devicees via the IP address of the device and the definition of a value going from from 1 to 100. Note: these settings will be lost when deactivating multi-room mode (kickout)

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to adjust the volume for in multi-room mode.

        volume : int
            The volume level to set for the specified LinkPlay device, ranging from 1 to 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.multiroom.slave_volume(
            ip="ip",
            volume=1,
        )
        """
        _response = self._raw_client.slave_volume(ip, volume, request_options=request_options)
        return _response.data

    def set_player_cmd_slave_volume(
        self, volume: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setPlayerCmd:slave_vol:volume

        Adjusts the overal volume of the multi-room with the definition of a value ranging from 1 to 100. Note: thesis settings will be lost When disabling multi-room mode

        Parameters
        ----------
        volume : int
            The overall volume level to set for multi-room mode, ranging from 1 to 100.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.multiroom.set_player_cmd_slave_volume(
            volume=1,
        )
        """
        _response = self._raw_client.set_player_cmd_slave_volume(volume, request_options=request_options)
        return _response.data

    def slave_mute(self, ip: str, mute: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveMute:ip:mute

        Enables the Mute on each device via the IP address of the device and by enabling (1) and disabling (0)

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to adjust the mute status for in multi-room mode.

        mute : int
            Mute status to set for the specified LinkPlay device, where 1 enables mute and 0 disables mute.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.multiroom.slave_mute(
            ip="ip",
            mute=1,
        )
        """
        _response = self._raw_client.slave_mute(ip, mute, request_options=request_options)
        return _response.data

    def set_player_cmd_slave_mute(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setPlayerCmd:slave_mute:mute

        Enables the Mute on all devices

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
        client.multiroom.set_player_cmd_slave_mute()
        """
        _response = self._raw_client.set_player_cmd_slave_mute(request_options=request_options)
        return _response.data

    def set_player_cmd_slave_unmute(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setPlayerCmd:slave_mute:unmute

        To disable the mute mode overall the

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
        client.multiroom.set_player_cmd_slave_unmute()
        """
        _response = self._raw_client.set_player_cmd_slave_unmute(request_options=request_options)
        return _response.data

    def slave_channel(self, ip: str, channel: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveChannel:ip:channel

        Enables the Mute on Each of the devices via the IP address of the device and by this parameter to signal right only Channe0 = left and only 1 = Channel signal

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to adjust the audio channel for in multi-room mode.

        channel : int
            Audio channel to set for the specified LinkPlay device, where 0 signals right only and 1 signals left only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.multiroom.slave_channel(
            ip="ip",
            channel=1,
        )
        """
        _response = self._raw_client.slave_channel(ip, channel, request_options=request_options)
        return _response.data

    def set_player_cmd_slave_channel(
        self, slave_channel: str, channel: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setPlayerCmd:slave_channel:channel

        Enables the Mute on Each of devices via the IP address of the device and by this parameter to signal right only Channel= 0 and left signal only 1 = Channel

        Parameters
        ----------
        slave_channel : str
            IP address of the device

        channel : int
            Audio channel to set for all devices in multi-room mode, where 0 signals right only and 1 signals left only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.multiroom.set_player_cmd_slave_channel(
            slave_channel="slave_channel",
            channel=1,
        )
        """
        _response = self._raw_client.set_player_cmd_slave_channel(
            slave_channel, channel, request_options=request_options
        )
        return _response.data

    def slave_set_device_name(
        self, ip: str, s: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveSetDeviceName:%ip:%s

        Individual settings of the name of the square in mode UPnP / Airplay

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to set the device name for in multi-room mode.

        s : str
            The device name to set for the specified LinkPlay device in multi-room mode.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.multiroom.slave_set_device_name(
            ip="ip",
            s="s",
        )
        """
        _response = self._raw_client.slave_set_device_name(ip, s, request_options=request_options)
        return _response.data

    def ungroup(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:Ungroup

        Disables the multi-room mode

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
        client.multiroom.ungroup()
        """
        _response = self._raw_client.ungroup(request_options=request_options)
        return _response.data

    def config_get_realtime_cache_limit(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:ConfigGet:realtime_cache_limit

        Get the real-time cache limit in multi-room mode. The value is in seconds.

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
        client.multiroom.config_get_realtime_cache_limit()
        """
        _response = self._raw_client.config_get_realtime_cache_limit(request_options=request_options)
        return _response.data

    def config_set_realtime_cache_limit(
        self, value: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:ConfigSet:realtime_cache_limit:%d

        Set the real-time cache limit in multi-room mode. The value is in seconds.

        Parameters
        ----------
        value : int
            The real-time cache limit to set for multi-room mode, in seconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.multiroom.config_set_realtime_cache_limit(
            value=1,
        )
        """
        _response = self._raw_client.config_set_realtime_cache_limit(value, request_options=request_options)
        return _response.data

    def multiroom_slave_start_wps(self, ip: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveStartWPS:%s

        Start WPS on a LinkPlay device based on its IP address. This can be used to connect the device to a new Wi-Fi network.

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to start WPS on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.multiroom.multiroom_slave_start_wps(
            ip="ip",
        )
        """
        _response = self._raw_client.multiroom_slave_start_wps(ip, request_options=request_options)
        return _response.data

    def get_name_group_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:getnamegrouplist

        Get the list of group names in multi-room mode. The output is a JSON array of strings, where each string is a group name.

        Response example:
        { "grouplist": [ ], "current_group_id": "" }

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
        client.multiroom.get_name_group_list()
        """
        _response = self._raw_client.get_name_group_list(request_options=request_options)
        return _response.data

    def leave_group(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.multiroom.leave_group()
        """
        _response = self._raw_client.leave_group(request_options=request_options)
        return _response.data

    def join_group(self, ip: str, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        ip : str
            The IP address of the multi-room group to join.

        uuid_ : str
            The UUID of the multi-room group to join.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.multiroom.join_group(
            ip="IP",
            uuid_="uuid",
        )
        """
        _response = self._raw_client.join_group(ip, uuid_, request_options=request_options)
        return _response.data

    def slave_device_name(self, ip: str, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        ip : str
            The IP address of the slave device

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
        client.multiroom.slave_device_name(
            ip="ip",
            str="str",
        )
        """
        _response = self._raw_client.slave_device_name(ip, str, request_options=request_options)
        return _response.data

    def subwoofer_forget(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        uuid_ : str
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
        client.multiroom.subwoofer_forget(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.subwoofer_forget(uuid_, request_options=request_options)
        return _response.data

    def subwoofer_get_pair_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.multiroom.subwoofer_get_pair_info()
        """
        _response = self._raw_client.subwoofer_get_pair_info(request_options=request_options)
        return _response.data

    def config_get_leadtime(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.multiroom.config_get_leadtime()
        """
        _response = self._raw_client.config_get_leadtime(request_options=request_options)
        return _response.data

    def subwoofer_pair(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.multiroom.subwoofer_pair(
            str="str",
        )
        """
        _response = self._raw_client.subwoofer_pair(str, request_options=request_options)
        return _response.data

    def config_set_leadtime(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.multiroom.config_set_leadtime(
            str="str",
        )
        """
        _response = self._raw_client.config_set_leadtime(str, request_options=request_options)
        return _response.data

    def set_mrm_sub_lpf(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.multiroom.set_mrm_sub_lpf(
            str="str",
        )
        """
        _response = self._raw_client.set_mrm_sub_lpf(str, request_options=request_options)
        return _response.data

    def get_sub_lpf(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.multiroom.get_sub_lpf()
        """
        _response = self._raw_client.get_sub_lpf(request_options=request_options)
        return _response.data

    def set_sub_lpf(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.multiroom.set_sub_lpf(
            str="str",
        )
        """
        _response = self._raw_client.set_sub_lpf(str, request_options=request_options)
        return _response.data

    def get_mrm_sub_lpf(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.multiroom.get_mrm_sub_lpf(
            str="str",
        )
        """
        _response = self._raw_client.get_mrm_sub_lpf(str, request_options=request_options)
        return _response.data


class AsyncMultiroomClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMultiroomClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMultiroomClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMultiroomClient
        """
        return self._raw_client

    async def get_slave_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:getSlaveList

        Allows to obtain the list of the devices using the same communication protocol.

        JSON output:
        {
          "Slaves": "1",
          "Slave_list": [
            {
              "Name": "FA5100_a3f4",
              "Mask": "0",
              "Volume": "90",
              "Mute": "0",
              "Channel": "0",
              "Ip": "10.10.10.100",
              "Version": "WIFIAudio.1.2.2321"
            }
          ]
        }

        Field    Description
        Slaves    Number of LinkPlay available
        Slave_list    Information about each Sonoé iEast case available
        name    Name
        mask    Case already in Multi-Room mode, Yes = 1, No = 0
        Volume    Volume level
        Mute    Enable Mute mode, Yes = 1, Off = 0
        Channel    Wifi channel
        ip    IP address of the LinkPlay Boot
        version    firmware version

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
            await client.multiroom.get_slave_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_slave_list(request_options=request_options)
        return _response.data

    async def slave_kickout(self, ip: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveKickout:ip

        Allows to remove from the multiroom mode a device Based on its IP address.

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to be removed from multi-room mode.

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
            await client.multiroom.slave_kickout(
                ip="ip",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slave_kickout(ip, request_options=request_options)
        return _response.data

    async def slave_mask(self, ip: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveMask:ip

        Allows to integrate a multi-room mode a device Based on its IP address. It is thus rendered invisible from the IP network.

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to be hidden from the IP network in multi-room mode.

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
            await client.multiroom.slave_mask(
                ip="ip",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slave_mask(ip, request_options=request_options)
        return _response.data

    async def slave_un_mask(self, ip: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveUnMask:ip

        Allows to release from the multi-room mode based on its IP address. It is thus visible on the IP network.

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to be released from multi-room mode.

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
            await client.multiroom.slave_un_mask(
                ip="ip",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slave_un_mask(ip, request_options=request_options)
        return _response.data

    async def slave_volume(
        self, ip: str, volume: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveVolume:ip:volume

        Allows you to adjust the individual volume of the each of the devicees via the IP address of the device and the definition of a value going from from 1 to 100. Note: these settings will be lost when deactivating multi-room mode (kickout)

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to adjust the volume for in multi-room mode.

        volume : int
            The volume level to set for the specified LinkPlay device, ranging from 1 to 100.

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
            await client.multiroom.slave_volume(
                ip="ip",
                volume=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slave_volume(ip, volume, request_options=request_options)
        return _response.data

    async def set_player_cmd_slave_volume(
        self, volume: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setPlayerCmd:slave_vol:volume

        Adjusts the overal volume of the multi-room with the definition of a value ranging from 1 to 100. Note: thesis settings will be lost When disabling multi-room mode

        Parameters
        ----------
        volume : int
            The overall volume level to set for multi-room mode, ranging from 1 to 100.

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
            await client.multiroom.set_player_cmd_slave_volume(
                volume=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_slave_volume(volume, request_options=request_options)
        return _response.data

    async def slave_mute(self, ip: str, mute: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveMute:ip:mute

        Enables the Mute on each device via the IP address of the device and by enabling (1) and disabling (0)

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to adjust the mute status for in multi-room mode.

        mute : int
            Mute status to set for the specified LinkPlay device, where 1 enables mute and 0 disables mute.

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
            await client.multiroom.slave_mute(
                ip="ip",
                mute=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slave_mute(ip, mute, request_options=request_options)
        return _response.data

    async def set_player_cmd_slave_mute(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setPlayerCmd:slave_mute:mute

        Enables the Mute on all devices

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
            await client.multiroom.set_player_cmd_slave_mute()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_slave_mute(request_options=request_options)
        return _response.data

    async def set_player_cmd_slave_unmute(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setPlayerCmd:slave_mute:unmute

        To disable the mute mode overall the

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
            await client.multiroom.set_player_cmd_slave_unmute()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_slave_unmute(request_options=request_options)
        return _response.data

    async def slave_channel(
        self, ip: str, channel: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveChannel:ip:channel

        Enables the Mute on Each of the devices via the IP address of the device and by this parameter to signal right only Channe0 = left and only 1 = Channel signal

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to adjust the audio channel for in multi-room mode.

        channel : int
            Audio channel to set for the specified LinkPlay device, where 0 signals right only and 1 signals left only.

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
            await client.multiroom.slave_channel(
                ip="ip",
                channel=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slave_channel(ip, channel, request_options=request_options)
        return _response.data

    async def set_player_cmd_slave_channel(
        self, slave_channel: str, channel: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=setPlayerCmd:slave_channel:channel

        Enables the Mute on Each of devices via the IP address of the device and by this parameter to signal right only Channel= 0 and left signal only 1 = Channel

        Parameters
        ----------
        slave_channel : str
            IP address of the device

        channel : int
            Audio channel to set for all devices in multi-room mode, where 0 signals right only and 1 signals left only.

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
            await client.multiroom.set_player_cmd_slave_channel(
                slave_channel="slave_channel",
                channel=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_player_cmd_slave_channel(
            slave_channel, channel, request_options=request_options
        )
        return _response.data

    async def slave_set_device_name(
        self, ip: str, s: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveSetDeviceName:%ip:%s

        Individual settings of the name of the square in mode UPnP / Airplay

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to set the device name for in multi-room mode.

        s : str
            The device name to set for the specified LinkPlay device in multi-room mode.

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
            await client.multiroom.slave_set_device_name(
                ip="ip",
                s="s",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slave_set_device_name(ip, s, request_options=request_options)
        return _response.data

    async def ungroup(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:Ungroup

        Disables the multi-room mode

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
            await client.multiroom.ungroup()


        asyncio.run(main())
        """
        _response = await self._raw_client.ungroup(request_options=request_options)
        return _response.data

    async def config_get_realtime_cache_limit(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:ConfigGet:realtime_cache_limit

        Get the real-time cache limit in multi-room mode. The value is in seconds.

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
            await client.multiroom.config_get_realtime_cache_limit()


        asyncio.run(main())
        """
        _response = await self._raw_client.config_get_realtime_cache_limit(request_options=request_options)
        return _response.data

    async def config_set_realtime_cache_limit(
        self, value: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:ConfigSet:realtime_cache_limit:%d

        Set the real-time cache limit in multi-room mode. The value is in seconds.

        Parameters
        ----------
        value : int
            The real-time cache limit to set for multi-room mode, in seconds.

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
            await client.multiroom.config_set_realtime_cache_limit(
                value=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.config_set_realtime_cache_limit(value, request_options=request_options)
        return _response.data

    async def multiroom_slave_start_wps(
        self, ip: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:SlaveStartWPS:%s

        Start WPS on a LinkPlay device based on its IP address. This can be used to connect the device to a new Wi-Fi network.

        Parameters
        ----------
        ip : str
            The IP address of the LinkPlay device to start WPS on.

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
            await client.multiroom.multiroom_slave_start_wps(
                ip="ip",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.multiroom_slave_start_wps(ip, request_options=request_options)
        return _response.data

    async def get_name_group_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: http://10.10.10.254/httpapi.asp?command=multiroom:getnamegrouplist

        Get the list of group names in multi-room mode. The output is a JSON array of strings, where each string is a group name.

        Response example:
        { "grouplist": [ ], "current_group_id": "" }

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
            await client.multiroom.get_name_group_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_name_group_list(request_options=request_options)
        return _response.data

    async def leave_group(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.multiroom.leave_group()


        asyncio.run(main())
        """
        _response = await self._raw_client.leave_group(request_options=request_options)
        return _response.data

    async def join_group(self, ip: str, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        ip : str
            The IP address of the multi-room group to join.

        uuid_ : str
            The UUID of the multi-room group to join.

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
            await client.multiroom.join_group(
                ip="IP",
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.join_group(ip, uuid_, request_options=request_options)
        return _response.data

    async def slave_device_name(
        self, ip: str, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        ip : str
            The IP address of the slave device

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
            await client.multiroom.slave_device_name(
                ip="ip",
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slave_device_name(ip, str, request_options=request_options)
        return _response.data

    async def subwoofer_forget(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        uuid_ : str
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
            await client.multiroom.subwoofer_forget(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subwoofer_forget(uuid_, request_options=request_options)
        return _response.data

    async def subwoofer_get_pair_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.multiroom.subwoofer_get_pair_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.subwoofer_get_pair_info(request_options=request_options)
        return _response.data

    async def config_get_leadtime(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.multiroom.config_get_leadtime()


        asyncio.run(main())
        """
        _response = await self._raw_client.config_get_leadtime(request_options=request_options)
        return _response.data

    async def subwoofer_pair(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.multiroom.subwoofer_pair(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subwoofer_pair(str, request_options=request_options)
        return _response.data

    async def config_set_leadtime(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.multiroom.config_set_leadtime(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.config_set_leadtime(str, request_options=request_options)
        return _response.data

    async def set_mrm_sub_lpf(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.multiroom.set_mrm_sub_lpf(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_mrm_sub_lpf(str, request_options=request_options)
        return _response.data

    async def get_sub_lpf(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.multiroom.get_sub_lpf()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sub_lpf(request_options=request_options)
        return _response.data

    async def set_sub_lpf(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.multiroom.set_sub_lpf(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_sub_lpf(str, request_options=request_options)
        return _response.data

    async def get_mrm_sub_lpf(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.multiroom.get_mrm_sub_lpf(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mrm_sub_lpf(str, request_options=request_options)
        return _response.data
