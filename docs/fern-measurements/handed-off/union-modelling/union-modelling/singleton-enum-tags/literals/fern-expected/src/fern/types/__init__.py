



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .author import Author, Author_Autopilot, Author_Contractor, Author_Crew, Author_Harbour
    from .author_autopilot import AuthorAutopilot
    from .author_harbour import AuthorHarbour
    from .contractor import Contractor
    from .crew_member import CrewMember
    from .entry import Entry
    from .lorry import Lorry
    from .mode_rail import ModeRail
    from .mode_road import ModeRoad
    from .mode_sea import ModeSea
    from .shipment import Shipment, Shipment_Rail, Shipment_Road, Shipment_Sea
    from .shipment_rail import ShipmentRail
    from .shipment_sea import ShipmentSea
_dynamic_imports: typing.Dict[str, str] = {
    "Author": ".author",
    "AuthorAutopilot": ".author_autopilot",
    "AuthorHarbour": ".author_harbour",
    "Author_Autopilot": ".author",
    "Author_Contractor": ".author",
    "Author_Crew": ".author",
    "Author_Harbour": ".author",
    "Contractor": ".contractor",
    "CrewMember": ".crew_member",
    "Entry": ".entry",
    "Lorry": ".lorry",
    "ModeRail": ".mode_rail",
    "ModeRoad": ".mode_road",
    "ModeSea": ".mode_sea",
    "Shipment": ".shipment",
    "ShipmentRail": ".shipment_rail",
    "ShipmentSea": ".shipment_sea",
    "Shipment_Rail": ".shipment",
    "Shipment_Road": ".shipment",
    "Shipment_Sea": ".shipment",
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
    "Author",
    "AuthorAutopilot",
    "AuthorHarbour",
    "Author_Autopilot",
    "Author_Contractor",
    "Author_Crew",
    "Author_Harbour",
    "Contractor",
    "CrewMember",
    "Entry",
    "Lorry",
    "ModeRail",
    "ModeRoad",
    "ModeSea",
    "Shipment",
    "ShipmentRail",
    "ShipmentSea",
    "Shipment_Rail",
    "Shipment_Road",
    "Shipment_Sea",
]
