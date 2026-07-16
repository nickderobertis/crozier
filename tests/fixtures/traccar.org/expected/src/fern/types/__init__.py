



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .attribute import Attribute
    from .calendar import Calendar
    from .calendar_attributes import CalendarAttributes
    from .command import Command
    from .command_attributes import CommandAttributes
    from .command_type import CommandType
    from .device import Device
    from .device_attributes import DeviceAttributes
    from .driver import Driver
    from .driver_attributes import DriverAttributes
    from .event import Event
    from .event_attributes import EventAttributes
    from .geofence import Geofence
    from .geofence_attributes import GeofenceAttributes
    from .group import Group
    from .group_attributes import GroupAttributes
    from .maintenance import Maintenance
    from .maintenance_attributes import MaintenanceAttributes
    from .notification import Notification
    from .notification_attributes import NotificationAttributes
    from .notification_type import NotificationType
    from .permission import Permission
    from .position import Position
    from .position_attributes import PositionAttributes
    from .position_network import PositionNetwork
    from .report_stops import ReportStops
    from .report_summary import ReportSummary
    from .report_trips import ReportTrips
    from .server import Server
    from .server_attributes import ServerAttributes
    from .statistics import Statistics
    from .user import User
    from .user_attributes import UserAttributes
_dynamic_imports: typing.Dict[str, str] = {
    "Attribute": ".attribute",
    "Calendar": ".calendar",
    "CalendarAttributes": ".calendar_attributes",
    "Command": ".command",
    "CommandAttributes": ".command_attributes",
    "CommandType": ".command_type",
    "Device": ".device",
    "DeviceAttributes": ".device_attributes",
    "Driver": ".driver",
    "DriverAttributes": ".driver_attributes",
    "Event": ".event",
    "EventAttributes": ".event_attributes",
    "Geofence": ".geofence",
    "GeofenceAttributes": ".geofence_attributes",
    "Group": ".group",
    "GroupAttributes": ".group_attributes",
    "Maintenance": ".maintenance",
    "MaintenanceAttributes": ".maintenance_attributes",
    "Notification": ".notification",
    "NotificationAttributes": ".notification_attributes",
    "NotificationType": ".notification_type",
    "Permission": ".permission",
    "Position": ".position",
    "PositionAttributes": ".position_attributes",
    "PositionNetwork": ".position_network",
    "ReportStops": ".report_stops",
    "ReportSummary": ".report_summary",
    "ReportTrips": ".report_trips",
    "Server": ".server",
    "ServerAttributes": ".server_attributes",
    "Statistics": ".statistics",
    "User": ".user",
    "UserAttributes": ".user_attributes",
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
    "Attribute",
    "Calendar",
    "CalendarAttributes",
    "Command",
    "CommandAttributes",
    "CommandType",
    "Device",
    "DeviceAttributes",
    "Driver",
    "DriverAttributes",
    "Event",
    "EventAttributes",
    "Geofence",
    "GeofenceAttributes",
    "Group",
    "GroupAttributes",
    "Maintenance",
    "MaintenanceAttributes",
    "Notification",
    "NotificationAttributes",
    "NotificationType",
    "Permission",
    "Position",
    "PositionAttributes",
    "PositionNetwork",
    "ReportStops",
    "ReportSummary",
    "ReportTrips",
    "Server",
    "ServerAttributes",
    "Statistics",
    "User",
    "UserAttributes",
]
