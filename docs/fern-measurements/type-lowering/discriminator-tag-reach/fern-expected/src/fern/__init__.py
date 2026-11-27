



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BikeHolder,
        BikeHolderType,
        Bin,
        BinContentsItem,
        BoltPart,
        BoltPartType,
        CarHolder,
        CarHolderType,
        DroneHolder,
        DroneHolderType,
        Loan,
        NutPart,
        NutPartType,
        Part,
        Part_Bolt,
        Part_Nut,
        Person,
        PersonHolder,
        Rental,
        RobotHolder,
        RobotHolderType,
        Share,
        TenantHolder,
        VanHolder,
        VanHolderType,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BikeHolder": ".types",
    "BikeHolderType": ".types",
    "Bin": ".types",
    "BinContentsItem": ".types",
    "BoltPart": ".types",
    "BoltPartType": ".types",
    "CarHolder": ".types",
    "CarHolderType": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DroneHolder": ".types",
    "DroneHolderType": ".types",
    "FernApi": ".client",
    "Loan": ".types",
    "NutPart": ".types",
    "NutPartType": ".types",
    "Part": ".types",
    "Part_Bolt": ".types",
    "Part_Nut": ".types",
    "Person": ".types",
    "PersonHolder": ".types",
    "Rental": ".types",
    "RobotHolder": ".types",
    "RobotHolderType": ".types",
    "Share": ".types",
    "TenantHolder": ".types",
    "VanHolder": ".types",
    "VanHolderType": ".types",
    "__version__": ".version",
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
    "BikeHolder",
    "BikeHolderType",
    "Bin",
    "BinContentsItem",
    "BoltPart",
    "BoltPartType",
    "CarHolder",
    "CarHolderType",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DroneHolder",
    "DroneHolderType",
    "FernApi",
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
    "__version__",
]
