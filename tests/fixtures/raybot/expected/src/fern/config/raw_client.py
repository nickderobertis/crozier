

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
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
from ..types.error_response import ErrorResponse
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawConfigClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_log_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[LogConfig]:
        """
        Get the log configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LogConfig]
            The log configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "configs/log",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogConfig,
                    parse_obj_as(
                        type_=LogConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_log_config(
        self,
        *,
        file: LogFileHandler,
        console: LogConsoleHandler,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LogConfig]:
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
        HttpResponse[LogConfig]
            The updated log configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "configs/log",
            method="PUT",
            json={
                "file": convert_and_respect_annotation_metadata(
                    object_=file, annotation=LogFileHandler, direction="write"
                ),
                "console": convert_and_respect_annotation_metadata(
                    object_=console, annotation=LogConsoleHandler, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogConfig,
                    parse_obj_as(
                        type_=LogConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_hardware_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[HardwareConfig]:
        """
        Get the hardware configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HardwareConfig]
            The hardware configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "configs/hardware",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HardwareConfig,
                    parse_obj_as(
                        type_=HardwareConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_hardware_config(
        self,
        *,
        esp: EspConfig,
        pic: PicConfig,
        leds: LedsConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[HardwareConfig]:
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
        HttpResponse[HardwareConfig]
            The updated hardware configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "configs/hardware",
            method="PUT",
            json={
                "esp": convert_and_respect_annotation_metadata(object_=esp, annotation=EspConfig, direction="write"),
                "pic": convert_and_respect_annotation_metadata(object_=pic, annotation=PicConfig, direction="write"),
                "leds": convert_and_respect_annotation_metadata(object_=leds, annotation=LedsConfig, direction="write"),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HardwareConfig,
                    parse_obj_as(
                        type_=HardwareConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_cloud_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[CloudConfig]:
        """
        Get the cloud configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CloudConfig]
            The cloud configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "configs/cloud",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudConfig,
                    parse_obj_as(
                        type_=CloudConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_cloud_config(
        self, *, enable: bool, address: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CloudConfig]:
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
        HttpResponse[CloudConfig]
            The updated cloud configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "configs/cloud",
            method="PUT",
            json={
                "enable": enable,
                "address": address,
                "token": token,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudConfig,
                    parse_obj_as(
                        type_=CloudConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_http_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[HttpConfig]:
        """
        Get the HTTP configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HttpConfig]
            The HTTP configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "configs/http",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HttpConfig,
                    parse_obj_as(
                        type_=HttpConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_http_config(
        self, *, port: int, swagger: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[HttpConfig]:
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
        HttpResponse[HttpConfig]
            The updated HTTP configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "configs/http",
            method="PUT",
            json={
                "port": port,
                "swagger": swagger,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HttpConfig,
                    parse_obj_as(
                        type_=HttpConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_wifi_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[WifiConfig]:
        """
        Get the wifi configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WifiConfig]
            The wifi configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "configs/wifi",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WifiConfig,
                    parse_obj_as(
                        type_=WifiConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_wifi_config(
        self, *, ap: ApConfig, sta: StaConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WifiConfig]:
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
        HttpResponse[WifiConfig]
            The wifi configuration was updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "configs/wifi",
            method="PUT",
            json={
                "ap": convert_and_respect_annotation_metadata(object_=ap, annotation=ApConfig, direction="write"),
                "sta": convert_and_respect_annotation_metadata(object_=sta, annotation=StaConfig, direction="write"),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WifiConfig,
                    parse_obj_as(
                        type_=WifiConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_command_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CommandConfig]:
        """
        Get the command configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CommandConfig]
            The command configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "configs/command",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CommandConfig,
                    parse_obj_as(
                        type_=CommandConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_command_config(
        self,
        *,
        cargo_lift: CargoLiftConfig,
        cargo_lower: CargoLowerConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CommandConfig]:
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
        HttpResponse[CommandConfig]
            The updated command configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "configs/command",
            method="PUT",
            json={
                "cargoLift": convert_and_respect_annotation_metadata(
                    object_=cargo_lift, annotation=CargoLiftConfig, direction="write"
                ),
                "cargoLower": convert_and_respect_annotation_metadata(
                    object_=cargo_lower, annotation=CargoLowerConfig, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CommandConfig,
                    parse_obj_as(
                        type_=CommandConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_battery_monitoring_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BatteryMonitoringConfig]:
        """
        Get the battery monitoring configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatteryMonitoringConfig]
            The battery monitoring configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "configs/monitoring/battery",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatteryMonitoringConfig,
                    parse_obj_as(
                        type_=BatteryMonitoringConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[BatteryMonitoringConfig]:
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
        HttpResponse[BatteryMonitoringConfig]
            The updated battery monitoring configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "configs/monitoring/battery",
            method="PUT",
            json={
                "voltageLow": convert_and_respect_annotation_metadata(
                    object_=voltage_low, annotation=BatteryVoltageLowConfig, direction="write"
                ),
                "voltageHigh": convert_and_respect_annotation_metadata(
                    object_=voltage_high, annotation=BatteryVoltageHighConfig, direction="write"
                ),
                "cellVoltageHigh": convert_and_respect_annotation_metadata(
                    object_=cell_voltage_high, annotation=BatteryCellVoltageHighConfig, direction="write"
                ),
                "cellVoltageLow": convert_and_respect_annotation_metadata(
                    object_=cell_voltage_low, annotation=BatteryCellVoltageLowConfig, direction="write"
                ),
                "cellVoltageDiff": convert_and_respect_annotation_metadata(
                    object_=cell_voltage_diff, annotation=BatteryCellVoltageDiffConfig, direction="write"
                ),
                "currentHigh": convert_and_respect_annotation_metadata(
                    object_=current_high, annotation=BatteryCurrentHighConfig, direction="write"
                ),
                "tempHigh": convert_and_respect_annotation_metadata(
                    object_=temp_high, annotation=BatteryTempHighConfig, direction="write"
                ),
                "percentLow": convert_and_respect_annotation_metadata(
                    object_=percent_low, annotation=BatteryPercentLowConfig, direction="write"
                ),
                "healthLow": convert_and_respect_annotation_metadata(
                    object_=health_low, annotation=BatteryHealthLowConfig, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatteryMonitoringConfig,
                    parse_obj_as(
                        type_=BatteryMonitoringConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawConfigClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_log_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LogConfig]:
        """
        Get the log configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LogConfig]
            The log configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "configs/log",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogConfig,
                    parse_obj_as(
                        type_=LogConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_log_config(
        self,
        *,
        file: LogFileHandler,
        console: LogConsoleHandler,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LogConfig]:
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
        AsyncHttpResponse[LogConfig]
            The updated log configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "configs/log",
            method="PUT",
            json={
                "file": convert_and_respect_annotation_metadata(
                    object_=file, annotation=LogFileHandler, direction="write"
                ),
                "console": convert_and_respect_annotation_metadata(
                    object_=console, annotation=LogConsoleHandler, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogConfig,
                    parse_obj_as(
                        type_=LogConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_hardware_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[HardwareConfig]:
        """
        Get the hardware configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HardwareConfig]
            The hardware configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "configs/hardware",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HardwareConfig,
                    parse_obj_as(
                        type_=HardwareConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_hardware_config(
        self,
        *,
        esp: EspConfig,
        pic: PicConfig,
        leds: LedsConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[HardwareConfig]:
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
        AsyncHttpResponse[HardwareConfig]
            The updated hardware configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "configs/hardware",
            method="PUT",
            json={
                "esp": convert_and_respect_annotation_metadata(object_=esp, annotation=EspConfig, direction="write"),
                "pic": convert_and_respect_annotation_metadata(object_=pic, annotation=PicConfig, direction="write"),
                "leds": convert_and_respect_annotation_metadata(object_=leds, annotation=LedsConfig, direction="write"),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HardwareConfig,
                    parse_obj_as(
                        type_=HardwareConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_cloud_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CloudConfig]:
        """
        Get the cloud configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CloudConfig]
            The cloud configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "configs/cloud",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudConfig,
                    parse_obj_as(
                        type_=CloudConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_cloud_config(
        self, *, enable: bool, address: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CloudConfig]:
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
        AsyncHttpResponse[CloudConfig]
            The updated cloud configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "configs/cloud",
            method="PUT",
            json={
                "enable": enable,
                "address": address,
                "token": token,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CloudConfig,
                    parse_obj_as(
                        type_=CloudConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_http_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[HttpConfig]:
        """
        Get the HTTP configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HttpConfig]
            The HTTP configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "configs/http",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HttpConfig,
                    parse_obj_as(
                        type_=HttpConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_http_config(
        self, *, port: int, swagger: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[HttpConfig]:
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
        AsyncHttpResponse[HttpConfig]
            The updated HTTP configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "configs/http",
            method="PUT",
            json={
                "port": port,
                "swagger": swagger,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HttpConfig,
                    parse_obj_as(
                        type_=HttpConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_wifi_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WifiConfig]:
        """
        Get the wifi configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WifiConfig]
            The wifi configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "configs/wifi",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WifiConfig,
                    parse_obj_as(
                        type_=WifiConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_wifi_config(
        self, *, ap: ApConfig, sta: StaConfig, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WifiConfig]:
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
        AsyncHttpResponse[WifiConfig]
            The wifi configuration was updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "configs/wifi",
            method="PUT",
            json={
                "ap": convert_and_respect_annotation_metadata(object_=ap, annotation=ApConfig, direction="write"),
                "sta": convert_and_respect_annotation_metadata(object_=sta, annotation=StaConfig, direction="write"),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WifiConfig,
                    parse_obj_as(
                        type_=WifiConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_command_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CommandConfig]:
        """
        Get the command configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CommandConfig]
            The command configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "configs/command",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CommandConfig,
                    parse_obj_as(
                        type_=CommandConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_command_config(
        self,
        *,
        cargo_lift: CargoLiftConfig,
        cargo_lower: CargoLowerConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CommandConfig]:
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
        AsyncHttpResponse[CommandConfig]
            The updated command configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "configs/command",
            method="PUT",
            json={
                "cargoLift": convert_and_respect_annotation_metadata(
                    object_=cargo_lift, annotation=CargoLiftConfig, direction="write"
                ),
                "cargoLower": convert_and_respect_annotation_metadata(
                    object_=cargo_lower, annotation=CargoLowerConfig, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CommandConfig,
                    parse_obj_as(
                        type_=CommandConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_battery_monitoring_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BatteryMonitoringConfig]:
        """
        Get the battery monitoring configuration

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatteryMonitoringConfig]
            The battery monitoring configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "configs/monitoring/battery",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatteryMonitoringConfig,
                    parse_obj_as(
                        type_=BatteryMonitoringConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[BatteryMonitoringConfig]:
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
        AsyncHttpResponse[BatteryMonitoringConfig]
            The updated battery monitoring configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "configs/monitoring/battery",
            method="PUT",
            json={
                "voltageLow": convert_and_respect_annotation_metadata(
                    object_=voltage_low, annotation=BatteryVoltageLowConfig, direction="write"
                ),
                "voltageHigh": convert_and_respect_annotation_metadata(
                    object_=voltage_high, annotation=BatteryVoltageHighConfig, direction="write"
                ),
                "cellVoltageHigh": convert_and_respect_annotation_metadata(
                    object_=cell_voltage_high, annotation=BatteryCellVoltageHighConfig, direction="write"
                ),
                "cellVoltageLow": convert_and_respect_annotation_metadata(
                    object_=cell_voltage_low, annotation=BatteryCellVoltageLowConfig, direction="write"
                ),
                "cellVoltageDiff": convert_and_respect_annotation_metadata(
                    object_=cell_voltage_diff, annotation=BatteryCellVoltageDiffConfig, direction="write"
                ),
                "currentHigh": convert_and_respect_annotation_metadata(
                    object_=current_high, annotation=BatteryCurrentHighConfig, direction="write"
                ),
                "tempHigh": convert_and_respect_annotation_metadata(
                    object_=temp_high, annotation=BatteryTempHighConfig, direction="write"
                ),
                "percentLow": convert_and_respect_annotation_metadata(
                    object_=percent_low, annotation=BatteryPercentLowConfig, direction="write"
                ),
                "healthLow": convert_and_respect_annotation_metadata(
                    object_=health_low, annotation=BatteryHealthLowConfig, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BatteryMonitoringConfig,
                    parse_obj_as(
                        type_=BatteryMonitoringConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
