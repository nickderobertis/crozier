



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Attribute,
        Calendar,
        CalendarAttributes,
        Command,
        CommandAttributes,
        CommandType,
        Device,
        DeviceAttributes,
        Driver,
        DriverAttributes,
        Event,
        EventAttributes,
        Geofence,
        GeofenceAttributes,
        Group,
        GroupAttributes,
        Maintenance,
        MaintenanceAttributes,
        Notification,
        NotificationAttributes,
        NotificationType,
        Permission,
        Position,
        PositionAttributes,
        PositionNetwork,
        ReportStops,
        ReportSummary,
        ReportTrips,
        Server,
        ServerAttributes,
        Statistics,
        User,
        UserAttributes,
    )
    from .errors import BadRequestError, NotFoundError, UnauthorizedError
    from . import (
        attributes,
        calendars,
        commands,
        devices,
        drivers,
        events,
        geofences,
        groups,
        maintenance,
        notifications,
        permissions,
        positions,
        reports,
        server,
        session,
        statistics,
        users,
    )
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "Attribute": ".types",
    "BadRequestError": ".errors",
    "Calendar": ".types",
    "CalendarAttributes": ".types",
    "Command": ".types",
    "CommandAttributes": ".types",
    "CommandType": ".types",
    "Device": ".types",
    "DeviceAttributes": ".types",
    "Driver": ".types",
    "DriverAttributes": ".types",
    "Event": ".types",
    "EventAttributes": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "Geofence": ".types",
    "GeofenceAttributes": ".types",
    "Group": ".types",
    "GroupAttributes": ".types",
    "Maintenance": ".types",
    "MaintenanceAttributes": ".types",
    "NotFoundError": ".errors",
    "Notification": ".types",
    "NotificationAttributes": ".types",
    "NotificationType": ".types",
    "Permission": ".types",
    "Position": ".types",
    "PositionAttributes": ".types",
    "PositionNetwork": ".types",
    "ReportStops": ".types",
    "ReportSummary": ".types",
    "ReportTrips": ".types",
    "Server": ".types",
    "ServerAttributes": ".types",
    "Statistics": ".types",
    "UnauthorizedError": ".errors",
    "User": ".types",
    "UserAttributes": ".types",
    "__version__": ".version",
    "attributes": ".attributes",
    "calendars": ".calendars",
    "commands": ".commands",
    "devices": ".devices",
    "drivers": ".drivers",
    "events": ".events",
    "geofences": ".geofences",
    "groups": ".groups",
    "maintenance": ".maintenance",
    "notifications": ".notifications",
    "permissions": ".permissions",
    "positions": ".positions",
    "reports": ".reports",
    "server": ".server",
    "session": ".session",
    "statistics": ".statistics",
    "users": ".users",
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
    "AsyncFernApi",
    "Attribute",
    "BadRequestError",
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
    "FernApi",
    "FernApiEnvironment",
    "Geofence",
    "GeofenceAttributes",
    "Group",
    "GroupAttributes",
    "Maintenance",
    "MaintenanceAttributes",
    "NotFoundError",
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
    "UnauthorizedError",
    "User",
    "UserAttributes",
    "__version__",
    "attributes",
    "calendars",
    "commands",
    "devices",
    "drivers",
    "events",
    "geofences",
    "groups",
    "maintenance",
    "notifications",
    "permissions",
    "positions",
    "reports",
    "server",
    "session",
    "statistics",
    "users",
]
