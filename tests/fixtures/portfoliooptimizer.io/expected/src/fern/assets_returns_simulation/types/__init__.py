



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_assets_returns_simulation_bootstrap_request_assets_item import (
        PostAssetsReturnsSimulationBootstrapRequestAssetsItem,
    )
    from .post_assets_returns_simulation_bootstrap_request_bootstrap_method import (
        PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod,
    )
    from .post_assets_returns_simulation_bootstrap_response import PostAssetsReturnsSimulationBootstrapResponse
    from .post_assets_returns_simulation_bootstrap_response_simulations_item import (
        PostAssetsReturnsSimulationBootstrapResponseSimulationsItem,
    )
    from .post_assets_returns_simulation_bootstrap_response_simulations_item_assets_item import (
        PostAssetsReturnsSimulationBootstrapResponseSimulationsItemAssetsItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostAssetsReturnsSimulationBootstrapRequestAssetsItem": ".post_assets_returns_simulation_bootstrap_request_assets_item",
    "PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod": ".post_assets_returns_simulation_bootstrap_request_bootstrap_method",
    "PostAssetsReturnsSimulationBootstrapResponse": ".post_assets_returns_simulation_bootstrap_response",
    "PostAssetsReturnsSimulationBootstrapResponseSimulationsItem": ".post_assets_returns_simulation_bootstrap_response_simulations_item",
    "PostAssetsReturnsSimulationBootstrapResponseSimulationsItemAssetsItem": ".post_assets_returns_simulation_bootstrap_response_simulations_item_assets_item",
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
    "PostAssetsReturnsSimulationBootstrapRequestAssetsItem",
    "PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod",
    "PostAssetsReturnsSimulationBootstrapResponse",
    "PostAssetsReturnsSimulationBootstrapResponseSimulationsItem",
    "PostAssetsReturnsSimulationBootstrapResponseSimulationsItemAssetsItem",
]
