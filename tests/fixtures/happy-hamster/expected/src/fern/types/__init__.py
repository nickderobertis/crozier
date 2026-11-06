



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .badge import Badge
    from .badge_type import BadgeType
    from .badge_update import BadgeUpdate
    from .badge_update_reason import BadgeUpdateReason
    from .coordinates import Coordinates
    from .level import Level
    from .level_xp import LevelXp
    from .location import Location
    from .location_details import LocationDetails
    from .location_id import LocationId
    from .location_search_result import LocationSearchResult
    from .location_type import LocationType
    from .occupancy import Occupancy
    from .stage import Stage
    from .user_badges import UserBadges
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "Badge": ".badge",
    "BadgeType": ".badge_type",
    "BadgeUpdate": ".badge_update",
    "BadgeUpdateReason": ".badge_update_reason",
    "Coordinates": ".coordinates",
    "Level": ".level",
    "LevelXp": ".level_xp",
    "Location": ".location",
    "LocationDetails": ".location_details",
    "LocationId": ".location_id",
    "LocationSearchResult": ".location_search_result",
    "LocationType": ".location_type",
    "Occupancy": ".occupancy",
    "Stage": ".stage",
    "UserBadges": ".user_badges",
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
    "Badge",
    "BadgeType",
    "BadgeUpdate",
    "BadgeUpdateReason",
    "Coordinates",
    "Level",
    "LevelXp",
    "Location",
    "LocationDetails",
    "LocationId",
    "LocationSearchResult",
    "LocationType",
    "Occupancy",
    "Stage",
    "UserBadges",
]
