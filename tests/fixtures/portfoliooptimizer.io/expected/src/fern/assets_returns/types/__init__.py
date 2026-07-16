



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_assets_returns_average_request_assets_item import PostAssetsReturnsAverageRequestAssetsItem
    from .post_assets_returns_average_response import PostAssetsReturnsAverageResponse
    from .post_assets_returns_average_response_assets_item import PostAssetsReturnsAverageResponseAssetsItem
    from .post_assets_returns_request_assets_item import PostAssetsReturnsRequestAssetsItem
    from .post_assets_returns_response import PostAssetsReturnsResponse
    from .post_assets_returns_response_assets_item import PostAssetsReturnsResponseAssetsItem
_dynamic_imports: typing.Dict[str, str] = {
    "PostAssetsReturnsAverageRequestAssetsItem": ".post_assets_returns_average_request_assets_item",
    "PostAssetsReturnsAverageResponse": ".post_assets_returns_average_response",
    "PostAssetsReturnsAverageResponseAssetsItem": ".post_assets_returns_average_response_assets_item",
    "PostAssetsReturnsRequestAssetsItem": ".post_assets_returns_request_assets_item",
    "PostAssetsReturnsResponse": ".post_assets_returns_response",
    "PostAssetsReturnsResponseAssetsItem": ".post_assets_returns_response_assets_item",
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
    "PostAssetsReturnsAverageRequestAssetsItem",
    "PostAssetsReturnsAverageResponse",
    "PostAssetsReturnsAverageResponseAssetsItem",
    "PostAssetsReturnsRequestAssetsItem",
    "PostAssetsReturnsResponse",
    "PostAssetsReturnsResponseAssetsItem",
]
