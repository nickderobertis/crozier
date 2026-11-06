



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Address,
        Badge,
        BadgeType,
        BadgeUpdate,
        BadgeUpdateReason,
        Coordinates,
        Level,
        LevelXp,
        Location,
        LocationDetails,
        LocationId,
        LocationSearchResult,
        LocationType,
        Occupancy,
        Stage,
        UserBadges,
    )
    from .errors import BadRequestError, NotFoundError, TooManyRequestsError, UnauthorizedError
    from . import location_types, locations, occupancy, user_badges, user_favorites, user_level
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .occupancy import OccupancyReportClientType
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "Badge": ".types",
    "BadgeType": ".types",
    "BadgeUpdate": ".types",
    "BadgeUpdateReason": ".types",
    "Coordinates": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "Level": ".types",
    "LevelXp": ".types",
    "Location": ".types",
    "LocationDetails": ".types",
    "LocationId": ".types",
    "LocationSearchResult": ".types",
    "LocationType": ".types",
    "NotFoundError": ".errors",
    "Occupancy": ".types",
    "OccupancyReportClientType": ".occupancy",
    "Stage": ".types",
    "TooManyRequestsError": ".errors",
    "UnauthorizedError": ".errors",
    "UserBadges": ".types",
    "__version__": ".version",
    "location_types": ".location_types",
    "locations": ".locations",
    "occupancy": ".occupancy",
    "user_badges": ".user_badges",
    "user_favorites": ".user_favorites",
    "user_level": ".user_level",
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
    "Address",
    "AsyncFernApi",
    "BadRequestError",
    "Badge",
    "BadgeType",
    "BadgeUpdate",
    "BadgeUpdateReason",
    "Coordinates",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "Level",
    "LevelXp",
    "Location",
    "LocationDetails",
    "LocationId",
    "LocationSearchResult",
    "LocationType",
    "NotFoundError",
    "Occupancy",
    "OccupancyReportClientType",
    "Stage",
    "TooManyRequestsError",
    "UnauthorizedError",
    "UserBadges",
    "__version__",
    "location_types",
    "locations",
    "occupancy",
    "user_badges",
    "user_favorites",
    "user_level",
]
