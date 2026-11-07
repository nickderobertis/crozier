



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .deploy_request_engine import DeployRequestEngine
    from .deploy_request_gpu_selection import DeployRequestGpuSelection
    from .deploy_request_gpu_selection_one import DeployRequestGpuSelectionOne
    from .deploy_request_profile import DeployRequestProfile
_dynamic_imports: typing.Dict[str, str] = {
    "DeployRequestEngine": ".deploy_request_engine",
    "DeployRequestGpuSelection": ".deploy_request_gpu_selection",
    "DeployRequestGpuSelectionOne": ".deploy_request_gpu_selection_one",
    "DeployRequestProfile": ".deploy_request_profile",
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


__all__ = ["DeployRequestEngine", "DeployRequestGpuSelection", "DeployRequestGpuSelectionOne", "DeployRequestProfile"]
