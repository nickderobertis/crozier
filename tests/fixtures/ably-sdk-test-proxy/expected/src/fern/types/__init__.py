



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .fatal_fault_type_dto import FatalFaultTypeDto
    from .fault_simulation_dto import FaultSimulationDto
    from .fault_type_dto import (
        FaultTypeDto,
        FaultTypeDto_Fatal,
        FaultTypeDto_Nonfatal,
        FaultTypeDto_NonfatalWhenResolved,
    )
    from .nonfatal_fault_type_dto import NonfatalFaultTypeDto
    from .nonfatal_when_resolved_fault_type_dto import NonfatalWhenResolvedFaultTypeDto
    from .proxy_dto import ProxyDto
_dynamic_imports: typing.Dict[str, str] = {
    "FatalFaultTypeDto": ".fatal_fault_type_dto",
    "FaultSimulationDto": ".fault_simulation_dto",
    "FaultTypeDto": ".fault_type_dto",
    "FaultTypeDto_Fatal": ".fault_type_dto",
    "FaultTypeDto_Nonfatal": ".fault_type_dto",
    "FaultTypeDto_NonfatalWhenResolved": ".fault_type_dto",
    "NonfatalFaultTypeDto": ".nonfatal_fault_type_dto",
    "NonfatalWhenResolvedFaultTypeDto": ".nonfatal_when_resolved_fault_type_dto",
    "ProxyDto": ".proxy_dto",
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
    "FatalFaultTypeDto",
    "FaultSimulationDto",
    "FaultTypeDto",
    "FaultTypeDto_Fatal",
    "FaultTypeDto_Nonfatal",
    "FaultTypeDto_NonfatalWhenResolved",
    "NonfatalFaultTypeDto",
    "NonfatalWhenResolvedFaultTypeDto",
    "ProxyDto",
]
