



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .alarm_data import AlarmData
    from .alarm_response import AlarmResponse
    from .alarm_type import AlarmType
    from .alarms_list_response import AlarmsListResponse
    from .ap_config import ApConfig
    from .app_connection import AppConnection
    from .battery_cell_voltage_diff_config import BatteryCellVoltageDiffConfig
    from .battery_cell_voltage_high_config import BatteryCellVoltageHighConfig
    from .battery_cell_voltage_low_config import BatteryCellVoltageLowConfig
    from .battery_current_high_config import BatteryCurrentHighConfig
    from .battery_health_low_config import BatteryHealthLowConfig
    from .battery_monitoring_config import BatteryMonitoringConfig
    from .battery_percent_low_config import BatteryPercentLowConfig
    from .battery_state import BatteryState
    from .battery_temp_high_config import BatteryTempHighConfig
    from .battery_voltage_high_config import BatteryVoltageHighConfig
    from .battery_voltage_low_config import BatteryVoltageLowConfig
    from .bottom_obstacle_tracking import BottomObstacleTracking
    from .cargo_check_qr_inputs import CargoCheckQrInputs
    from .cargo_check_qr_outputs import CargoCheckQrOutputs
    from .cargo_close_inputs import CargoCloseInputs
    from .cargo_close_outputs import CargoCloseOutputs
    from .cargo_door_motor_state import CargoDoorMotorState
    from .cargo_door_motor_state_direction import CargoDoorMotorStateDirection
    from .cargo_lift_config import CargoLiftConfig
    from .cargo_lift_inputs import CargoLiftInputs
    from .cargo_lift_outputs import CargoLiftOutputs
    from .cargo_lower_config import CargoLowerConfig
    from .cargo_lower_inputs import CargoLowerInputs
    from .cargo_lower_outputs import CargoLowerOutputs
    from .cargo_open_inputs import CargoOpenInputs
    from .cargo_open_outputs import CargoOpenOutputs
    from .cargo_state import CargoState
    from .charge_state import ChargeState
    from .cloud_config import CloudConfig
    from .cloud_connection import CloudConnection
    from .command_config import CommandConfig
    from .command_inputs import CommandInputs
    from .command_outputs import CommandOutputs
    from .command_response import CommandResponse
    from .command_source import CommandSource
    from .command_status import CommandStatus
    from .command_type import CommandType
    from .commands_list_response import CommandsListResponse
    from .data_battery_cell_voltage_diff import DataBatteryCellVoltageDiff
    from .data_battery_cell_voltage_high import DataBatteryCellVoltageHigh
    from .data_battery_cell_voltage_low import DataBatteryCellVoltageLow
    from .data_battery_current_high import DataBatteryCurrentHigh
    from .data_battery_health_low import DataBatteryHealthLow
    from .data_battery_percent_low import DataBatteryPercentLow
    from .data_battery_temp_high import DataBatteryTempHigh
    from .data_battery_voltage_high import DataBatteryVoltageHigh
    from .data_battery_voltage_low import DataBatteryVoltageLow
    from .discharge_state import DischargeState
    from .distance_sensor_state import DistanceSensorState
    from .drive_motor_state import DriveMotorState
    from .drive_motor_state_direction import DriveMotorStateDirection
    from .error_code_response import ErrorCodeResponse
    from .error_response import ErrorResponse
    from .esp_config import EspConfig
    from .esp_serial_connection import EspSerialConnection
    from .field_error import FieldError
    from .hardware_config import HardwareConfig
    from .health_response import HealthResponse
    from .http_config import HttpConfig
    from .led import Led
    from .led_config import LedConfig
    from .led_connection import LedConnection
    from .led_mode import LedMode
    from .led_state import LedState
    from .leds_config import LedsConfig
    from .lift_motor_state import LiftMotorState
    from .limit_switch import LimitSwitch
    from .limit_switch_state import LimitSwitchState
    from .location import Location
    from .location_state import LocationState
    from .log_config import LogConfig
    from .log_console_handler import LogConsoleHandler
    from .log_console_handler_format import LogConsoleHandlerFormat
    from .log_console_handler_level import LogConsoleHandlerLevel
    from .log_file_handler import LogFileHandler
    from .log_file_handler_format import LogFileHandlerFormat
    from .log_file_handler_level import LogFileHandlerLevel
    from .motor_speed import MotorSpeed
    from .move_backward_inputs import MoveBackwardInputs
    from .move_backward_outputs import MoveBackwardOutputs
    from .move_direction import MoveDirection
    from .move_forward_inputs import MoveForwardInputs
    from .move_forward_outputs import MoveForwardOutputs
    from .move_to_inputs import MoveToInputs
    from .move_to_outputs import MoveToOutputs
    from .obstacle_tracking import ObstacleTracking
    from .pic_config import PicConfig
    from .pic_serial_connection import PicSerialConnection
    from .rfidusb_connection import RfidusbConnection
    from .robot_state_response import RobotStateResponse
    from .robot_state_response_leds import RobotStateResponseLeds
    from .scan_location_inputs import ScanLocationInputs
    from .scan_location_outputs import ScanLocationOutputs
    from .serial_config import SerialConfig
    from .serial_config_parity import SerialConfigParity
    from .serial_port import SerialPort
    from .serial_port_list_response import SerialPortListResponse
    from .sta_config import StaConfig
    from .stop_inputs import StopInputs
    from .stop_outputs import StopOutputs
    from .system_info import SystemInfo
    from .system_status import SystemStatus
    from .system_status_status import SystemStatusStatus
    from .version import Version
    from .wait_inputs import WaitInputs
    from .wait_outputs import WaitOutputs
    from .wifi_config import WifiConfig
_dynamic_imports: typing.Dict[str, str] = {
    "AlarmData": ".alarm_data",
    "AlarmResponse": ".alarm_response",
    "AlarmType": ".alarm_type",
    "AlarmsListResponse": ".alarms_list_response",
    "ApConfig": ".ap_config",
    "AppConnection": ".app_connection",
    "BatteryCellVoltageDiffConfig": ".battery_cell_voltage_diff_config",
    "BatteryCellVoltageHighConfig": ".battery_cell_voltage_high_config",
    "BatteryCellVoltageLowConfig": ".battery_cell_voltage_low_config",
    "BatteryCurrentHighConfig": ".battery_current_high_config",
    "BatteryHealthLowConfig": ".battery_health_low_config",
    "BatteryMonitoringConfig": ".battery_monitoring_config",
    "BatteryPercentLowConfig": ".battery_percent_low_config",
    "BatteryState": ".battery_state",
    "BatteryTempHighConfig": ".battery_temp_high_config",
    "BatteryVoltageHighConfig": ".battery_voltage_high_config",
    "BatteryVoltageLowConfig": ".battery_voltage_low_config",
    "BottomObstacleTracking": ".bottom_obstacle_tracking",
    "CargoCheckQrInputs": ".cargo_check_qr_inputs",
    "CargoCheckQrOutputs": ".cargo_check_qr_outputs",
    "CargoCloseInputs": ".cargo_close_inputs",
    "CargoCloseOutputs": ".cargo_close_outputs",
    "CargoDoorMotorState": ".cargo_door_motor_state",
    "CargoDoorMotorStateDirection": ".cargo_door_motor_state_direction",
    "CargoLiftConfig": ".cargo_lift_config",
    "CargoLiftInputs": ".cargo_lift_inputs",
    "CargoLiftOutputs": ".cargo_lift_outputs",
    "CargoLowerConfig": ".cargo_lower_config",
    "CargoLowerInputs": ".cargo_lower_inputs",
    "CargoLowerOutputs": ".cargo_lower_outputs",
    "CargoOpenInputs": ".cargo_open_inputs",
    "CargoOpenOutputs": ".cargo_open_outputs",
    "CargoState": ".cargo_state",
    "ChargeState": ".charge_state",
    "CloudConfig": ".cloud_config",
    "CloudConnection": ".cloud_connection",
    "CommandConfig": ".command_config",
    "CommandInputs": ".command_inputs",
    "CommandOutputs": ".command_outputs",
    "CommandResponse": ".command_response",
    "CommandSource": ".command_source",
    "CommandStatus": ".command_status",
    "CommandType": ".command_type",
    "CommandsListResponse": ".commands_list_response",
    "DataBatteryCellVoltageDiff": ".data_battery_cell_voltage_diff",
    "DataBatteryCellVoltageHigh": ".data_battery_cell_voltage_high",
    "DataBatteryCellVoltageLow": ".data_battery_cell_voltage_low",
    "DataBatteryCurrentHigh": ".data_battery_current_high",
    "DataBatteryHealthLow": ".data_battery_health_low",
    "DataBatteryPercentLow": ".data_battery_percent_low",
    "DataBatteryTempHigh": ".data_battery_temp_high",
    "DataBatteryVoltageHigh": ".data_battery_voltage_high",
    "DataBatteryVoltageLow": ".data_battery_voltage_low",
    "DischargeState": ".discharge_state",
    "DistanceSensorState": ".distance_sensor_state",
    "DriveMotorState": ".drive_motor_state",
    "DriveMotorStateDirection": ".drive_motor_state_direction",
    "ErrorCodeResponse": ".error_code_response",
    "ErrorResponse": ".error_response",
    "EspConfig": ".esp_config",
    "EspSerialConnection": ".esp_serial_connection",
    "FieldError": ".field_error",
    "HardwareConfig": ".hardware_config",
    "HealthResponse": ".health_response",
    "HttpConfig": ".http_config",
    "Led": ".led",
    "LedConfig": ".led_config",
    "LedConnection": ".led_connection",
    "LedMode": ".led_mode",
    "LedState": ".led_state",
    "LedsConfig": ".leds_config",
    "LiftMotorState": ".lift_motor_state",
    "LimitSwitch": ".limit_switch",
    "LimitSwitchState": ".limit_switch_state",
    "Location": ".location",
    "LocationState": ".location_state",
    "LogConfig": ".log_config",
    "LogConsoleHandler": ".log_console_handler",
    "LogConsoleHandlerFormat": ".log_console_handler_format",
    "LogConsoleHandlerLevel": ".log_console_handler_level",
    "LogFileHandler": ".log_file_handler",
    "LogFileHandlerFormat": ".log_file_handler_format",
    "LogFileHandlerLevel": ".log_file_handler_level",
    "MotorSpeed": ".motor_speed",
    "MoveBackwardInputs": ".move_backward_inputs",
    "MoveBackwardOutputs": ".move_backward_outputs",
    "MoveDirection": ".move_direction",
    "MoveForwardInputs": ".move_forward_inputs",
    "MoveForwardOutputs": ".move_forward_outputs",
    "MoveToInputs": ".move_to_inputs",
    "MoveToOutputs": ".move_to_outputs",
    "ObstacleTracking": ".obstacle_tracking",
    "PicConfig": ".pic_config",
    "PicSerialConnection": ".pic_serial_connection",
    "RfidusbConnection": ".rfidusb_connection",
    "RobotStateResponse": ".robot_state_response",
    "RobotStateResponseLeds": ".robot_state_response_leds",
    "ScanLocationInputs": ".scan_location_inputs",
    "ScanLocationOutputs": ".scan_location_outputs",
    "SerialConfig": ".serial_config",
    "SerialConfigParity": ".serial_config_parity",
    "SerialPort": ".serial_port",
    "SerialPortListResponse": ".serial_port_list_response",
    "StaConfig": ".sta_config",
    "StopInputs": ".stop_inputs",
    "StopOutputs": ".stop_outputs",
    "SystemInfo": ".system_info",
    "SystemStatus": ".system_status",
    "SystemStatusStatus": ".system_status_status",
    "Version": ".version",
    "WaitInputs": ".wait_inputs",
    "WaitOutputs": ".wait_outputs",
    "WifiConfig": ".wifi_config",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AlarmData",
    "AlarmResponse",
    "AlarmType",
    "AlarmsListResponse",
    "ApConfig",
    "AppConnection",
    "BatteryCellVoltageDiffConfig",
    "BatteryCellVoltageHighConfig",
    "BatteryCellVoltageLowConfig",
    "BatteryCurrentHighConfig",
    "BatteryHealthLowConfig",
    "BatteryMonitoringConfig",
    "BatteryPercentLowConfig",
    "BatteryState",
    "BatteryTempHighConfig",
    "BatteryVoltageHighConfig",
    "BatteryVoltageLowConfig",
    "BottomObstacleTracking",
    "CargoCheckQrInputs",
    "CargoCheckQrOutputs",
    "CargoCloseInputs",
    "CargoCloseOutputs",
    "CargoDoorMotorState",
    "CargoDoorMotorStateDirection",
    "CargoLiftConfig",
    "CargoLiftInputs",
    "CargoLiftOutputs",
    "CargoLowerConfig",
    "CargoLowerInputs",
    "CargoLowerOutputs",
    "CargoOpenInputs",
    "CargoOpenOutputs",
    "CargoState",
    "ChargeState",
    "CloudConfig",
    "CloudConnection",
    "CommandConfig",
    "CommandInputs",
    "CommandOutputs",
    "CommandResponse",
    "CommandSource",
    "CommandStatus",
    "CommandType",
    "CommandsListResponse",
    "DataBatteryCellVoltageDiff",
    "DataBatteryCellVoltageHigh",
    "DataBatteryCellVoltageLow",
    "DataBatteryCurrentHigh",
    "DataBatteryHealthLow",
    "DataBatteryPercentLow",
    "DataBatteryTempHigh",
    "DataBatteryVoltageHigh",
    "DataBatteryVoltageLow",
    "DischargeState",
    "DistanceSensorState",
    "DriveMotorState",
    "DriveMotorStateDirection",
    "ErrorCodeResponse",
    "ErrorResponse",
    "EspConfig",
    "EspSerialConnection",
    "FieldError",
    "HardwareConfig",
    "HealthResponse",
    "HttpConfig",
    "Led",
    "LedConfig",
    "LedConnection",
    "LedMode",
    "LedState",
    "LedsConfig",
    "LiftMotorState",
    "LimitSwitch",
    "LimitSwitchState",
    "Location",
    "LocationState",
    "LogConfig",
    "LogConsoleHandler",
    "LogConsoleHandlerFormat",
    "LogConsoleHandlerLevel",
    "LogFileHandler",
    "LogFileHandlerFormat",
    "LogFileHandlerLevel",
    "MotorSpeed",
    "MoveBackwardInputs",
    "MoveBackwardOutputs",
    "MoveDirection",
    "MoveForwardInputs",
    "MoveForwardOutputs",
    "MoveToInputs",
    "MoveToOutputs",
    "ObstacleTracking",
    "PicConfig",
    "PicSerialConnection",
    "RfidusbConnection",
    "RobotStateResponse",
    "RobotStateResponseLeds",
    "ScanLocationInputs",
    "ScanLocationOutputs",
    "SerialConfig",
    "SerialConfigParity",
    "SerialPort",
    "SerialPortListResponse",
    "StaConfig",
    "StopInputs",
    "StopOutputs",
    "SystemInfo",
    "SystemStatus",
    "SystemStatusStatus",
    "Version",
    "WaitInputs",
    "WaitOutputs",
    "WifiConfig",
]
