

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ap_config import ApConfig
from ..types.battery_cell_voltage_diff_config import BatteryCellVoltageDiffConfig
from ..types.battery_cell_voltage_high_config import BatteryCellVoltageHighConfig
from ..types.battery_cell_voltage_low_config import BatteryCellVoltageLowConfig
from ..types.battery_current_high_config import BatteryCurrentHighConfig
from ..types.battery_health_low_config import BatteryHealthLowConfig
from ..types.battery_monitoring_config import BatteryMonitoringConfig
from ..types.battery_percent_low_config import BatteryPercentLowConfig
from ..types.battery_temp_high_config import BatteryTempHighConfig
from ..types.battery_voltage_high_config import BatteryVoltageHighConfig
from ..types.battery_voltage_low_config import BatteryVoltageLowConfig
from ..types.cargo_lift_config import CargoLiftConfig
from ..types.cargo_lower_config import CargoLowerConfig
from ..types.cloud_config import CloudConfig
from ..types.command_config import CommandConfig
from ..types.esp_config import EspConfig
from ..types.hardware_config import HardwareConfig
from ..types.http_config import HttpConfig
from ..types.leds_config import LedsConfig
from ..types.log_config import LogConfig
from ..types.log_console_handler import LogConsoleHandler
from ..types.log_file_handler import LogFileHandler
from ..types.pic_config import PicConfig
from ..types.sta_config import StaConfig
from ..types.wifi_config import WifiConfig
from .raw_client import AsyncRawConfigClient, RawConfigClient


OMIT = typing.cast(typing.Any, ...)


class ConfigClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConfigClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConfigClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConfigClient
        """
        return self._raw_client

    def get_log_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> LogConfig:
        """
        Get the log configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogConfig
            The log configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.config.get_log_config()
        """
        _response = self._raw_client.get_log_config(request_options=request_options)
        return _response.data

    def update_log_config(
        self,
        *,
        file: LogFileHandler,
        console: LogConsoleHandler,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogConfig:
        """
        Update the log configuration

        Parameters
        ----------
        file : LogFileHandler

        console : LogConsoleHandler

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogConfig
            The updated log configuration

        Examples
        --------
        from fern import (
            FernApi,
            LogConsoleHandler,
            LogConsoleHandlerFormat,
            LogConsoleHandlerLevel,
            LogFileHandler,
            LogFileHandlerFormat,
            LogFileHandlerLevel,
        )

        client = FernApi()
        client.config.update_log_config(
            file=LogFileHandler(
                enable=True,
                path="logs/raybot.log",
                rotation_count=10,
                level=LogFileHandlerLevel.DEBUG,
                format=LogFileHandlerFormat.JSON,
            ),
            console=LogConsoleHandler(
                enable=True,
                level=LogConsoleHandlerLevel.DEBUG,
                format=LogConsoleHandlerFormat.JSON,
            ),
        )
        """
        _response = self._raw_client.update_log_config(file=file, console=console, request_options=request_options)
        return _response.data

    def get_hardware_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> HardwareConfig:
        """
        Get the hardware configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HardwareConfig
            The hardware configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.config.get_hardware_config()
        """
        _response = self._raw_client.get_hardware_config(request_options=request_options)
        return _response.data

    def update_hardware_config(
        self,
        *,
        esp: EspConfig,
        pic: PicConfig,
        leds: LedsConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HardwareConfig:
        """
        Update the hardware configuration

        Parameters
        ----------
        esp : EspConfig

        pic : PicConfig

        leds : LedsConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HardwareConfig
            The updated hardware configuration

        Examples
        --------
        from fern import (
            EspConfig,
            FernApi,
            LedConfig,
            LedsConfig,
            PicConfig,
            SerialConfig,
            SerialConfigParity,
        )

        client = FernApi()
        client.config.update_hardware_config(
            esp=EspConfig(
                serial=SerialConfig(
                    port="/dev/ttyUSB0",
                    baud_rate=9600,
                    data_bits=8,
                    stop_bits=1.0,
                    parity=SerialConfigParity.NONE,
                    read_timeout=1.0,
                ),
                enable_ack=True,
                command_ack_timeout=1.0,
            ),
            pic=PicConfig(
                serial=SerialConfig(
                    port="/dev/ttyUSB0",
                    baud_rate=9600,
                    data_bits=8,
                    stop_bits=1.0,
                    parity=SerialConfigParity.NONE,
                    read_timeout=1.0,
                ),
                enable_ack=True,
                command_ack_timeout=1.0,
                reset_pin="59",
            ),
            leds=LedsConfig(
                system=LedConfig(
                    pin="GPIO2",
                ),
                alert=LedConfig(
                    pin="GPIO2",
                ),
            ),
        )
        """
        _response = self._raw_client.update_hardware_config(
            esp=esp, pic=pic, leds=leds, request_options=request_options
        )
        return _response.data

    def get_cloud_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> CloudConfig:
        """
        Get the cloud configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudConfig
            The cloud configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.config.get_cloud_config()
        """
        _response = self._raw_client.get_cloud_config(request_options=request_options)
        return _response.data

    def update_cloud_config(
        self, *, enable: bool, address: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudConfig:
        """
        Update the cloud configuration

        Parameters
        ----------
        enable : bool
            Whether to enable the cloud service

        address : str
            The address for the cloud service

        token : str
            The token for the cloud service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudConfig
            The updated cloud configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.config.update_cloud_config(
            enable=True,
            address="localhost:50051",
            token="4d24e88b41374b34a54806c0124b4052",
        )
        """
        _response = self._raw_client.update_cloud_config(
            enable=enable, address=address, token=token, request_options=request_options
        )
        return _response.data

    def get_http_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpConfig:
        """
        Get the HTTP configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpConfig
            The HTTP configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.config.get_http_config()
        """
        _response = self._raw_client.get_http_config(request_options=request_options)
        return _response.data

    def update_http_config(
        self, *, port: int, swagger: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpConfig:
        """
        Update the HTTP configuration

        Parameters
        ----------
        port : int
            The port for the HTTP server

        swagger : bool
            Whether to enable the Swagger UI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpConfig
            The updated HTTP configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.config.update_http_config(
            port=8000,
            swagger=True,
        )
        """
        _response = self._raw_client.update_http_config(port=port, swagger=swagger, request_options=request_options)
        return _response.data

    def get_wifi_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> WifiConfig:
        """
        Get the wifi configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WifiConfig
            The wifi configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.config.get_wifi_config()
        """
        _response = self._raw_client.get_wifi_config(request_options=request_options)
        return _response.data

    def update_wifi_config(
        self, *, ap: ApConfig, sta: StaConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> WifiConfig:
        """
        Update the wifi configuration

        Parameters
        ----------
        ap : ApConfig

        sta : StaConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WifiConfig
            The wifi configuration was updated successfully

        Examples
        --------
        from fern import ApConfig, FernApi, StaConfig

        client = FernApi()
        client.config.update_wifi_config(
            ap=ApConfig(
                enable=True,
                ssid="raybot",
                password="password",
                ip="192.168.1.1",
            ),
            sta=StaConfig(
                enable=True,
                ssid="raybot",
                password="password",
                ip="192.168.1.100/24",
            ),
        )
        """
        _response = self._raw_client.update_wifi_config(ap=ap, sta=sta, request_options=request_options)
        return _response.data

    def get_command_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> CommandConfig:
        """
        Get the command configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandConfig
            The command configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.config.get_command_config()
        """
        _response = self._raw_client.get_command_config(request_options=request_options)
        return _response.data

    def update_command_config(
        self,
        *,
        cargo_lift: CargoLiftConfig,
        cargo_lower: CargoLowerConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommandConfig:
        """
        Update the command configuration

        Parameters
        ----------
        cargo_lift : CargoLiftConfig

        cargo_lower : CargoLowerConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandConfig
            The updated command configuration

        Examples
        --------
        from fern import CargoLiftConfig, CargoLowerConfig, FernApi, ObstacleTracking

        client = FernApi()
        client.config.update_command_config(
            cargo_lift=CargoLiftConfig(
                stable_read_count=3,
            ),
            cargo_lower=CargoLowerConfig(
                stable_read_count=3,
                bottom_obstacle_tracking=ObstacleTracking(
                    enter_distance=20,
                    exit_distance=30,
                ),
            ),
        )
        """
        _response = self._raw_client.update_command_config(
            cargo_lift=cargo_lift, cargo_lower=cargo_lower, request_options=request_options
        )
        return _response.data

    def get_battery_monitoring_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BatteryMonitoringConfig:
        """
        Get the battery monitoring configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatteryMonitoringConfig
            The battery monitoring configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.config.get_battery_monitoring_config()
        """
        _response = self._raw_client.get_battery_monitoring_config(request_options=request_options)
        return _response.data

    def update_battery_monitoring_config(
        self,
        *,
        voltage_low: BatteryVoltageLowConfig,
        voltage_high: BatteryVoltageHighConfig,
        cell_voltage_high: BatteryCellVoltageHighConfig,
        cell_voltage_low: BatteryCellVoltageLowConfig,
        cell_voltage_diff: BatteryCellVoltageDiffConfig,
        current_high: BatteryCurrentHighConfig,
        temp_high: BatteryTempHighConfig,
        percent_low: BatteryPercentLowConfig,
        health_low: BatteryHealthLowConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatteryMonitoringConfig:
        """
        Update the battery monitoring configuration

        Parameters
        ----------
        voltage_low : BatteryVoltageLowConfig

        voltage_high : BatteryVoltageHighConfig

        cell_voltage_high : BatteryCellVoltageHighConfig

        cell_voltage_low : BatteryCellVoltageLowConfig

        cell_voltage_diff : BatteryCellVoltageDiffConfig

        current_high : BatteryCurrentHighConfig

        temp_high : BatteryTempHighConfig

        percent_low : BatteryPercentLowConfig

        health_low : BatteryHealthLowConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatteryMonitoringConfig
            The updated battery monitoring configuration

        Examples
        --------
        from fern import (
            BatteryCellVoltageDiffConfig,
            BatteryCellVoltageHighConfig,
            BatteryCellVoltageLowConfig,
            BatteryCurrentHighConfig,
            BatteryHealthLowConfig,
            BatteryPercentLowConfig,
            BatteryTempHighConfig,
            BatteryVoltageHighConfig,
            BatteryVoltageLowConfig,
            FernApi,
        )

        client = FernApi()
        client.config.update_battery_monitoring_config(
            voltage_low=BatteryVoltageLowConfig(
                enable=False,
                threshold=14.0,
            ),
            voltage_high=BatteryVoltageHighConfig(
                enable=False,
                threshold=18.0,
            ),
            cell_voltage_high=BatteryCellVoltageHighConfig(
                enable=False,
                threshold=4.3,
            ),
            cell_voltage_low=BatteryCellVoltageLowConfig(
                enable=False,
                threshold=3.8,
            ),
            cell_voltage_diff=BatteryCellVoltageDiffConfig(
                enable=False,
                threshold=0.5,
            ),
            current_high=BatteryCurrentHighConfig(
                enable=False,
                threshold=6.0,
            ),
            temp_high=BatteryTempHighConfig(
                enable=False,
                threshold=60.0,
            ),
            percent_low=BatteryPercentLowConfig(
                enable=False,
                threshold=20.0,
            ),
            health_low=BatteryHealthLowConfig(
                enable=False,
                threshold=60.0,
            ),
        )
        """
        _response = self._raw_client.update_battery_monitoring_config(
            voltage_low=voltage_low,
            voltage_high=voltage_high,
            cell_voltage_high=cell_voltage_high,
            cell_voltage_low=cell_voltage_low,
            cell_voltage_diff=cell_voltage_diff,
            current_high=current_high,
            temp_high=temp_high,
            percent_low=percent_low,
            health_low=health_low,
            request_options=request_options,
        )
        return _response.data


class AsyncConfigClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConfigClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConfigClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConfigClient
        """
        return self._raw_client

    async def get_log_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> LogConfig:
        """
        Get the log configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogConfig
            The log configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.get_log_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_log_config(request_options=request_options)
        return _response.data

    async def update_log_config(
        self,
        *,
        file: LogFileHandler,
        console: LogConsoleHandler,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogConfig:
        """
        Update the log configuration

        Parameters
        ----------
        file : LogFileHandler

        console : LogConsoleHandler

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogConfig
            The updated log configuration

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            LogConsoleHandler,
            LogConsoleHandlerFormat,
            LogConsoleHandlerLevel,
            LogFileHandler,
            LogFileHandlerFormat,
            LogFileHandlerLevel,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.update_log_config(
                file=LogFileHandler(
                    enable=True,
                    path="logs/raybot.log",
                    rotation_count=10,
                    level=LogFileHandlerLevel.DEBUG,
                    format=LogFileHandlerFormat.JSON,
                ),
                console=LogConsoleHandler(
                    enable=True,
                    level=LogConsoleHandlerLevel.DEBUG,
                    format=LogConsoleHandlerFormat.JSON,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_log_config(
            file=file, console=console, request_options=request_options
        )
        return _response.data

    async def get_hardware_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> HardwareConfig:
        """
        Get the hardware configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HardwareConfig
            The hardware configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.get_hardware_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_hardware_config(request_options=request_options)
        return _response.data

    async def update_hardware_config(
        self,
        *,
        esp: EspConfig,
        pic: PicConfig,
        leds: LedsConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HardwareConfig:
        """
        Update the hardware configuration

        Parameters
        ----------
        esp : EspConfig

        pic : PicConfig

        leds : LedsConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HardwareConfig
            The updated hardware configuration

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            EspConfig,
            LedConfig,
            LedsConfig,
            PicConfig,
            SerialConfig,
            SerialConfigParity,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.update_hardware_config(
                esp=EspConfig(
                    serial=SerialConfig(
                        port="/dev/ttyUSB0",
                        baud_rate=9600,
                        data_bits=8,
                        stop_bits=1.0,
                        parity=SerialConfigParity.NONE,
                        read_timeout=1.0,
                    ),
                    enable_ack=True,
                    command_ack_timeout=1.0,
                ),
                pic=PicConfig(
                    serial=SerialConfig(
                        port="/dev/ttyUSB0",
                        baud_rate=9600,
                        data_bits=8,
                        stop_bits=1.0,
                        parity=SerialConfigParity.NONE,
                        read_timeout=1.0,
                    ),
                    enable_ack=True,
                    command_ack_timeout=1.0,
                    reset_pin="59",
                ),
                leds=LedsConfig(
                    system=LedConfig(
                        pin="GPIO2",
                    ),
                    alert=LedConfig(
                        pin="GPIO2",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_hardware_config(
            esp=esp, pic=pic, leds=leds, request_options=request_options
        )
        return _response.data

    async def get_cloud_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> CloudConfig:
        """
        Get the cloud configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudConfig
            The cloud configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.get_cloud_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cloud_config(request_options=request_options)
        return _response.data

    async def update_cloud_config(
        self, *, enable: bool, address: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CloudConfig:
        """
        Update the cloud configuration

        Parameters
        ----------
        enable : bool
            Whether to enable the cloud service

        address : str
            The address for the cloud service

        token : str
            The token for the cloud service

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudConfig
            The updated cloud configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.update_cloud_config(
                enable=True,
                address="localhost:50051",
                token="4d24e88b41374b34a54806c0124b4052",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_cloud_config(
            enable=enable, address=address, token=token, request_options=request_options
        )
        return _response.data

    async def get_http_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpConfig:
        """
        Get the HTTP configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpConfig
            The HTTP configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.get_http_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_http_config(request_options=request_options)
        return _response.data

    async def update_http_config(
        self, *, port: int, swagger: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpConfig:
        """
        Update the HTTP configuration

        Parameters
        ----------
        port : int
            The port for the HTTP server

        swagger : bool
            Whether to enable the Swagger UI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpConfig
            The updated HTTP configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.update_http_config(
                port=8000,
                swagger=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_http_config(
            port=port, swagger=swagger, request_options=request_options
        )
        return _response.data

    async def get_wifi_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> WifiConfig:
        """
        Get the wifi configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WifiConfig
            The wifi configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.get_wifi_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_wifi_config(request_options=request_options)
        return _response.data

    async def update_wifi_config(
        self, *, ap: ApConfig, sta: StaConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> WifiConfig:
        """
        Update the wifi configuration

        Parameters
        ----------
        ap : ApConfig

        sta : StaConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WifiConfig
            The wifi configuration was updated successfully

        Examples
        --------
        import asyncio

        from fern import ApConfig, AsyncFernApi, StaConfig

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.update_wifi_config(
                ap=ApConfig(
                    enable=True,
                    ssid="raybot",
                    password="password",
                    ip="192.168.1.1",
                ),
                sta=StaConfig(
                    enable=True,
                    ssid="raybot",
                    password="password",
                    ip="192.168.1.100/24",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_wifi_config(ap=ap, sta=sta, request_options=request_options)
        return _response.data

    async def get_command_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> CommandConfig:
        """
        Get the command configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandConfig
            The command configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.get_command_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_command_config(request_options=request_options)
        return _response.data

    async def update_command_config(
        self,
        *,
        cargo_lift: CargoLiftConfig,
        cargo_lower: CargoLowerConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommandConfig:
        """
        Update the command configuration

        Parameters
        ----------
        cargo_lift : CargoLiftConfig

        cargo_lower : CargoLowerConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandConfig
            The updated command configuration

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            CargoLiftConfig,
            CargoLowerConfig,
            ObstacleTracking,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.update_command_config(
                cargo_lift=CargoLiftConfig(
                    stable_read_count=3,
                ),
                cargo_lower=CargoLowerConfig(
                    stable_read_count=3,
                    bottom_obstacle_tracking=ObstacleTracking(
                        enter_distance=20,
                        exit_distance=30,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_command_config(
            cargo_lift=cargo_lift, cargo_lower=cargo_lower, request_options=request_options
        )
        return _response.data

    async def get_battery_monitoring_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BatteryMonitoringConfig:
        """
        Get the battery monitoring configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatteryMonitoringConfig
            The battery monitoring configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.get_battery_monitoring_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_battery_monitoring_config(request_options=request_options)
        return _response.data

    async def update_battery_monitoring_config(
        self,
        *,
        voltage_low: BatteryVoltageLowConfig,
        voltage_high: BatteryVoltageHighConfig,
        cell_voltage_high: BatteryCellVoltageHighConfig,
        cell_voltage_low: BatteryCellVoltageLowConfig,
        cell_voltage_diff: BatteryCellVoltageDiffConfig,
        current_high: BatteryCurrentHighConfig,
        temp_high: BatteryTempHighConfig,
        percent_low: BatteryPercentLowConfig,
        health_low: BatteryHealthLowConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatteryMonitoringConfig:
        """
        Update the battery monitoring configuration

        Parameters
        ----------
        voltage_low : BatteryVoltageLowConfig

        voltage_high : BatteryVoltageHighConfig

        cell_voltage_high : BatteryCellVoltageHighConfig

        cell_voltage_low : BatteryCellVoltageLowConfig

        cell_voltage_diff : BatteryCellVoltageDiffConfig

        current_high : BatteryCurrentHighConfig

        temp_high : BatteryTempHighConfig

        percent_low : BatteryPercentLowConfig

        health_low : BatteryHealthLowConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatteryMonitoringConfig
            The updated battery monitoring configuration

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            BatteryCellVoltageDiffConfig,
            BatteryCellVoltageHighConfig,
            BatteryCellVoltageLowConfig,
            BatteryCurrentHighConfig,
            BatteryHealthLowConfig,
            BatteryPercentLowConfig,
            BatteryTempHighConfig,
            BatteryVoltageHighConfig,
            BatteryVoltageLowConfig,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.config.update_battery_monitoring_config(
                voltage_low=BatteryVoltageLowConfig(
                    enable=False,
                    threshold=14.0,
                ),
                voltage_high=BatteryVoltageHighConfig(
                    enable=False,
                    threshold=18.0,
                ),
                cell_voltage_high=BatteryCellVoltageHighConfig(
                    enable=False,
                    threshold=4.3,
                ),
                cell_voltage_low=BatteryCellVoltageLowConfig(
                    enable=False,
                    threshold=3.8,
                ),
                cell_voltage_diff=BatteryCellVoltageDiffConfig(
                    enable=False,
                    threshold=0.5,
                ),
                current_high=BatteryCurrentHighConfig(
                    enable=False,
                    threshold=6.0,
                ),
                temp_high=BatteryTempHighConfig(
                    enable=False,
                    threshold=60.0,
                ),
                percent_low=BatteryPercentLowConfig(
                    enable=False,
                    threshold=20.0,
                ),
                health_low=BatteryHealthLowConfig(
                    enable=False,
                    threshold=60.0,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_battery_monitoring_config(
            voltage_low=voltage_low,
            voltage_high=voltage_high,
            cell_voltage_high=cell_voltage_high,
            cell_voltage_low=cell_voltage_low,
            cell_voltage_diff=cell_voltage_diff,
            current_high=current_high,
            temp_high=temp_high,
            percent_low=percent_low,
            health_low=health_low,
            request_options=request_options,
        )
        return _response.data
