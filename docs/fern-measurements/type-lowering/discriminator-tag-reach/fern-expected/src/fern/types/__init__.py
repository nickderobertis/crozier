



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bike_holder import BikeHolder
    from .bike_holder_type import BikeHolderType
    from .bin import Bin
    from .bin_contents_item import BinContentsItem
    from .bolt_part import BoltPart
    from .bolt_part_type import BoltPartType
    from .car_holder import CarHolder
    from .car_holder_type import CarHolderType
    from .drone_holder import DroneHolder
    from .drone_holder_type import DroneHolderType
    from .loan import Loan
    from .nut_part import NutPart
    from .nut_part_type import NutPartType
    from .part import Part, Part_Bolt, Part_Nut
    from .person import Person
    from .person_holder import PersonHolder
    from .rental import Rental
    from .robot_holder import RobotHolder
    from .robot_holder_type import RobotHolderType
    from .share import Share
    from .tenant_holder import TenantHolder
    from .van_holder import VanHolder
    from .van_holder_type import VanHolderType
_dynamic_imports: typing.Dict[str, str] = {
    "BikeHolder": ".bike_holder",
    "BikeHolderType": ".bike_holder_type",
    "Bin": ".bin",
    "BinContentsItem": ".bin_contents_item",
    "BoltPart": ".bolt_part",
    "BoltPartType": ".bolt_part_type",
    "CarHolder": ".car_holder",
    "CarHolderType": ".car_holder_type",
    "DroneHolder": ".drone_holder",
    "DroneHolderType": ".drone_holder_type",
    "Loan": ".loan",
    "NutPart": ".nut_part",
    "NutPartType": ".nut_part_type",
    "Part": ".part",
    "Part_Bolt": ".part",
    "Part_Nut": ".part",
    "Person": ".person",
    "PersonHolder": ".person_holder",
    "Rental": ".rental",
    "RobotHolder": ".robot_holder",
    "RobotHolderType": ".robot_holder_type",
    "Share": ".share",
    "TenantHolder": ".tenant_holder",
    "VanHolder": ".van_holder",
    "VanHolderType": ".van_holder_type",
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
    "BikeHolder",
    "BikeHolderType",
    "Bin",
    "BinContentsItem",
    "BoltPart",
    "BoltPartType",
    "CarHolder",
    "CarHolderType",
    "DroneHolder",
    "DroneHolderType",
    "Loan",
    "NutPart",
    "NutPartType",
    "Part",
    "Part_Bolt",
    "Part_Nut",
    "Person",
    "PersonHolder",
    "Rental",
    "RobotHolder",
    "RobotHolderType",
    "Share",
    "TenantHolder",
    "VanHolder",
    "VanHolderType",
]
